import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import AsyncStorage from '@react-native-async-storage/async-storage';

export interface DailyRewardItem {
  day: number;
  type: 'moves' | 'powerup' | 'lives';
  amount: number;
  powerupType?: 'rowBomb' | 'colBomb' | 'colorBomb' | 'shuffle';
}

const REWARD_CYCLE: DailyRewardItem[] = [
  { day: 1, type: 'moves', amount: 3 },
  { day: 2, type: 'powerup', amount: 1, powerupType: 'rowBomb' },
  { day: 3, type: 'moves', amount: 5 },
  { day: 4, type: 'powerup', amount: 1, powerupType: 'colorBomb' },
  { day: 5, type: 'lives', amount: 2 },
  { day: 6, type: 'powerup', amount: 1, powerupType: 'shuffle' },
  { day: 7, type: 'moves', amount: 10 },
];

function getTodayStr(): string {
  return new Date().toISOString().split('T')[0];
}

interface DailyRewardState {
  lastClaimDate: string | null;
  streakDay: number;
  totalDaysClaimed: number;

  canClaim: () => boolean;
  claim: () => DailyRewardItem | null;
  getRewards: () => (DailyRewardItem & { claimed: boolean; current: boolean })[];
  getCurrentReward: () => DailyRewardItem;
}

export const useDailyRewardStore = create<DailyRewardState>()(
  persist(
    (set, get) => ({
      lastClaimDate: null,
      streakDay: 0,
      totalDaysClaimed: 0,

      canClaim: () => {
        const { lastClaimDate } = get();
        if (!lastClaimDate) return true;
        return lastClaimDate !== getTodayStr();
      },

      getCurrentReward: () => {
        const { streakDay } = get();
        const nextDay = (streakDay % 7) + 1;
        return REWARD_CYCLE[nextDay - 1];
      },

      claim: () => {
        const { canClaim, streakDay, totalDaysClaimed } = get();
        if (!canClaim()) return null;

        const nextDay = (streakDay % 7) + 1;
        const reward = REWARD_CYCLE[nextDay - 1];

        set({
          lastClaimDate: getTodayStr(),
          streakDay: nextDay,
          totalDaysClaimed: totalDaysClaimed + 1,
        });

        return reward;
      },

      getRewards: () => {
        const { streakDay } = get();
        return REWARD_CYCLE.map((r) => ({
          ...r,
          claimed: r.day <= streakDay,
          current: r.day === (streakDay % 7) + 1,
        }));
      },
    }),
    {
      name: 'popblast-daily',
      storage: createJSONStorage(() => AsyncStorage),
      partialize: (state) => ({
        lastClaimDate: state.lastClaimDate,
        streakDay: state.streakDay,
        totalDaysClaimed: state.totalDaysClaimed,
      }),
    }
  )
);
