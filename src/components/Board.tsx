import React, { useEffect, useCallback, useState, useRef, useMemo } from 'react';
import { View, StyleSheet, Image } from 'react-native';
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
import {
  TILE_SIZE,
  BOARD_WIDTH,
  GRID_ROWS,
  GRID_COLS,
} from '../constants/dimensions';
import { getWorldTheme } from '../constants/themes';
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
  const currentLevel = useGameStore((s) => s.currentLevel);

  const activePowerUp = usePowerUpStore((s) => s.activePowerUp);
  const usePowerUp = usePowerUpStore((s) => s.usePowerUp);
  const setActivePowerUp = usePowerUpStore((s) => s.setActivePowerUp);

  const addPowerUpUsed = useStatsStore((s) => s.addPowerUpUsed);

  const [popups, setPopups] = useState<PopupData[]>([]);
  const [showCombo, setShowCombo] = useState(false);
  const [entryKey, setEntryKey] = useState(0);

  // Tema bilgisi
  const worldTheme = useMemo(() => getWorldTheme(currentLevel), [currentLevel]);

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

      if (lastMatchCount >= 4) {
        hapticService.heavyMatch();
      } else {
        hapticService.match();
      }

      // Screen shake for big matches
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

        let targetRow = start.row;
        let targetCol = start.col;

        if (Math.abs(translationX) > Math.abs(translationY)) {
          if (Math.abs(translationX) >= threshold) {
            targetCol = translationX > 0 ? start.col + 1 : start.col - 1;
          } else {
            swipeStartTile.current = null;
            return;
          }
        } else {
          if (Math.abs(translationY) >= threshold) {
            targetRow = translationY > 0 ? start.row + 1 : start.row - 1;
          } else {
            swipeStartTile.current = null;
            return;
          }
        }

        if (targetRow < 0 || targetRow >= GRID_ROWS || targetCol < 0 || targetCol >= GRID_COLS) {
          swipeStartTile.current = null;
          return;
        }

        const { phase: currentPhase, selectedTile: currentSelected } = useGameStore.getState();
        if (currentPhase !== 'idle') {
          swipeStartTile.current = null;
          return;
        }

        hapticService.tap();

        if (!currentSelected) {
          selectTile(start.row, start.col);
          setTimeout(() => {
            selectTile(targetRow, targetCol);
          }, 16);
        } else {
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

  const tileEmojis = worldTheme.tileTheme.emojis;
  const tileShape = worldTheme.tileTheme.shape;

  return (
    <View style={styles.container}>
      {/* Karakter - Board'un sol altında */}
      <Image
        source={worldTheme.character}
        style={styles.character}
        resizeMode="contain"
      />

      <GestureDetector gesture={panGesture}>
        <Animated.View
          style={[
            styles.board,
            {
              width: BOARD_WIDTH,
              backgroundColor: worldTheme.boardBg,
              borderColor: worldTheme.boardBorder,
            },
            shakeStyle,
          ]}
        >
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
                    emoji={tileEmojis[tile.color % tileEmojis.length]}
                    shape={tileShape}
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
    borderRadius: 20,
    overflow: 'hidden',
    padding: 2,
    borderWidth: 2,
    // Gölge efekti
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 8 },
    shadowOpacity: 0.4,
    shadowRadius: 16,
    elevation: 12,
  },
  row: {
    flexDirection: 'row',
  },
  emptyCell: {
    width: TILE_SIZE,
    height: TILE_SIZE,
  },
  character: {
    position: 'absolute',
    bottom: -50,
    left: -30,
    width: 80,
    height: 80,
    zIndex: 10,
  },
});
