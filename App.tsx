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

type Screen = 'menu' | 'levelSelect' | 'game' | 'settings';

export default function App() {
  const [screen, setScreen] = useState<Screen>('menu');
  const [selectedLevel, setSelectedLevel] = useState(1);
  const [showDailyReward, setShowDailyReward] = useState(false);

  const checkRegen = useLivesStore((s) => s.checkRegen);
  const soundEnabled = useSettingsStore((s) => s.soundEnabled);

  // Initialize on app start
  useEffect(() => {
    soundManager.preload();
    soundManager.setMuted(!soundEnabled);
    checkRegen();
  }, []);

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
        <GameScreen level={selectedLevel} onBack={handleBackToLevels} />
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
