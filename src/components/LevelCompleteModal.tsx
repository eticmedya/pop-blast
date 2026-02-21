import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Modal } from 'react-native';
import { useGameStore } from '../stores/gameStore';
import { ACCENT_COLOR, TEXT_COLOR, SCORE_COLOR } from '../constants/colors';

interface Props {
  visible: boolean;
  onNext: () => void;
  onMenu: () => void;
}

export default function LevelCompleteModal({ visible, onNext, onMenu }: Props) {
  const score = useGameStore((s) => s.score);
  const stars = useGameStore((s) => s.stars);
  const currentLevel = useGameStore((s) => s.currentLevel);

  const starDisplay = Array.from({ length: 3 }, (_, i) =>
    i < stars ? '\u2605' : '\u2606'
  ).join(' ');

  return (
    <Modal transparent visible={visible} animationType="fade">
      <View style={styles.overlay}>
        <View style={styles.modal}>
          <Text style={styles.title}>Tebrikler!</Text>
          <Text style={styles.level}>Seviye {currentLevel}</Text>

          <Text style={styles.stars}>{starDisplay}</Text>

          <View style={styles.scoreRow}>
            <Text style={styles.scoreLabel}>Skor</Text>
            <Text style={styles.scoreValue}>{score.toLocaleString()}</Text>
          </View>

          <TouchableOpacity style={styles.nextBtn} onPress={onNext}>
            <Text style={styles.nextText}>Sonraki Seviye</Text>
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
    borderColor: SCORE_COLOR,
  },
  title: {
    color: SCORE_COLOR,
    fontSize: 32,
    fontWeight: 'bold',
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
  nextBtn: {
    backgroundColor: ACCENT_COLOR,
    paddingHorizontal: 40,
    paddingVertical: 14,
    borderRadius: 16,
    marginTop: 24,
    width: '100%',
    alignItems: 'center',
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
    color: 'rgba(255,255,255,0.5)',
    fontSize: 14,
  },
});
