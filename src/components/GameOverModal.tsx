import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Modal } from 'react-native';
import { useTranslation } from 'react-i18next';
import { useGameStore } from '../stores/gameStore';
import { ACCENT_COLOR, TEXT_COLOR, SCORE_COLOR, DANGER_COLOR } from '../constants/colors';

interface Props {
  visible: boolean;
  onRestart: () => void;
  onMenu: () => void;
}

export default function GameOverModal({ visible, onRestart, onMenu }: Props) {
  const { t } = useTranslation();
  const score = useGameStore((s) => s.score);
  const levelConfig = useGameStore((s) => s.levelConfig);

  return (
    <Modal transparent visible={visible} animationType="fade">
      <View style={styles.overlay}>
        <View style={styles.modal}>
          <Text style={styles.icon}>😢</Text>
          <Text style={styles.title}>{t('gameOver.title')}</Text>
          <Text style={styles.subtitle}>{t('gameOver.subtitle')}</Text>

          <View style={styles.scoreRow}>
            <Text style={styles.scoreLabel}>{t('game.score')}</Text>
            <Text style={styles.scoreValue}>{score.toLocaleString()}</Text>
          </View>
          <View style={styles.scoreRow}>
            <Text style={styles.scoreLabel}>{t('gameOver.target', { target: '' })}</Text>
            <Text style={styles.targetValue}>
              {levelConfig?.targetScore.toLocaleString()}
            </Text>
          </View>

          <TouchableOpacity style={styles.retryBtn} onPress={onRestart}>
            <Text style={styles.retryText}>{t('gameOver.retry')}</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.menuBtn} onPress={onMenu}>
            <Text style={styles.menuText}>{t('gameOver.mainMenu')}</Text>
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
    width: '80%',
    borderWidth: 2,
    borderColor: 'rgba(255,71,87,0.3)',
  },
  icon: {
    fontSize: 48,
    marginBottom: 8,
  },
  title: {
    color: DANGER_COLOR,
    fontSize: 28,
    fontWeight: '900',
    marginBottom: 4,
  },
  subtitle: {
    color: 'rgba(255,255,255,0.5)',
    fontSize: 14,
    marginBottom: 24,
    textAlign: 'center',
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
    fontSize: 18,
    fontWeight: 'bold',
  },
  targetValue: {
    color: 'rgba(255,255,255,0.4)',
    fontSize: 18,
    fontWeight: 'bold',
  },
  retryBtn: {
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
  retryText: {
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
