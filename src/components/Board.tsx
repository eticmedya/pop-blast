import React, { useEffect, useCallback, useState, useRef, useMemo } from 'react';
import { View, StyleSheet } from 'react-native';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withSequence,
  withTiming,
} from 'react-native-reanimated';
import { GestureDetector, Gesture } from 'react-native-gesture-handler';
import { useGameStore } from '../stores/gameStore';
import { usePowerUpStore, PowerUpType } from '../stores/powerupStore';
import { useStatsStore } from '../stores/statsStore';
import { executeRowBomb, executeColBomb, executeColorBomb, shuffleGrid } from '../game-engine/powerups';
import { GRID_BG_COLOR } from '../constants/colors';
import {
  TILE_SIZE,
  BOARD_WIDTH,
  GRID_ROWS,
  GRID_COLS,
} from '../constants/dimensions';
import AnimatedTile from './AnimatedTile';
import ScorePopup from './ScorePopup';
import ComboEffect from './ComboEffect';
import { soundManager } from '../services/SoundManager';
import { hapticService } from '../services/HapticService';

interface PopupData {
  id: number;
  text: string;
  x: number;
  y: number;
  color?: string;
}

let popupId = 0;

export default function Board() {
  const grid = useGameStore((s) => s.grid);
  const phase = useGameStore((s) => s.phase);
  const selectedTile = useGameStore((s) => s.selectedTile);
  const selectTile = useGameStore((s) => s.selectTile);
  const executeSwap = useGameStore((s) => s.executeSwap);
  const completeMatchPhase = useGameStore((s) => s.completeMatchPhase);
  const lastMatchCount = useGameStore((s) => s.lastMatchCount);
  const lastCascadeCount = useGameStore((s) => s.lastCascadeCount);
  const setGrid = useGameStore((s) => s.setGrid);
  const addScore = useGameStore((s) => s.addScore);
  const setPhase = useGameStore((s) => s.setPhase);

  const activePowerUp = usePowerUpStore((s) => s.activePowerUp);
  const usePowerUp = usePowerUpStore((s) => s.usePowerUp);
  const setActivePowerUp = usePowerUpStore((s) => s.setActivePowerUp);

  const addPowerUpUsed = useStatsStore((s) => s.addPowerUpUsed);

  const [popups, setPopups] = useState<PopupData[]>([]);
  const [showCombo, setShowCombo] = useState(false);
  const [entryKey, setEntryKey] = useState(0);

  // --- Screen Shake shared values ---
  const shakeX = useSharedValue(0);
  const shakeY = useSharedValue(0);

  const shakeStyle = useAnimatedStyle(() => ({
    transform: [{ translateX: shakeX.value }, { translateY: shakeY.value }],
  }));

  // --- Swipe gesture tracking refs ---
  const swipeStartTile = useRef<{ row: number; col: number } | null>(null);

  // Board entry animation - trigger on new grid
  useEffect(() => {
    if (grid.length > 0) {
      setEntryKey((k) => k + 1);
    }
  }, [grid.length === 0]);

  // Phase transitions with animation timings
  useEffect(() => {
    if (phase === 'swapping') {
      soundManager.play('swap');
      soundManager.resetCascade();
      const timer = setTimeout(() => completeMatchPhase(), 300);
      return () => clearTimeout(timer);
    }
    if (phase === 'matching') {
      soundManager.playMatchCascade();

      // Haptic feedback for matching
      if (lastMatchCount >= 4) {
        hapticService.heavyMatch();
      } else {
        hapticService.match();
      }

      // Screen shake for big matches (4+ matches or cascades > 1)
      if (lastMatchCount >= 4 || lastCascadeCount > 1) {
        const intensity = Math.min(lastMatchCount * 1.5, 12);
        shakeX.value = withSequence(
          withTiming(intensity, { duration: 30 }),
          withTiming(-intensity, { duration: 30 }),
          withTiming(intensity * 0.6, { duration: 30 }),
          withTiming(-intensity * 0.6, { duration: 30 }),
          withTiming(0, { duration: 40 })
        );
        shakeY.value = withSequence(
          withTiming(intensity * 0.5, { duration: 30 }),
          withTiming(-intensity * 0.5, { duration: 30 }),
          withTiming(intensity * 0.3, { duration: 30 }),
          withTiming(-intensity * 0.3, { duration: 30 }),
          withTiming(0, { duration: 40 })
        );
      }

      // Show score popups
      if (lastMatchCount > 0) {
        const score = lastMatchCount * 30;
        const newPopup: PopupData = {
          id: popupId++,
          text: `+${score}`,
          x: BOARD_WIDTH / 2 - 20,
          y: TILE_SIZE * 3,
          color: lastCascadeCount > 0 ? '#FFD700' : undefined,
        };
        setPopups((prev) => [...prev, newPopup]);
      }

      // Show combo effect for cascades
      if (lastCascadeCount > 1) {
        soundManager.play('combo');
        setShowCombo(true);
        setTimeout(() => setShowCombo(false), 1200);
      }

      const timer = setTimeout(() => completeMatchPhase(), 450);
      return () => clearTimeout(timer);
    }
  }, [phase, completeMatchPhase, lastMatchCount, lastCascadeCount, shakeX, shakeY]);

  const handleTilePress = useCallback(
    (row: number, col: number) => {
      if (phase !== 'idle') return;

      // Haptic tap feedback
      hapticService.tap();

      // --- Power-up handling ---
      if (activePowerUp) {
        const tile = grid[row]?.[col];
        if (!tile) return;

        let result: { grid: typeof grid; destroyed: number } | null = null;
        let newGrid: typeof grid | null = null;

        switch (activePowerUp) {
          case 'rowBomb': {
            result = executeRowBomb(grid, row);
            break;
          }
          case 'colBomb': {
            result = executeColBomb(grid, col);
            break;
          }
          case 'colorBomb': {
            result = executeColorBomb(grid, tile.color);
            break;
          }
          case 'shuffle': {
            newGrid = shuffleGrid(grid);
            break;
          }
        }

        if (result) {
          setGrid(result.grid);
          addScore(result.destroyed * 20);
        } else if (newGrid) {
          setGrid(newGrid);
        }

        usePowerUp(activePowerUp);
        setActivePowerUp(null);
        addPowerUpUsed();
        hapticService.powerUp();
        setPhase('swapping');
        return;
      }

      soundManager.play('tap');
      selectTile(row, col);
    },
    [phase, selectTile, activePowerUp, grid, setGrid, addScore, usePowerUp, setActivePowerUp, addPowerUpUsed, setPhase]
  );

  // --- Swipe Gesture ---
  const panGesture = useMemo(() => {
    return Gesture.Pan()
      .minDistance(TILE_SIZE / 4)
      .onStart((e) => {
        // Determine which tile the touch started on
        const col = Math.floor(e.x / TILE_SIZE);
        const row = Math.floor(e.y / TILE_SIZE);
        if (row >= 0 && row < GRID_ROWS && col >= 0 && col < GRID_COLS) {
          swipeStartTile.current = { row, col };
        } else {
          swipeStartTile.current = null;
        }
      })
      .onEnd((e) => {
        const start = swipeStartTile.current;
        if (!start) return;

        const { translationX, translationY } = e;
        const threshold = TILE_SIZE / 3;

        // Determine swipe direction
        let targetRow = start.row;
        let targetCol = start.col;

        if (Math.abs(translationX) > Math.abs(translationY)) {
          // Horizontal swipe
          if (Math.abs(translationX) >= threshold) {
            targetCol = translationX > 0 ? start.col + 1 : start.col - 1;
          } else {
            swipeStartTile.current = null;
            return;
          }
        } else {
          // Vertical swipe
          if (Math.abs(translationY) >= threshold) {
            targetRow = translationY > 0 ? start.row + 1 : start.row - 1;
          } else {
            swipeStartTile.current = null;
            return;
          }
        }

        // Bounds check
        if (targetRow < 0 || targetRow >= GRID_ROWS || targetCol < 0 || targetCol >= GRID_COLS) {
          swipeStartTile.current = null;
          return;
        }

        // Execute via selectTile: first select the start tile, then the target
        // This reuses the existing game logic (adjacency check, match validation)
        const { phase: currentPhase, selectedTile: currentSelected } = useGameStore.getState();
        if (currentPhase !== 'idle') {
          swipeStartTile.current = null;
          return;
        }

        hapticService.tap();

        // If no tile is selected, select start then target to trigger swap
        if (!currentSelected) {
          selectTile(start.row, start.col);
          // Use setTimeout to let the first selectTile process
          setTimeout(() => {
            selectTile(targetRow, targetCol);
          }, 16);
        } else {
          // If a tile is already selected, just select the target
          selectTile(targetRow, targetCol);
        }

        swipeStartTile.current = null;
      })
      .runOnJS(true);
  }, [selectTile]);

  const removePopup = useCallback((id: number) => {
    setPopups((prev) => prev.filter((p) => p.id !== id));
  }, []);

  if (grid.length === 0) return null;

  return (
    <View style={styles.container}>
      <GestureDetector gesture={panGesture}>
        <Animated.View style={[styles.board, { width: BOARD_WIDTH }, shakeStyle]}>
          {Array.from({ length: GRID_ROWS }, (_, r) => (
            <View key={r} style={styles.row}>
              {grid[r]?.map((tile, c) => {
                if (!tile) {
                  return <View key={`empty-${r}-${c}`} style={styles.emptyCell} />;
                }

                const isSelected =
                  selectedTile?.row === r && selectedTile?.col === c;

                return (
                  <AnimatedTile
                    key={tile.id}
                    color={tile.color}
                    isSelected={isSelected}
                    isMatched={false}
                    onPress={() => handleTilePress(r, c)}
                    fallDistance={0}
                    isNew={entryKey > 0}
                    entryDelay={r * 30 + c * 20}
                  />
                );
              })}
            </View>
          ))}

          {/* Score Popups */}
          {popups.map((p) => (
            <ScorePopup
              key={p.id}
              text={p.text}
              x={p.x}
              y={p.y}
              color={p.color}
              onDone={() => removePopup(p.id)}
            />
          ))}
        </Animated.View>
      </GestureDetector>

      {/* Combo Effect */}
      <ComboEffect
        multiplier={lastCascadeCount + 1}
        visible={showCombo}
      />
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
  },
  board: {
    backgroundColor: GRID_BG_COLOR,
    borderRadius: 16,
    overflow: 'hidden',
    padding: 2,
    borderWidth: 1,
    borderColor: 'rgba(255,255,255,0.08)',
  },
  row: {
    flexDirection: 'row',
  },
  emptyCell: {
    width: TILE_SIZE,
    height: TILE_SIZE,
  },
});
