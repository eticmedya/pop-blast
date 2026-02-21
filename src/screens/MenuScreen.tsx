import React from 'react';
import { View, Text, StyleSheet, TouchableOpacity } from 'react-native';
import { BG_COLOR, TEXT_COLOR, ACCENT_COLOR, SCORE_COLOR } from '../constants/colors';

interface Props {
  onPlay: () => void;
}

export default function MenuScreen({ onPlay }: Props) {
  return (
    <View style={styles.container}>
      <View style={styles.titleContainer}>
        <Text style={styles.titlePop}>POP</Text>
        <Text style={styles.titleBlast}>BLAST</Text>
      </View>

      <Text style={styles.subtitle}>Match & Shoot Puzzle</Text>

      {/* Dekoratif toplar */}
      <View style={styles.ballRow}>
        <View style={[styles.ball, { backgroundColor: '#FF4757' }]} />
        <View style={[styles.ball, { backgroundColor: '#3742FA' }]} />
        <View style={[styles.ball, { backgroundColor: '#2ED573' }]} />
        <View style={[styles.ball, { backgroundColor: '#FFA502' }]} />
        <View style={[styles.ball, { backgroundColor: '#A855F7' }]} />
      </View>

      <TouchableOpacity style={styles.playBtn} onPress={onPlay}>
        <Text style={styles.playText}>OYNA</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: BG_COLOR,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 32,
  },
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'baseline',
    marginBottom: 8,
  },
  titlePop: {
    fontSize: 56,
    fontWeight: '900',
    color: ACCENT_COLOR,
    letterSpacing: 2,
  },
  titleBlast: {
    fontSize: 56,
    fontWeight: '900',
    color: SCORE_COLOR,
    letterSpacing: 2,
    marginLeft: 4,
  },
  subtitle: {
    color: 'rgba(255,255,255,0.4)',
    fontSize: 16,
    letterSpacing: 4,
    marginBottom: 48,
  },
  ballRow: {
    flexDirection: 'row',
    gap: 12,
    marginBottom: 60,
  },
  ball: {
    width: 32,
    height: 32,
    borderRadius: 16,
  },
  playBtn: {
    backgroundColor: ACCENT_COLOR,
    paddingHorizontal: 64,
    paddingVertical: 18,
    borderRadius: 20,
    shadowColor: ACCENT_COLOR,
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.4,
    shadowRadius: 12,
    elevation: 8,
  },
  playText: {
    color: TEXT_COLOR,
    fontSize: 24,
    fontWeight: 'bold',
    letterSpacing: 4,
  },
});
