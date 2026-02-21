import React, { useEffect } from 'react';
import { StyleSheet, TouchableOpacity } from 'react-native';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withTiming,
  withSpring,
  withSequence,
  withRepeat,
  withDelay,
  Easing,
  runOnJS,
} from 'react-native-reanimated';
import { TILE_COLORS, TILE_GLOW_COLORS } from '../constants/colors';
import { TILE_SIZE, BALL_RADIUS } from '../constants/dimensions';

interface AnimatedTileProps {
  color: number;
  isSelected: boolean;
  isMatched: boolean;
  onPress: () => void;
  fallDistance: number;
  isNew: boolean;
  entryDelay: number;
}

const AnimatedTouchable = Animated.createAnimatedComponent(TouchableOpacity);

function AnimatedTileInner({
  color,
  isSelected,
  isMatched,
  onPress,
  fallDistance,
  isNew,
  entryDelay,
}: AnimatedTileProps) {
  const scale = useSharedValue(isNew ? 0 : 1);
  const opacity = useSharedValue(isNew ? 0 : 1);
  const translateY = useSharedValue(isNew ? -TILE_SIZE * 2 : fallDistance > 0 ? -fallDistance * TILE_SIZE : 0);
  const selectionScale = useSharedValue(1);

  // Entry animation for new tiles
  useEffect(() => {
    if (isNew) {
      scale.value = withDelay(entryDelay, withSpring(1, { damping: 12, stiffness: 120 }));
      opacity.value = withDelay(entryDelay, withTiming(1, { duration: 200 }));
      translateY.value = withDelay(entryDelay, withSpring(0, { damping: 14, stiffness: 100 }));
    }
  }, [isNew, entryDelay]);

  // Fall animation
  useEffect(() => {
    if (fallDistance > 0 && !isNew) {
      translateY.value = -fallDistance * TILE_SIZE;
      translateY.value = withSpring(0, { damping: 12, stiffness: 100 });
    }
  }, [fallDistance]);

  // Match explosion
  useEffect(() => {
    if (isMatched) {
      scale.value = withSequence(
        withTiming(1.3, { duration: 150, easing: Easing.out(Easing.quad) }),
        withTiming(0, { duration: 150, easing: Easing.in(Easing.quad) })
      );
      opacity.value = withDelay(150, withTiming(0, { duration: 150 }));
    }
  }, [isMatched]);

  // Selection pulse
  useEffect(() => {
    if (isSelected) {
      selectionScale.value = withRepeat(
        withSequence(
          withTiming(1.12, { duration: 400, easing: Easing.inOut(Easing.ease) }),
          withTiming(1.0, { duration: 400, easing: Easing.inOut(Easing.ease) })
        ),
        -1,
        true
      );
    } else {
      selectionScale.value = withTiming(1, { duration: 150 });
    }
  }, [isSelected]);

  const animStyle = useAnimatedStyle(() => ({
    transform: [
      { translateY: translateY.value },
      { scale: scale.value * selectionScale.value },
    ],
    opacity: opacity.value,
  }));

  const baseColor = TILE_COLORS[color] ?? TILE_COLORS[0];
  const glowColor = TILE_GLOW_COLORS[color] ?? TILE_GLOW_COLORS[0];

  return (
    <AnimatedTouchable
      onPress={onPress}
      activeOpacity={0.7}
      style={[styles.cell, animStyle]}
    >
      {isSelected && (
        <Animated.View
          style={[
            styles.selectionRing,
            { borderColor: baseColor, shadowColor: baseColor },
          ]}
        />
      )}
      <Animated.View
        style={[
          styles.ball,
          {
            backgroundColor: baseColor,
            width: BALL_RADIUS * 2,
            height: BALL_RADIUS * 2,
            borderRadius: BALL_RADIUS,
            shadowColor: baseColor,
          },
        ]}
      >
        <Animated.View style={styles.highlight} />
        <Animated.View style={styles.bottomShadow} />
      </Animated.View>
    </AnimatedTouchable>
  );
}

export default React.memo(AnimatedTileInner);

const styles = StyleSheet.create({
  cell: {
    width: TILE_SIZE,
    height: TILE_SIZE,
    alignItems: 'center',
    justifyContent: 'center',
  },
  selectionRing: {
    position: 'absolute',
    width: BALL_RADIUS * 2 + 12,
    height: BALL_RADIUS * 2 + 12,
    borderRadius: BALL_RADIUS + 6,
    borderWidth: 2.5,
    zIndex: 2,
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.8,
    shadowRadius: 8,
    elevation: 6,
  },
  ball: {
    shadowOffset: { width: 0, height: 3 },
    shadowOpacity: 0.5,
    shadowRadius: 6,
    elevation: 5,
    alignItems: 'center',
    overflow: 'hidden',
  },
  highlight: {
    width: '60%',
    height: '30%',
    backgroundColor: 'rgba(255,255,255,0.35)',
    borderRadius: 100,
    marginTop: 3,
  },
  bottomShadow: {
    position: 'absolute',
    bottom: 2,
    width: '70%',
    height: '20%',
    backgroundColor: 'rgba(0,0,0,0.15)',
    borderRadius: 100,
  },
});
