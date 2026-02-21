import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Modal } from 'react-native';
import { useGameStore } from '../stores/gameStore';
import { ACCENT_COLOR, TEXT_COLOR, BG_COLOR, SCORE_COLOR } from '../constants/colors';

interface Props {
  visible: boolean;
  onRestart: () => void;
  onMenu: () => void;
}

export default function GameOverModal({ visible, onRestart, onMenu }: Props) {
  const score = useGameStore((s) => s.score);
  const levelConfig = useGameStore((s) => s.levelConfig);

  return (
    <Modal transparent visible={visible} animationType="fade">
      <View style={styles.overlay}>
        <View style={styles.modal}>
          <Text style={styles.title}>Oyun Bitti!</Text>
          <Text style={styles.subtitle}>Hedef skora ulaşamadın</Text>

          <View style={styles.scoreRow}>
            <Text style={styles.scoreLabel}>Skorun</Text>
            <Text style={styles.scoreValue}>{score.toLocaleString()}</Text>
          </View>
          <View style={styles.scoreRow}>
            <Text style={styles.scoreLabel}>Hedef</Text>
            <Text style={styles.targetValue}>
              {levelConfig?.targetScore.toLocaleString()}
            </Text>
          </View>

          <TouchableOpacity style={styles.retryBtn} onPress={onRestart}>
            <Text style={styles.retryText}>Tekrar Dene</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.menuBtn} onPress={onMenu}>
            <Text style={styles.menuText}>Ana Menü</Text>
          </TouchableOpacity>
        </View>
      </View>
    </Modal>
  );
}

const styles = StyleSheet.create({
  overlay: {
    flex: 1,
    backgroundColor: 'rgba(0,0,0,0.7)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  modal: {
    backgroundColor: '#1A1A2E',
    borderRadius: 24,
    padding: 32,
    alignItems: 'center',
    width: '80%',
    borderWidth: 2,
    borderColor: 'rgba(255,255,255,0.1)',
  },
  title: {
    color: '#FF4757',
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 4,
  },
  subtitle: {
    color: 'rgba(255,255,255,0.5)',
    fontSize: 14,
    marginBottom: 24,
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
    borderRadius: 16,
    marginTop: 24,
    width: '100%',
    alignItems: 'center',
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
    color: 'rgba(255,255,255,0.5)',
    fontSize: 14,
  },
});
