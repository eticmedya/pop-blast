import React, { useEffect, useCallback, useState, useRef } from 'react';
import { View, StyleSheet } from 'react-native';
import { useGameStore } from '../stores/gameStore';
import { GRID_BG_COLOR } from '../constants/colors';
import {
  TILE_SIZE,
  BOARD_WIDTH,
  GRID_ROWS,
} from '../constants/dimensions';
import AnimatedTile from './AnimatedTile';
import ScorePopup from './ScorePopup';
import ComboEffect from './ComboEffect';
import { soundManager } from '../services/SoundManager';

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
  const completeMatchPhase = useGameStore((s) => s.completeMatchPhase);
  const lastMatchCount = useGameStore((s) => s.lastMatchCount);
  const lastCascadeCount = useGameStore((s) => s.lastCascadeCount);

  const [popups, setPopups] = useState<PopupData[]>([]);
  const [showCombo, setShowCombo] = useState(false);
  const [entryKey, setEntryKey] = useState(0);

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
      const timer = setTimeout(() => completeMatchPhase(), 300);
      return () => clearTimeout(timer);
    }
    if (phase === 'matching') {
      soundManager.play('match');

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
  }, [phase, completeMatchPhase, lastMatchCount, lastCascadeCount]);

  const handleTilePress = useCallback(
    (row: number, col: number) => {
      if (phase !== 'idle') return;
      soundManager.play('tap');
      selectTile(row, col);
    },
    [phase, selectTile]
  );

  const removePopup = useCallback((id: number) => {
    setPopups((prev) => prev.filter((p) => p.id !== id));
  }, []);

  if (grid.length === 0) return null;

  return (
    <View style={styles.container}>
      <View style={[styles.board, { width: BOARD_WIDTH }]}>
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
      </View>

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
