import React, { useEffect } from 'react';
import { StyleSheet } from 'react-native';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withTiming,
  withDelay,
  withSpring,
  Easing,
  runOnJS,
} from 'react-native-reanimated';
import { SCORE_COLOR } from '../constants/colors';

interface ScorePopupProps {
  text: string;
  x: number;
  y: number;
  color?: string;
  onDone: () => void;
}

export default function ScorePopup({ text, x, y, color, onDone }: ScorePopupProps) {
  const translateY = useSharedValue(0);
  const opacity = useSharedValue(1);
  const scale = useSharedValue(0.5);

  useEffect(() => {
    scale.value = withSpring(1.2, { damping: 8 });
    translateY.value = withTiming(-60, { duration: 800, easing: Easing.out(Easing.quad) });
    opacity.value = withDelay(500, withTiming(0, { duration: 300 }));

    const timer = setTimeout(() => onDone(), 850);
    return () => clearTimeout(timer);
  }, []);

  const animStyle = useAnimatedStyle(() => ({
    transform: [{ translateY: translateY.value }, { scale: scale.value }],
    opacity: opacity.value,
  }));

  return (
    <Animated.Text
      style={[
        styles.popup,
        { left: x, top: y, color: color ?? SCORE_COLOR },
        animStyle,
      ]}
    >
      {text}
    </Animated.Text>
  );
}

const styles = StyleSheet.create({
  popup: {
    position: 'absolute',
    fontWeight: 'bold',
    fontSize: 18,
    textShadowColor: 'rgba(0,0,0,0.7)',
    textShadowOffset: { width: 1, height: 1 },
    textShadowRadius: 3,
    zIndex: 100,
  },
});
