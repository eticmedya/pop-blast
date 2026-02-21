import { GRID_COLS, GRID_ROWS } from '../constants/dimensions';
import { TILE_COLORS } from '../constants/colors';

export interface Tile {
  color: number; // index into TILE_COLORS
  row: number;
  col: number;
  id: string;
}

export type Grid = (Tile | null)[][];

// Benzersiz tile ID üret
let tileIdCounter = 0;
export function nextTileId(): string {
  return `tile_${++tileIdCounter}`;
}

export function resetTileIdCounter(): void {
  tileIdCounter = 0;
}

// Rastgele renk index döndür
function randomColor(numColors: number = TILE_COLORS.length): number {
  return Math.floor(Math.random() * numColors);
}

// Başlangıçta match olmayan grid oluştur
export function createGrid(rows: number = GRID_ROWS, cols: number = GRID_COLS): Grid {
  const grid: Grid = [];

  for (let r = 0; r < rows; r++) {
    grid[r] = [];
    for (let c = 0; c < cols; c++) {
      let color: number;
      do {
        color = randomColor();
      } while (wouldCreateMatch(grid, r, c, color));

      grid[r][c] = {
        color,
        row: r,
        col: c,
        id: nextTileId(),
      };
    }
  }
  return grid;
}

// Bu pozisyona bu renk koyarsak match oluşur mu?
function wouldCreateMatch(grid: Grid, row: number, col: number, color: number): boolean {
  // Yatay kontrol: sola 2 tane aynı renk var mı?
  if (
    col >= 2 &&
    grid[row][col - 1]?.color === color &&
    grid[row][col - 2]?.color === color
  ) {
    return true;
  }

  // Dikey kontrol: yukarı 2 tane aynı renk var mı?
  if (
    row >= 2 &&
    grid[row - 1]?.[col]?.color === color &&
    grid[row - 2]?.[col]?.color === color
  ) {
    return true;
  }

  return false;
}

// İki tile'ın pozisyonunu swap et
export function swapTiles(
  grid: Grid,
  r1: number,
  c1: number,
  r2: number,
  c2: number
): Grid {
  const newGrid = grid.map((row) => [...row]);
  const temp = newGrid[r1][c1];
  newGrid[r1][c1] = newGrid[r2][c2];
  newGrid[r2][c2] = temp;

  // Pozisyonları güncelle
  if (newGrid[r1][c1]) {
    newGrid[r1][c1] = { ...newGrid[r1][c1]!, row: r1, col: c1 };
  }
  if (newGrid[r2][c2]) {
    newGrid[r2][c2] = { ...newGrid[r2][c2]!, row: r2, col: c2 };
  }

  return newGrid;
}

// İki hücre komşu mu?
export function areAdjacent(r1: number, c1: number, r2: number, c2: number): boolean {
  const dr = Math.abs(r1 - r2);
  const dc = Math.abs(c1 - c2);
  return (dr === 1 && dc === 0) || (dr === 0 && dc === 1);
}

// Grid'in deep copy'si
export function cloneGrid(grid: Grid): Grid {
  return grid.map((row) =>
    row.map((tile) => (tile ? { ...tile } : null))
  );
}
