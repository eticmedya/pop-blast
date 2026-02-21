import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { useTranslation } from 'react-i18next';
import { usePowerUpStore, PowerUpType } from '../stores/powerupStore';
import { POWERUP_COLORS, TEXT_COLOR } from '../constants/colors';

const POWERUPS: { type: PowerUpType; icon: string; colorKey: keyof typeof POWERUP_COLORS }[] = [
  { type: 'rowBomb', icon: '💥', colorKey: 'rowBomb' },
  { type: 'colBomb', icon: '⚡', colorKey: 'colBomb' },
  { type: 'colorBomb', icon: '🌈', colorKey: 'colorBomb' },
  { type: 'shuffle', icon: '🔀', colorKey: 'shuffle' },
];

interface Props {
  disabled: boolean;
}

export default function PowerUpBar({ disabled }: Props) {
  const { t } = useTranslation();
  const inventory = usePowerUpStore((s) => s.inventory);
  const activePowerUp = usePowerUpStore((s) => s.activePowerUp);
  const setActivePowerUp = usePowerUpStore((s) => s.setActivePowerUp);

  return (
    <View style={styles.container}>
      {POWERUPS.map(({ type, icon, colorKey }) => {
        const count = inventory[type];
        const isActive = activePowerUp === type;
        const color = POWERUP_COLORS[colorKey];

        return (
          <TouchableOpacity
            key={type}
            style={[
              styles.button,
              isActive && { borderColor: color, borderWidth: 2 },
              (count === 0 || disabled) && styles.disabled,
            ]}
            onPress={() => {
              if (disabled || count === 0) return;
              setActivePowerUp(isActive ? null : type);
            }}
            disabled={disabled || count === 0}
          >
            <Text style={styles.icon}>{icon}</Text>
            <View style={[styles.badge, { backgroundColor: color }]}>
              <Text style={styles.badgeText}>{count}</Text>
            </View>
          </TouchableOpacity>
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
  },
  disabled: {
    opacity: 0.35,
  },
  icon: {
    fontSize: 22,
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
