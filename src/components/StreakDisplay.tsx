import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { useGameStore } from '../stores/gameStore';
import { ACCENT_COLOR, SCORE_COLOR } from '../constants/colors';

export default function StreakDisplay() {
  const consecutiveWins = useGameStore((s) => s.consecutiveWins);
  const streakMultiplier = useGameStore((s) => s.streakMultiplier);

  if (streakMultiplier <= 1) return null;

  return (
    <View style={styles.container}>
      <Text style={styles.flame}>🔥</Text>
      <Text style={styles.multiplier}>x{streakMultiplier}</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(255,107,53,0.2)',
    paddingHorizontal: 8,
    paddingVertical: 3,
    borderRadius: 10,
    gap: 2,
  },
  flame: {
    fontSize: 12,
  },
  multiplier: {
    color: SCORE_COLOR,
    fontSize: 13,
    fontWeight: 'bold',
  },
});
