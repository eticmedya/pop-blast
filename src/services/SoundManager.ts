type SoundName = 'tap' | 'swap' | 'match' | 'combo' | 'cannon' | 'win' | 'lose';

class SoundManager {
  private muted: boolean = false;
  private loaded: boolean = false;

  async preload(): Promise<void> {
    if (this.loaded) return;

    try {
      // expo-audio will be initialized when sound files are added
      this.loaded = true;
    } catch {
      // Audio not available (e.g., web without audio context)
    }
  }

  setMuted(muted: boolean): void {
    this.muted = muted;
  }

  isMuted(): boolean {
    return this.muted;
  }

  async play(_name: SoundName): Promise<void> {
    if (this.muted || !this.loaded) return;

    // Sound playback placeholder - will be activated when MP3 files are added
    // to assets/sounds/ directory. Each sound maps to a file:
    // tap.mp3, swap.mp3, match.mp3, combo.mp3, cannon.mp3, win.mp3, lose.mp3
  }

  async cleanup(): Promise<void> {
    this.loaded = false;
  }
}

export const soundManager = new SoundManager();
