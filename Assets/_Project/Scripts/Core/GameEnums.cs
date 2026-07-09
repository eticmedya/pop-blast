// STATUE PANIC! - Core enums & constants
// Tüm modlarda ortak kullanılan tipler.

namespace StatuePanic.Core
{
    public enum GameMode : byte
    {
        Statue = 0,   // Mod 1 - Heykel (lansman modu)
        Echo = 1,     // Mod 2 - Ses Taklidi (Faz 3)
        FakeWaiter = 2 // Mod 3 - Sahte Garson (Faz 4)
    }

    public enum PlayerRole : byte
    {
        None = 0,
        Seeker = 1,  // Arayan
        Hider = 2    // Heykel / Saklanan
    }

    public enum MatchPhase : byte
    {
        Lobby = 0,
        Preparation = 1,  // Heykeller yer + poz seçer (45 sn), arayanlar bekler
        Hunt = 2,         // Avlanma fazı (240 sn)
        RoundEnd = 3,     // Tur sonucu
        PoseGallery = 4,  // Poz galerisi + oylama (viral ekran)
        MatchEnd = 5
    }

    public enum HiderState : byte
    {
        Free = 0,       // Hareket edebilir (görülmüyor)
        Petrified = 1,  // Donmuş (taş dokusu aktif)
        Exposed = 2,    // Görüş konisindeyken hareket etti -> renkleniyor
        Caught = 3      // Yakalandı
    }

    public static class GameConstants
    {
        // --- Tur zamanlaması (saniye) ---
        public const float PrepDuration = 45f;
        public const float HuntDuration = 240f;
        public const float RoundEndDuration = 8f;
        public const float PoseGalleryDuration = 20f;
        public const int RoundsPerMatch = 5;

        // --- Görüş konisi (host-otoriter) ---
        public const float SeekerFovDegrees = 70f;
        public const float SeekerViewDistance = 25f;
        public const float FreezeGraceSeconds = 0.3f;   // Görüldükten sonra donmak için tanınan süre
        public const float ExposureRatePerSecond = 0.02f; // Görülürken hareket = %2/sn renklenme

        // --- Dokunma sistemi ---
        public const int TouchBudgetPerSeeker = 5;
        public const float TouchRange = 2.2f;
        public const float WrongTouchStunSeconds = 5f;

        // --- Puanlama ---
        public const int PointsPerSecondInSight = 2;    // Görüş konisinde geçen saniye (risk = ödül)
        public const int TauntSurvivalBonus = 50;       // Taunt sonrası 10 sn yakalanmama
        public const float TauntWindowSeconds = 10f;
        public const int SurvivalBonus = 100;
        public const int CatchReward = 75;
        public const int WrongTouchPenalty = -25;

        // --- Oyuncu sayıları ---
        public const int MinPlayers = 2;   // Test için 2; canlıda 4 önerilir
        public const int MaxPlayers = 10;

        // --- Hareket (host doğrulama sınırları / anti-cheat) ---
        public const float MoveSpeed = 4.5f;
        public const float MaxAllowedSpeed = 6.5f; // Bunun üstü = hız hilesi şüphesi
    }

    /// <summary>Oyuncu sayısına göre arayan sayısı (tasarım dokümanı bölüm 3).</summary>
    public static class RoleBalance
    {
        public static int SeekerCountFor(int playerCount)
        {
            if (playerCount <= 4) return 1;
            if (playerCount <= 7) return 2;
            return 3;
        }
    }
}
