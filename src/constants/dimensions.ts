import { Dimensions } from 'react-native';

const { width: SCREEN_WIDTH, height: SCREEN_HEIGHT } = Dimensions.get('window');

export const GRID_COLS = 8;
export const GRID_ROWS = 8;

// Grid ekranın %90 genişliğini kaplar
export const GRID_PADDING = 16;
export const BOARD_WIDTH = SCREEN_WIDTH - GRID_PADDING * 2;
export const TILE_SIZE = Math.floor(BOARD_WIDTH / GRID_COLS);
export const BOARD_HEIGHT = TILE_SIZE * GRID_ROWS;

// Tile içindeki top boyutu (tile'ın %80'i)
export const BALL_RADIUS = Math.floor(TILE_SIZE * 0.38);

// Cannon alanı
export const CANNON_HEIGHT = 80;

// Skor barı
export const SCORE_BAR_HEIGHT = 100;

export { SCREEN_WIDTH, SCREEN_HEIGHT };
