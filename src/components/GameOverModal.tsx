import React, { useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withTiming,
  withDelay,
  withSpring,
  Easing,
} from 'react-native-reanimated';
import { MaterialIcons } from '@expo/vector-icons';
import { useTranslation } from 'react-i18next';
import { useGameStore } from '../stores/gameStore';
import { ACCENT_COLOR, TEXT_COLOR, SCORE_COLOR, DANGER_COLOR } from '../constants/colors';
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

  const getProximityColor = (): string => {
    if (progress >= 0.9) return SCORE_COLOR;
    if (progress >= 0.75) return '#FFA502';
    if (progress >= 0.5) return ACCENT_COLOR;
    return 'rgba(255,255,255,0.5)';
  };

  useEffect(() => {
    if (visible) {
      hapticService.failure();

      bgOpacity.value = withTiming(0.8, { duration: 300 });
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
        <View style={styles.modal}>
          <Animated.View style={contentStyle}>
            <View style={styles.iconContainer}>
              <MaterialIcons name="sentiment-dissatisfied" size={52} color={DANGER_COLOR} />
            </View>
            <Text style={styles.title}>{t('gameOver.title')}</Text>
            <Text style={[styles.subtitle, { color: getProximityColor() }]}>
              {getProximityMessage()}
            </Text>

            {/* Ghost progress bar */}
            <View style={styles.ghostProgressContainer}>
              <View style={styles.ghostProgressBg}>
                <Animated.View
                  style={[
                    styles.ghostProgressFill,
                    progressFillStyle,
                    { backgroundColor: getProximityColor() },
                  ]}
                />
                {/* Target marker */}
                <View style={styles.targetMarker} />
              </View>
              <Text style={styles.ghostProgressLabel}>
                {Math.round(progress * 100)}%
              </Text>
            </View>

            <View style={styles.scoreRow}>
              <Text style={styles.scoreLabel}>{t('game.score')}</Text>
              <Text style={styles.scoreValue}>{score.toLocaleString()}</Text>
            </View>
            <View style={styles.scoreRow}>
              <Text style={styles.scoreLabel}>{t('gameOver.target', { target: '' })}</Text>
              <Text style={styles.targetValue}>
                {levelConfig?.targetScore.toLocaleString()}
              </Text>
            </View>
          </Animated.View>

          <Animated.View style={[styles.buttonsContainer, buttonsStyle]}>
            <AnimatedButton style={styles.retryBtn} onPress={onRestart}>
              <Text style={styles.retryText}>{t('gameOver.retry')}</Text>
            </AnimatedButton>
            <AnimatedButton style={styles.menuBtn} onPress={onMenu}>
              <Text style={styles.menuText}>{t('gameOver.mainMenu')}</Text>
            </AnimatedButton>
          </Animated.View>
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
    width: '80%',
    zIndex: 201,
  },
  modal: {
    backgroundColor: '#1A1A2E',
    borderRadius: 28,
    padding: 32,
    alignItems: 'center',
    borderWidth: 2,
    borderColor: 'rgba(255,71,87,0.3)',
  },
  iconContainer: {
    alignItems: 'center',
    marginBottom: 8,
  },
  title: {
    color: DANGER_COLOR,
    fontSize: 28,
    fontWeight: '900',
    marginBottom: 4,
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 16,
    fontWeight: '700',
    marginBottom: 16,
    textAlign: 'center',
  },
  ghostProgressContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    width: '100%',
    gap: 8,
    marginBottom: 20,
  },
  ghostProgressBg: {
    flex: 1,
    height: 12,
    backgroundColor: 'rgba(255,255,255,0.08)',
    borderRadius: 6,
    overflow: 'hidden',
    position: 'relative',
  },
  ghostProgressFill: {
    height: '100%',
    borderRadius: 6,
  },
  targetMarker: {
    position: 'absolute',
    right: 0,
    top: -2,
    bottom: -2,
    width: 3,
    backgroundColor: 'rgba(255,255,255,0.4)',
    borderRadius: 2,
  },
  ghostProgressLabel: {
    color: 'rgba(255,255,255,0.6)',
    fontSize: 13,
    fontWeight: 'bold',
    minWidth: 38,
    textAlign: 'right',
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
    fontSize: 18,
    fontWeight: 'bold',
  },
  targetValue: {
    color: 'rgba(255,255,255,0.4)',
    fontSize: 18,
    fontWeight: 'bold',
  },
  buttonsContainer: {
    width: '100%',
    alignItems: 'center',
  },
  retryBtn: {
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
  retryText: {
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
