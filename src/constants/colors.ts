export const TILE_COLORS = [
  '#FF4757', // Kırmızı
  '#3742FA', // Mavi
  '#2ED573', // Yeşil
  '#FFA502', // Turuncu
  '#A855F7', // Mor
  '#FBBF24', // Sarı
] as const;

export type TileColor = (typeof TILE_COLORS)[number];

export const BG_COLOR = '#0F0F23';
export const GRID_BG_COLOR = '#1A1A2E';
export const ACCENT_COLOR = '#FF6B35';
export const TEXT_COLOR = '#FFFFFF';
export const SCORE_COLOR = '#FFD700';
