import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Modal } from 'react-native';
import { useTranslation } from 'react-i18next';
import { useGameStore } from '../stores/gameStore';
import { ACCENT_COLOR, TEXT_COLOR, SCORE_COLOR } from '../constants/colors';
import Confetti from './Confetti';

interface Props {
  visible: boolean;
  onNext: () => void;
  onMenu: () => void;
}

export default function LevelCompleteModal({ visible, onNext, onMenu }: Props) {
  const { t } = useTranslation();
  const score = useGameStore((s) => s.score);
  const stars = useGameStore((s) => s.stars);
  const currentLevel = useGameStore((s) => s.currentLevel);
  const streakMultiplier = useGameStore((s) => s.streakMultiplier);

  const starDisplay = Array.from({ length: 3 }, (_, i) =>
    i < stars ? '\u2605' : '\u2606'
  ).join(' ');

  return (
    <Modal transparent visible={visible} animationType="fade">
      <View style={styles.overlay}>
        <Confetti visible={visible} />
        <View style={styles.modal}>
          <Text style={styles.title}>{t('levelComplete.title')}</Text>
          <Text style={styles.level}>
            {t('levelComplete.level', { number: currentLevel })}
          </Text>

          <Text style={styles.stars}>{starDisplay}</Text>

          <View style={styles.scoreRow}>
            <Text style={styles.scoreLabel}>{t('game.score')}</Text>
            <Text style={styles.scoreValue}>{score.toLocaleString()}</Text>
          </View>

          {streakMultiplier > 1 && (
            <View style={styles.streakRow}>
              <Text style={styles.streakLabel}>🔥 Streak Bonus</Text>
              <Text style={styles.streakValue}>x{streakMultiplier}</Text>
            </View>
          )}

          <TouchableOpacity style={styles.nextBtn} onPress={onNext}>
            <Text style={styles.nextText}>{t('levelComplete.nextLevel')}</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.menuBtn} onPress={onMenu}>
            <Text style={styles.menuText}>{t('levelComplete.mainMenu')}</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
}

const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.8)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  modal: {
    backgroundColor: '#1A1A2E',
    borderRadius: 28,
    padding: 32,
    alignItems: 'center',
    width: '82%',
    borderWidth: 2,
    borderColor: SCORE_COLOR,
    shadowColor: SCORE_COLOR,
    shadowOffset: { width: 0, height: 0 },
    shadowOpacity: 0.3,
    shadowRadius: 20,
    elevation: 12,
  },
  title: {
    color: SCORE_COLOR,
    fontSize: 32,
    fontWeight: '900',
    marginBottom: 4,
  },
  level: {
    color: 'rgba(255,255,255,0.5)',
    fontSize: 14,
    marginBottom: 16,
  },
  stars: {
    fontSize: 48,
    color: SCORE_COLOR,
    marginBottom: 20,
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
    fontSize: 20,
    fontWeight: 'bold',
  },
  streakRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    width: '100%',
    marginBottom: 8,
  },
  streakLabel: {
    color: 'rgba(255,255,255,0.6)',
    fontSize: 14,
  },
  streakValue: {
    color: ACCENT_COLOR,
    fontSize: 18,
    fontWeight: 'bold',
  },
  nextBtn: {
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
  nextText: {
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
