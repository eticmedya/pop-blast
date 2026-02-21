import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
} from 'react-native';
import { useTranslation } from 'react-i18next';
import { useGameStore } from '../stores/gameStore';
import { LEVELS } from '../game-engine/levels';
import {
  BG_COLOR,
  TEXT_COLOR,
  ACCENT_COLOR,
  SCORE_COLOR,
  WORLD_COLORS,
} from '../constants/colors';

interface Props {
  onSelectLevel: (level: number) => void;
  onBack: () => void;
}

const WORLD_NAMES: string[] = [
  'levelSelect.world1',
  'levelSelect.world2',
  'levelSelect.world3',
  'levelSelect.world4',
  'levelSelect.world5',
  'levelSelect.world6',
  'levelSelect.world7',
  'levelSelect.world8',
  'levelSelect.world9',
  'levelSelect.world10',
];

export default function LevelSelectScreen({ onSelectLevel, onBack }: Props) {
  const { t } = useTranslation();
  const unlockedLevel = useGameStore((s) => s.unlockedLevel);
  const highScores = useGameStore((s) => s.highScores);

  const LEVELS_PER_WORLD = 5;
  const worlds = Array.from(
    { length: Math.ceil(LEVELS.length / LEVELS_PER_WORLD) },
    (_, i) => LEVELS.slice(i * LEVELS_PER_WORLD, (i + 1) * LEVELS_PER_WORLD),
  );

  return (
    <View style={styles.container}>
      <View style={styles.header}>
        <TouchableOpacity onPress={onBack} style={styles.backBtn}>
          <Text style={styles.backText}>{'<'} {t('levelSelect.back')}</Text>
        </TouchableOpacity>
        <Text style={styles.title}>{t('levelSelect.title')}</Text>
        <View style={styles.backBtn} />
      </View>

      <ScrollView contentContainerStyle={styles.scrollContent}>
        {worlds.map((world, worldIdx) => {
          const theme = WORLD_COLORS[worldIdx];
          return (
            <View key={worldIdx} style={styles.worldSection}>
              <View style={[styles.worldHeader, { borderBottomColor: theme.primary }]}>
                <Text style={[styles.worldTitle, { color: theme.primary }]}>
                  {t(WORLD_NAMES[worldIdx])}
                </Text>
              </View>
              <View style={styles.levelGrid}>
                {world.map((level) => {
                  const isLocked = level.level > unlockedLevel;
                  const hs = highScores[level.level];
                  const starCount = hs?.stars ?? 0;

                  return (
                    <TouchableOpacity
                      key={level.level}
                      style={[
                        styles.levelBtn,
                        {
                          backgroundColor: isLocked
                            ? 'rgba(255,255,255,0.05)'
                            : theme.primary,
                        },
                        level.level === unlockedLevel && !isLocked && {
                          borderWidth: 2,
                          borderColor: '#fff',
                          shadowColor: theme.primary,
                          shadowOffset: { width: 0, height: 0 },
                          shadowOpacity: 0.6,
                          shadowRadius: 8,
                          elevation: 8,
                        },
                      ]}
                      onPress={() => {
                        if (!isLocked) onSelectLevel(level.level);
                      }}
                      disabled={isLocked}
                    >
                      {isLocked ? (
                        <Text style={styles.lockIcon}>🔒</Text>
                      ) : (
                        <>
                          <Text style={styles.levelNum}>{level.level}</Text>
                          {starCount > 0 && (
                            <Text style={styles.miniStars}>
                              {'★'.repeat(starCount)}
                              {'☆'.repeat(3 - starCount)}
                            </Text>
                          )}
                        </>
                      )}
                    </TouchableOpacity>
                  );
                })}
              </View>
            </View>
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
    fontSize: 22,
    fontWeight: '900',
    letterSpacing: 1,
  },
  scrollContent: {
    padding: 16,
    paddingBottom: 40,
  },
  worldSection: {
    marginBottom: 28,
  },
  worldHeader: {
    borderBottomWidth: 2,
    paddingBottom: 8,
    marginBottom: 14,
  },
  worldTitle: {
    fontSize: 16,
    fontWeight: '800',
    letterSpacing: 1,
  },
  levelGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'center',
    gap: 12,
  },
  levelBtn: {
    width: 60,
    height: 60,
    borderRadius: 16,
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
    elevation: 3,
  },
  levelNum: {
    color: TEXT_COLOR,
    fontSize: 22,
    fontWeight: 'bold',
  },
  miniStars: {
    color: SCORE_COLOR,
    fontSize: 8,
    marginTop: 1,
  },
  lockIcon: {
    fontSize: 18,
  },
});
