import React, { useMemo } from 'react';
import { View, Text, StyleSheet, Image, Pressable } from 'react-native';
import { LinearGradient } from 'expo-linear-gradient';
import { Ionicons } from '@expo/vector-icons';
import { useTranslation } from 'react-i18next';
import { getLevelConfig } from '../game-engine/levels';
import { getWorldTheme } from '../constants/themes';
import { usePowerUpStore } from '../stores/powerupStore';
import { SCREEN_WIDTH } from '../constants/dimensions';
import { TILE_COLORS } from '../constants/colors';

interface Props {
  level: number;
  onStart: () => void;
  onBack: () => void;
}

export default function LevelStartModal({ level, onStart, onBack }: Props) {
  const { t } = useTranslation();
  const config = useMemo(() => getLevelConfig(level), [level]);
  const theme = useMemo(() => getWorldTheme(level), [level]);

  const inventory = usePowerUpStore((s) => s.inventory);

  if (!config) return null;

  const emojis = theme.tileTheme.emojis.slice(0, config.numColors);

  return (
    <View style={styles.overlay}>
      <View style={styles.card}>
        <LinearGradient
          colors={['#FFFBF0', '#FFF5E1', '#FFEED4']}
          style={styles.cardGradient}
          start={{ x: 0, y: 0 }}
          end={{ x: 0, y: 1 }}
        >
          {/* Üst mor banner */}
          <LinearGradient
            colors={[theme.accent, theme.secondary]}
            style={styles.banner}
            start={{ x: 0, y: 0 }}
            end={{ x: 1, y: 0 }}
          >
            <Pressable style={styles.closeBtn} onPress={onBack}>
              <Ionicons name="close" size={22} color="#fff" />
            </Pressable>
            <Text style={styles.levelText}>{t('levelStart.level', { number: level })}</Text>
          </LinearGradient>

          {/* Karakter */}
          <Image
            source={theme.character}
            style={styles.character}
            resizeMode="contain"
          />

          {/* Hedef bölümü */}
          <Text style={styles.goalTitle}>{t('levelStart.goal')}</Text>
          <View style={styles.goalRow}>
            {emojis.map((emoji, i) => (
              <View key={i} style={styles.goalItem}>
                <View style={[styles.goalBg, { backgroundColor: TILE_COLORS[i] + '25' }]}>
                  <Text style={styles.goalEmoji}>{emoji}</Text>
                </View>
              </View>
            ))}
          </View>

          {/* Hedef skor */}
          <View style={styles.targetRow}>
            <View style={styles.targetItem}>
              <Ionicons name="trophy" size={18} color="#F39C12" />
              <Text style={styles.targetLabel}>{config.targetScore.toLocaleString()}</Text>
            </View>
            <View style={styles.targetItem}>
              <Ionicons name="swap-horizontal" size={18} color={theme.accent} />
              <Text style={styles.targetLabel}>{config.maxMoves} {t('levelStart.moves')}</Text>
            </View>
          </View>

          {/* Booster seçimi */}
          <View style={styles.boosterSection}>
            <Text style={styles.boosterTitle}>{t('levelStart.boosters')}</Text>
            <View style={styles.boosterRow}>
              {(['rowBomb', 'colBomb', 'colorBomb', 'shuffle'] as const).map((type) => (
                <View key={type} style={styles.boosterItem}>
                  <View style={styles.boosterIcon}>
                    <Text style={styles.boosterEmoji}>
                      {type === 'rowBomb' ? '💣' : type === 'colBomb' ? '🧨' : type === 'colorBomb' ? '🌈' : '🔄'}
                    </Text>
                  </View>
                  <View style={styles.boosterBadge}>
                    <Text style={styles.boosterCount}>{inventory[type]}</Text>
                  </View>
                </View>
              ))}
            </View>
          </View>

          {/* Başla butonu */}
          <Pressable onPress={onStart}>
            <LinearGradient
              colors={[theme.accent, theme.secondary]}
              style={styles.startBtn}
              start={{ x: 0, y: 0 }}
              end={{ x: 1, y: 0 }}
            >
              <Ionicons name="play" size={28} color="#fff" />
            </LinearGradient>
          </Pressable>
        </LinearGradient>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  overlay: {
    position: 'absolute',
    top: 0,
    left: 0,
    right: 0,
    bottom: 0,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: 'rgba(0,0,0,0.7)',
    zIndex: 300,
  },
  card: {
    width: SCREEN_WIDTH * 0.82,
    borderRadius: 28,
    overflow: 'hidden',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 12 },
    shadowOpacity: 0.4,
    shadowRadius: 20,
    elevation: 16,
  },
  cardGradient: {
    padding: 0,
    alignItems: 'center',
  },
  banner: {
    width: '100%',
    paddingVertical: 18,
    alignItems: 'center',
    borderTopLeftRadius: 28,
    borderTopRightRadius: 28,
  },
  closeBtn: {
    position: 'absolute',
    right: 16,
    top: 14,
    width: 32,
    height: 32,
    borderRadius: 16,
    backgroundColor: 'rgba(0,0,0,0.2)',
    justifyContent: 'center',
    alignItems: 'center',
  },
  levelText: {
    color: '#fff',
    fontSize: 24,
    fontWeight: '900',
    letterSpacing: 1,
    textShadowColor: 'rgba(0,0,0,0.3)',
    textShadowOffset: { width: 0, height: 2 },
    textShadowRadius: 4,
  },
  character: {
    width: 80,
    height: 80,
    marginTop: -20,
    marginBottom: 4,
  },
  goalTitle: {
    fontSize: 16,
    fontWeight: '800',
    color: '#5D4037',
    letterSpacing: 2,
    marginBottom: 10,
  },
  goalRow: {
    flexDirection: 'row',
    gap: 12,
    marginBottom: 16,
  },
  goalItem: {
    alignItems: 'center',
  },
  goalBg: {
    width: 48,
    height: 48,
    borderRadius: 12,
    justifyContent: 'center',
    alignItems: 'center',
  },
  goalEmoji: {
    fontSize: 28,
  },
  targetRow: {
    flexDirection: 'row',
    gap: 24,
    marginBottom: 16,
  },
  targetItem: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 6,
    backgroundColor: 'rgba(0,0,0,0.05)',
    paddingHorizontal: 14,
    paddingVertical: 8,
    borderRadius: 12,
  },
  targetLabel: {
    fontSize: 15,
    fontWeight: '700',
    color: '#5D4037',
  },
  boosterSection: {
    width: '100%',
    paddingHorizontal: 24,
    marginBottom: 16,
  },
  boosterTitle: {
    fontSize: 12,
    fontWeight: '700',
    color: '#9E9E9E',
    letterSpacing: 1,
    textAlign: 'center',
    marginBottom: 10,
  },
  boosterRow: {
    flexDirection: 'row',
    justifyContent: 'center',
    gap: 16,
  },
  boosterItem: {
    position: 'relative',
  },
  boosterIcon: {
    width: 50,
    height: 50,
    borderRadius: 14,
    backgroundColor: '#FFF8E1',
    justifyContent: 'center',
    alignItems: 'center',
    borderWidth: 2,
    borderColor: 'rgba(0,0,0,0.08)',
  },
  boosterEmoji: {
    fontSize: 26,
  },
  boosterBadge: {
    position: 'absolute',
    top: -6,
    right: -6,
    backgroundColor: '#F39C12',
    borderRadius: 10,
    minWidth: 20,
    height: 20,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: 4,
  },
  boosterCount: {
    color: '#fff',
    fontSize: 11,
    fontWeight: '900',
  },
  startBtn: {
    width: 64,
    height: 64,
    borderRadius: 32,
    justifyContent: 'center',
    alignItems: 'center',
    marginBottom: 24,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 4 },
    shadowOpacity: 0.3,
    shadowRadius: 8,
    elevation: 8,
  },
});
