export const TILE_COLORS = [
  '#FF4757', // Red
  '#3742FA', // Blue
  '#2ED573', // Green
  '#FFA502', // Orange
  '#A855F7', // Purple
  '#FBBF24', // Yellow
] as const;

export const TILE_GLOW_COLORS = [
  'rgba(255,71,87,0.4)',
  'rgba(55,66,250,0.4)',
  'rgba(46,213,115,0.4)',
  'rgba(255,165,2,0.4)',
  'rgba(168,85,247,0.4)',
  'rgba(251,191,36,0.4)',
] as const;

export type TileColor = (typeof TILE_COLORS)[number];

// Main UI Colors
export const BG_COLOR = '#0F0F23';
export const GRID_BG_COLOR = '#1A1A2E';
export const ACCENT_COLOR = '#FF6B35';
export const TEXT_COLOR = '#FFFFFF';
export const SCORE_COLOR = '#FFD700';
export const DANGER_COLOR = '#FF4757';
export const SUCCESS_COLOR = '#2ED573';

// Gradient Sets
export const BG_GRADIENT = ['#0F0F23', '#1A1A2E', '#16213E'];
export const MENU_GRADIENT = ['#1A0533', '#0F0F23', '#0A1628'];
export const GAME_GRADIENT = ['#0F0F23', '#141432'];

// World Theme Colors (10 worlds)
export const WORLD_COLORS = [
  { primary: '#2ED573', secondary: '#7BED9F', bg: '#0a2e1a' }, // 1  Garden
  { primary: '#3742FA', secondary: '#70A1FF', bg: '#0a1a3e' }, // 2  Ocean
  { primary: '#FF6B35', secondary: '#FF9F43', bg: '#2e1a0a' }, // 3  Volcanic
  { primary: '#A855F7', secondary: '#D388FF', bg: '#1a0a2e' }, // 4  Nebula
  { primary: '#00D2D3', secondary: '#48DBFB', bg: '#0a2e2e' }, // 5  Crystal Cave
  { primary: '#FC427B', secondary: '#FD7272', bg: '#2e0a1a' }, // 6  Sunset Valley
  { primary: '#3D3D6B', secondary: '#706FD3', bg: '#14142e' }, // 7  Deep Space
  { primary: '#74B9FF', secondary: '#A3D8F4', bg: '#0a1e2e' }, // 8  Snow Kingdom
  { primary: '#E74C3C', secondary: '#FF6B6B', bg: '#2e0a0a' }, // 9  Dragon Island
  { primary: '#00B894', secondary: '#55EFC4', bg: '#0a2e22' }, // 10 Enchanted Forest
];

// Power-Up Colors
export const POWERUP_COLORS = {
  rowBomb: '#FF6B6B',
  colBomb: '#4ECDC4',
  colorBomb: '#FFE66D',
  shuffle: '#A855F7',
};
