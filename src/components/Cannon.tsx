import React, { useState } from 'react';
import { View, StyleSheet, Text, TouchableOpacity } from 'react-native';
import { useGameStore } from '../stores/gameStore';
import { TILE_COLORS, ACCENT_COLOR, TEXT_COLOR } from '../constants/colors';
import {
  TILE_SIZE,
  BALL_RADIUS,
  BOARD_WIDTH,
  GRID_COLS,
  GRID_ROWS,
} from '../constants/dimensions';

export default function Cannon() {
  const comboMeter = useGameStore((s) => s.comboMeter);
  const grid = useGameStore((s) => s.grid);
  const phase = useGameStore((s) => s.phase);
  const setPhase = useGameStore((s) => s.setPhase);
  const setGrid = useGameStore((s) => s.setGrid);
  const addScore = useGameStore((s) => s.addScore);
  const resetCombo = useGameStore((s) => s.resetCombo);

  const [cannonColor] = useState(() => Math.floor(Math.random() * TILE_COLORS.length));
  const isActive = comboMeter >= 100 && phase === 'idle';

  function fireCannon(col: number) {
    const newGrid = grid.map((row) => [...row]);
    let destroyed = 0;

    // Hedef sütundaki aynı renkleri patlatır
    for (let r = 0; r < GRID_ROWS; r++) {
      const tile = newGrid[r][col];
      if (tile && tile.color === cannonColor) {
        newGrid[r][col] = null;
        destroyed++;
      }
    }

    // Çarpma noktasında 3x3 patlama
    let hitRow = GRID_ROWS - 1;
    for (let r = 0; r < GRID_ROWS; r++) {
      if (newGrid[r][col] !== null) {
        hitRow = r;
        break;
      }
    }

    for (let dr = -1; dr <= 1; dr++) {
      for (let dc = -1; dc <= 1; dc++) {
        const nr = hitRow + dr;
        const nc = col + dc;
        if (nr >= 0 && nr < GRID_ROWS && nc >= 0 && nc < GRID_COLS) {
          if (newGrid[nr][nc] !== null) {
            newGrid[nr][nc] = null;
            destroyed++;
          }
        }
      }
    }

    addScore(destroyed * 20);
    resetCombo();
    setGrid(newGrid);
    setPhase('swapping');
  }

  if (!isActive) return null;

  return (
    <View style={styles.container}>
      <Text style={styles.readyText}>CANNON HAZIR! Sutuna dokun!</Text>
      <View style={styles.cannonRow}>
        {Array.from({ length: GRID_COLS }, (_, col) => (
          <TouchableOpacity
            key={col}
            style={styles.colTarget}
            onPress={() => fireCannon(col)}
          >
            <View style={styles.targetDot} />
          </TouchableOpacity>
        ))}
      </View>
      <View style={styles.cannonBody}>
        <View
          style={[
            styles.cannonBall,
            { backgroundColor: TILE_COLORS[cannonColor] },
          ]}
        />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    marginTop: 12,
  },
  readyText: {
    color: ACCENT_COLOR,
    fontSize: 14,
    fontWeight: 'bold',
    marginBottom: 8,
    textAlign: 'center',
  },
  cannonRow: {
    flexDirection: 'row',
    width: BOARD_WIDTH,
    justifyContent: 'center',
  },
  colTarget: {
    width: TILE_SIZE,
    height: 36,
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 1,
    borderColor: 'rgba(255,107,53,0.3)',
    borderRadius: 6,
    marginHorizontal: 1,
  },
  targetDot: {
    width: 8,
    height: 8,
    borderRadius: 4,
    backgroundColor: 'rgba(255,107,53,0.5)',
  },
  cannonBody: {
    width: 50,
    height: 50,
    backgroundColor: ACCENT_COLOR,
    borderRadius: 8,
    alignItems: 'center',
    justifyContent: 'center',
    marginTop: 8,
  },
  cannonBall: {
    width: BALL_RADIUS * 2,
    height: BALL_RADIUS * 2,
    borderRadius: BALL_RADIUS,
  },
});
