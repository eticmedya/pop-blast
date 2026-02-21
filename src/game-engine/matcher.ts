import { Grid, Tile } from './grid';
import { GRID_COLS, GRID_ROWS } from '../constants/dimensions';

export interface Match {
  tiles: { row: number; col: number }[];
  length: number;
}

// Grid'deki tüm match'leri bul (yatay + dikey, 3+)
export function findAllMatches(grid: Grid): Match[] {
  const matches: Match[] = [];
  const matched = new Set<string>();

  // Yatay match'ler
  for (let r = 0; r < GRID_ROWS; r++) {
    let runStart = 0;
    for (let c = 1; c <= GRID_COLS; c++) {
      const current = c < GRID_COLS ? grid[r][c] : null;
      const runTile = grid[r][runStart];

      if (current && runTile && current.color === runTile.color) {
        continue;
      }

      const runLength = c - runStart;
      if (runLength >= 3 && runTile) {
        const tiles: { row: number; col: number }[] = [];
        for (let i = runStart; i < c; i++) {
          tiles.push({ row: r, col: i });
          matched.add(`${r},${i}`);
        }
        matches.push({ tiles, length: runLength });
      }
      runStart = c;
    }
  }

  // Dikey match'ler
  for (let c = 0; c < GRID_COLS; c++) {
    let runStart = 0;
    for (let r = 1; r <= GRID_ROWS; r++) {
      const current = r < GRID_ROWS ? grid[r][c] : null;
      const runTile = grid[runStart][c];

      if (current && runTile && current.color === runTile.color) {
        continue;
      }

      const runLength = r - runStart;
      if (runLength >= 3 && runTile) {
        const tiles: { row: number; col: number }[] = [];
        for (let i = runStart; i < r; i++) {
          // Yatayda zaten eklenmişse tekrar ekleme ama match'e dahil et
          tiles.push({ row: i, col: c });
          matched.add(`${i},${c}`);
        }
        matches.push({ tiles, length: runLength });
      }
      runStart = r;
    }
  }

  return matches;
}

// Match olan tile pozisyonlarını set olarak döndür
export function getMatchedPositions(matches: Match[]): Set<string> {
  const positions = new Set<string>();
  for (const match of matches) {
    for (const tile of match.tiles) {
      positions.add(`${tile.row},${tile.col}`);
    }
  }
  return positions;
}

// Bir swap hamlesinin en az bir match oluşturup oluşturmadığını kontrol et
export function wouldSwapCreateMatch(
  grid: Grid,
  r1: number,
  c1: number,
  r2: number,
  c2: number
): boolean {
  // Geçici swap
  const tempGrid = grid.map((row) => [...row]);
  const temp = tempGrid[r1][c1];
  tempGrid[r1][c1] = tempGrid[r2][c2];
  tempGrid[r2][c2] = temp;

  const matches = findAllMatches(tempGrid);
  return matches.length > 0;
}

// Grid'de geçerli hamle var mı?
export function hasValidMoves(grid: Grid): boolean {
  for (let r = 0; r < GRID_ROWS; r++) {
    for (let c = 0; c < GRID_COLS; c++) {
      // Sağla swap
      if (c < GRID_COLS - 1 && wouldSwapCreateMatch(grid, r, c, r, c + 1)) {
        return true;
      }
      // Altla swap
      if (r < GRID_ROWS - 1 && wouldSwapCreateMatch(grid, r, c, r + 1, c)) {
        return true;
      }
    }
  }
  return false;
}

// Match skorunu hesapla
export function calculateMatchScore(matches: Match[]): number {
  let score = 0;
  for (const match of matches) {
    // 3'lü: 30 puan, 4'lü: 60 puan, 5'li: 150 puan
    if (match.length === 3) score += 30;
    else if (match.length === 4) score += 60;
    else if (match.length >= 5) score += 150;
  }
  return score;
}
