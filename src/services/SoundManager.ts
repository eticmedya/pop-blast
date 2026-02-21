import { createAudioPlayer, AudioPlayer } from 'expo-audio';

type SoundName = 'tap' | 'swap' | 'match' | 'combo' | 'cannon' | 'win' | 'lose';

const SOUND_FILES: Record<SoundName, number> = {
  tap: require('../../assets/sounds/tap.wav'),
  swap: require('../../assets/sounds/swap.wav'),
  match: require('../../assets/sounds/match.wav'),
  combo: require('../../assets/sounds/combo.wav'),
  cannon: require('../../assets/sounds/cannon.wav'),
  win: require('../../assets/sounds/win.wav'),
  lose: require('../../assets/sounds/lose.wav'),
};

const VOLUME_MAP: Record<SoundName, number> = {
  tap: 0.3,
  swap: 0.4,
  match: 0.5,
  combo: 0.7,
  cannon: 0.6,
  win: 0.8,
  lose: 0.6,
};

class SoundManager {
  private muted: boolean = false;
  private loaded: boolean = false;
  private players: Partial<Record<SoundName, AudioPlayer>> = {};

  async preload(): Promise<void> {
    if (this.loaded) return;

    try {
      for (const [name, source] of Object.entries(SOUND_FILES)) {
        const player = createAudioPlayer(source);
        player.volume = VOLUME_MAP[name as SoundName];
        this.players[name as SoundName] = player;
      }
      this.loaded = true;
    } catch {
      // Audio not available (e.g., web without audio context)
    }
  }

  setMuted(muted: boolean): void {
    this.muted = muted;
    for (const player of Object.values(this.players)) {
      if (player) player.muted = muted;
    }
  }

  isMuted(): boolean {
    return this.muted;
  }

  async play(name: SoundName): Promise<void> {
    if (this.muted || !this.loaded) return;

    const player = this.players[name];
    if (!player) return;

    try {
      await player.seekTo(0);
      player.play();
    } catch {
      // Playback error - ignore silently
    }
  }

  async cleanup(): Promise<void> {
    for (const player of Object.values(this.players)) {
      if (player) player.remove();
    }
    this.players = {};
    this.loaded = false;
  }
}

export const soundManager = new SoundManager();
