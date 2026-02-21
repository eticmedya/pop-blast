import React from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { useGameStore } from '../stores/gameStore';
import { ACCENT_COLOR, SCORE_COLOR, TEXT_COLOR, BG_COLOR } from '../constants/colors';

export default function ScoreBar() {
  const score = useGameStore((s) => s.score);
  const movesLeft = useGameStore((s) => s.movesLeft);
  const comboMeter = useGameStore((s) => s.comboMeter);
  const levelConfig = useGameStore((s) => s.levelConfig);
  const currentLevel = useGameStore((s) => s.currentLevel);

  const targetScore = levelConfig?.targetScore ?? 0;
  const progress = Math.min(1, score / Math.max(1, targetScore));

  return (
    <View style={styles.container}>
      <View style={styles.topRow}>
        <View style={styles.levelBadge}>
          <Text style={styles.levelText}>Seviye {currentLevel}</Text>
        </View>
        <View style={styles.scoreContainer}>
          <Text style={styles.scoreLabel}>SKOR</Text>
          <Text style={styles.scoreValue}>{score.toLocaleString()}</Text>
        </View>
        <View style={styles.movesContainer}>
          <Text style={styles.movesValue}>{movesLeft}</Text>
          <Text style={styles.movesLabel}>Hamle</Text>
        </View>
      </View>

      {/* Hedef skor progress bar */}
      <View style={styles.progressContainer}>
        <View style={styles.progressBg}>
          <View style={[styles.progressFill, { width: `${progress * 100}%` }]} />
        </View>
        <Text style={styles.targetText}>{targetScore.toLocaleString()}</Text>
      </View>

      {/* Combo metre */}
      <View style={styles.comboContainer}>
        <Text style={styles.comboLabel}>COMBO</Text>
        <View style={styles.comboBg}>
          <View style={[styles.comboFill, { width: `${comboMeter}%` }]} />
        </View>
        {comboMeter >= 100 && (
          <Text style={styles.cannonReady}>CANNON!</Text>
        )}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    backgroundColor: 'rgba(26, 26, 46, 0.9)',
    borderBottomLeftRadius: 16,
    borderBottomRightRadius: 16,
  },
  topRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 8,
  },
  levelBadge: {
    backgroundColor: ACCENT_COLOR,
    paddingHorizontal: 12,
    paddingVertical: 4,
    borderRadius: 12,
  },
  levelText: {
    color: TEXT_COLOR,
    fontWeight: 'bold',
    fontSize: 14,
  },
  scoreContainer: {
    alignItems: 'center',
  },
  scoreLabel: {
    color: 'rgba(255,255,255,0.6)',
    fontSize: 10,
    fontWeight: '600',
  },
  scoreValue: {
    color: SCORE_COLOR,
    fontSize: 22,
    fontWeight: 'bold',
  },
  movesContainer: {
    alignItems: 'center',
    backgroundColor: 'rgba(255,255,255,0.1)',
    paddingHorizontal: 14,
    paddingVertical: 4,
    borderRadius: 12,
  },
  movesValue: {
    color: TEXT_COLOR,
    fontSize: 20,
    fontWeight: 'bold',
  },
  movesLabel: {
    color: 'rgba(255,255,255,0.6)',
    fontSize: 10,
  },
  progressContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    marginBottom: 6,
  },
  progressBg: {
    flex: 1,
    height: 8,
    backgroundColor: 'rgba(255,255,255,0.1)',
    borderRadius: 4,
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
    backgroundColor: SCORE_COLOR,
    borderRadius: 4,
  },
  targetText: {
    color: 'rgba(255,255,255,0.5)',
    fontSize: 11,
    fontWeight: '600',
    minWidth: 45,
    textAlign: 'right',
  },
  comboContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  comboLabel: {
    color: 'rgba(255,255,255,0.5)',
    fontSize: 10,
    fontWeight: '700',
    minWidth: 42,
  },
  comboBg: {
    flex: 1,
    height: 6,
    backgroundColor: 'rgba(255,255,255,0.1)',
    borderRadius: 3,
    overflow: 'hidden',
  },
  comboFill: {
    height: '100%',
    backgroundColor: ACCENT_COLOR,
    borderRadius: 3,
  },
  cannonReady: {
    color: ACCENT_COLOR,
    fontSize: 11,
    fontWeight: 'bold',
  },
});
