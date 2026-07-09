// STATUE PANIC! - Arayan Dokunma Sistemi
// Arayan başına 5 dokunma hakkı. Menzil ve hedef doğrulaması HOST'ta yapılır
// (client sadece "şuna dokunmak istiyorum" der — aimbot menzil dışından vuramaz).
//
// Sahte heykel (oyuncu)  -> yakalama (+75)
// Gerçek NPC heykel      -> 1 hak kaybı, -25 puan, 5 sn utanç stun'ı (heykel kafa sallar = klip anı)

using System.Linq;
using Unity.Netcode;
using UnityEngine;
using StatuePanic.Core;
using StatuePanic.Player;

namespace StatuePanic.Modes.Statue
{
    [RequireComponent(typeof(PlayerIdentity))]
    public class SeekerTouch : NetworkBehaviour
    {
        private PlayerIdentity _identity;
        public NetworkVariable<bool> IsStunned = new(false);
        private float _stunTimer;

        private void Awake() => _identity = GetComponent<PlayerIdentity>();

        private void Update()
        {
            if (IsServer && IsStunned.Value)
            {
                _stunTimer -= Time.deltaTime;
                if (_stunTimer <= 0f) IsStunned.Value = false;
            }
        }

        // ---------------- OWNER ----------------

        /// <summary>HUD "DOKUN ✋" butonu / E tuşu. Bakılan hedefe dokunma isteği yollar.</summary>
        public void OwnerTryTouch()
        {
            if (!IsOwner || !_identity.IsSeeker || IsStunned.Value) return;

            // Client sadece niyet bildirir; ekranın ortasından ray at, hedef ID'sini gönder.
            Vector3 origin = transform.position + Vector3.up * 1.6f;
            if (Physics.SphereCast(origin, 0.4f, transform.forward, out var hit, GameConstants.TouchRange + 0.5f))
            {
                var netObj = hit.collider.GetComponentInParent<NetworkObject>();
                if (netObj != null) { RequestTouchPlayerRpc(netObj.NetworkObjectId); return; }

                var npc = hit.collider.GetComponentInParent<NpcStatue>();
                if (npc != null) { RequestTouchNpcRpc(npc.StatueId); return; }
            }
            // Boşa dokunma: hak harcamaz, sadece animasyon oynar (yerel).
        }

        // ---------------- HOST DOĞRULAMA ----------------

        [Rpc(SendTo.Server)]
        private void RequestTouchPlayerRpc(ulong targetNetId, RpcParams rpcParams = default)
        {
            if (!ValidateTouchRequest(rpcParams)) return;

            if (!NetworkManager.SpawnManager.SpawnedObjects.TryGetValue(targetNetId, out var target)) return;
            var targetIdentity = target.GetComponent<PlayerIdentity>();
            if (targetIdentity == null || !targetIdentity.IsAliveHider) return;

            // MENZİL host'ta ölçülür (anti-cheat)
            if (Vector3.Distance(transform.position, target.transform.position) > GameConstants.TouchRange * 1.15f)
            {
                Debug.LogWarning($"[AntiCheat] Client {OwnerClientId} menzil dışı dokunma denemesi.");
                return;
            }

            _identity.TouchBudget.Value--;

            // YAKALAMA!
            targetIdentity.State.Value = HiderState.Caught;
            _identity.AddScore(GameConstants.CatchReward);
            ScoreSystem.Instance?.OnHiderCaught(targetIdentity, _identity);

            // Tüm heykeller yakalandıysa tur biter
            bool anyLeft = NetworkManager.Singleton.ConnectedClientsList.Any(c =>
            {
                var pi = c.PlayerObject != null ? c.PlayerObject.GetComponent<PlayerIdentity>() : null;
                return pi != null && pi.IsAliveHider;
            });
            if (!anyLeft) MatchManager.Instance.EndHunt(seekersWin: true);
        }

        [Rpc(SendTo.Server)]
        private void RequestTouchNpcRpc(int statueId, RpcParams rpcParams = default)
        {
            if (!ValidateTouchRequest(rpcParams)) return;

            var npc = NpcStatue.Find(statueId);
            if (npc == null) return;
            if (Vector3.Distance(transform.position, npc.transform.position) > GameConstants.TouchRange * 1.15f)
                return;

            // YANLIŞ DOKUNMA: hak kaybı + ceza + utanç stun'ı
            _identity.TouchBudget.Value--;
            _identity.AddScore(GameConstants.WrongTouchPenalty);
            IsStunned.Value = true;
            _stunTimer = GameConstants.WrongTouchStunSeconds;

            // Klip anı: NPC heykel kafa sallar — herkese oynat
            PlayShameRpc(statueId);
        }

        private bool ValidateTouchRequest(RpcParams rpcParams)
        {
            if (rpcParams.Receive.SenderClientId != OwnerClientId) return false;
            if (!_identity.IsSeeker || IsStunned.Value) return false;
            if (_identity.TouchBudget.Value <= 0) return false;
            if (MatchManager.Instance == null ||
                MatchManager.Instance.Phase.Value != MatchPhase.Hunt) return false;
            return true;
        }

        [Rpc(SendTo.ClientsAndHost)]
        private void PlayShameRpc(int statueId)
        {
            NpcStatue.Find(statueId)?.PlayShameAnimation();
            // TODO(ClaudeCode): kamera shake + "YANLIŞ HEYKEL!" HUD overlay — sadece bu arayanın client'ında
            // Sahipliği kontrol ederek sadece hatayı yapan oyuncuya efekt göster.
            if (IsOwner) UI.HudEvents.RaiseWrongTouch();
        }
    }
}
