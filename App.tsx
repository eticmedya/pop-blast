import React, { useState, useCallback } from 'react';
import { StatusBar } from 'expo-status-bar';
import MenuScreen from './src/screens/MenuScreen';
import LevelSelectScreen from './src/screens/LevelSelectScreen';
import GameScreen from './src/screens/GameScreen';

type Screen = 'menu' | 'levelSelect' | 'game';

export default function App() {
  const [screen, setScreen] = useState<Screen>('menu');
  const [selectedLevel, setSelectedLevel] = useState(1);

  const handlePlay = useCallback(() => {
    setScreen('levelSelect');
  }, []);

  const handleSelectLevel = useCallback((level: number) => {
    setSelectedLevel(level);
    setScreen('game');
  }, []);

  const handleBack = useCallback(() => {
    setScreen('menu');
  }, []);

  const handleBackToLevels = useCallback(() => {
    setScreen('levelSelect');
  }, []);

  return (
    <>
      <StatusBar style="light" />
      {screen === 'menu' && <MenuScreen onPlay={handlePlay} />}
      {screen === 'levelSelect' && (
        <LevelSelectScreen onSelectLevel={handleSelectLevel} onBack={handleBack} />
      )}
      {screen === 'game' && (
        <GameScreen level={selectedLevel} onBack={handleBackToLevels} />
      )}
    </>
  );
}
