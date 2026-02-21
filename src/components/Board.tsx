import React, { useEffect, useCallback } from 'react';
import { View, StyleSheet, TouchableOpacity } from 'react-native';
import { useGameStore } from '../stores/gameStore';
import { TILE_COLORS, GRID_BG_COLOR } from '../constants/colors';
import {
  TILE_SIZE,
  BALL_RADIUS,
  BOARD_WIDTH,
  GRID_ROWS,
} from '../constants/dimensions';

function TileCell({ row, col }: { row: number; col: number }) {
  const tile = useGameStore((s) => s.grid[row]?.[col]);
  const phase = useGameStore((s) => s.phase);
  const selectedTile = useGameStore((s) => s.selectedTile);
  const selectTile = useGameStore((s) => s.selectTile);

  const isSelected = selectedTile?.row === row && selectedTile?.col === col;

  const handlePress = useCallback(() => {
    if (phase !== 'idle') return;
    selectTile(row, col);
  }, [phase, selectTile, row, col]);

  if (!tile) {
    return <View style={styles.emptyCell} />;
  }

  const baseColor = TILE_COLORS[tile.color];

  return (
    <TouchableOpacity
      onPress={handlePress}
      activeOpacity={0.7}
      style={styles.cell}
    >
      <View style={styles.cellBg} />
      {isSelected && <View style={styles.selectionRing} />}
      <View
        style={[
          styles.ball,
          {
            backgroundColor: baseColor,
            width: BALL_RADIUS * 2,
            height: BALL_RADIUS * 2,
            borderRadius: BALL_RADIUS,
          },
        ]}
      >
        <View style={styles.highlight} />
      </View>
    </TouchableOpacity>
  );
}

export default function Board() {
  const grid = useGameStore((s) => s.grid);
  const phase = useGameStore((s) => s.phase);
  const completeMatchPhase = useGameStore((s) => s.completeMatchPhase);

  useEffect(() => {
    if (phase === 'swapping') {
      const timer = setTimeout(() => completeMatchPhase(), 250);
      return () => clearTimeout(timer);
    }
    if (phase === 'matching') {
      const timer = setTimeout(() => completeMatchPhase(), 350);
      return () => clearTimeout(timer);
    }
  }, [phase, completeMatchPhase]);

  if (grid.length === 0) return null;

  return (
    <View style={styles.container}>
      <View style={[styles.board, { width: BOARD_WIDTH }]}>
        {Array.from({ length: GRID_ROWS }, (_, r) => (
          <View key={r} style={styles.row}>
            {grid[r]?.map((_, c) => (
              <TileCell key={`${r}-${c}`} row={r} col={c} />
            ))}
          </View>
        ))}
      </View>
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
    borderRadius: 12,
    overflow: 'hidden',
    padding: 2,
  },
  row: {
    flexDirection: 'row',
  },
  cell: {
    width: TILE_SIZE,
    height: TILE_SIZE,
    alignItems: 'center',
    justifyContent: 'center',
  },
  emptyCell: {
    width: TILE_SIZE,
    height: TILE_SIZE,
  },
  cellBg: {
    position: 'absolute',
    width: TILE_SIZE - 4,
    height: TILE_SIZE - 4,
    borderRadius: 8,
    backgroundColor: 'rgba(255,255,255,0.05)',
  },
  selectionRing: {
    position: 'absolute',
    width: BALL_RADIUS * 2 + 10,
    height: BALL_RADIUS * 2 + 10,
    borderRadius: BALL_RADIUS + 5,
    borderWidth: 3,
    borderColor: 'rgba(255,255,255,0.5)',
    zIndex: 2,
  },
  ball: {
    shadowColor: '#000',
    shadowOffset: { width: 1, height: 2 },
    shadowOpacity: 0.3,
    shadowRadius: 3,
    elevation: 4,
    alignItems: 'center',
    overflow: 'hidden',
  },
  highlight: {
    width: '50%',
    height: '30%',
    backgroundColor: 'rgba(255,255,255,0.3)',
    borderRadius: 100,
    marginTop: 4,
  },
});
