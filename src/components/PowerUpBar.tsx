import React, { useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import Animated, {
  useSharedValue,
  useAnimatedStyle,
  withRepeat,
  withSequence,
  withTiming,
  Easing,
} from 'react-native-reanimated';
import { MaterialCommunityIcons } from '@expo/vector-icons';
import { useTranslation } from 'react-i18next';
import { usePowerUpStore, PowerUpType } from '../stores/powerupStore';
import { POWERUP_COLORS, TEXT_COLOR } from '../constants/colors';
import AnimatedButton from './AnimatedButton';

const POWERUPS: {
  type: PowerUpType;
  iconName: keyof typeof MaterialCommunityIcons.glyphMap;
  colorKey: keyof typeof POWERUP_COLORS;
}[] = [
  { type: 'rowBomb', iconName: 'bomb', colorKey: 'rowBomb' },
  { type: 'colBomb', iconName: 'lightning-bolt', colorKey: 'colBomb' },
  { type: 'colorBomb', iconName: 'palette', colorKey: 'colorBomb' },
  { type: 'shuffle', iconName: 'shuffle-variant', colorKey: 'shuffle' },
];

interface Props {
  disabled: boolean;
}

function PowerUpButton({
  type,
  iconName,
  colorKey,
  count,
  isActive,
  disabled,
  onPress,
}: {
  type: PowerUpType;
  iconName: keyof typeof MaterialCommunityIcons.glyphMap;
  colorKey: keyof typeof POWERUP_COLORS;
  count: number;
  isActive: boolean;
  disabled: boolean;
  onPress: () => void;
}) {
  const color = POWERUP_COLORS[colorKey];
  const glowOpacity = useSharedValue(0);

  useEffect(() => {
    if (isActive) {
      glowOpacity.value = withRepeat(
        withSequence(
          withTiming(0.6, { duration: 600, easing: Easing.inOut(Easing.ease) }),
          withTiming(0.2, { duration: 600, easing: Easing.inOut(Easing.ease) })
        ),
        -1,
        true
      );
    } else {
      glowOpacity.value = withTiming(0, { duration: 200 });
    }
  }, [isActive]);

  const glowStyle = useAnimatedStyle(() => ({
    opacity: glowOpacity.value,
  }));

  return (
    <AnimatedButton
      style={[
        styles.button,
        isActive && { borderColor: color, borderWidth: 2 },
        (count === 0 || disabled) && styles.disabled,
      ]}
      onPress={onPress}
      disabled={disabled || count === 0}
    >
      {/* Glow layer */}
      <Animated.View
        style={[
          styles.glowLayer,
          { backgroundColor: color },
          glowStyle,
        ]}
      />
      <MaterialCommunityIcons
        name={iconName}
        size={24}
        color={isActive ? color : 'rgba(255,255,255,0.8)'}
      />
      <View style={[styles.badge, { backgroundColor: color }]}>
        <Text style={styles.badgeText}>{count}</Text>
      </View>
    </AnimatedButton>
  );
}

export default function PowerUpBar({ disabled }: Props) {
  const { t } = useTranslation();
  const inventory = usePowerUpStore((s) => s.inventory);
  const activePowerUp = usePowerUpStore((s) => s.activePowerUp);
  const setActivePowerUp = usePowerUpStore((s) => s.setActivePowerUp);

  return (
    <View style={styles.container}>
      {POWERUPS.map(({ type, iconName, colorKey }) => {
        const count = inventory[type];
        const isActive = activePowerUp === type;

        return (
          <PowerUpButton
            key={type}
            type={type}
            iconName={iconName}
            colorKey={colorKey}
            count={count}
            isActive={isActive}
            disabled={disabled}
            onPress={() => {
              if (disabled || count === 0) return;
              setActivePowerUp(isActive ? null : type);
            }}
          />
        );
      })}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: 12,
    paddingVertical: 10,
    paddingHorizontal: 20,
  },
  button: {
    width: 52,
    height: 52,
    borderRadius: 14,
    backgroundColor: 'rgba(255,255,255,0.08)',
    alignItems: 'center',
    justifyContent: 'center',
    borderWidth: 1,
    borderColor: 'rgba(255,255,255,0.1)',
    overflow: 'hidden',
  },
  disabled: {
    opacity: 0.35,
  },
  glowLayer: {
    ...StyleSheet.absoluteFillObject,
    borderRadius: 14,
  },
  badge: {
    position: 'absolute',
    top: -4,
    right: -4,
    width: 20,
    height: 20,
    borderRadius: 10,
    alignItems: 'center',
    justifyContent: 'center',
  },
  badgeText: {
    color: TEXT_COLOR,
    fontSize: 11,
    fontWeight: 'bold',
  },
});
