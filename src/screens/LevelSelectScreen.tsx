import React from 'react';
import {
  View,
  Text,
  StyleSheet,
  TouchableOpacity,
  ScrollView,
  Image,
} from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { Ionicons } from '@expo/vector-icons';
import { useTranslation } from 'react-i18next';
import { useGameStore } from '../stores/gameStore';
import { LEVELS } from '../game-engine/levels';
import { WORLD_THEMES } from '../constants/themes';
import { SCREEN_WIDTH } from '../constants/dimensions';

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
    <LinearGradient
      colors={['#7B2FF7', '#4A90D9', '#67D5B5']}
      style={styles.container}
      start={{ x: 0, y: 0 }}
      end={{ x: 0.3, y: 1 }}
    >
      <View style={styles.header}>
        <TouchableOpacity onPress={onBack} style={styles.backBtn}>
          <Ionicons name="arrow-back" size={22} color="#fff" />
        </TouchableOpacity>
        <Text style={styles.title}>{t('levelSelect.title')}</Text>
        <View style={styles.backBtn} />
      </View>

      <ScrollView contentContainerStyle={styles.scrollContent} showsVerticalScrollIndicator={false}>
        {worlds.map((world, worldIdx) => {
          const theme = WORLD_THEMES[worldIdx % WORLD_THEMES.length];
          return (
            <View key={worldIdx} style={styles.worldSection}>
              {/* Dünya başlığı - karakterli */}
              <LinearGradient
                colors={[theme.accent + 'DD', theme.secondary + 'DD']}
                style={styles.worldHeader}
                start={{ x: 0, y: 0 }}
                end={{ x: 1, y: 0 }}
              >
                <Image source={theme.character} style={styles.worldCharacter} resizeMode="contain" />
                <View>
                  <Text style={styles.worldTitle}>{t(WORLD_NAMES[worldIdx])}</Text>
                  <Text style={styles.worldEmojis}>
                    {theme.tileTheme.emojis.slice(0, 4).join(' ')}
                  </Text>
                </View>
              </LinearGradient>

              {/* Seviye butonları */}
              <View style={styles.levelGrid}>
                {world.map((level) => {
                  const isLocked = level.level > unlockedLevel;
                  const isCurrent = level.level === unlockedLevel;
                  const hs = highScores[level.level];
                  const starCount = hs?.stars ?? 0;

                  return (
                    <TouchableOpacity
                      key={level.level}
                      style={[
                        styles.levelBtn,
                        isLocked && styles.levelBtnLocked,
                        isCurrent && !isLocked && {
                          borderWidth: 3,
                          borderColor: theme.accent,
                          shadowColor: theme.accent,
                          shadowOffset: { width: 0, height: 0 },
                          shadowOpacity: 0.6,
                          shadowRadius: 10,
                          elevation: 10,
                        },
                      ]}
                      onPress={() => {
                        if (!isLocked) onSelectLevel(level.level);
                      }}
                      disabled={isLocked}
                    >
                      {isLocked ? (
                        <Ionicons name="lock-closed" size={20} color="rgba(0,0,0,0.2)" />
                      ) : (
                        <>
                          <Text style={styles.levelNum}>{level.level}</Text>
                          <View style={styles.starsRow}>
                            {Array.from({ length: 3 }, (_, i) => (
                              <Ionicons
                                key={i}
                                name={i < starCount ? 'star' : 'star-outline'}
                                size={10}
                                color={i < starCount ? '#F59E0B' : 'rgba(0,0,0,0.15)'}
                              />
                            ))}
                          </View>
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
    </LinearGradient>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
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
    width: 44,
    height: 44,
    borderRadius: 22,
    backgroundColor: 'rgba(0,0,0,0.15)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    color: '#fff',
    fontSize: 24,
    fontWeight: '900',
    letterSpacing: 1,
    textShadowColor: 'rgba(0,0,0,0.2)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 4,
  },
  scrollContent: {
    padding: 16,
    paddingBottom: 40,
  },
  worldSection: {
    marginBottom: 24,
  },
  worldHeader: {
    flexDirection: 'row',
    alignItems: 'center',
    borderRadius: 16,
    paddingVertical: 12,
    paddingHorizontal: 16,
    marginBottom: 12,
    gap: 12,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.2,
    shadowRadius: 8,
    elevation: 4,
  },
  worldCharacter: {
    width: 44,
    height: 44,
  },
  worldTitle: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '800',
    letterSpacing: 0.5,
    textShadowColor: 'rgba(0,0,0,0.2)',
    textShadowOffset: { width: 0, height: 1 },
    textShadowRadius: 2,
  },
  worldEmojis: {
    fontSize: 14,
    marginTop: 2,
  },
  levelGrid: {
    flexDirection: 'row',
    flexWrap: 'wrap',
    justifyContent: 'center',
    gap: 12,
  },
  levelBtn: {
    width: 62,
    height: 62,
    borderRadius: 18,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#FFFBF0',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.15,
    shadowRadius: 4,
    elevation: 3,
  },
  levelBtnLocked: {
    backgroundColor: 'rgba(255,255,255,0.3)',
  },
  levelNum: {
    color: '#5D4037',
    fontSize: 22,
    fontWeight: '900',
  },
  starsRow: {
    flexDirection: 'row',
    gap: 1,
    marginTop: 2,
  },
});
