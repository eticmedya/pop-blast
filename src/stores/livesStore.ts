import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import AsyncStorage from '@react-native-async-storage/async-storage';

const MAX_LIVES = 5;
const REGEN_MS = 30 * 60 * 1000; // 30 minutes

interface LivesState {
  lives: number;
  maxLives: number;
  lastRegenTime: number;

  hasLives: () => boolean;
  loseLife: () => void;
  addLife: (count: number) => void;
  checkRegen: () => void;
  getTimeUntilNextLife: () => number;
}

export const useLivesStore = create<LivesState>()(
  persist(
    (set, get) => ({
      lives: MAX_LIVES,
      maxLives: MAX_LIVES,
      lastRegenTime: Date.now(),

      hasLives: () => get().lives > 0,

      loseLife: () => {
        const { lives, lastRegenTime } = get();
        const wasFullBefore = lives >= MAX_LIVES;
        set({
          lives: Math.max(0, lives - 1),
          lastRegenTime: wasFullBefore ? Date.now() : lastRegenTime,
        });
      },

      addLife: (count) =>
        set((s) => ({ lives: Math.min(MAX_LIVES, s.lives + count) })),

      checkRegen: () => {
        const { lives, lastRegenTime } = get();
        if (lives >= MAX_LIVES) return;

        const elapsed = Date.now() - lastRegenTime;
        const livesToAdd = Math.floor(elapsed / REGEN_MS);

        if (livesToAdd > 0) {
          const newLives = Math.min(MAX_LIVES, lives + livesToAdd);
          set({
            lives: newLives,
            lastRegenTime:
              newLives >= MAX_LIVES
                ? Date.now()
                : lastRegenTime + livesToAdd * REGEN_MS,
          });
        }
      },

      getTimeUntilNextLife: () => {
        const { lives, lastRegenTime } = get();
        if (lives >= MAX_LIVES) return 0;
        const elapsed = Date.now() - lastRegenTime;
        return Math.max(0, REGEN_MS - (elapsed % REGEN_MS));
      },
    }),
    {
      name: 'popblast-lives',
      storage: createJSONStorage(() => AsyncStorage),
      partialize: (state) => ({
        lives: state.lives,
        lastRegenTime: state.lastRegenTime,
      }),
    }
  )
);
