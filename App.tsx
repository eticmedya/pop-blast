import React, { useState, useCallback, useEffect } from 'react';
import { StatusBar } from 'expo-status-bar';
import './src/i18n';
import MenuScreen from './src/screens/MenuScreen';
import LevelSelectScreen from './src/screens/LevelSelectScreen';
import GameScreen from './src/screens/GameScreen';
import SettingsScreen from './src/screens/SettingsScreen';
import DailyRewardModal from './src/components/DailyRewardModal';
import { soundManager } from './src/services/SoundManager';
import { useLivesStore } from './src/stores/livesStore';
import { useSettingsStore } from './src/stores/settingsStore';
import { useGameStore } from './src/stores/gameStore';

type Screen = 'menu' | 'levelSelect' | 'game' | 'settings';

export default function App() {
  const [screen, setScreen] = useState<Screen>('menu');
  const [selectedLevel, setSelectedLevel] = useState(1);
  const [isResuming, setIsResuming] = useState(false);
  const [showDailyReward, setShowDailyReward] = useState(false);

  const checkRegen = useLivesStore((s) => s.checkRegen);
  const soundEnabled = useSettingsStore((s) => s.soundEnabled);
  const activeLevel = useGameStore((s) => s.currentLevel);

  // Initialize on app start
  useEffect(() => {
    soundManager.preload();
    soundManager.setMuted(!soundEnabled);
    checkRegen();
  }, []);

  const handlePlay = useCallback(() => {
    setIsResuming(false);
    setScreen('levelSelect');
  }, []);

  const handleContinue = useCallback(() => {
    setSelectedLevel(activeLevel);
    setIsResuming(true);
    setScreen('game');
  }, [activeLevel]);

  const handleSelectLevel = useCallback((level: number) => {
    setSelectedLevel(level);
    setIsResuming(false);
    setScreen('game');
  }, []);

  const handleBack = useCallback(() => {
    setIsResuming(false);
    setScreen('menu');
  }, []);

  const handleBackToLevels = useCallback(() => {
    setIsResuming(false);
    setScreen('levelSelect');
  }, []);

  const handleSettings = useCallback(() => {
    setScreen('settings');
  }, []);

  const handleDailyReward = useCallback(() => {
    setShowDailyReward(true);
  }, []);

  return (
    <>
      <StatusBar style="light" />
      {screen === 'menu' && (
        <MenuScreen
          onPlay={handlePlay}
          onContinue={handleContinue}
          onSettings={handleSettings}
          onDailyReward={handleDailyReward}
        />
      )}
      {screen === 'levelSelect' && (
        <LevelSelectScreen
          onSelectLevel={handleSelectLevel}
          onBack={handleBack}
        />
      )}
      {screen === 'game' && (
        <GameScreen
          level={selectedLevel}
          resume={isResuming}
          onBack={handleBackToLevels}
        />
      )}
      {screen === 'settings' && (
        <SettingsScreen onBack={handleBack} />
      )}
      <DailyRewardModal
        visible={showDailyReward}
        onClose={() => setShowDailyReward(false)}
      />
    </>
  );
}
