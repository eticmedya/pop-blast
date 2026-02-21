import { Grid, Tile } from './grid';
import { GRID_ROWS, GRID_COLS } from '../constants/dimensions';

let _nextId = 90000;
function nextPowerUpTileId(): string {
  return `pu_${_nextId++}`;
}

function cloneGrid(grid: Grid): Grid {
  return grid.map((row) => row.map((tile) => (tile ? { ...tile } : null)));
}

export function executeRowBomb(
  grid: Grid,
  row: number
): { grid: Grid; destroyed: number } {
  const newGrid = cloneGrid(grid);
  let destroyed = 0;

  for (let c = 0; c < GRID_COLS; c++) {
    if (newGrid[row] && newGrid[row][c] !== null) {
      newGrid[row][c] = null;
      destroyed++;
    }
  }

  return { grid: newGrid, destroyed };
}

export function executeColBomb(
  grid: Grid,
  col: number
): { grid: Grid; destroyed: number } {
  const newGrid = cloneGrid(grid);
  let destroyed = 0;

  for (let r = 0; r < GRID_ROWS; r++) {
    if (newGrid[r] && newGrid[r][col] !== null) {
      newGrid[r][col] = null;
      destroyed++;
    }
  }

  return { grid: newGrid, destroyed };
}

export function executeColorBomb(
  grid: Grid,
  colorIndex: number
): { grid: Grid; destroyed: number } {
  const newGrid = cloneGrid(grid);
  let destroyed = 0;

  for (let r = 0; r < GRID_ROWS; r++) {
    for (let c = 0; c < GRID_COLS; c++) {
      const tile = newGrid[r][c];
      if (tile && tile.color === colorIndex) {
        newGrid[r][c] = null;
        destroyed++;
      }
    }
  }

  return { grid: newGrid, destroyed };
}

export function shuffleGrid(grid: Grid, numColors: number = 6): Grid {
  const newGrid = cloneGrid(grid);
  const tiles: Tile[] = [];

  // Collect all non-null tiles
  for (let r = 0; r < newGrid.length; r++) {
    for (let c = 0; c < (newGrid[r]?.length ?? 0); c++) {
      if (newGrid[r][c]) {
        tiles.push(newGrid[r][c]!);
      }
    }
  }

  // Shuffle colors
  for (let i = tiles.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    const tmpColor = tiles[i].color;
    tiles[i].color = tiles[j].color;
    tiles[j].color = tmpColor;
  }

  // Put back
  let idx = 0;
  for (let r = 0; r < newGrid.length; r++) {
    for (let c = 0; c < (newGrid[r]?.length ?? 0); c++) {
      if (newGrid[r][c]) {
        newGrid[r][c] = {
          ...tiles[idx],
          row: r,
          col: c,
          id: nextPowerUpTileId(),
        };
        idx++;
      }
    }
  }

  return newGrid;
}
