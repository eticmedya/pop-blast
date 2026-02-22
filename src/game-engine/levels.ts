export interface LevelConfig {
  level: number;
  targetScore: number;
  maxMoves: number;
  numColors: number; // Kaç farklı renk kullanılacak (3-6)
  gridRows: number;
  gridCols: number;
  starThresholds: [number, number, number]; // 1, 2, 3 yıldız için skor eşikleri
}

// Seviye tanımları — 50 seviye, 10 dünya (her dünyada 5 seviye)
// Testere dişi zorluk eğrisi: Dünya 4 sonrası zorluk düşer, ardından tekrar tırmanır
export const LEVELS: LevelConfig[] = [
  // Dünya 1: Garden / Başlangıç Bahçesi (Seviye 1-5) — 4 renk, 18-20 hamle, hedef 200-1000
  { level: 1,  targetScore: 200,   maxMoves: 20, numColors: 4, gridRows: 8, gridCols: 8, starThresholds: [200, 300, 440] },
  { level: 2,  targetScore: 350,   maxMoves: 19, numColors: 4, gridRows: 8, gridCols: 8, starThresholds: [350, 525, 770] },
  { level: 3,  targetScore: 500,   maxMoves: 19, numColors: 4, gridRows: 8, gridCols: 8, starThresholds: [500, 750, 1100] },
  { level: 4,  targetScore: 700,   maxMoves: 18, numColors: 4, gridRows: 8, gridCols: 8, starThresholds: [700, 1050, 1540] },
  { level: 5,  targetScore: 1000,  maxMoves: 18, numColors: 4, gridRows: 8, gridCols: 8, starThresholds: [1000, 1500, 2200] },

  // Dünya 2: Ocean / Okyanus Derinlikleri (Seviye 6-10) — 5 renk, 15-18 hamle, hedef 1200-2800
  { level: 6,  targetScore: 1200,  maxMoves: 18, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [1200, 1800, 2640] },
  { level: 7,  targetScore: 1500,  maxMoves: 17, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [1500, 2250, 3300] },
  { level: 8,  targetScore: 1800,  maxMoves: 16, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [1800, 2700, 3960] },
  { level: 9,  targetScore: 2200,  maxMoves: 15, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [2200, 3300, 4840] },
  { level: 10, targetScore: 2800,  maxMoves: 15, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [2800, 4200, 6160] },

  // Dünya 3: Volcanic / Volkanik Zirveler (Seviye 11-15) — 6 renk, 12-15 hamle, hedef 3000-5000
  { level: 11, targetScore: 3000,  maxMoves: 15, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [3000, 4500, 6600] },
  { level: 12, targetScore: 3500,  maxMoves: 14, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [3500, 5250, 7700] },
  { level: 13, targetScore: 4000,  maxMoves: 13, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [4000, 6000, 8800] },
  { level: 14, targetScore: 4500,  maxMoves: 12, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [4500, 6750, 9900] },
  { level: 15, targetScore: 5000,  maxMoves: 12, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [5000, 7500, 11000] },

  // Dünya 4: Nebula / Yıldız Bulutsusu (Seviye 16-20) — 6 renk, 11-13 hamle, hedef 5500-10000
  { level: 16, targetScore: 5500,  maxMoves: 13, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [5500, 8250, 12100] },
  { level: 17, targetScore: 6500,  maxMoves: 12, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [6500, 9750, 14300] },
  { level: 18, targetScore: 7500,  maxMoves: 12, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [7500, 11250, 16500] },
  { level: 19, targetScore: 8500,  maxMoves: 11, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [8500, 12750, 18700] },
  { level: 20, targetScore: 10000, maxMoves: 11, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [10000, 15000, 22000] },

  // ── SAWTOOTH RESET ── Zorluk düşüşü
  // Dünya 5: Crystal Cave / Kristal Mağara (Seviye 21-25) — 5 renk, 16-19 hamle, hedef 3000-6000
  { level: 21, targetScore: 3000,  maxMoves: 19, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [3000, 4500, 6600] },
  { level: 22, targetScore: 3700,  maxMoves: 18, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [3700, 5550, 8140] },
  { level: 23, targetScore: 4400,  maxMoves: 17, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [4400, 6600, 9680] },
  { level: 24, targetScore: 5200,  maxMoves: 16, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [5200, 7800, 11440] },
  { level: 25, targetScore: 6000,  maxMoves: 16, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [6000, 9000, 13200] },

  // Dünya 6: Sunset Valley / Gün Batımı Vadisi (Seviye 26-30) — 5 renk, 14-17 hamle, hedef 4000-8000
  { level: 26, targetScore: 4000,  maxMoves: 17, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [4000, 6000, 8800] },
  { level: 27, targetScore: 5000,  maxMoves: 16, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [5000, 7500, 11000] },
  { level: 28, targetScore: 6000,  maxMoves: 15, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [6000, 9000, 13200] },
  { level: 29, targetScore: 7000,  maxMoves: 15, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [7000, 10500, 15400] },
  { level: 30, targetScore: 8000,  maxMoves: 14, numColors: 5, gridRows: 8, gridCols: 8, starThresholds: [8000, 12000, 17600] },

  // Dünya 7: Deep Space / Derin Uzay (Seviye 31-35) — 6 renk, 13-16 hamle, hedef 5000-10000
  { level: 31, targetScore: 5000,  maxMoves: 16, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [5000, 7500, 11000] },
  { level: 32, targetScore: 6200,  maxMoves: 15, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [6200, 9300, 13640] },
  { level: 33, targetScore: 7500,  maxMoves: 14, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [7500, 11250, 16500] },
  { level: 34, targetScore: 8800,  maxMoves: 14, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [8800, 13200, 19360] },
  { level: 35, targetScore: 10000, maxMoves: 13, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [10000, 15000, 22000] },

  // ── SAWTOOTH RESET ── Hafif zorluk düşüşü
  // Dünya 8: Snow Kingdom / Kar Krallığı (Seviye 36-40) — 6 renk, 12-15 hamle, hedef 6000-12000
  { level: 36, targetScore: 6000,  maxMoves: 15, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [6000, 9000, 13200] },
  { level: 37, targetScore: 7500,  maxMoves: 14, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [7500, 11250, 16500] },
  { level: 38, targetScore: 9000,  maxMoves: 13, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [9000, 13500, 19800] },
  { level: 39, targetScore: 10500, maxMoves: 13, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [10500, 15750, 23100] },
  { level: 40, targetScore: 12000, maxMoves: 12, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [12000, 18000, 26400] },

  // Dünya 9: Dragon Island / Ejderha Adası (Seviye 41-45) — 6 renk, 11-14 hamle, hedef 7000-14000
  { level: 41, targetScore: 7000,  maxMoves: 14, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [7000, 10500, 15400] },
  { level: 42, targetScore: 8800,  maxMoves: 13, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [8800, 13200, 19360] },
  { level: 43, targetScore: 10500, maxMoves: 12, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [10500, 15750, 23100] },
  { level: 44, targetScore: 12500, maxMoves: 12, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [12500, 18750, 27500] },
  { level: 45, targetScore: 14000, maxMoves: 11, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [14000, 21000, 30800] },

  // Dünya 10: Enchanted Forest / Büyülü Orman (Seviye 46-50) — 6 renk, 10-13 hamle, hedef 8000-18000
  { level: 46, targetScore: 8000,  maxMoves: 13, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [8000, 12000, 17600] },
  { level: 47, targetScore: 10000, maxMoves: 12, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [10000, 15000, 22000] },
  { level: 48, targetScore: 13000, maxMoves: 11, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [13000, 19500, 28600] },
  { level: 49, targetScore: 15500, maxMoves: 11, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [15500, 23250, 34100] },
  { level: 50, targetScore: 18000, maxMoves: 10, numColors: 6, gridRows: 8, gridCols: 8, starThresholds: [18000, 27000, 39600] },
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
