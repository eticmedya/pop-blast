import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import AsyncStorage from '@react-native-async-storage/async-storage';
import { Grid, createGrid, swapTiles, areAdjacent } from '../game-engine/grid';
import { findAllMatches, wouldSwapCreateMatch, hasValidMoves } from '../game-engine/matcher';
import { processBoard } from '../game-engine/gravity';
import { getLevelConfig, getStars, LevelConfig } from '../game-engine/levels';
import { usePowerUpStore, PowerUpType } from './powerupStore';

export type GamePhase =
  | 'idle'
  | 'swapping'
  | 'matching'
  | 'falling'
  | 'cannon'
  | 'levelComplete'
  | 'gameOver';

interface SelectedTile {
  row: number;
  col: number;
}

interface HighScoreEntry {
  score: number;
  stars: number;
}

interface GameState {
  // Grid
  grid: Grid;
  phase: GamePhase;

  // Level
  currentLevel: number;
  levelConfig: LevelConfig | null;

  // Score
  score: number;
  movesLeft: number;
  bonusMoves: number;
  comboMeter: number;
  stars: number;
  lastMatchCount: number;
  lastCascadeCount: number;

  // Selection
  selectedTile: SelectedTile | null;

  // Progress (persisted)
  unlockedLevel: number;
  highScores: Record<number, HighScoreEntry>;

  // Streak
  consecutiveWins: number;
  streakMultiplier: number;

  // Actions
  startLevel: (level: number) => void;
  selectTile: (row: number, col: number) => void;
  executeSwap: (r1: number, c1: number, r2: number, c2: number) => void;
  completeMatchPhase: () => void;
  setPhase: (phase: GamePhase) => void;
  setGrid: (grid: Grid) => void;
  addScore: (points: number) => void;
  addCombo: (amount: number) => void;
  resetCombo: () => void;
  unlockNextLevel: () => void;
  addBonusMoves: (count: number) => void;
  incrementStreak: () => void;
  resetStreak: () => void;
  saveHighScore: () => void;
  getHighScore: (level: number) => HighScoreEntry | null;
}

function getStreakMultiplier(wins: number): number {
  if (wins >= 8) return 5;
  if (wins >= 5) return 3;
  if (wins >= 3) return 2;
  return 1;
}

export const useGameStore = create<GameState>()(
  persist(
    (set, get) => ({
      grid: [],
      phase: 'idle',
      currentLevel: 1,
      levelConfig: null,
      score: 0,
      movesLeft: 0,
      bonusMoves: 0,
      comboMeter: 0,
      stars: 0,
      lastMatchCount: 0,
      lastCascadeCount: 0,
      selectedTile: null,
      unlockedLevel: 1,
      highScores: {},
      consecutiveWins: 0,
      streakMultiplier: 1,

      startLevel: (level: number) => {
        const config = getLevelConfig(level);
        if (!config) return;

        const { bonusMoves } = get();
        const grid = createGrid(config.gridRows, config.gridCols);

        set({
          grid,
          phase: 'idle',
          currentLevel: level,
          levelConfig: config,
          score: 0,
          movesLeft: config.maxMoves + bonusMoves,
          bonusMoves: 0,
          comboMeter: 0,
          stars: 0,
          lastMatchCount: 0,
          lastCascadeCount: 0,
          selectedTile: null,
        });
      },

      selectTile: (row: number, col: number) => {
        const { phase, selectedTile, grid } = get();
        if (phase !== 'idle') return;

        if (!selectedTile) {
          set({ selectedTile: { row, col } });
          return;
        }

        if (selectedTile.row === row && selectedTile.col === col) {
          set({ selectedTile: null });
          return;
        }

        if (areAdjacent(selectedTile.row, selectedTile.col, row, col)) {
          if (wouldSwapCreateMatch(grid, selectedTile.row, selectedTile.col, row, col)) {
            get().executeSwap(selectedTile.row, selectedTile.col, row, col);
          } else {
            set({ selectedTile: null });
          }
        } else {
          set({ selectedTile: { row, col } });
        }
      },

      executeSwap: (r1: number, c1: number, r2: number, c2: number) => {
        const { grid, movesLeft } = get();
        const newGrid = swapTiles(grid, r1, c1, r2, c2);

        set({
          grid: newGrid,
          phase: 'swapping',
          selectedTile: null,
          movesLeft: movesLeft - 1,
        });
      },

      completeMatchPhase: () => {
        const { grid, score, comboMeter, movesLeft, levelConfig, streakMultiplier } = get();

        const matches = findAllMatches(grid);
        if (matches.length === 0) {
          if (levelConfig && score >= levelConfig.targetScore) {
            const stars = getStars(score, levelConfig.starThresholds);
            set({ phase: 'levelComplete', stars });
            return;
          }
          if (movesLeft <= 0 && levelConfig) {
            set({ phase: 'gameOver' });
            return;
          }
          if (!hasValidMoves(grid)) {
            const newGrid = createGrid();
            set({ grid: newGrid, phase: 'idle' });
          } else {
            set({ phase: 'idle' });
          }
          return;
        }

        const result = processBoard(grid, matches);

        // Power-up düşürme: en uzun eşleşmeye göre
        const maxMatchLen = Math.max(...matches.map((m) => m.length));
        const dropChance = maxMatchLen >= 5 ? 0.6 : maxMatchLen >= 4 ? 0.3 : 0;
        if (dropChance > 0 && Math.random() < dropChance) {
          const types: PowerUpType[] = ['rowBomb', 'colBomb', 'colorBomb', 'shuffle'];
          const randomType = types[Math.floor(Math.random() * types.length)];
          usePowerUpStore.getState().addPowerUp(randomType, 1);
        }

        const comboGain = matches.length * 15 + result.cascadeCount * 25;
        const newCombo = Math.min(100, comboMeter + comboGain);

        // Apply streak multiplier to score
        const baseScore = result.totalScore;
        const multipliedScore = Math.floor(baseScore * streakMultiplier);
        const newScore = score + multipliedScore;

        if (levelConfig && newScore >= levelConfig.targetScore) {
          const stars = getStars(newScore, levelConfig.starThresholds);
          set({
            grid: result.finalGrid,
            score: newScore,
            comboMeter: newCombo,
            phase: 'levelComplete',
            stars,
            lastMatchCount: matches.length,
            lastCascadeCount: result.cascadeCount,
          });
          return;
        }

        set({
          grid: result.finalGrid,
          score: newScore,
          comboMeter: newCombo,
          phase: 'matching',
          lastMatchCount: matches.length,
          lastCascadeCount: result.cascadeCount,
        });
      },

      setPhase: (phase) => set({ phase }),
      setGrid: (grid) => set({ grid }),
      addScore: (points) => set((s) => ({ score: s.score + points })),
      addCombo: (amount) => set((s) => ({ comboMeter: Math.min(100, s.comboMeter + amount) })),
      resetCombo: () => set({ comboMeter: 0 }),

      unlockNextLevel: () =>
        set((s) => ({
          unlockedLevel: Math.max(s.unlockedLevel, s.currentLevel + 1),
        })),

      addBonusMoves: (count) =>
        set((s) => ({ bonusMoves: s.bonusMoves + count })),

      incrementStreak: () =>
        set((s) => {
          const next = s.consecutiveWins + 1;
          return {
            consecutiveWins: next,
            streakMultiplier: getStreakMultiplier(next),
          };
        }),

      resetStreak: () =>
        set({ consecutiveWins: 0, streakMultiplier: 1 }),

      saveHighScore: () => {
        const { currentLevel, score, stars, highScores } = get();
        const existing = highScores[currentLevel];
        if (!existing || score > existing.score) {
          set({
            highScores: {
              ...highScores,
              [currentLevel]: { score, stars: Math.max(stars, existing?.stars ?? 0) },
            },
          });
        }
      },

      getHighScore: (level: number) => {
        return get().highScores[level] ?? null;
      },
    }),
    {
      name: 'popblast-game',
      storage: createJSONStorage(() => AsyncStorage),
      partialize: (state) => ({
        unlockedLevel: state.unlockedLevel,
        highScores: state.highScores,
        consecutiveWins: state.consecutiveWins,
        streakMultiplier: state.streakMultiplier,
      }),
    }
  )
);

// Debug
if (typeof window !== 'undefined') {
  (window as unknown as Record<string, unknown>).__gameStore = useGameStore;
}
