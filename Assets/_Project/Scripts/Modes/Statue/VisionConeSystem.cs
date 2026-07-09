// STATUE PANIC! - Görüş Konisi Sistemi (HOST-OTORİTER — oyunun anti-cheat çekirdeği)
// Her tick'te: her arayanın FOV konisi + raycast ile hangi heykellerin "görüldüğünü" hesaplar.
// Sonuç sadece ilgili heykele bildirilir ("GÖRÜLÜYORSUN" uyarısı) — arayanlara ASLA
// heykel kimliği gönderilmez (wallhack'in işe yaramaması için).
//
// Sahnedeki tek bir NetworkObject'te durur (MatchManager ile aynı objede olabilir).

using System.Collections.Generic;
using Unity.Netcode;
using UnityEngine;
using StatuePanic.Core;
using StatuePanic.Player;

namespace StatuePanic.Modes.Statue
{
    public class VisionConeSystem : NetworkBehaviour
    {
        public static VisionConeSystem Instance { get; private set; }

        [SerializeField] private LayerMask occlusionMask;   // Duvarlar/zemin (heykel katmanı HARİÇ)
        [SerializeField] private float tickRate = 10f;      // sn başına hesap sayısı (mobil host dostu)

        // Host tarafı: hider clientId -> şu an kaç arayan tarafından görülüyor
        private readonly Dictionary<ulong, bool> _observed = new();
        private float _tickTimer;

        public override void OnNetworkSpawn() => Instance = this;

        private void Update()
        {
            if (!IsServer || MatchManager.Instance == null) return;
            if (MatchManager.Instance.Phase.Value != MatchPhase.Hunt) return;

            _tickTimer += Time.deltaTime;
            if (_tickTimer < 1f / tickRate) return;
            float dt = _tickTimer;
            _tickTimer = 0f;

            ComputeVisibility(dt);
        }

        private void ComputeVisibility(float dt)
        {
            var clients = NetworkManager.Singleton.ConnectedClientsList;
            var seekers = new List<(Transform t, PlayerIdentity id)>();
            var hiders = new List<(Transform t, PlayerIdentity id)>();

            foreach (var c in clients)
            {
                var po = c.PlayerObject;
                if (po == null) continue;
                var pi = po.GetComponent<PlayerIdentity>();
                if (pi == null) continue;
                if (pi.IsSeeker) seekers.Add((po.transform, pi));
                else if (pi.IsAliveHider) hiders.Add((po.transform, pi));
            }

            foreach (var (hiderT, hiderId) in hiders)
            {
                bool seenNow = false;
                foreach (var (seekerT, _) in seekers)
                {
                    if (IsInCone(seekerT, hiderT.position)) { seenNow = true; break; }
                }

                bool wasSeen = _observed.TryGetValue(hiderId.OwnerClientId, out var prev) && prev;
                _observed[hiderId.OwnerClientId] = seenNow;

                // Durum değiştiyse sadece o heykele bildir
                if (seenNow != wasSeen)
                    NotifyObservedRpc(seenNow, RpcTarget.Single(hiderId.OwnerClientId, RpcTargetUse.Temp));

                // Görülürken taşlaşmamışsa exposure cezası (PetrifyController state'ine göre)
                var petrify = hiderT.GetComponent<PetrifyController>();
                if (seenNow && petrify != null)
                    petrify.ServerTickExposure(dt);

                // Risk = ödül: görüş konisinde geçen süre puan kazandırır
                if (seenNow && hiderId.State.Value == HiderState.Petrified)
                    ScoreSystem.Instance?.AccumulateInSightTime(hiderId, dt);
            }
        }

        /// <summary>Host: hider şu anda herhangi bir arayan tarafından görülüyor mu?</summary>
        public bool IsObserved(ulong hiderClientId) =>
            _observed.TryGetValue(hiderClientId, out var v) && v;

        private bool IsInCone(Transform seeker, Vector3 targetPos)
        {
            Vector3 eye = seeker.position + Vector3.up * 1.6f;
            Vector3 target = targetPos + Vector3.up * 1.0f;
            Vector3 toTarget = target - eye;

            if (toTarget.sqrMagnitude > GameConstants.SeekerViewDistance * GameConstants.SeekerViewDistance)
                return false;

            float angle = Vector3.Angle(seeker.forward, toTarget);
            if (angle > GameConstants.SeekerFovDegrees * 0.5f) return false;

            // Duvar arkası kontrolü: occlusion varsa görünmüyor
            if (Physics.Raycast(eye, toTarget.normalized, toTarget.magnitude, occlusionMask))
                return false;

            return true;
        }

        [Rpc(SendTo.SpecifiedInParams)]
        private void NotifyObservedRpc(bool observed, RpcParams rpcParams = default)
        {
            // Client tarafı: HUD'da "GÖRÜLÜYORSUN" uyarısını aç/kapat
            UI.HudEvents.RaiseObservedChanged(observed);
        }
    }
}
