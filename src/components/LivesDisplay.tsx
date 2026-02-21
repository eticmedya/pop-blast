import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet } from 'react-native';
import { useTranslation } from 'react-i18next';
import { useLivesStore } from '../stores/livesStore';
import { DANGER_COLOR, TEXT_COLOR } from '../constants/colors';

export default function LivesDisplay() {
  const { t } = useTranslation();
  const lives = useLivesStore((s) => s.lives);
  const maxLives = useLivesStore((s) => s.maxLives);
  const getTimeUntilNextLife = useLivesStore((s) => s.getTimeUntilNextLife);
  const checkRegen = useLivesStore((s) => s.checkRegen);

  const [timeStr, setTimeStr] = useState('');

  useEffect(() => {
    checkRegen();
    const interval = setInterval(() => {
      checkRegen();
      const ms = getTimeUntilNextLife();
      if (ms <= 0 || lives >= maxLives) {
        setTimeStr('');
      } else {
        const min = Math.floor(ms / 60000);
        const sec = Math.floor((ms % 60000) / 1000);
        setTimeStr(`${min}:${sec.toString().padStart(2, '0')}`);
      }
    }, 1000);
    return () => clearInterval(interval);
  }, [lives]);

  return (
    <View style={styles.container}>
      <View style={styles.heartsRow}>
        {Array.from({ length: maxLives }, (_, i) => (
          <Text key={i} style={[styles.heart, i >= lives && styles.emptyHeart]}>
            {i < lives ? '❤️' : '🖤'}
          </Text>
        ))}
      </View>
      {timeStr ? (
        <Text style={styles.timer}>{t('lives.nextIn', { time: timeStr })}</Text>
      ) : lives >= maxLives ? (
        <Text style={styles.full}>{t('lives.full')}</Text>
      ) : null}
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    alignItems: 'center',
    gap: 2,
  },
  heartsRow: {
    flexDirection: 'row',
    gap: 2,
  },
  heart: {
    fontSize: 14,
  },
  emptyHeart: {
    opacity: 0.4,
  },
  timer: {
    color: DANGER_COLOR,
    fontSize: 9,
    fontWeight: '600',
  },
  full: {
    color: 'rgba(255,255,255,0.4)',
    fontSize: 9,
  },
});
