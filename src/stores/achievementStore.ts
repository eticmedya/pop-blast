import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { useStatsStore } from './statsStore';

export interface Achievement {
  id: string;
  titleKey: string;
  descriptionKey: string;
  icon: string;
  threshold: number;
  statKey: keyof ReturnType<typeof useStatsStore.getState>;
  unlocked: boolean;
}

const ACHIEVEMENT_DEFS: Omit<Achievement, 'unlocked'>[] = [
  { id: 'firstMatch', titleKey: 'achievements.firstMatch', descriptionKey: 'achievements.firstMatchDesc', icon: '✨', threshold: 1, statKey: 'totalMatches' },
  { id: 'matchMaster', titleKey: 'achievements.matchMaster', descriptionKey: 'achievements.matchMasterDesc', icon: '🎯', threshold: 100, statKey: 'totalMatches' },
  { id: 'matchLegend', titleKey: 'achievements.matchLegend', descriptionKey: 'achievements.matchLegendDesc', icon: '👑', threshold: 1000, statKey: 'totalMatches' },
  { id: 'levelUp', titleKey: 'achievements.levelUp', descriptionKey: 'achievements.levelUpDesc', icon: '⭐', threshold: 5, statKey: 'totalLevelsCompleted' },
  { id: 'halfway', titleKey: 'achievements.halfway', descriptionKey: 'achievements.halfwayDesc', icon: '🏆', threshold: 10, statKey: 'totalLevelsCompleted' },
  { id: 'champion', titleKey: 'achievements.champion', descriptionKey: 'achievements.championDesc', icon: '💎', threshold: 20, statKey: 'totalLevelsCompleted' },
  { id: 'cascadeKing', titleKey: 'achievements.cascadeKing', descriptionKey: 'achievements.cascadeKingDesc', icon: '🌊', threshold: 3, statKey: 'maxCascade' },
  { id: 'cascadeLegend', titleKey: 'achievements.cascadeLegend', descriptionKey: 'achievements.cascadeLegendDesc', icon: '🌀', threshold: 5, statKey: 'maxCascade' },
  { id: 'scorer', titleKey: 'achievements.scorer', descriptionKey: 'achievements.scorerDesc', icon: '💰', threshold: 5000, statKey: 'totalScore' },
  { id: 'megaScorer', titleKey: 'achievements.megaScorer', descriptionKey: 'achievements.megaScorerDesc', icon: '🤑', threshold: 50000, statKey: 'totalScore' },
  { id: 'streakHot', titleKey: 'achievements.streakHot', descriptionKey: 'achievements.streakHotDesc', icon: '🔥', threshold: 3, statKey: 'bestStreak' },
  { id: 'streakBlazing', titleKey: 'achievements.streakBlazing', descriptionKey: 'achievements.streakBlazingDesc', icon: '☄️', threshold: 10, statKey: 'bestStreak' },
  { id: 'powerUser', titleKey: 'achievements.powerUser', descriptionKey: 'achievements.powerUserDesc', icon: '💣', threshold: 10, statKey: 'totalPowerUpsUsed' },
  { id: 'cannoneer', titleKey: 'achievements.cannoneer', descriptionKey: 'achievements.cannoneerDesc', icon: '🎆', threshold: 5, statKey: 'totalCannonsFired' },
  { id: 'collector', titleKey: 'achievements.collector', descriptionKey: 'achievements.collectorDesc', icon: '🌟', threshold: 10, statKey: 'threeStarLevels' },
];

interface AchievementState {
  achievements: Achievement[];
  pendingPopup: Achievement | null;

  checkAchievements: () => void;
  dismissPopup: () => void;
}

export const useAchievementStore = create<AchievementState>()(
  persist(
    (set, get) => ({
      achievements: ACHIEVEMENT_DEFS.map((a) => ({ ...a, unlocked: false })),
      pendingPopup: null,

      checkAchievements: () => {
        const stats = useStatsStore.getState();
        const { achievements } = get();
        let newlyUnlocked: Achievement | null = null;

        const updated = achievements.map((a) => {
          if (a.unlocked) return a;
          const statValue = stats[a.statKey];
          if (typeof statValue === 'number' && statValue >= a.threshold) {
            if (!newlyUnlocked) {
              newlyUnlocked = { ...a, unlocked: true };
            }
            return { ...a, unlocked: true };
          }
          return a;
        });

        if (newlyUnlocked) {
          set({ achievements: updated, pendingPopup: newlyUnlocked });
        }
      },

      dismissPopup: () => set({ pendingPopup: null }),
    }),
    {
      name: 'popblast-achievements',
      storage: createJSONStorage(() => AsyncStorage),
      partialize: (state) => ({ achievements: state.achievements }),
    }
  )
);
