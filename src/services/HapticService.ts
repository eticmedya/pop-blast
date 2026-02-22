import * as Haptics from 'expo-haptics';
import { useSettingsStore } from '../stores/settingsStore';

class HapticService {
  private get enabled(): boolean {
    return useSettingsStore.getState().hapticsEnabled;
  }

  /** Tile'a dokunma */
  tap(): void {
    if (!this.enabled) return;
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
  }

  /** 3'lü eşleşme */
  match(): void {
    if (!this.enabled) return;
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Medium);
  }

  /** 4+ eşleşme veya cascade */
  heavyMatch(): void {
    if (!this.enabled) return;
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Heavy);
  }

  /** Power-up kullanımı */
  powerUp(): void {
    if (!this.enabled) return;
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Heavy);
  }

  /** Seviye tamamlama */
  success(): void {
    if (!this.enabled) return;
    Haptics.notificationAsync(Haptics.NotificationFeedbackType.Success);
  }

  /** Game over */
  failure(): void {
    if (!this.enabled) return;
    Haptics.notificationAsync(Haptics.NotificationFeedbackType.Error);
  }

  /** Buton basma */
  buttonPress(): void {
    if (!this.enabled) return;
    Haptics.impactAsync(Haptics.ImpactFeedbackStyle.Light);
  }

  /** Uyarı (az hamle) */
  warning(): void {
    if (!this.enabled) return;
    Haptics.notificationAsync(Haptics.NotificationFeedbackType.Warning);
  }
}

export const hapticService = new HapticService();
