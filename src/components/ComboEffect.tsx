import React, { useEffect } from 'react';
import { StyleSheet } from 'react-native';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withSequence,
  withTiming,
  withSpring,
  Easing,
} from 'react-native-reanimated';
import { ACCENT_COLOR, SCORE_COLOR } from '../constants/colors';

interface ComboEffectProps {
  multiplier: number;
  visible: boolean;
}

export default function ComboEffect({ multiplier, visible }: ComboEffectProps) {
  const scale = useSharedValue(0);
  const opacity = useSharedValue(0);

  useEffect(() => {
    if (visible && multiplier > 1) {
      scale.value = withSequence(
        withSpring(1.5, { damping: 6, stiffness: 200 }),
        withTiming(1, { duration: 200 }),
        withTiming(1, { duration: 600 }),
        withTiming(0, { duration: 300 })
      );
      opacity.value = withSequence(
        withTiming(1, { duration: 100 }),
        withTiming(1, { duration: 800 }),
        withTiming(0, { duration: 300 })
      );
    }
  }, [visible, multiplier]);

  const animStyle = useAnimatedStyle(() => ({
    transform: [{ scale: scale.value }],
    opacity: opacity.value,
  }));

  if (!visible || multiplier <= 1) return null;

  return (
    <Animated.View style={[styles.container, animStyle]} pointerEvents="none">
      <Animated.Text style={styles.comboText}>COMBO</Animated.Text>
      <Animated.Text style={styles.multiplierText}>x{multiplier}</Animated.Text>
    </Animated.View>
  );
}

const styles = StyleSheet.create({
  container: {
    position: 'absolute',
    alignSelf: 'center',
    alignItems: 'center',
    justifyContent: 'center',
    top: '35%',
    zIndex: 200,
  },
  comboText: {
    fontSize: 32,
    fontWeight: '900',
    color: ACCENT_COLOR,
    textShadowColor: 'rgba(0,0,0,0.8)',
    textShadowOffset: { width: 2, height: 2 },
    textShadowRadius: 6,
    letterSpacing: 4,
  },
  multiplierText: {
    fontSize: 48,
    fontWeight: '900',
    color: SCORE_COLOR,
    textShadowColor: 'rgba(0,0,0,0.8)',
    textShadowOffset: { width: 2, height: 2 },
    textShadowRadius: 6,
  },
});
