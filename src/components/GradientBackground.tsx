import React from 'react';
import { ColorValue, StyleSheet } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';

interface Props {
  colors?: [ColorValue, ColorValue, ...ColorValue[]];
  children?: React.ReactNode;
}

export default function GradientBackground({ colors, children }: Props) {
  const gradientColors: [ColorValue, ColorValue, ...ColorValue[]] = colors ?? ['#0F0F23', '#1A1A2E', '#16213E'];

  return (
    <LinearGradient
      colors={gradientColors}
      style={styles.gradient}
      start={{ x: 0, y: 0 }}
      end={{ x: 1, y: 1 }}
    >
      {children}
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  gradient: {
    flex: 1,
  },
});
