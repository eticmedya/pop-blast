import { Grid, Tile, nextTileId } from './grid';
import { GRID_COLS, GRID_ROWS } from '../constants/dimensions';
import { TILE_COLORS } from '../constants/colors';
import { getMatchedPositions, findAllMatches, Match } from './matcher';

export interface FallMove {
  tileId: string;
  fromRow: number;
  toRow: number;
  col: number;
}

// Match olan tile'ları kaldır (null yap)
export function removeMatches(grid: Grid, matches: Match[]): Grid {
  const newGrid = grid.map((row) => [...row]);
  const positions = getMatchedPositions(matches);

  for (const pos of positions) {
    const [r, c] = pos.split(',').map(Number);
    newGrid[r][c] = null;
  }
  return newGrid;
}

// Yer çekimi uygula: boş hücrelerin üstündeki tile'lar düşer
// Düşme hareketlerini döndürür (animasyon için)
export function applyGravity(grid: Grid): { grid: Grid; moves: FallMove[] } {
  const newGrid = grid.map((row) => [...row]);
  const moves: FallMove[] = [];

  for (let c = 0; c < GRID_COLS; c++) {
    // Alttan yukarı tara, boş yerleri doldur
    let writePos = GRID_ROWS - 1;

    for (let r = GRID_ROWS - 1; r >= 0; r--) {
      if (newGrid[r][c] !== null) {
        if (r !== writePos) {
          // Tile düşecek
          const tile = newGrid[r][c]!;
          moves.push({
            tileId: tile.id,
            fromRow: r,
            toRow: writePos,
            col: c,
          });
          newGrid[writePos][c] = { ...tile, row: writePos };
          newGrid[r][c] = null;
        }
        writePos--;
      }
    }
  }

  return { grid: newGrid, moves };
}

// Boş hücreleri yeni rastgele tile'larla doldur
export function fillEmptyCells(grid: Grid): { grid: Grid; newTiles: Tile[] } {
  const newGrid = grid.map((row) => [...row]);
  const newTiles: Tile[] = [];

  for (let c = 0; c < GRID_COLS; c++) {
    for (let r = 0; r < GRID_ROWS; r++) {
      if (newGrid[r][c] === null) {
        const tile: Tile = {
          color: Math.floor(Math.random() * TILE_COLORS.length),
          row: r,
          col: c,
          id: nextTileId(),
        };
        newGrid[r][c] = tile;
        newTiles.push(tile);
      }
    }
  }

  return { grid: newGrid, newTiles };
}

// Tam bir tur: match kaldır -> gravity -> fill -> tekrar match varsa devam
export function processBoard(grid: Grid, matches: Match[]): {
  finalGrid: Grid;
  totalScore: number;
  cascadeCount: number;
  allMoves: FallMove[][];
  allNewTiles: Tile[][];
  allMatches: Match[][];
} {
  let currentGrid = removeMatches(grid, matches);
  let totalScore = 0;
  let cascadeCount = 0;
  const allMoves: FallMove[][] = [];
  const allNewTiles: Tile[][] = [];
  const allMatches: Match[][] = [matches];

  // İlk match skoru
  for (const match of matches) {
    if (match.length === 3) totalScore += 30;
    else if (match.length === 4) totalScore += 60;
    else if (match.length >= 5) totalScore += 150;
  }

  // Cascade döngüsü
  let processing = true;
  while (processing) {
    // Gravity
    const gravityResult = applyGravity(currentGrid);
    currentGrid = gravityResult.grid;
    allMoves.push(gravityResult.moves);

    // Fill
    const fillResult = fillEmptyCells(currentGrid);
    currentGrid = fillResult.grid;
    allNewTiles.push(fillResult.newTiles);

    // Yeni match'ler var mı?
    const newMatches = findAllMatches(currentGrid);
    if (newMatches.length > 0) {
      cascadeCount++;
      allMatches.push(newMatches);

      // Cascade bonus (her cascade %50 daha fazla puan)
      const cascadeMultiplier = 1 + cascadeCount * 0.5;
      for (const match of newMatches) {
        let base = 0;
        if (match.length === 3) base = 30;
        else if (match.length === 4) base = 60;
        else if (match.length >= 5) base = 150;
        totalScore += Math.floor(base * cascadeMultiplier);
      }

      currentGrid = removeMatches(currentGrid, newMatches);
    } else {
      processing = false;
    }
  }

  return {
    finalGrid: currentGrid,
    totalScore,
    cascadeCount,
    allMoves,
    allNewTiles,
    allMatches,
  };
}
