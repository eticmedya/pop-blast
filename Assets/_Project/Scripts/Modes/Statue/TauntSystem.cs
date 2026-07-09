// STATUE PANIC! - Taunt Sistemi
// Heykel ıslık/gıcırtı sesi çıkarır (3D pozisyonel), arayan 10 sn içinde yakalayamazsa +50.
// Yüksek risk = yüksek ödül = klip anı.

using Unity.Netcode;
using UnityEngine;
using StatuePanic.Core;
using StatuePanic.Player;

namespace StatuePanic.Modes.Statue
{
    [RequireComponent(typeof(PlayerIdentity))]
    public class TauntSystem : NetworkBehaviour
    {
        [SerializeField] private AudioSource tauntSource; // 3D spatial, maxDistance ~20m
        [SerializeField] private float cooldown = 25f;

        private PlayerIdentity _identity;
        private float _cooldownTimer;
        private float _rewardTimer; // host: taunt sonrası hayatta kalma penceresi
        private bool _rewardPending;

        private void Awake() => _identity = GetComponent<PlayerIdentity>();

        private void Update()
        {
            if (_cooldownTimer > 0f) _cooldownTimer -= Time.deltaTime;

            if (IsServer && _rewardPending)
            {
                _rewardTimer -= Time.deltaTime;
                if (_identity.State.Value == HiderState.Caught) _rewardPending = false;
                else if (_rewardTimer <= 0f)
                {
                    _rewardPending = false;
                    _identity.AddScore(GameConstants.TauntSurvivalBonus);
                }
            }
        }

        /// <summary>HUD "TAUNT 🎵" butonu.</summary>
        public void OwnerTaunt()
        {
            if (!IsOwner || !_identity.IsAliveHider || _cooldownTimer > 0f) return;
            _cooldownTimer = cooldown;
            RequestTauntRpc();
        }

        [Rpc(SendTo.Server)]
        private void RequestTauntRpc(RpcParams rpcParams = default)
        {
            if (rpcParams.Receive.SenderClientId != OwnerClientId) return;
            if (!_identity.IsAliveHider) return;
            if (MatchManager.Instance.Phase.Value != MatchPhase.Hunt) return;

            _rewardPending = true;
            _rewardTimer = GameConstants.TauntWindowSeconds;
            PlayTauntRpc();
        }

        [Rpc(SendTo.ClientsAndHost)]
        private void PlayTauntRpc()
        {
            if (tauntSource != null) tauntSource.Play();
        }
    }
}
