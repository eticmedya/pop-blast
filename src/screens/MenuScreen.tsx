import React, { useEffect, useMemo } from 'react';
import { View, Text, StyleSheet, Image } from 'react-native';
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
import { LinearGradient } from 'expo-linear-gradient';
import { useTranslation } from 'react-i18next';
import { Ionicons } from '@expo/vector-icons';
import { TILE_COLORS } from '../constants/colors';
import { useDailyRewardStore } from '../stores/dailyRewardStore';
import { useGameStore } from '../stores/gameStore';
import GradientBackground from '../components/GradientBackground';
import AnimatedButton from '../components/AnimatedButton';
import { SCREEN_WIDTH } from '../constants/dimensions';

interface Props {
  onPlay: () => void;
  onContinue?: () => void;
  onSettings: () => void;
  onDailyReward: () => void;
}

function FloatingEmoji({ emoji, delay, x, y }: { emoji: string; delay: number; x: number; y: number }) {
  const translateY = useSharedValue(0);
  const translateX = useSharedValue(0);
  const opacity = useSharedValue(0);

  useEffect(() => {
    opacity.value = withDelay(delay, withTiming(0.5, { duration: 500 }));
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
        styles.floatingEmoji,
        { left: x, top: y },
        animStyle,
      ]}
    >
      <Text style={styles.floatingEmojiText}>{emoji}</Text>
    </Animated.View>
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

  const floatingEmojis = [
    { emoji: '🍬', delay: 0, x: 30, y: 120 },
    { emoji: '🐵', delay: 200, x: SCREEN_WIDTH - 70, y: 90 },
    { emoji: '🍭', delay: 400, x: 50, y: 480 },
    { emoji: '🐧', delay: 600, x: SCREEN_WIDTH - 80, y: 440 },
    { emoji: '💎', delay: 300, x: SCREEN_WIDTH / 2 - 10, y: 580 },
    { emoji: '🦁', delay: 500, x: SCREEN_WIDTH - 50, y: 260 },
    { emoji: '🍩', delay: 150, x: 20, y: 300 },
    { emoji: '🌟', delay: 450, x: SCREEN_WIDTH / 2 + 40, y: 150 },
  ];

  return (
    <GradientBackground
      colors={['#7B2FF7', '#4A90D9', '#67D5B5', '#A8E6CF']}
      showBubbles
      bubbleColors={['#FF6B9D', '#C471ED', '#12CBC4', '#FFC312', '#A3CB38', '#FDA7DF']}
    >
      <View style={styles.content}>
        {floatingEmojis.map((item, i) => (
          <FloatingEmoji key={i} {...item} />
        ))}

        <Animated.View style={[styles.titleContainer, titleAnimStyle]}>
          <Text style={styles.titlePop}>POP</Text>
          <Text style={styles.titleBlast}>BLAST</Text>
        </Animated.View>

        <Text style={styles.subtitle}>{t('menu.subtitle')}</Text>

        {/* Emoji satırı */}
        <View style={styles.emojiRow}>
          {['🍬', '🐙', '🔥', '🌟', '💎', '🍓'].map((e, i) => (
            <View key={i} style={[styles.emojiBall, { backgroundColor: TILE_COLORS[i] + '30' }]}>
              <Text style={styles.emojiBallText}>{e}</Text>
            </View>
          ))}
        </View>

        <Animated.View style={btnAnimStyle}>
          <AnimatedButton style={styles.playBtn} onPress={onPlay}>
            <LinearGradient
              colors={['#FF6B9D', '#FF3366']}
              style={styles.playBtnGradient}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 0 }}
            >
              <Ionicons name="play" size={24} color="#fff" />
              <Text style={styles.playText}>{t('menu.play')}</Text>
            </LinearGradient>
          </AnimatedButton>
        </Animated.View>

        {hasActiveGame && onContinue && (
          <AnimatedButton style={styles.continueBtn} onPress={onContinue}>
            <Ionicons name="play-circle" size={20} color="#F59E0B" />
            <Text style={styles.continueText}>
              {t('menu.continue', { level: activeLevel })}
            </Text>
          </AnimatedButton>
        )}

        <View style={styles.bottomRow}>
          <AnimatedButton style={styles.settingsBtn} onPress={onSettings}>
            <Ionicons name="settings-outline" size={18} color="rgba(255,255,255,0.7)" />
            <Text style={styles.settingsText}>{t('menu.settings')}</Text>
          </AnimatedButton>

          {canClaim && (
            <AnimatedButton style={styles.rewardBtn} onPress={onDailyReward}>
              <Text style={styles.rewardEmoji}>🎁</Text>
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
  floatingEmoji: {
    position: 'absolute',
  },
  floatingEmojiText: {
    fontSize: 32,
  },
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'baseline',
    marginBottom: 8,
  },
  titlePop: {
    fontSize: 64,
    fontWeight: '900',
    color: '#fff',
    letterSpacing: 3,
    textShadowColor: 'rgba(0,0,0,0.3)',
    textShadowOffset: { width: 0, height: 4 },
    textShadowRadius: 12,
  },
  titleBlast: {
    fontSize: 64,
    fontWeight: '900',
    color: '#FBBF24',
    letterSpacing: 3,
    marginLeft: 6,
    textShadowColor: 'rgba(251,191,36,0.4)',
    textShadowOffset: { width: 0, height: 4 },
    textShadowRadius: 12,
  },
  subtitle: {
    color: 'rgba(255,255,255,0.6)',
    fontSize: 13,
    letterSpacing: 5,
    marginBottom: 40,
    textTransform: 'uppercase',
  },
  emojiRow: {
    flexDirection: 'row',
    gap: 10,
    marginBottom: 48,
  },
  emojiBall: {
    width: 40,
    height: 40,
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
  },
  emojiBallText: {
    fontSize: 22,
  },
  playBtn: {
    borderRadius: 28,
    overflow: 'hidden',
    shadowColor: '#FF3366',
    shadowOffset: { width: 0, height: 6 },
    shadowOpacity: 0.5,
    shadowRadius: 16,
    elevation: 10,
  },
  playBtnGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 10,
    paddingHorizontal: 56,
    paddingVertical: 18,
  },
  playText: {
    color: '#fff',
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
    backgroundColor: 'rgba(245,158,11,0.15)',
    borderWidth: 1,
    borderColor: 'rgba(245,158,11,0.3)',
  },
  continueText: {
    color: '#F59E0B',
    fontSize: 15,
    fontWeight: '700',
  },
  bottomRow: {
    flexDirection: 'row',
    gap: 16,
    marginTop: 40,
  },
  settingsBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingHorizontal: 18,
    paddingVertical: 12,
    borderRadius: 16,
    backgroundColor: 'rgba(255,255,255,0.12)',
  },
  settingsText: {
    color: 'rgba(255,255,255,0.7)',
    fontSize: 13,
    fontWeight: '600',
  },
  rewardBtn: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    paddingHorizontal: 18,
    paddingVertical: 12,
    borderRadius: 16,
    backgroundColor: 'rgba(245,158,11,0.15)',
    borderWidth: 1,
    borderColor: 'rgba(245,158,11,0.3)',
  },
  rewardEmoji: {
    fontSize: 16,
  },
  rewardText: {
    color: '#F59E0B',
    fontSize: 13,
    fontWeight: '600',
  },
});
