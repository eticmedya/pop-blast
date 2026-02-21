import React, { useEffect, useMemo } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withRepeat,
  withSequence,
  withTiming,
  withDelay,
  withSpring,
  Easing,
} from 'react-native-reanimated';
import { useTranslation } from 'react-i18next';
import { Ionicons } from '@expo/vector-icons';
import { TEXT_COLOR, ACCENT_COLOR, SCORE_COLOR, TILE_COLORS } from '../constants/colors';
import { useDailyRewardStore } from '../stores/dailyRewardStore';
import { useGameStore } from '../stores/gameStore';
import GradientBackground from '../components/GradientBackground';
import AnimatedButton from '../components/AnimatedButton';

interface Props {
  onPlay: () => void;
  onContinue?: () => void;
  onSettings: () => void;
  onDailyReward: () => void;
}

function FloatingBall({ color, delay, x, y }: { color: string; delay: number; x: number; y: number }) {
  const translateY = useSharedValue(0);
  const translateX = useSharedValue(0);
  const opacity = useSharedValue(0);

  useEffect(() => {
    opacity.value = withDelay(delay, withTiming(0.6, { duration: 500 }));
    translateY.value = withDelay(
      delay,
      withRepeat(
        withSequence(
          withTiming(-15, { duration: 2000 + Math.random() * 1000, easing: Easing.inOut(Easing.ease) }),
          withTiming(15, { duration: 2000 + Math.random() * 1000, easing: Easing.inOut(Easing.ease) })
        ),
        -1,
        true
      )
    );
    translateX.value = withDelay(
      delay,
      withRepeat(
        withSequence(
          withTiming(8, { duration: 3000, easing: Easing.inOut(Easing.ease) }),
          withTiming(-8, { duration: 3000, easing: Easing.inOut(Easing.ease) })
        ),
        -1,
        true
      )
    );
  }, []);

  const animStyle = useAnimatedStyle(() => ({
    transform: [{ translateY: translateY.value }, { translateX: translateX.value }],
    opacity: opacity.value,
  }));

  return (
    <Animated.View
      style={[
        styles.floatingBall,
        { backgroundColor: color, left: x, top: y },
        animStyle,
      ]}
    />
  );
}

export default function MenuScreen({ onPlay, onContinue, onSettings, onDailyReward }: Props) {
  const { t } = useTranslation();
  const lastClaimDate = useDailyRewardStore((s) => s.lastClaimDate);
  const hasActiveGame = useGameStore((s) => s.hasActiveGame);
  const activeLevel = useGameStore((s) => s.currentLevel);

  const canClaim = useMemo(() => {
    if (!lastClaimDate) return true;
    return lastClaimDate !== new Date().toISOString().split('T')[0];
  }, [lastClaimDate]);

  const titleScale = useSharedValue(0.8);
  const titleOpacity = useSharedValue(0);
  const btnScale = useSharedValue(1);

  useEffect(() => {
    titleOpacity.value = withTiming(1, { duration: 600 });
    titleScale.value = withSpring(1, { damping: 8 });
    btnScale.value = withDelay(
      400,
      withRepeat(
        withSequence(
          withTiming(1.04, { duration: 800, easing: Easing.inOut(Easing.ease) }),
          withTiming(1, { duration: 800, easing: Easing.inOut(Easing.ease) })
        ),
        -1,
        true
      )
    );
  }, []);

  const titleAnimStyle = useAnimatedStyle(() => ({
    transform: [{ scale: titleScale.value }],
    opacity: titleOpacity.value,
  }));

  const btnAnimStyle = useAnimatedStyle(() => ({
    transform: [{ scale: btnScale.value }],
  }));

  const floatingBalls = [
    { color: TILE_COLORS[0], delay: 0, x: 30, y: 120 },
    { color: TILE_COLORS[1], delay: 200, x: 280, y: 80 },
    { color: TILE_COLORS[2], delay: 400, x: 60, y: 500 },
    { color: TILE_COLORS[3], delay: 600, x: 300, y: 450 },
    { color: TILE_COLORS[4], delay: 300, x: 180, y: 600 },
    { color: TILE_COLORS[5], delay: 500, x: 320, y: 250 },
  ];

  return (
    <GradientBackground colors={['#1A0533', '#0F0F23', '#0A1628']}>
      <View style={styles.content}>
        {floatingBalls.map((ball, i) => (
          <FloatingBall key={i} {...ball} />
        ))}

        <Animated.View style={[styles.titleContainer, titleAnimStyle]}>
          <Text style={styles.titlePop}>POP</Text>
          <Text style={styles.titleBlast}>BLAST</Text>
        </Animated.View>

        <Text style={styles.subtitle}>{t('menu.subtitle')}</Text>

        <View style={styles.ballRow}>
          {TILE_COLORS.map((color, i) => (
            <View key={i} style={[styles.ball, { backgroundColor: color }]} />
          ))}
        </View>

        <Animated.View style={btnAnimStyle}>
          <AnimatedButton style={styles.playBtn} onPress={onPlay}>
            <Text style={styles.playText}>{t('menu.play')}</Text>
          </AnimatedButton>
        </Animated.View>

        {hasActiveGame && onContinue && (
          <AnimatedButton style={styles.continueBtn} onPress={onContinue}>
            <Ionicons name="play-circle" size={20} color={SCORE_COLOR} />
            <Text style={styles.continueText}>
              {t('menu.continue', { level: activeLevel })}
            </Text>
          </AnimatedButton>
        )}

        <View style={styles.bottomRow}>
          <AnimatedButton style={styles.settingsBtn} onPress={onSettings}>
            <Text style={styles.settingsText}>{t('menu.settings')}</Text>
          </AnimatedButton>

          {canClaim && (
            <AnimatedButton style={styles.rewardBtn} onPress={onDailyReward}>
              <Text style={styles.rewardText}>{t('menu.dailyReward')}</Text>
            </AnimatedButton>
          )}
        </View>
      </View>
    </GradientBackground>
  );
}

const styles = StyleSheet.create({
  content: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 32,
  },
  floatingBall: {
    position: 'absolute',
    width: 24,
    height: 24,
    borderRadius: 12,
  },
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'baseline',
    marginBottom: 8,
  },
  titlePop: {
    fontSize: 60,
    fontWeight: '900',
    color: ACCENT_COLOR,
    letterSpacing: 3,
    textShadowColor: 'rgba(255,107,53,0.4)',
    textShadowOffset: { width: 0, height: 4 },
    textShadowRadius: 12,
  },
  titleBlast: {
    fontSize: 60,
    fontWeight: '900',
    color: SCORE_COLOR,
    letterSpacing: 3,
    marginLeft: 6,
    textShadowColor: 'rgba(255,215,0,0.4)',
    textShadowOffset: { width: 0, height: 4 },
    textShadowRadius: 12,
  },
  subtitle: {
    color: 'rgba(255,255,255,0.35)',
    fontSize: 14,
    letterSpacing: 5,
    marginBottom: 48,
    textTransform: 'uppercase',
  },
  ballRow: {
    flexDirection: 'row',
    gap: 14,
    marginBottom: 60,
  },
  ball: {
    width: 28,
    height: 28,
    borderRadius: 14,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
    elevation: 4,
  },
  playBtn: {
    backgroundColor: ACCENT_COLOR,
    paddingHorizontal: 72,
    paddingVertical: 18,
    borderRadius: 24,
    shadowColor: ACCENT_COLOR,
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.5,
    shadowRadius: 16,
    elevation: 10,
  },
  playText: {
    color: TEXT_COLOR,
    fontSize: 26,
    fontWeight: '900',
    letterSpacing: 6,
  },
  continueBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
    marginTop: 16,
    paddingHorizontal: 24,
    paddingVertical: 12,
    borderRadius: 16,
    backgroundColor: 'rgba(255,215,0,0.08)',
    borderWidth: 1,
    borderColor: 'rgba(255,215,0,0.25)',
  },
  continueText: {
    color: SCORE_COLOR,
    fontSize: 15,
    fontWeight: '700',
  },
  bottomRow: {
    flexDirection: 'row',
    gap: 16,
    marginTop: 40,
  },
  settingsBtn: {
    paddingHorizontal: 16,
    paddingVertical: 10,
    borderRadius: 12,
    backgroundColor: 'rgba(255,255,255,0.06)',
  },
  settingsText: {
    color: 'rgba(255,255,255,0.5)',
    fontSize: 13,
    fontWeight: '600',
  },
  rewardBtn: {
    paddingHorizontal: 16,
    paddingVertical: 10,
    borderRadius: 12,
    backgroundColor: 'rgba(255,215,0,0.1)',
    borderWidth: 1,
    borderColor: 'rgba(255,215,0,0.3)',
  },
  rewardText: {
    color: SCORE_COLOR,
    fontSize: 13,
    fontWeight: '600',
  },
});
