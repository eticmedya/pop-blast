// STATUE PANIC! - Puanlama Sistemi (host-otoriter)
// Tasarım kuralı: risk = ödül. Köşede saklanmak puan getirmez;
// arayanın görüş konisinde donuk kalmak getirir.

using Unity.Netcode;
using UnityEngine;
using StatuePanic.Core;
using StatuePanic.Player;

namespace StatuePanic.Modes.Statue
{
    public class ScoreSystem : NetworkBehaviour
    {
        public static ScoreSystem Instance { get; private set; }

        // Görüş konisi puanı kesirli birikir, tam sayıya dönünce yazılır
        private readonly System.Collections.Generic.Dictionary<ulong, float> _inSightAccum = new();

        public override void OnNetworkSpawn() => Instance = this;

        public void ResetRoundState()
        {
            if (!IsServer) return;
            _inSightAccum.Clear();
        }

        /// <summary>VisionConeSystem çağırır: görüş konisinde donuk geçen süre.</summary>
        public void AccumulateInSightTime(PlayerIdentity hider, float dt)
        {
            if (!IsServer) return;
            ulong id = hider.OwnerClientId;
            _inSightAccum.TryGetValue(id, out float acc);
            acc += dt * GameConstants.PointsPerSecondInSight;

            int whole = Mathf.FloorToInt(acc);
            if (whole > 0)
            {
                hider.AddScore(whole);
                acc -= whole;
            }
            _inSightAccum[id] = acc;
        }

        public void OnHiderCaught(PlayerIdentity hider, PlayerIdentity seeker)
        {
            if (!IsServer) return;
            Debug.Log($"[Score] {seeker.DisplayName.Value} yakaladı: {hider.DisplayName.Value}");

            // Kısa reveal kamerası: yakalanan heykel konumunu tüm clientlara gönder.
            // Her client kendi RevealCameraController'ı üzerinden 1.5 saniyelik zoom-in oynatır.
            SendRevealRpc(hider.transform.position);
        }

        /// <summary>Tüm clientlara yakalanan heykel konumunu iletir; her client yerel reveal kameraını tetikler.</summary>
        [Rpc(SendTo.ClientsAndHost)]
        private void SendRevealRpc(Vector3 hiderPosition)
        {
            UI.HudEvents.RaiseHiderCaughtReveal(hiderPosition);
        }

        /// <summary>Tur bitiminde hayatta kalma bonusları.</summary>
        public void ApplyRoundEndBonuses(bool seekersWin)
        {
            if (!IsServer) return;
            foreach (var c in NetworkManager.Singleton.ConnectedClientsList)
            {
                var pi = c.PlayerObject != null ? c.PlayerObject.GetComponent<PlayerIdentity>() : null;
                if (pi == null) continue;
                if (pi.IsAliveHider && !seekersWin)
                    pi.AddScore(GameConstants.SurvivalBonus);
            }
        }
    }
}
