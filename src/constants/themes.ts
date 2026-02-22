import { ImageSourcePropType } from 'react-native';

// ─── Tile Theme: Her dünya için farklı emoji/obje seti ───
export interface TileTheme {
  /** Tile üzerinde gösterilecek emoji/sembol (6 renk için 6 adet) */
  emojis: string[];
  /** Tile şekli */
  shape: 'circle' | 'rounded_square';
}

// ─── World Theme: Her dünya için tam görsel tema ───
export interface WorldTheme {
  name: string;
  /** Arka plan gradient renkleri (üstten alta) */
  bgGradient: string[];
  /** Board çerçeve rengi */
  boardBorder: string;
  /** Board arka plan rengi */
  boardBg: string;
  /** Tile teması */
  tileTheme: TileTheme;
  /** Karakter resmi (require ile) */
  character: ImageSourcePropType;
  /** Karakterin adı */
  characterName: string;
  /** Dekoratif parçacık renkleri */
  particleColors: string[];
  /** Üst bar arka plan rengi */
  headerBg: string;
  /** Accent renk (butonlar vb.) */
  accent: string;
  /** İkincil renk */
  secondary: string;
}

// Karakter resimleri
const CHARACTERS = {
  monkey: require('../../assets/images/characters/monkey.png'),
  penguin: require('../../assets/images/characters/penguin.png'),
  aslan: require('../../assets/images/characters/aslan.png'),
  fil: require('../../assets/images/characters/fil.png'),
  snake: require('../../assets/images/characters/snake.png'),
  kaplan: require('../../assets/images/characters/kaplan.png'),
  esek: require('../../assets/images/characters/esek.png'),
};

// ─── 10 Dünya Teması ───
export const WORLD_THEMES: WorldTheme[] = [
  // Dünya 1: Tatlı Bahçe (Şekerler)
  {
    name: 'Tatlı Bahçe',
    bgGradient: ['#7B2FF7', '#4A90D9', '#67D5B5', '#A8E6CF'],
    boardBorder: 'rgba(255,255,255,0.25)',
    boardBg: 'rgba(255,255,255,0.12)',
    tileTheme: {
      emojis: ['🍬', '🍭', '🧁', '🍩', '🍪', '🎂'],
      shape: 'rounded_square',
    },
    character: CHARACTERS.monkey,
    characterName: 'Monkey',
    particleColors: ['#FF6B9D', '#C471ED', '#12CBC4', '#FFC312', '#A3CB38', '#FDA7DF'],
    headerBg: 'rgba(123,47,247,0.85)',
    accent: '#FF6B9D',
    secondary: '#C471ED',
  },

  // Dünya 2: Okyanus Derinlikleri (Deniz canlıları)
  {
    name: 'Okyanus Derinlikleri',
    bgGradient: ['#0C2461', '#1B4F72', '#2E86C1', '#85C1E9'],
    boardBorder: 'rgba(133,193,233,0.3)',
    boardBg: 'rgba(14,36,97,0.6)',
    tileTheme: {
      emojis: ['🐙', '🐠', '🦀', '🐚', '🦈', '🐬'],
      shape: 'circle',
    },
    character: CHARACTERS.penguin,
    characterName: 'Penguin',
    particleColors: ['#00D2D3', '#54A0FF', '#48DBFB', '#5F27CD', '#01A3A4', '#0ABDE3'],
    headerBg: 'rgba(12,36,97,0.85)',
    accent: '#00D2D3',
    secondary: '#54A0FF',
  },

  // Dünya 3: Volkanik Adalar (Ateş & Lav)
  {
    name: 'Volkanik Adalar',
    bgGradient: ['#6D214F', '#B33771', '#E55039', '#F39C12'],
    boardBorder: 'rgba(243,156,18,0.3)',
    boardBg: 'rgba(109,33,79,0.5)',
    tileTheme: {
      emojis: ['🔥', '🌋', '💎', '⭐', '🪨', '🌙'],
      shape: 'rounded_square',
    },
    character: CHARACTERS.aslan,
    characterName: 'Aslan',
    particleColors: ['#E55039', '#F39C12', '#EB2F06', '#FFC312', '#B33771', '#FA983A'],
    headerBg: 'rgba(109,33,79,0.85)',
    accent: '#E55039',
    secondary: '#F39C12',
  },

  // Dünya 4: Yıldız Bulutsusu (Uzay)
  {
    name: 'Yıldız Bulutsusu',
    bgGradient: ['#0C0032', '#190061', '#3500D3', '#282A7A'],
    boardBorder: 'rgba(168,85,247,0.3)',
    boardBg: 'rgba(12,0,50,0.6)',
    tileTheme: {
      emojis: ['🌟', '🪐', '🚀', '☄️', '🌙', '💫'],
      shape: 'circle',
    },
    character: CHARACTERS.kaplan,
    characterName: 'Kaplan',
    particleColors: ['#A855F7', '#D388FF', '#6C5CE7', '#FD79A8', '#00CEC9', '#FDCB6E'],
    headerBg: 'rgba(12,0,50,0.85)',
    accent: '#A855F7',
    secondary: '#D388FF',
  },

  // Dünya 5: Kristal Mağara (Mücevherler)
  {
    name: 'Kristal Mağara',
    bgGradient: ['#1B1464', '#0C2461', '#0652DD', '#1289A7'],
    boardBorder: 'rgba(18,137,167,0.3)',
    boardBg: 'rgba(27,20,100,0.5)',
    tileTheme: {
      emojis: ['💎', '🔮', '💠', '🧊', '✨', '🪩'],
      shape: 'rounded_square',
    },
    character: CHARACTERS.fil,
    characterName: 'Fil',
    particleColors: ['#00D2D3', '#48DBFB', '#0652DD', '#1289A7', '#C4E538', '#A3CB38'],
    headerBg: 'rgba(27,20,100,0.85)',
    accent: '#00D2D3',
    secondary: '#48DBFB',
  },

  // Dünya 6: Gün Batımı Vadisi (Meyveler)
  {
    name: 'Gün Batımı Vadisi',
    bgGradient: ['#E44D26', '#F0932B', '#FFBE76', '#BADC58'],
    boardBorder: 'rgba(255,190,118,0.3)',
    boardBg: 'rgba(228,77,38,0.35)',
    tileTheme: {
      emojis: ['🍓', '🍊', '🍇', '🍋', '🍎', '🥝'],
      shape: 'circle',
    },
    character: CHARACTERS.snake,
    characterName: 'Snake',
    particleColors: ['#FC427B', '#FD7272', '#F0932B', '#FFBE76', '#BADC58', '#6AB04C'],
    headerBg: 'rgba(228,77,38,0.85)',
    accent: '#FC427B',
    secondary: '#F0932B',
  },

  // Dünya 7: Derin Uzay (Galaksi)
  {
    name: 'Derin Uzay',
    bgGradient: ['#0A0A2A', '#1A1A4A', '#2D1B69', '#11998E'],
    boardBorder: 'rgba(17,153,142,0.3)',
    boardBg: 'rgba(10,10,42,0.7)',
    tileTheme: {
      emojis: ['🌌', '🛸', '👾', '🌠', '🔭', '🛰️'],
      shape: 'rounded_square',
    },
    character: CHARACTERS.esek,
    characterName: 'Esek',
    particleColors: ['#706FD3', '#3D3D6B', '#11998E', '#38ADA9', '#82CCDD', '#6A89CC'],
    headerBg: 'rgba(10,10,42,0.85)',
    accent: '#11998E',
    secondary: '#706FD3',
  },

  // Dünya 8: Kar Krallığı (Kış)
  {
    name: 'Kar Krallığı',
    bgGradient: ['#2C3A47', '#3B6978', '#84B9EF', '#D6E6F2'],
    boardBorder: 'rgba(132,185,239,0.3)',
    boardBg: 'rgba(44,58,71,0.5)',
    tileTheme: {
      emojis: ['❄️', '⛄', '🎿', '🧣', '🎄', '🌨️'],
      shape: 'circle',
    },
    character: CHARACTERS.penguin,
    characterName: 'Penguin',
    particleColors: ['#74B9FF', '#A3D8F4', '#DFE6E9', '#B2BEC3', '#0984E3', '#00B894'],
    headerBg: 'rgba(44,58,71,0.85)',
    accent: '#74B9FF',
    secondary: '#A3D8F4',
  },

  // Dünya 9: Ejderha Adası (Efsanevi)
  {
    name: 'Ejderha Adası',
    bgGradient: ['#6B0848', '#A40A3C', '#E74C3C', '#F9BF3B'],
    boardBorder: 'rgba(231,76,60,0.3)',
    boardBg: 'rgba(107,8,72,0.5)',
    tileTheme: {
      emojis: ['🐉', '🗡️', '🛡️', '👑', '🏰', '🧙'],
      shape: 'rounded_square',
    },
    character: CHARACTERS.aslan,
    characterName: 'Aslan',
    particleColors: ['#E74C3C', '#FF6B6B', '#F9BF3B', '#F39C12', '#D63031', '#E17055'],
    headerBg: 'rgba(107,8,72,0.85)',
    accent: '#E74C3C',
    secondary: '#F9BF3B',
  },

  // Dünya 10: Büyülü Orman (Doğa)
  {
    name: 'Büyülü Orman',
    bgGradient: ['#0A3D2D', '#1E8449', '#27AE60', '#82E0AA'],
    boardBorder: 'rgba(39,174,96,0.3)',
    boardBg: 'rgba(10,61,45,0.5)',
    tileTheme: {
      emojis: ['🍄', '🦋', '🌺', '🌿', '🐝', '🦜'],
      shape: 'circle',
    },
    character: CHARACTERS.monkey,
    characterName: 'Monkey',
    particleColors: ['#00B894', '#55EFC4', '#00CEC9', '#FFEAA7', '#FDCB6E', '#6C5CE7'],
    headerBg: 'rgba(10,61,45,0.85)',
    accent: '#00B894',
    secondary: '#55EFC4',
  },
];

/** Seviye numarasına göre dünya temasını getir */
export function getWorldTheme(level: number): WorldTheme {
  const worldIndex = Math.floor((level - 1) / 5);
  return WORLD_THEMES[worldIndex % WORLD_THEMES.length];
}

/** Seviye numarasına göre dünya indexini getir (0-based) */
export function getWorldIndex(level: number): number {
  return Math.floor((level - 1) / 5);
}

/** Tile renk indexine göre emoji getir */
export function getTileEmoji(level: number, colorIndex: number): string {
  const theme = getWorldTheme(level);
  return theme.tileTheme.emojis[colorIndex % theme.tileTheme.emojis.length];
}
