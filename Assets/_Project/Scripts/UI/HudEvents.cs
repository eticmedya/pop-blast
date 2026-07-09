// STATUE PANIC! - HUD olay köprüsü
// Ağ katmanı ile UI arasındaki gevşek bağlantı (UI, network scriptlerine referans tutmaz).

using System;
using UnityEngine;

namespace StatuePanic.UI
{
    public static class HudEvents
    {
        /// <summary>true = "GÖRÜLÜYORSUN!" uyarısı açık.</summary>
        public static event Action<bool> ObservedChanged;
        public static void RaiseObservedChanged(bool observed) => ObservedChanged?.Invoke(observed);

        /// <summary>Yanlış NPC heykele dokunma: kamera sallantısı + "YANLIŞ HEYKEL!" overlay.</summary>
        public static event Action WrongTouchOccurred;
        public static void RaiseWrongTouch() => WrongTouchOccurred?.Invoke();

        /// <summary>Bir heykel yakalandığında: kısa reveal kamera efekti.
        /// hiderPosition = yakalanan heykel dünya konumu.</summary>
        public static event Action<Vector3> HiderCaughtReveal;
        public static void RaiseHiderCaughtReveal(Vector3 hiderPosition) =>
            HiderCaughtReveal?.Invoke(hiderPosition);
    }
}
