export interface LevelConfig {
  level: number;
  targetScore: number;
  maxMoves: number;
  numColors: number; // Kaç farklı renk kullanılacak (3-6)
  gridRows: number;
  gridCols: number;
  starThresholds: [number, number, number]; // 1, 2, 3 yıldız için skor eşikleri
}

// Seviye tanımları
export const LEVELS: LevelConfig[] = [
  // Dünya 1: Başlangıç (Seviye 1-5)
  { level: 1,  targetScore: 200,  maxMoves: 20, numColors: 4, gridRows: 8, gridCols: 8, starThresholds: [200, 400, 700] },
  { level: 2,  targetScore: 350,  maxMoves: 18, numColors: 4, gridRows: 8, gridCols: 8, starThresholds: [350, 600, 1000] },
  { level: 3,  targetScore: 500,  maxMoves: 18, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [500, 800, 1200] },
  { level: 4,  targetScore: 700,  maxMoves: 16, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [700, 1100, 1600] },
  { level: 5,  targetScore: 1000, maxMoves: 15, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [1000, 1500, 2200] },

  // Dünya 2: Orta (Seviye 6-10)
  { level: 6,  targetScore: 1200, maxMoves: 18, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [1200, 1800, 2500] },
  { level: 7,  targetScore: 1500, maxMoves: 16, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [1500, 2200, 3000] },
  { level: 8,  targetScore: 1800, maxMoves: 15, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [1800, 2600, 3500] },
  { level: 9,  targetScore: 2200, maxMoves: 14, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [2200, 3000, 4000] },
  { level: 10, targetScore: 2800, maxMoves: 14, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [2800, 3800, 5000] },

  // Dünya 3: Zor (Seviye 11-15)
  { level: 11, targetScore: 3000,  maxMoves: 15, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [3000, 4200, 5500] },
  { level: 12, targetScore: 3500,  maxMoves: 14, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [3500, 4800, 6200] },
  { level: 13, targetScore: 4000,  maxMoves: 13, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [4000, 5500, 7000] },
  { level: 14, targetScore: 4500,  maxMoves: 12, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [4500, 6200, 8000] },
  { level: 15, targetScore: 5000,  maxMoves: 12, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [5000, 7000, 9000] },

  // Dünya 4: Uzman (Seviye 16-20)
  { level: 16, targetScore: 5500,  maxMoves: 13, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [5500, 7500, 10000] },
  { level: 17, targetScore: 6000,  maxMoves: 12, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [6000, 8500, 11000] },
  { level: 18, targetScore: 7000,  maxMoves: 12, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [7000, 9500, 12500] },
  { level: 19, targetScore: 8000,  maxMoves: 11, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [8000, 11000, 14000] },
  { level: 20, targetScore: 10000, maxMoves: 10, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [10000, 14000, 18000] },
];

export function getLevelConfig(level: number): LevelConfig | undefined {
  return LEVELS.find((l) => l.level === level);
}

export function getStars(score: number, thresholds: [number, number, number]): number {
  if (score >= thresholds[2]) return 3;
  if (score >= thresholds[1]) return 2;
  if (score >= thresholds[0]) return 1;
  return 0;
}
