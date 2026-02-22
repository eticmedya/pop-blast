import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import AsyncStorage from '@react-native-async-storage/async-storage';

export type PowerUpType = 'rowBomb' | 'colBomb' | 'colorBomb' | 'shuffle';

export interface PowerUpInventory {
  rowBomb: number;
  colBomb: number;
  colorBomb: number;
  shuffle: number;
}

interface PowerUpState {
  inventory: PowerUpInventory;
  activePowerUp: PowerUpType | null;

  usePowerUp: (type: PowerUpType) => boolean;
  addPowerUp: (type: PowerUpType, count: number) => void;
  setActivePowerUp: (type: PowerUpType | null) => void;
  hasAny: (type: PowerUpType) => boolean;
}

export const usePowerUpStore = create<PowerUpState>()(
  persist(
    (set, get) => ({
      inventory: { rowBomb: 2, colBomb: 2, colorBomb: 1, shuffle: 1 },
      activePowerUp: null,

      usePowerUp: (type) => {
        const { inventory } = get();
        if (inventory[type] <= 0) return false;
        set({
          inventory: { ...inventory, [type]: inventory[type] - 1 },
          activePowerUp: null,
        });
        return true;
      },

      addPowerUp: (type, count) =>
        set((s) => ({
          inventory: { ...s.inventory, [type]: s.inventory[type] + count },
        })),

      setActivePowerUp: (type) => set({ activePowerUp: type }),

      hasAny: (type) => get().inventory[type] > 0,
    }),
    {
      name: 'popblast-powerups',
      storage: createJSONStorage(() => AsyncStorage),
      partialize: (state) => ({ inventory: state.inventory }),
    }
  )
);
