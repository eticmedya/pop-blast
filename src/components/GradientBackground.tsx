import React, { useMemo } from 'react';
import { ColorValue, StyleSheet, View } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { SCREEN_WIDTH, SCREEN_HEIGHT } from '../constants/dimensions';

interface Props {
  colors?: [ColorValue, ColorValue, ...ColorValue[]];
  children?: React.ReactNode;
  /** Dekoratif baloncuklar gösterilsin mi */
  showBubbles?: boolean;
  /** Baloncuk renkleri */
  bubbleColors?: string[];
}

// Sabit pozisyonlar (her render'da aynı kalır)
const BUBBLE_CONFIGS = [
  { left: '8%', top: '5%', size: 80, opacity: 0.08 },
  { left: '75%', top: '12%', size: 120, opacity: 0.06 },
  { left: '60%', top: '65%', size: 100, opacity: 0.07 },
  { left: '15%', top: '78%', size: 60, opacity: 0.09 },
  { left: '85%', top: '45%', size: 90, opacity: 0.05 },
  { left: '35%', top: '88%', size: 70, opacity: 0.08 },
  { left: '5%', top: '40%', size: 50, opacity: 0.1 },
  { left: '90%', top: '80%', size: 110, opacity: 0.04 },
];

export default function GradientBackground({ colors, children, showBubbles = false, bubbleColors }: Props) {
  const gradientColors: [ColorValue, ColorValue, ...ColorValue[]] = colors ?? ['#0F0F23', '#1A1A2E', '#16213E'];

  const bubbles = useMemo(() => {
    if (!showBubbles) return null;
    const bColors = bubbleColors ?? ['#fff'];
    return BUBBLE_CONFIGS.map((cfg, i) => (
      <View
        key={i}
        style={{
          position: 'absolute',
          left: cfg.left as unknown as number,
          top: cfg.top as unknown as number,
          width: cfg.size,
          height: cfg.size,
          borderRadius: cfg.size / 2,
          backgroundColor: bColors[i % bColors.length],
          opacity: cfg.opacity,
        }}
      />
    ));
  }, [showBubbles, bubbleColors]);

  return (
    <LinearGradient
      colors={gradientColors}
      style={styles.gradient}
      start={{ x: 0, y: 0 }}
      end={{ x: 0.3, y: 1 }}
    >
      {bubbles}
      {children}
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  gradient: {
    flex: 1,
  },
});
