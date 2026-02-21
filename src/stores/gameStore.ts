import { create } from 'zustand';
import { Grid, createGrid, swapTiles, areAdjacent, Tile } from '../game-engine/grid';
import { findAllMatches, wouldSwapCreateMatch, hasValidMoves, Match } from '../game-engine/matcher';
import { processBoard } from '../game-engine/gravity';
import { getLevelConfig, getStars, LevelConfig } from '../game-engine/levels';

export type GamePhase =
  | 'idle'           // Oyuncu hamle yapabilir
  | 'swapping'       // Swap animasyonu
  | 'matching'       // Patlama animasyonu
  | 'falling'        // Düşme animasyonu
  | 'cannon'         // Cannon modu aktif
  | 'levelComplete'  // Seviye bitti
  | 'gameOver';      // Hamle bitti, hedef tutmadı

interface SelectedTile {
  row: number;
  col: number;
}

interface GameState {
  // Grid
  grid: Grid;
  phase: GamePhase;

  // Seviye
  currentLevel: number;
  levelConfig: LevelConfig | null;

  // Skor
  score: number;
  movesLeft: number;
  comboMeter: number; // 0-100, 100 olunca cannon aktif
  stars: number;

  // Seçim
  selectedTile: SelectedTile | null;

  // İlerleme
  unlockedLevel: number; // En yüksek açılmış seviye

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
}

export const useGameStore = create<GameState>((set, get) => ({
  grid: [],
  phase: 'idle',
  currentLevel: 1,
  levelConfig: null,
  score: 0,
  movesLeft: 0,
  comboMeter: 0,
  stars: 0,
  selectedTile: null,
  unlockedLevel: 1,

  startLevel: (level: number) => {
    const config = getLevelConfig(level);
    if (!config) return;

    const grid = createGrid(config.gridRows, config.gridCols);

    set({
      grid,
      phase: 'idle',
      currentLevel: level,
      levelConfig: config,
      score: 0,
      movesLeft: config.maxMoves,
      comboMeter: 0,
      stars: 0,
      selectedTile: null,
    });
  },

  selectTile: (row: number, col: number) => {
    const { phase, selectedTile, grid } = get();
    if (phase !== 'idle') return;

    if (!selectedTile) {
      // İlk seçim
      set({ selectedTile: { row, col } });
      return;
    }

    // İkinci seçim
    if (selectedTile.row === row && selectedTile.col === col) {
      // Aynı tile'a tıkladı, seçimi kaldır
      set({ selectedTile: null });
      return;
    }

    if (areAdjacent(selectedTile.row, selectedTile.col, row, col)) {
      // Komşu tile - swap dene
      if (wouldSwapCreateMatch(grid, selectedTile.row, selectedTile.col, row, col)) {
        get().executeSwap(selectedTile.row, selectedTile.col, row, col);
      } else {
        // Geçersiz hamle - seçimi sıfırla
        set({ selectedTile: null });
      }
    } else {
      // Komşu değil - yeni seçim
      set({ selectedTile: { row, col } });
    }
  },

  executeSwap: (r1: number, c1: number, r2: number, c2: number) => {
    const { grid, movesLeft } = get();

    // Swap yap
    const newGrid = swapTiles(grid, r1, c1, r2, c2);

    set({
      grid: newGrid,
      phase: 'swapping',
      selectedTile: null,
      movesLeft: movesLeft - 1,
    });
  },

  completeMatchPhase: () => {
    const { grid, score, comboMeter, movesLeft, levelConfig } = get();

    const matches = findAllMatches(grid);
    if (matches.length === 0) {
      // Match yok, idle'a dön
      // Hamle bitti mi kontrol et
      if (movesLeft <= 0 && levelConfig) {
        if (score >= levelConfig.targetScore) {
          const stars = getStars(score, levelConfig.starThresholds);
          set({ phase: 'levelComplete', stars });
        } else {
          set({ phase: 'gameOver' });
        }
      } else {
        // Geçerli hamle var mı kontrol et
        if (!hasValidMoves(grid)) {
          // Grid'i yeniden oluştur
          const newGrid = createGrid();
          set({ grid: newGrid, phase: 'idle' });
        } else {
          set({ phase: 'idle' });
        }
      }
      return;
    }

    // Match'leri işle
    const result = processBoard(grid, matches);

    // Combo metre güncelle
    const comboGain = matches.length * 15 + result.cascadeCount * 25;
    const newCombo = Math.min(100, comboMeter + comboGain);

    const newScore = score + result.totalScore;

    set({
      grid: result.finalGrid,
      score: newScore,
      comboMeter: newCombo,
      phase: 'matching',
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
}));
