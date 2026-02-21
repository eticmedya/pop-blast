import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
} from 'react-native';
import { useGameStore } from '../stores/gameStore';
import { LEVELS } from '../game-engine/levels';
import { BG_COLOR, TEXT_COLOR, ACCENT_COLOR, SCORE_COLOR } from '../constants/colors';

interface Props {
  onSelectLevel: (level: number) => void;
  onBack: () => void;
}

export default function LevelSelectScreen({ onSelectLevel, onBack }: Props) {
  const unlockedLevel = useGameStore((s) => s.unlockedLevel);

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <TouchableOpacity onPress={onBack} style={styles.backBtn}>
          <Text style={styles.backText}>{'<'} Geri</Text>
        </TouchableOpacity>
        <Text style={styles.title}>Seviyeler</Text>
        <View style={styles.backBtn} />
      </View>

      <ScrollView contentContainerStyle={styles.grid}>
        {LEVELS.map((level) => {
          const isLocked = level.level > unlockedLevel;

          return (
            <TouchableOpacity
              key={level.level}
              style={[
                styles.levelBtn,
                isLocked && styles.lockedBtn,
              ]}
              onPress={() => {
                if (!isLocked) onSelectLevel(level.level);
              }}
              disabled={isLocked}
            >
              {isLocked ? (
                <Text style={styles.lockIcon}>🔒</Text>
              ) : (
                <Text style={styles.levelNum}>{level.level}</Text>
              )}
            </TouchableOpacity>
          );
        })}
      </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: BG_COLOR,
  },
  header: {
    flexDirection: 'row',
    alignItems: 'center',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingTop: 60,
    paddingBottom: 16,
  },
  backBtn: {
    width: 80,
  },
  backText: {
    color: ACCENT_COLOR,
    fontSize: 16,
    fontWeight: '600',
  },
  title: {
    color: TEXT_COLOR,
    fontSize: 24,
    fontWeight: 'bold',
  },
  grid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'center',
    padding: 16,
    gap: 12,
  },
  levelBtn: {
    width: 64,
    height: 64,
    borderRadius: 16,
    backgroundColor: ACCENT_COLOR,
    justifyContent: 'center',
    alignItems: 'center',
  },
  lockedBtn: {
    backgroundColor: 'rgba(255,255,255,0.08)',
  },
  levelNum: {
    color: TEXT_COLOR,
    fontSize: 22,
    fontWeight: 'bold',
  },
  lockIcon: {
    fontSize: 20,
  },
});
