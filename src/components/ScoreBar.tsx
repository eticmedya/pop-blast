import React, { useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withRepeat,
  withSequence,
  withTiming,
  Easing,
} from 'react-native-reanimated';
import { useTranslation } from 'react-i18next';
import { useGameStore } from '../stores/gameStore';
import { ACCENT_COLOR, SCORE_COLOR, TEXT_COLOR, DANGER_COLOR } from '../constants/colors';
import LivesDisplay from './LivesDisplay';
import StreakDisplay from './StreakDisplay';

export default function ScoreBar() {
  const { t } = useTranslation();
  const score = useGameStore((s) => s.score);
  const movesLeft = useGameStore((s) => s.movesLeft);
  const comboMeter = useGameStore((s) => s.comboMeter);
  const levelConfig = useGameStore((s) => s.levelConfig);
  const currentLevel = useGameStore((s) => s.currentLevel);

  const targetScore = levelConfig?.targetScore ?? 0;
  const progress = Math.min(1, score / Math.max(1, targetScore));

  const pulseScale = useSharedValue(1);

  // Pulse animation when moves <= 3
  useEffect(() => {
    if (movesLeft <= 3 && movesLeft > 0) {
      pulseScale.value = withRepeat(
        withSequence(
          withTiming(1.15, { duration: 400, easing: Easing.inOut(Easing.ease) }),
          withTiming(1, { duration: 400, easing: Easing.inOut(Easing.ease) })
        ),
        -1,
        true
      );
    } else {
      pulseScale.value = withTiming(1, { duration: 200 });
    }
  }, [movesLeft]);

  const movesPulseStyle = useAnimatedStyle(() => ({
    transform: [{ scale: pulseScale.value }],
  }));

  // Determine moves color
  const movesColor = movesLeft <= 5 ? DANGER_COLOR : TEXT_COLOR;

  // Combo bar color changes as it fills
  const comboColor =
    comboMeter >= 80
      ? '#FF4757'
      : comboMeter >= 50
      ? '#FFA502'
      : comboMeter >= 25
      ? '#FBBF24'
      : ACCENT_COLOR;

  return (
    <View style={styles.container}>
      <View style={styles.topRow}>
        <View style={styles.leftCol}>
          <View style={styles.levelBadge}>
            <Text style={styles.levelText}>
              {t('game.level', { number: currentLevel })}
            </Text>
          </View>
          <StreakDisplay />
        </View>

        <View style={styles.scoreContainer}>
          <Text style={styles.scoreLabel}>{t('game.score')}</Text>
          <Text style={styles.scoreValue}>{score.toLocaleString()}</Text>
        </View>

        <View style={styles.rightCol}>
          <View style={styles.movesContainer}>
            <Animated.View style={movesPulseStyle}>
              <Text style={[styles.movesValue, { color: movesColor }]}>
                {movesLeft}
              </Text>
            </Animated.View>
            <Text style={styles.movesLabel}>{t('game.moves')}</Text>
          </View>
          <LivesDisplay />
        </View>
      </View>

      {/* Target progress bar */}
      <View style={styles.progressContainer}>
        <View style={styles.progressBg}>
          <View
            style={[
              styles.progressFill,
              { width: `${progress * 100}%` },
            ]}
          />
        </View>
        <Text style={styles.targetText}>{targetScore.toLocaleString()}</Text>
      </View>

      {/* Combo meter */}
      <View style={styles.comboContainer}>
        <Text style={styles.comboLabel}>{t('game.combo')}</Text>
        <View style={styles.comboBg}>
          <View
            style={[
              styles.comboFill,
              { width: `${comboMeter}%`, backgroundColor: comboColor },
            ]}
          />
        </View>
        {comboMeter >= 100 && (
          <Text style={styles.cannonReady}>{t('game.cannon')}</Text>
        )}
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    paddingHorizontal: 16,
    paddingVertical: 8,
    backgroundColor: 'rgba(26, 26, 46, 0.95)',
    borderBottomLeftRadius: 20,
    borderBottomRightRadius: 20,
    borderBottomWidth: 1,
    borderBottomColor: 'rgba(255,255,255,0.05)',
  },
  topRow: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    marginBottom: 8,
  },
  leftCol: {
    alignItems: 'flex-start',
    gap: 4,
    flex: 1,
  },
  rightCol: {
    alignItems: 'flex-end',
    gap: 4,
    flex: 1,
  },
  levelBadge: {
    backgroundColor: ACCENT_COLOR,
    paddingHorizontal: 12,
    paddingVertical: 4,
    borderRadius: 12,
    shadowColor: ACCENT_COLOR,
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
    elevation: 3,
  },
  levelText: {
    color: TEXT_COLOR,
    fontWeight: 'bold',
    fontSize: 13,
  },
  scoreContainer: {
    alignItems: 'center',
  },
  scoreLabel: {
    color: 'rgba(255,255,255,0.5)',
    fontSize: 10,
    fontWeight: '700',
    letterSpacing: 1,
  },
  scoreValue: {
    color: SCORE_COLOR,
    fontSize: 24,
    fontWeight: 'bold',
  },
  movesContainer: {
    alignItems: 'center',
    backgroundColor: 'rgba(255,255,255,0.08)',
    paddingHorizontal: 14,
    paddingVertical: 4,
    borderRadius: 12,
  },
  movesValue: {
    fontSize: 28,
    fontWeight: '900',
  },
  movesLabel: {
    color: 'rgba(255,255,255,0.5)',
    fontSize: 9,
    fontWeight: '600',
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
    backgroundColor: 'rgba(255,255,255,0.08)',
    borderRadius: 4,
    overflow: 'hidden',
  },
  progressFill: {
    height: '100%',
    backgroundColor: SCORE_COLOR,
    borderRadius: 4,
  },
  targetText: {
    color: 'rgba(255,255,255,0.4)',
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
    color: 'rgba(255,255,255,0.4)',
    fontSize: 10,
    fontWeight: '700',
    minWidth: 42,
  },
  comboBg: {
    flex: 1,
    height: 6,
    backgroundColor: 'rgba(255,255,255,0.08)',
    borderRadius: 3,
    overflow: 'hidden',
  },
  comboFill: {
    height: '100%',
    borderRadius: 3,
  },
  cannonReady: {
    color: ACCENT_COLOR,
    fontSize: 11,
    fontWeight: 'bold',
  },
});
