import React, { useEffect } from 'react';
import { StyleSheet, Text, View } from 'react-native';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withTiming,
  withDelay,
  withSequence,
  Easing,
} from 'react-native-reanimated';
import { useTranslation } from 'react-i18next';
import { useAchievementStore, Achievement } from '../stores/achievementStore';
import { SCORE_COLOR, ACCENT_COLOR } from '../constants/colors';

export default function AchievementPopup() {
  const { t } = useTranslation();
  const pendingPopup = useAchievementStore((s) => s.pendingPopup);
  const dismissPopup = useAchievementStore((s) => s.dismissPopup);

  const translateY = useSharedValue(-100);
  const opacity = useSharedValue(0);

  useEffect(() => {
    if (pendingPopup) {
      translateY.value = withSequence(
        withTiming(60, { duration: 400, easing: Easing.out(Easing.back(1.5)) }),
        withDelay(2500, withTiming(-100, { duration: 300 }))
      );
      opacity.value = withSequence(
        withTiming(1, { duration: 300 }),
        withDelay(2500, withTiming(0, { duration: 300 }))
      );
      const timer = setTimeout(dismissPopup, 3300);
      return () => clearTimeout(timer);
    }
  }, [pendingPopup]);

  const animStyle = useAnimatedStyle(() => ({
    transform: [{ translateY: translateY.value }],
    opacity: opacity.value,
  }));

  if (!pendingPopup) return null;

  return (
    <Animated.View style={[styles.container, animStyle]}>
      <Text style={styles.icon}>{pendingPopup.icon}</Text>
      <View style={styles.textContainer}>
        <Text style={styles.title}>{t('achievements.unlocked')}</Text>
        <Text style={styles.name}>{t(pendingPopup.titleKey)}</Text>
      </View>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  container: {
    position: 'absolute',
    top: 0,
    left: 20,
    right: 20,
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: 'rgba(26,26,46,0.95)',
    borderRadius: 16,
    padding: 14,
    borderWidth: 1,
    borderColor: SCORE_COLOR,
    gap: 12,
    zIndex: 500,
    shadowColor: SCORE_COLOR,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 12,
    elevation: 10,
  },
  icon: {
    fontSize: 32,
  },
  textContainer: {
    flex: 1,
  },
  title: {
    color: SCORE_COLOR,
    fontSize: 11,
    fontWeight: '600',
    letterSpacing: 1,
    textTransform: 'uppercase',
  },
  name: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 'bold',
    marginTop: 2,
  },
});
