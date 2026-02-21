import React, { useCallback, useEffect } from 'react';
import { View, StyleSheet } from 'react-native';
import { Canvas, Circle, RoundedRect, Group, Shadow, LinearGradient, vec } from '@shopify/react-native-skia';
import { Gesture, GestureDetector } from 'react-native-gesture-handler';
import { useGameStore } from '../stores/gameStore';
import { TILE_COLORS, GRID_BG_COLOR } from '../constants/colors';
import {
  TILE_SIZE,
  BALL_RADIUS,
  BOARD_WIDTH,
  BOARD_HEIGHT,
  GRID_COLS,
  GRID_ROWS,
} from '../constants/dimensions';

// Renk tonları (gradient efekti için)
const COLOR_LIGHT: Record<string, string> = {
  '#FF4757': '#FF6B81',
  '#3742FA': '#5352ED',
  '#2ED573': '#7BED9F',
  '#FFA502': '#FFBE76',
  '#A855F7': '#C084FC',
  '#FBBF24': '#FDE68A',
};

export default function Board() {
  const grid = useGameStore((s) => s.grid);
  const phase = useGameStore((s) => s.phase);
  const selectedTile = useGameStore((s) => s.selectedTile);
  const selectTile = useGameStore((s) => s.selectTile);
  const completeMatchPhase = useGameStore((s) => s.completeMatchPhase);
  const setPhase = useGameStore((s) => s.setPhase);

  // Swap sonrası match kontrolü
  useEffect(() => {
    if (phase === 'swapping') {
      // Kısa bir delay sonra match kontrol et
      const timer = setTimeout(() => {
        completeMatchPhase();
      }, 200);
      return () => clearTimeout(timer);
    }
    if (phase === 'matching') {
      // Patlama animasyonu sonrası idle'a dön
      const timer = setTimeout(() => {
        // Yeni match var mı tekrar kontrol et
        completeMatchPhase();
      }, 400);
      return () => clearTimeout(timer);
    }
  }, [phase, completeMatchPhase]);

  const tapGesture = Gesture.Tap().onEnd((event) => {
    if (phase !== 'idle') return;

    const col = Math.floor(event.x / TILE_SIZE);
    const row = Math.floor(event.y / TILE_SIZE);

    if (row >= 0 && row < GRID_ROWS && col >= 0 && col < GRID_COLS) {
      selectTile(row, col);
    }
  });

  if (grid.length === 0) return null;

  return (
    <View style={styles.container}>
      <GestureDetector gesture={tapGesture}>
        <Canvas style={{ width: BOARD_WIDTH, height: BOARD_HEIGHT }}>
          {/* Grid arka planı */}
          <RoundedRect
            x={0}
            y={0}
            width={BOARD_WIDTH}
            height={BOARD_HEIGHT}
            r={12}
            color={GRID_BG_COLOR}
          />

          {/* Grid hücreleri */}
          {grid.map((row, r) =>
            row.map((tile, c) => {
              if (!tile) return null;

              const cx = c * TILE_SIZE + TILE_SIZE / 2;
              const cy = r * TILE_SIZE + TILE_SIZE / 2;
              const baseColor = TILE_COLORS[tile.color];
              const isSelected =
                selectedTile?.row === r && selectedTile?.col === c;

              return (
                <Group key={tile.id}>
                  {/* Hücre arka planı */}
                  <RoundedRect
                    x={c * TILE_SIZE + 2}
                    y={r * TILE_SIZE + 2}
                    width={TILE_SIZE - 4}
                    height={TILE_SIZE - 4}
                    r={8}
                    color="rgba(255,255,255,0.05)"
                  />

                  {/* Seçim göstergesi */}
                  {isSelected && (
                    <Circle
                      cx={cx}
                      cy={cy}
                      r={BALL_RADIUS + 4}
                      color="rgba(255,255,255,0.4)"
                      style="stroke"
                      strokeWidth={3}
                    />
                  )}

                  {/* Top gölgesi */}
                  <Circle
                    cx={cx + 1}
                    cy={cy + 2}
                    r={BALL_RADIUS}
                    color="rgba(0,0,0,0.3)"
                  />

                  {/* Top */}
                  <Circle
                    cx={cx}
                    cy={cy}
                    r={BALL_RADIUS}
                    color={baseColor}
                  />

                  {/* Parlak efekt (üstte küçük bir daire) */}
                  <Circle
                    cx={cx - BALL_RADIUS * 0.25}
                    cy={cy - BALL_RADIUS * 0.25}
                    r={BALL_RADIUS * 0.35}
                    color="rgba(255,255,255,0.3)"
                  />
                </Group>
              );
            })
          )}
        </Canvas>
      </GestureDetector>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    justifyContent: 'center',
  },
});
