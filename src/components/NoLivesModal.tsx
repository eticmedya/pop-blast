import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Modal } from 'react-native';
import { useTranslation } from 'react-i18next';
import { useLivesStore } from '../stores/livesStore';
import { ACCENT_COLOR, TEXT_COLOR, DANGER_COLOR } from '../constants/colors';

interface Props {
  visible: boolean;
  onClose: () => void;
}

export default function NoLivesModal({ visible, onClose }: Props) {
  const { t } = useTranslation();
  const getTimeUntilNextLife = useLivesStore((s) => s.getTimeUntilNextLife);
  const checkRegen = useLivesStore((s) => s.checkRegen);
  const lives = useLivesStore((s) => s.lives);
  const [timeStr, setTimeStr] = useState('');

  useEffect(() => {
    if (!visible) return;
    const interval = setInterval(() => {
      checkRegen();
      const ms = getTimeUntilNextLife();
      if (ms <= 0) {
        setTimeStr('');
        onClose();
      } else {
        const min = Math.floor(ms / 60000);
        const sec = Math.floor((ms % 60000) / 1000);
        setTimeStr(`${min}:${sec.toString().padStart(2, '0')}`);
      }
    }, 1000);
    return () => clearInterval(interval);
  }, [visible]);

  return (
    <Modal transparent visible={visible} animationType="fade">
      <View style={styles.overlay}>
        <View style={styles.modal}>
          <Text style={styles.icon}>💔</Text>
          <Text style={styles.title}>{t('lives.noLives')}</Text>
          {timeStr ? (
            <Text style={styles.timer}>
              {t('lives.waitMessage', { time: timeStr })}
            </Text>
          ) : null}
          <TouchableOpacity style={styles.closeBtn} onPress={onClose}>
            <Text style={styles.closeText}>{t('common.ok')}</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
}

const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.75)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  modal: {
    backgroundColor: '#1A1A2E',
    borderRadius: 24,
    padding: 32,
    alignItems: 'center',
    width: '75%',
    borderWidth: 2,
    borderColor: DANGER_COLOR,
  },
  icon: {
    fontSize: 48,
    marginBottom: 12,
  },
  title: {
    color: DANGER_COLOR,
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 12,
  },
  timer: {
    color: 'rgba(255,255,255,0.6)',
    fontSize: 16,
    marginBottom: 20,
    textAlign: 'center',
  },
  closeBtn: {
    backgroundColor: ACCENT_COLOR,
    paddingHorizontal: 40,
    paddingVertical: 12,
    borderRadius: 14,
  },
  closeText: {
    color: TEXT_COLOR,
    fontSize: 16,
    fontWeight: 'bold',
  },
});
