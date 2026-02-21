import React, { useEffect, useCallback } from 'react';
import { View, StyleSheet, StatusBar } from 'react-native';
import { GestureHandlerRootView } from 'react-native-gesture-handler';
import Board from '../components/Board';
import ScoreBar from '../components/ScoreBar';
import LevelCompleteModal from '../components/LevelCompleteModal';
import GameOverModal from '../components/GameOverModal';
import { useGameStore } from '../stores/gameStore';
import { BG_COLOR } from '../constants/colors';
import { GRID_PADDING } from '../constants/dimensions';

interface Props {
  level?: number;
  onBack?: () => void;
}

export default function GameScreen({ level = 1, onBack }: Props) {
  const phase = useGameStore((s) => s.phase);
  const startLevel = useGameStore((s) => s.startLevel);
  const currentLevel = useGameStore((s) => s.currentLevel);
  const unlockNextLevel = useGameStore((s) => s.unlockNextLevel);

  useEffect(() => {
    startLevel(level);
  }, [level, startLevel]);

  const handleRestart = useCallback(() => {
    startLevel(currentLevel);
  }, [currentLevel, startLevel]);

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

  return (
    <GestureHandlerRootView style={styles.root}>
      <View style={styles.container}>
        <StatusBar barStyle="light-content" backgroundColor={BG_COLOR} />

        <ScoreBar />

        <View style={styles.boardWrapper}>
          <Board />
        </View>

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
      </View>
    </GestureHandlerRootView>
  );
}

const styles = StyleSheet.create({
  root: {
    flex: 1,
  },
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
