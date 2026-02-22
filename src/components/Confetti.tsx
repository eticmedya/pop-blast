import React, { useEffect, useMemo } from 'react';
import { StyleSheet } from 'react-native';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withTiming,
  withDelay,
  withRepeat,
  withSequence,
  Easing,
} from 'react-native-reanimated';
import { TILE_COLORS } from '../constants/colors';
import { SCREEN_WIDTH, SCREEN_HEIGHT } from '../constants/dimensions';

const PARTICLE_COUNT = 40;

interface Particle {
  x: number;
  color: string;
  size: number;
  delay: number;
  duration: number;
  drift: number;
  rotation: number;
}

function ConfettiParticle({ particle }: { particle: Particle }) {
  const translateY = useSharedValue(-20);
  const translateX = useSharedValue(particle.x);
  const rotate = useSharedValue(0);
  const opacity = useSharedValue(0);

  useEffect(() => {
    opacity.value = withDelay(particle.delay, withTiming(1, { duration: 200 }));
    translateY.value = withDelay(
      particle.delay,
      withTiming(SCREEN_HEIGHT + 50, {
        duration: particle.duration,
        easing: Easing.in(Easing.quad),
      })
    );
    translateX.value = withDelay(
      particle.delay,
      withTiming(particle.x + particle.drift, {
        duration: particle.duration,
        easing: Easing.inOut(Easing.ease),
      })
    );
    rotate.value = withDelay(
      particle.delay,
      withTiming(particle.rotation, {
        duration: particle.duration,
      })
    );
  }, []);

  const style = useAnimatedStyle(() => ({
    transform: [
      { translateX: translateX.value },
      { translateY: translateY.value },
      { rotate: `${rotate.value}deg` },
    ],
    opacity: opacity.value,
  }));

  return (
    <Animated.View
      style={[
        styles.particle,
        {
          width: particle.size,
          height: particle.size * 0.6,
          backgroundColor: particle.color,
          borderRadius: 2,
        },
        style,
      ]}
    />
  );
}

export default function Confetti({ visible }: { visible: boolean }) {
  const particles = useMemo<Particle[]>(() => {
    if (!visible) return [];
    return Array.from({ length: PARTICLE_COUNT }, () => ({
      x: Math.random() * SCREEN_WIDTH,
      color: TILE_COLORS[Math.floor(Math.random() * TILE_COLORS.length)],
      size: 6 + Math.random() * 8,
      delay: Math.random() * 800,
      duration: 2000 + Math.random() * 2000,
      drift: (Math.random() - 0.5) * 100,
      rotation: Math.random() * 720 - 360,
    }));
  }, [visible]);

  if (!visible) return null;

  return (
    <>
      {particles.map((p, i) => (
        <ConfettiParticle key={i} particle={p} />
      ))}
    </>
  );
}

const styles = StyleSheet.create({
  particle: {
    position: 'absolute',
    top: 0,
    zIndex: 300,
  },
});
