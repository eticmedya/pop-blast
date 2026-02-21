import { Dimensions } from 'react-native';

const { width: SCREEN_WIDTH, height: SCREEN_HEIGHT } = Dimensions.get('window');

export const GRID_COLS = 8;
export const GRID_ROWS = 8;

// Skor barı + cannon + padding için ayrılan alan
export const SCORE_BAR_HEIGHT = 110;
export const CANNON_HEIGHT = 80;
const VERTICAL_RESERVED = SCORE_BAR_HEIGHT + CANNON_HEIGHT + 60; // üst + alt boşluk

export const GRID_PADDING = 12;

// Genişlik ve yüksekliğe göre en uygun tile boyutunu hesapla
const maxWidthBased = Math.floor((SCREEN_WIDTH - GRID_PADDING * 2) / GRID_COLS);
const maxHeightBased = Math.floor((SCREEN_HEIGHT - VERTICAL_RESERVED) / GRID_ROWS);
export const TILE_SIZE = Math.min(maxWidthBased, maxHeightBased, 56); // max 56px

export const BOARD_WIDTH = TILE_SIZE * GRID_COLS;
export const BOARD_HEIGHT = TILE_SIZE * GRID_ROWS;

// Tile içindeki top boyutu (tile'ın %80'i)
export const BALL_RADIUS = Math.floor(TILE_SIZE * 0.38);

export { SCREEN_WIDTH, SCREEN_HEIGHT };
