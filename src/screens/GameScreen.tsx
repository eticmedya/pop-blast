import React, { useEffect, useCallback, useState, useMemo } from 'react';
import { View, StyleSheet, StatusBar, Pressable } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import Board from '../components/Board';
import ScoreBar from '../components/ScoreBar';
import Cannon from '../components/Cannon';
import PowerUpBar from '../components/PowerUpBar';
import LevelCompleteModal from '../components/LevelCompleteModal';
import GameOverModal from '../components/GameOverModal';
import NoLivesModal from '../components/NoLivesModal';
import AchievementPopup from '../components/AchievementPopup';
import GradientBackground from '../components/GradientBackground';
import LevelStartModal from '../components/LevelStartModal';
import { useGameStore } from '../stores/gameStore';
import { useSettingsStore } from '../stores/settingsStore';
import { useLivesStore } from '../stores/livesStore';
import { useStatsStore } from '../stores/statsStore';
import { useAchievementStore } from '../stores/achievementStore';
import { getWorldTheme } from '../constants/themes';
import { GRID_PADDING } from '../constants/dimensions';
import { soundManager } from '../services/SoundManager';
import { hapticService } from '../services/HapticService';

interface Props {
  level?: number;
  resume?: boolean;
  onBack?: () => void;
}

export default function GameScreen({ level = 1, resume = false, onBack }: Props) {
  const phase = useGameStore((s) => s.phase);
  const startLevel = useGameStore((s) => s.startLevel);
  const currentLevel = useGameStore((s) => s.currentLevel);
  const unlockNextLevel = useGameStore((s) => s.unlockNextLevel);
  const incrementStreak = useGameStore((s) => s.incrementStreak);
  const resetStreak = useGameStore((s) => s.resetStreak);
  const saveHighScore = useGameStore((s) => s.saveHighScore);
  const clearActiveGame = useGameStore((s) => s.clearActiveGame);
  const stars = useGameStore((s) => s.stars);

  const soundEnabled = useSettingsStore((s) => s.soundEnabled);
  const setSoundEnabled = useSettingsStore((s) => s.setSoundEnabled);

  const hasLives = useLivesStore((s) => s.hasLives());
  const loseLife = useLivesStore((s) => s.loseLife);

  const addLevelCompleted = useStatsStore((s) => s.addLevelCompleted);
  const incrementWinStreak = useStatsStore((s) => s.incrementWinStreak);
  const resetWinStreak = useStatsStore((s) => s.resetWinStreak);
  const addThreeStarLevel = useStatsStore((s) => s.addThreeStarLevel);

  const checkAchievements = useAchievementStore((s) => s.checkAchievements);

  const [showNoLives, setShowNoLives] = useState(false);
  const [showLevelStart, setShowLevelStart] = useState(!resume);

  // Dünya teması
  const worldTheme = useMemo(() => getWorldTheme(resume ? currentLevel : level), [level, resume, currentLevel]);
  const gradientColors = worldTheme.bgGradient as [string, string, ...string[]];

  useEffect(() => {
    if (!resume && !showLevelStart) {
      startLevel(level);
    }
  }, [level, resume, startLevel, showLevelStart]);

  // Handle level complete
  useEffect(() => {
    if (phase === 'levelComplete') {
      soundManager.play('win');
      saveHighScore();
      incrementStreak();
      addLevelCompleted();
      incrementWinStreak();
      if (stars >= 3) addThreeStarLevel();
      setTimeout(() => checkAchievements(), 500);
    }
  }, [phase === 'levelComplete']);

  // Handle game over
  useEffect(() => {
    if (phase === 'gameOver') {
      soundManager.play('lose');
      loseLife();
      resetStreak();
      resetWinStreak();
    }
  }, [phase === 'gameOver']);

  const handleStartLevel = useCallback(() => {
    setShowLevelStart(false);
    startLevel(level);
  }, [level, startLevel]);

  const handleRestart = useCallback(() => {
    if (!hasLives) {
      setShowNoLives(true);
      return;
    }
    startLevel(currentLevel);
  }, [currentLevel, startLevel, hasLives]);

  const handleNextLevel = useCallback(() => {
    unlockNextLevel();
    startLevel(currentLevel + 1);
  }, [currentLevel, startLevel, unlockNextLevel]);

  const handleMenu = useCallback(() => {
    if (phase === 'levelComplete') {
      unlockNextLevel();
      clearActiveGame();
    } else if (phase === 'gameOver') {
      clearActiveGame();
    }
    onBack?.();
  }, [phase, unlockNextLevel, clearActiveGame, onBack]);

  const handleHome = useCallback(() => {
    hapticService.buttonPress();
    onBack?.();
  }, [onBack]);

  const toggleSound = useCallback(() => {
    hapticService.buttonPress();
    const newValue = !soundEnabled;
    setSoundEnabled(newValue);
    soundManager.setMuted(!newValue);
  }, [soundEnabled, setSoundEnabled]);

  const isPlaying = phase === 'idle' || phase === 'swapping' || phase === 'matching' || phase === 'falling';

  return (
    <GradientBackground
      colors={gradientColors}
      showBubbles
      bubbleColors={worldTheme.particleColors}
    >
      <StatusBar barStyle="light-content" backgroundColor="transparent" translucent />

      {/* Seviye Başlangıç Modalı */}
      {showLevelStart && !resume && (
        <LevelStartModal
          level={level}
          onStart={handleStartLevel}
          onBack={handleHome}
        />
      )}

      {/* Üst aksiyon butonları */}
      <View style={styles.actionBar}>
        <Pressable
          style={[styles.actionBtn, { backgroundColor: worldTheme.headerBg }]}
          onPress={handleHome}
        >
          <Ionicons name="home-outline" size={22} color="rgba(255,255,255,0.85)" />
        </Pressable>
        <Pressable
          style={[styles.actionBtn, { backgroundColor: worldTheme.headerBg }]}
          onPress={toggleSound}
        >
          <Ionicons
            name={soundEnabled ? 'volume-high' : 'volume-mute'}
            size={22}
            color={soundEnabled ? 'rgba(255,255,255,0.85)' : 'rgba(255,80,80,0.85)'}
          />
        </Pressable>
      </View>

      <ScoreBar />

      <View style={styles.boardWrapper}>
        <Board />
        <Cannon />
      </View>

      <PowerUpBar disabled={!isPlaying || phase !== 'idle'} />

      <LevelCompleteModal
        visible={phase === 'levelComplete'}
        onNext={handleNextLevel}
        onMenu={handleMenu}
      />

      <GameOverModal
        visible={phase === 'gameOver'}
        onRestart={handleRestart}
        onMenu={handleMenu}
      />

      <NoLivesModal
        visible={showNoLives}
        onClose={() => setShowNoLives(false)}
      />

      <AchievementPopup />
    </GradientBackground>
  );
}

const styles = StyleSheet.create({
  actionBar: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    paddingHorizontal: 16,
    paddingTop: 4,
  },
  actionBtn: {
    width: 44,
    height: 44,
    borderRadius: 22,
    justifyContent: 'center',
    alignItems: 'center',
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.3,
    shadowRadius: 4,
    elevation: 4,
  },
  boardWrapper: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: GRID_PADDING,
  },
});
