import React, { useEffect, useCallback, useState } from 'react';
import { View, StyleSheet, StatusBar } from 'react-native';
import Board from '../components/Board';
import ScoreBar from '../components/ScoreBar';
import Cannon from '../components/Cannon';
import PowerUpBar from '../components/PowerUpBar';
import LevelCompleteModal from '../components/LevelCompleteModal';
import GameOverModal from '../components/GameOverModal';
import NoLivesModal from '../components/NoLivesModal';
import AchievementPopup from '../components/AchievementPopup';
import { useGameStore } from '../stores/gameStore';
import { useLivesStore } from '../stores/livesStore';
import { useStatsStore } from '../stores/statsStore';
import { useAchievementStore } from '../stores/achievementStore';
import { BG_COLOR } from '../constants/colors';
import { GRID_PADDING } from '../constants/dimensions';
import { soundManager } from '../services/SoundManager';

interface Props {
  level?: number;
  onBack?: () => void;
}

export default function GameScreen({ level = 1, onBack }: Props) {
  const phase = useGameStore((s) => s.phase);
  const startLevel = useGameStore((s) => s.startLevel);
  const currentLevel = useGameStore((s) => s.currentLevel);
  const unlockNextLevel = useGameStore((s) => s.unlockNextLevel);
  const incrementStreak = useGameStore((s) => s.incrementStreak);
  const resetStreak = useGameStore((s) => s.resetStreak);
  const saveHighScore = useGameStore((s) => s.saveHighScore);
  const stars = useGameStore((s) => s.stars);

  const hasLives = useLivesStore((s) => s.hasLives());
  const loseLife = useLivesStore((s) => s.loseLife);

  const addLevelCompleted = useStatsStore((s) => s.addLevelCompleted);
  const incrementWinStreak = useStatsStore((s) => s.incrementWinStreak);
  const resetWinStreak = useStatsStore((s) => s.resetWinStreak);
  const addThreeStarLevel = useStatsStore((s) => s.addThreeStarLevel);

  const checkAchievements = useAchievementStore((s) => s.checkAchievements);

  const [showNoLives, setShowNoLives] = useState(false);

  useEffect(() => {
    startLevel(level);
  }, [level, startLevel]);

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
    }
    onBack?.();
  }, [phase, unlockNextLevel, onBack]);

  const isPlaying = phase === 'idle' || phase === 'swapping' || phase === 'matching' || phase === 'falling';

  return (
    <View style={styles.container}>
      <StatusBar barStyle="light-content" backgroundColor={BG_COLOR} />

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
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: BG_COLOR,
  },
  boardWrapper: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    paddingHorizontal: GRID_PADDING,
  },
});
