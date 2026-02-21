import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { useGameStore } from '../stores/gameStore';
import { ACCENT_COLOR, SCORE_COLOR } from '../constants/colors';

export default function StreakDisplay() {
  const consecutiveWins = useGameStore((s) => s.consecutiveWins);
  const streakMultiplier = useGameStore((s) => s.streakMultiplier);

  if (streakMultiplier <= 1) return null;

  return (
    <View style={styles.container}>
      <MaterialCommunityIcons name="fire" size={14} color={ACCENT_COLOR} />
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
  multiplier: {
    color: SCORE_COLOR,
    fontSize: 13,
    fontWeight: 'bold',
  },
});
