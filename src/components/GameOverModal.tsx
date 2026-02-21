import React, { useEffect, useMemo } from 'react';
import { View, Text, StyleSheet, Image } from 'react-native';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withTiming,
  withDelay,
  withSpring,
  Easing,
} from 'react-native-reanimated';
import { Ionicons } from '@expo/vector-icons';
import { LinearGradient } from 'expo-linear-gradient';
import { useTranslation } from 'react-i18next';
import { useGameStore } from '../stores/gameStore';
import { getWorldTheme } from '../constants/themes';
import { SCREEN_WIDTH } from '../constants/dimensions';
import { hapticService } from '../services/HapticService';
import AnimatedButton from './AnimatedButton';

interface Props {
  visible: boolean;
  onRestart: () => void;
  onMenu: () => void;
}

export default function GameOverModal({ visible, onRestart, onMenu }: Props) {
  const { t } = useTranslation();
  const score = useGameStore((s) => s.score);
  const levelConfig = useGameStore((s) => s.levelConfig);
  const currentLevel = useGameStore((s) => s.currentLevel);

  const worldTheme = useMemo(() => getWorldTheme(currentLevel), [currentLevel]);

  const bgOpacity = useSharedValue(0);
  const modalTranslateY = useSharedValue(300);
  const contentOpacity = useSharedValue(0);
  const buttonsOpacity = useSharedValue(0);
  const progressWidth = useSharedValue(0);

  const targetScore = levelConfig?.targetScore ?? 1;
  const progress = Math.min(1, score / Math.max(1, targetScore));

  const getProximityMessage = (): string => {
    if (progress >= 0.9) return t('gameOver.soClose');
    if (progress >= 0.75) return t('gameOver.almostThere');
    if (progress >= 0.5) return t('gameOver.goodTry');
    return t('gameOver.subtitle');
  };

  const getProgressColor = (): string => {
    if (progress >= 0.9) return '#F59E0B';
    if (progress >= 0.75) return '#FB923C';
    if (progress >= 0.5) return worldTheme.accent;
    return '#EF4444';
  };

  useEffect(() => {
    if (visible) {
      hapticService.failure();

      bgOpacity.value = withTiming(0.7, { duration: 300 });
      modalTranslateY.value = withSpring(0, { damping: 14, stiffness: 100 });
      contentOpacity.value = withDelay(200, withTiming(1, { duration: 400 }));
      buttonsOpacity.value = withDelay(800, withTiming(1, { duration: 400 }));
      progressWidth.value = withDelay(
        400,
        withTiming(progress * 100, { duration: 800, easing: Easing.out(Easing.quad) })
      );
    } else {
      bgOpacity.value = 0;
      modalTranslateY.value = 300;
      contentOpacity.value = 0;
      buttonsOpacity.value = 0;
      progressWidth.value = 0;
    }
  }, [visible]);

  const bgStyle = useAnimatedStyle(() => ({
    opacity: bgOpacity.value,
  }));

  const modalStyle = useAnimatedStyle(() => ({
    transform: [{ translateY: modalTranslateY.value }],
  }));

  const contentStyle = useAnimatedStyle(() => ({
    opacity: contentOpacity.value,
  }));

  const buttonsStyle = useAnimatedStyle(() => ({
    opacity: buttonsOpacity.value,
  }));

  const progressFillStyle = useAnimatedStyle(() => ({
    width: `${progressWidth.value}%`,
  }));

  if (!visible) return null;

  return (
    <View style={styles.fullScreen}>
      <Animated.View style={[styles.overlay, bgStyle]} />

      <Animated.View style={[styles.modalContainer, modalStyle]}>
        <View style={styles.card}>
          <LinearGradient
            colors={['#FFFBF0', '#FFF5E1', '#FFEED4']}
            style={styles.cardGradient}
            start={{ x: 0, y: 0 }}
            end={{ x: 0, y: 1 }}
          >
            {/* Kırmızı banner */}
            <LinearGradient
              colors={['#EF4444', '#DC2626']}
              style={styles.banner}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 0 }}
            >
              <Text style={styles.title}>{t('gameOver.title').toUpperCase()}</Text>
            </LinearGradient>

            {/* Karakter (üzgün poz) */}
            <Image
              source={worldTheme.character}
              style={styles.character}
              resizeMode="contain"
            />

            <Animated.View style={[styles.contentSection, contentStyle]}>
              <Text style={styles.subtitle}>{getProximityMessage()}</Text>

              {/* İlerleme çubuğu */}
              <View style={styles.progressContainer}>
                <View style={styles.progressBg}>
                  <Animated.View
                    style={[
                      styles.progressFill,
                      progressFillStyle,
                      { backgroundColor: getProgressColor() },
                    ]}
                  />
                  <View style={styles.targetMarker} />
                </View>
                <Text style={[styles.progressLabel, { color: getProgressColor() }]}>
                  {Math.round(progress * 100)}%
                </Text>
              </View>

              {/* Skor detayları */}
              <View style={styles.scoreSection}>
                <View style={styles.scoreRow}>
                  <View style={styles.scoreLeft}>
                    <Ionicons name="trophy" size={16} color="#F59E0B" />
                    <Text style={styles.scoreLabel}>{t('game.score')}</Text>
                  </View>
                  <Text style={styles.scoreValue}>{score.toLocaleString()}</Text>
                </View>
                <View style={styles.scoreRow}>
                  <View style={styles.scoreLeft}>
                    <Ionicons name="flag" size={16} color="#9E9E9E" />
                    <Text style={styles.scoreLabel}>{t('gameOver.target', { target: '' })}</Text>
                  </View>
                  <Text style={styles.targetValue}>
                    {levelConfig?.targetScore.toLocaleString()}
                  </Text>
                </View>
              </View>
            </Animated.View>

            <Animated.View style={[styles.buttonsContainer, buttonsStyle]}>
              <AnimatedButton style={styles.retryBtn} onPress={onRestart}>
                <LinearGradient
                  colors={[worldTheme.accent, worldTheme.secondary]}
                  style={styles.retryBtnGradient}
                  start={{ x: 0, y: 0 }}
                  end={{ x: 1, y: 0 }}
                >
                  <Ionicons name="refresh" size={20} color="#fff" />
                  <Text style={styles.retryText}>{t('gameOver.retry')}</Text>
                </LinearGradient>
              </AnimatedButton>
              <AnimatedButton style={styles.menuBtn} onPress={onMenu}>
                <Text style={styles.menuText}>{t('gameOver.mainMenu')}</Text>
              </AnimatedButton>
            </Animated.View>
          </LinearGradient>
        </View>
      </Animated.View>
    </View>
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
    paddingVertical: 18,
    alignItems: 'center',
  },
  title: {
    color: '#fff',
    fontSize: 24,
    fontWeight: '900',
    letterSpacing: 2,
    textShadowColor: 'rgba(0,0,0,0.3)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 4,
  },
  character: {
    width: 70,
    height: 70,
    marginTop: -16,
    marginBottom: 4,
    opacity: 0.7,
  },
  contentSection: {
    width: '85%',
    alignItems: 'center',
  },
  subtitle: {
    fontSize: 16,
    fontWeight: '700',
    color: '#5D4037',
    marginBottom: 12,
    textAlign: 'center',
  },
  progressContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    width: '100%',
    gap: 8,
    marginBottom: 16,
  },
  progressBg: {
    flex: 1,
    height: 14,
    backgroundColor: 'rgba(0,0,0,0.06)',
    borderRadius: 7,
    overflow: 'hidden',
    position: 'relative',
  },
  progressFill: {
    height: '100%',
    borderRadius: 7,
  },
  targetMarker: {
    position: 'absolute',
    right: 0,
    top: -2,
    bottom: -2,
    width: 3,
    backgroundColor: 'rgba(0,0,0,0.15)',
    borderRadius: 2,
  },
  progressLabel: {
    fontSize: 14,
    fontWeight: '800',
    minWidth: 42,
    textAlign: 'right',
  },
  scoreSection: {
    width: '100%',
    marginBottom: 8,
  },
  scoreRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    alignItems: 'center',
    backgroundColor: 'rgba(0,0,0,0.04)',
    paddingHorizontal: 14,
    paddingVertical: 10,
    borderRadius: 10,
    marginBottom: 4,
  },
  scoreLeft: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  scoreLabel: {
    color: '#5D4037',
    fontSize: 14,
    fontWeight: '600',
  },
  scoreValue: {
    color: '#F59E0B',
    fontSize: 18,
    fontWeight: '900',
  },
  targetValue: {
    color: '#9E9E9E',
    fontSize: 18,
    fontWeight: '700',
  },
  buttonsContainer: {
    width: '85%',
    alignItems: 'center',
    marginTop: 8,
  },
  retryBtn: {
    width: '100%',
    borderRadius: 20,
    overflow: 'hidden',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 6,
  },
  retryBtnGradient: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'center',
    gap: 8,
    paddingVertical: 16,
  },
  retryText: {
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
