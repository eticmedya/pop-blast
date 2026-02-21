import React, { useEffect, useCallback } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withTiming,
  withDelay,
  withSpring,
  withRepeat,
  withSequence,
  runOnJS,
  Easing,
} from 'react-native-reanimated';
import { MaterialIcons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { useTranslation } from 'react-i18next';
import { useGameStore } from '../stores/gameStore';
import { ACCENT_COLOR, TEXT_COLOR, SCORE_COLOR } from '../constants/colors';
import { hapticService } from '../services/HapticService';
import AnimatedButton from './AnimatedButton';
import Confetti from './Confetti';

interface Props {
  visible: boolean;
  onNext: () => void;
  onMenu: () => void;
}

function AnimatedStar({ filled, index }: { filled: boolean; index: number }) {
  const scale = useSharedValue(0);
  const rotation = useSharedValue(0);

  useEffect(() => {
    if (filled) {
      const delay = 500 + index * 300;
      scale.value = withDelay(
        delay,
        withSpring(1, { damping: 6, stiffness: 150, mass: 0.8 })
      );
      rotation.value = withDelay(
        delay,
        withSpring(360, { damping: 12, stiffness: 80 })
      );
    } else {
      scale.value = withDelay(500 + index * 300, withTiming(1, { duration: 300 }));
    }
  }, [filled, index]);

  const animStyle = useAnimatedStyle(() => ({
    transform: [
      { scale: scale.value },
      { rotate: `${rotation.value}deg` },
    ],
  }));

  return (
    <Animated.View style={[styles.starWrapper, animStyle]}>
      <MaterialIcons
        name="star"
        size={48}
        color={filled ? SCORE_COLOR : 'rgba(255,255,255,0.2)'}
      />
    </Animated.View>
  );
}

export default function LevelCompleteModal({ visible, onNext, onMenu }: Props) {
  const { t } = useTranslation();
  const score = useGameStore((s) => s.score);
  const stars = useGameStore((s) => s.stars);
  const currentLevel = useGameStore((s) => s.currentLevel);
  const streakMultiplier = useGameStore((s) => s.streakMultiplier);
  const getHighScore = useGameStore((s) => s.getHighScore);

  const bgOpacity = useSharedValue(0);
  const modalTranslateY = useSharedValue(300);
  const titleScale = useSharedValue(0);
  const scoreDisplay = useSharedValue(0);
  const buttonsOpacity = useSharedValue(0);
  const recordScale = useSharedValue(0);
  const recordPulse = useSharedValue(1);

  const previousHigh = getHighScore(currentLevel);
  const isNewRecord = !previousHigh || score > previousHigh.score;

  useEffect(() => {
    if (visible) {
      hapticService.success();

      bgOpacity.value = withTiming(0.8, { duration: 300 });
      modalTranslateY.value = withSpring(0, { damping: 12, stiffness: 100 });
      titleScale.value = withDelay(200, withSpring(1, { damping: 8, stiffness: 120 }));

      // Animate score counting up
      scoreDisplay.value = withDelay(
        1400,
        withTiming(score, { duration: 800, easing: Easing.out(Easing.quad) })
      );

      // Buttons appear after stars
      buttonsOpacity.value = withDelay(1800, withTiming(1, { duration: 400 }));

      // New record banner
      if (isNewRecord) {
        recordScale.value = withDelay(1600, withSpring(1, { damping: 8, stiffness: 120 }));
        recordPulse.value = withDelay(
          2000,
          withRepeat(
            withSequence(
              withTiming(1.08, { duration: 600, easing: Easing.inOut(Easing.ease) }),
              withTiming(1, { duration: 600, easing: Easing.inOut(Easing.ease) })
            ),
            -1,
            true
          )
        );
      }
    } else {
      bgOpacity.value = 0;
      modalTranslateY.value = 300;
      titleScale.value = 0;
      scoreDisplay.value = 0;
      buttonsOpacity.value = 0;
      recordScale.value = 0;
      recordPulse.value = 1;
    }
  }, [visible]);

  const bgStyle = useAnimatedStyle(() => ({
    opacity: bgOpacity.value,
  }));

  const modalStyle = useAnimatedStyle(() => ({
    transform: [{ translateY: modalTranslateY.value }],
  }));

  const titleStyle = useAnimatedStyle(() => ({
    transform: [{ scale: titleScale.value }],
  }));

  const scoreStyle = useAnimatedStyle(() => ({
    opacity: 1,
  }));

  const scoreTextStyle = useAnimatedStyle(() => {
    const displayVal = Math.round(scoreDisplay.value);
    return {
      // We can't directly set text in animated style,
      // but we use this to track the value
    };
  });

  const buttonsStyle = useAnimatedStyle(() => ({
    opacity: buttonsOpacity.value,
  }));

  const recordStyle = useAnimatedStyle(() => ({
    transform: [
      { scale: recordScale.value * recordPulse.value },
    ],
  }));

  if (!visible) return null;

  return (
    <View style={styles.fullScreen}>
      <Animated.View style={[styles.overlay, bgStyle]} />
      <Confetti visible={visible} />

      <Animated.View style={[styles.modalContainer, modalStyle]}>
        <LinearGradient
          colors={['#2A1A4E', '#1A1A2E', '#0F1A2E']}
          style={styles.modal}
          start={{ x: 0, y: 0 }}
          end={{ x: 1, y: 1 }}
        >
          <Animated.View style={titleStyle}>
            <Text style={styles.title}>{t('levelComplete.title')}</Text>
          </Animated.View>

          <Text style={styles.level}>
            {t('levelComplete.level', { number: currentLevel })}
          </Text>

          <View style={styles.starsRow}>
            {Array.from({ length: 3 }, (_, i) => (
              <AnimatedStar key={i} filled={i < stars} index={i} />
            ))}
          </View>

          {isNewRecord && (
            <Animated.View style={[styles.recordBanner, recordStyle]}>
              <Text style={styles.recordText}>{t('levelComplete.newRecord')}</Text>
            </Animated.View>
          )}

          <Animated.View style={[styles.scoreRow, scoreStyle]}>
            <Text style={styles.scoreLabel}>{t('game.score')}</Text>
            <AnimatedScoreText targetScore={score} visible={visible} />
          </Animated.View>

          {streakMultiplier > 1 && (
            <View style={styles.streakRow}>
              <Text style={styles.streakLabel}>Streak Bonus</Text>
              <Text style={styles.streakValue}>x{streakMultiplier}</Text>
            </View>
          )}

          <Animated.View style={[styles.buttonsContainer, buttonsStyle]}>
            <AnimatedButton style={styles.nextBtn} onPress={onNext}>
              <Text style={styles.nextText}>{t('levelComplete.nextLevel')}</Text>
            </AnimatedButton>
            <AnimatedButton style={styles.menuBtn} onPress={onMenu}>
              <Text style={styles.menuText}>{t('levelComplete.mainMenu')}</Text>
            </AnimatedButton>
          </Animated.View>
        </LinearGradient>
      </Animated.View>
    </View>
  );
}

function AnimatedScoreText({ targetScore, visible }: { targetScore: number; visible: boolean }) {
  const animValue = useSharedValue(0);
  const [displayScore, setDisplayScore] = React.useState(0);

  const updateDisplay = useCallback((val: number) => {
    setDisplayScore(Math.round(val));
  }, []);

  useEffect(() => {
    if (visible) {
      animValue.value = 0;
      animValue.value = withDelay(
        1400,
        withTiming(targetScore, {
          duration: 800,
          easing: Easing.out(Easing.quad),
        })
      );

      // Poll the value for display
      const interval = setInterval(() => {
        // Using a timeout-based approach for the counting animation
      }, 16);

      // Simple fallback: animate with setTimeout
      let start: number | null = null;
      const duration = 800;
      const delayMs = 1400;

      const timeout = setTimeout(() => {
        const animFrame = (timestamp: number) => {
          if (!start) start = timestamp;
          const elapsed = timestamp - start;
          const progress = Math.min(elapsed / duration, 1);
          const eased = 1 - Math.pow(1 - progress, 2);
          setDisplayScore(Math.round(eased * targetScore));
          if (progress < 1) {
            requestAnimationFrame(animFrame);
          }
        };
        requestAnimationFrame(animFrame);
      }, delayMs);

      return () => {
        clearInterval(interval);
        clearTimeout(timeout);
      };
    } else {
      setDisplayScore(0);
    }
  }, [visible, targetScore]);

  return (
    <Text style={styles.scoreValue}>{displayScore.toLocaleString()}</Text>
  );
}

const styles = StyleSheet.create({
  fullScreen: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    justifyContent: 'center',
    alignItems: 'center',
    zIndex: 200,
  },
  overlay: {
    ...StyleSheet.absoluteFillObject,
    backgroundColor: '#000',
  },
  modalContainer: {
    width: '82%',
    zIndex: 201,
  },
  modal: {
    borderRadius: 28,
    padding: 32,
    alignItems: 'center',
    borderWidth: 2,
    borderColor: SCORE_COLOR,
    shadowColor: SCORE_COLOR,
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.3,
    shadowRadius: 20,
    elevation: 12,
  },
  title: {
    color: SCORE_COLOR,
    fontSize: 32,
    fontWeight: '900',
    marginBottom: 4,
  },
  level: {
    color: 'rgba(255,255,255,0.5)',
    fontSize: 14,
    marginBottom: 16,
  },
  starsRow: {
    flexDirection: 'row',
    gap: 12,
    marginBottom: 16,
  },
  starWrapper: {
    // empty wrapper for animated styles
  },
  recordBanner: {
    backgroundColor: SCORE_COLOR,
    paddingHorizontal: 20,
    paddingVertical: 6,
    borderRadius: 14,
    marginBottom: 16,
    shadowColor: SCORE_COLOR,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.5,
    shadowRadius: 8,
    elevation: 6,
  },
  recordText: {
    color: '#1A1A2E',
    fontSize: 16,
    fontWeight: '900',
    letterSpacing: 2,
  },
  scoreRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '100%',
    marginBottom: 8,
  },
  scoreLabel: {
    color: 'rgba(255,255,255,0.6)',
    fontSize: 16,
  },
  scoreValue: {
    color: SCORE_COLOR,
    fontSize: 20,
    fontWeight: 'bold',
  },
  streakRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '100%',
    marginBottom: 8,
  },
  streakLabel: {
    color: 'rgba(255,255,255,0.6)',
    fontSize: 14,
  },
  streakValue: {
    color: ACCENT_COLOR,
    fontSize: 18,
    fontWeight: 'bold',
  },
  buttonsContainer: {
    width: '100%',
    alignItems: 'center',
  },
  nextBtn: {
    backgroundColor: ACCENT_COLOR,
    paddingHorizontal: 40,
    paddingVertical: 14,
    borderRadius: 18,
    marginTop: 24,
    width: '100%',
    alignItems: 'center',
    shadowColor: ACCENT_COLOR,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.4,
    shadowRadius: 8,
    elevation: 6,
  },
  nextText: {
    color: TEXT_COLOR,
    fontSize: 18,
    fontWeight: 'bold',
  },
  menuBtn: {
    paddingVertical: 12,
    marginTop: 12,
  },
  menuText: {
    color: 'rgba(255,255,255,0.4)',
    fontSize: 14,
  },
});
