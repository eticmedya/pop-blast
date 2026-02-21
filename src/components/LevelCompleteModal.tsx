import React, { useEffect, useCallback, useMemo } from 'react';
import { View, Text, StyleSheet, Image } from 'react-native';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withTiming,
  withDelay,
  withSpring,
  withRepeat,
  withSequence,
  Easing,
} from 'react-native-reanimated';
import { MaterialIcons, Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { useTranslation } from 'react-i18next';
import { useGameStore } from '../stores/gameStore';
import { getWorldTheme } from '../constants/themes';
import { SCREEN_WIDTH } from '../constants/dimensions';
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
      <Ionicons
        name={filled ? 'star' : 'star-outline'}
        size={48}
        color={filled ? '#F59E0B' : 'rgba(0,0,0,0.15)'}
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

  const worldTheme = useMemo(() => getWorldTheme(currentLevel), [currentLevel]);

  const bgOpacity = useSharedValue(0);
  const modalTranslateY = useSharedValue(300);
  const titleScale = useSharedValue(0);
  const buttonsOpacity = useSharedValue(0);
  const recordScale = useSharedValue(0);
  const recordPulse = useSharedValue(1);

  const previousHigh = getHighScore(currentLevel);
  const isNewRecord = !previousHigh || score > previousHigh.score;

  useEffect(() => {
    if (visible) {
      hapticService.success();

      bgOpacity.value = withTiming(0.7, { duration: 300 });
      modalTranslateY.value = withSpring(0, { damping: 12, stiffness: 100 });
      titleScale.value = withDelay(200, withSpring(1, { damping: 8, stiffness: 120 }));
      buttonsOpacity.value = withDelay(1800, withTiming(1, { duration: 400 }));

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
        <View style={styles.card}>
          <LinearGradient
            colors={['#FFFBF0', '#FFF5E1', '#FFEED4']}
            style={styles.cardGradient}
            start={{ x: 0, y: 0 }}
            end={{ x: 0, y: 1 }}
          >
            {/* Üst banner */}
            <LinearGradient
              colors={[worldTheme.accent, worldTheme.secondary]}
              style={styles.banner}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 0 }}
            >
              <Animated.View style={titleStyle}>
                <Text style={styles.title}>{t('levelComplete.title').toUpperCase()}</Text>
              </Animated.View>
            </LinearGradient>

            {/* Karakter */}
            <Image
              source={worldTheme.character}
              style={styles.character}
              resizeMode="contain"
            />

            {/* Yıldızlar */}
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

            {/* Ödül detayları */}
            <View style={styles.rewardSection}>
              <View style={styles.rewardRow}>
                <View style={styles.rewardLeft}>
                  <Ionicons name="trophy" size={18} color="#F59E0B" />
                  <Text style={styles.rewardLabel}>{t('game.score')}</Text>
                </View>
                <AnimatedScoreText targetScore={score} visible={visible} />
              </View>

              {streakMultiplier > 1 && (
                <View style={styles.rewardRow}>
                  <View style={styles.rewardLeft}>
                    <Ionicons name="flame" size={18} color="#EF4444" />
                    <Text style={styles.rewardLabel}>Streak Bonus</Text>
                  </View>
                  <Text style={styles.rewardMultiplier}>x{streakMultiplier}</Text>
                </View>
              )}
            </View>

            <Animated.View style={[styles.buttonsContainer, buttonsStyle]}>
              <AnimatedButton style={[styles.nextBtn, { shadowColor: worldTheme.accent }]} onPress={onNext}>
                <LinearGradient
                  colors={[worldTheme.accent, worldTheme.secondary]}
                  style={styles.nextBtnGradient}
                  start={{ x: 0, y: 0 }}
                  end={{ x: 1, y: 0 }}
                >
                  <Ionicons name="play-forward" size={20} color="#fff" />
                  <Text style={styles.nextText}>{t('levelComplete.nextLevel')}</Text>
                </LinearGradient>
              </AnimatedButton>
              <AnimatedButton style={styles.menuBtn} onPress={onMenu}>
                <Text style={styles.menuText}>{t('levelComplete.mainMenu')}</Text>
              </AnimatedButton>
            </Animated.View>
          </LinearGradient>
        </View>
      </Animated.View>
    </View>
  );
}

function AnimatedScoreText({ targetScore, visible }: { targetScore: number; visible: boolean }) {
  const [displayScore, setDisplayScore] = React.useState(0);

  useEffect(() => {
    if (visible) {
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
        clearTimeout(timeout);
      };
    } else {
      setDisplayScore(0);
    }
  }, [visible, targetScore]);

  return (
    <Text style={styles.rewardValue}>{displayScore.toLocaleString()}</Text>
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
    width: SCREEN_WIDTH * 0.85,
    zIndex: 201,
  },
  card: {
    borderRadius: 28,
    overflow: 'hidden',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 12 },
    shadowOpacity: 0.4,
    shadowRadius: 20,
    elevation: 16,
  },
  cardGradient: {
    alignItems: 'center',
    paddingBottom: 24,
  },
  banner: {
    width: '100%',
    paddingVertical: 20,
    alignItems: 'center',
  },
  title: {
    color: '#fff',
    fontSize: 26,
    fontWeight: '900',
    letterSpacing: 2,
    textShadowColor: 'rgba(0,0,0,0.3)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 4,
  },
  character: {
    width: 80,
    height: 80,
    marginTop: -20,
    marginBottom: 4,
  },
  starsRow: {
    flexDirection: 'row',
    gap: 12,
    marginBottom: 12,
  },
  starWrapper: {},
  recordBanner: {
    backgroundColor: '#F59E0B',
    paddingHorizontal: 22,
    paddingVertical: 8,
    borderRadius: 16,
    marginBottom: 12,
    shadowColor: '#F59E0B',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.5,
    shadowRadius: 8,
    elevation: 6,
  },
  recordText: {
    color: '#fff',
    fontSize: 14,
    fontWeight: '900',
    letterSpacing: 2,
  },
  rewardSection: {
    width: '85%',
    marginBottom: 8,
  },
  rewardRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: 'rgba(0,0,0,0.04)',
    paddingHorizontal: 16,
    paddingVertical: 12,
    borderRadius: 12,
    marginBottom: 6,
  },
  rewardLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  rewardLabel: {
    color: '#5D4037',
    fontSize: 15,
    fontWeight: '600',
  },
  rewardValue: {
    color: '#F59E0B',
    fontSize: 20,
    fontWeight: '900',
  },
  rewardMultiplier: {
    color: '#EF4444',
    fontSize: 20,
    fontWeight: '900',
  },
  buttonsContainer: {
    width: '85%',
    alignItems: 'center',
    marginTop: 8,
  },
  nextBtn: {
    width: '100%',
    borderRadius: 20,
    overflow: 'hidden',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.4,
    shadowRadius: 8,
    elevation: 6,
  },
  nextBtnGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    paddingVertical: 16,
  },
  nextText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '800',
  },
  menuBtn: {
    paddingVertical: 14,
    marginTop: 8,
  },
  menuText: {
    color: '#9E9E9E',
    fontSize: 14,
    fontWeight: '600',
  },
});
