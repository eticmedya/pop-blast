import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import AsyncStorage from '@react-native-async-storage/async-storage';

interface StatsState {
  totalMatches: number;
  totalLevelsCompleted: number;
  totalScore: number;
  totalCombos: number;
  totalPowerUpsUsed: number;
  totalCannonsFired: number;
  maxCascade: number;
  consecutiveWins: number;
  bestStreak: number;
  threeStarLevels: number;

  addMatches: (count: number) => void;
  addLevelCompleted: () => void;
  addScore: (score: number) => void;
  addCombo: () => void;
  addPowerUpUsed: () => void;
  addCannonFired: () => void;
  setMaxCascade: (cascade: number) => void;
  incrementWinStreak: () => void;
  resetWinStreak: () => void;
  addThreeStarLevel: () => void;
}

export const useStatsStore = create<StatsState>()(
  persist(
    (set, get) => ({
      totalMatches: 0,
      totalLevelsCompleted: 0,
      totalScore: 0,
      totalCombos: 0,
      totalPowerUpsUsed: 0,
      totalCannonsFired: 0,
      maxCascade: 0,
      consecutiveWins: 0,
      bestStreak: 0,
      threeStarLevels: 0,

      addMatches: (count) =>
        set((s) => ({ totalMatches: s.totalMatches + count })),
      addLevelCompleted: () =>
        set((s) => ({ totalLevelsCompleted: s.totalLevelsCompleted + 1 })),
      addScore: (score) =>
        set((s) => ({ totalScore: s.totalScore + score })),
      addCombo: () =>
        set((s) => ({ totalCombos: s.totalCombos + 1 })),
      addPowerUpUsed: () =>
        set((s) => ({ totalPowerUpsUsed: s.totalPowerUpsUsed + 1 })),
      addCannonFired: () =>
        set((s) => ({ totalCannonsFired: s.totalCannonsFired + 1 })),
      setMaxCascade: (cascade) =>
        set((s) => ({
          maxCascade: Math.max(s.maxCascade, cascade),
        })),
      incrementWinStreak: () =>
        set((s) => {
          const next = s.consecutiveWins + 1;
          return {
            consecutiveWins: next,
            bestStreak: Math.max(s.bestStreak, next),
          };
        }),
      resetWinStreak: () => set({ consecutiveWins: 0 }),
      addThreeStarLevel: () =>
        set((s) => ({ threeStarLevels: s.threeStarLevels + 1 })),
    }),
    {
      name: 'popblast-stats',
      storage: createJSONStorage(() => AsyncStorage),
    }
  )
);
