// STATUE PANIC! - Taşlaşma Kontrolcüsü
// Heykel oyuncusunun Free <-> Petrified geçişi + görülürken hareket cezası (Exposure).
// Görsel taraf: Petrify.shader'daki _PetrifyAmount ve _Exposure parametrelerini sürer.
//
// Akış:
// - Oyuncu "Don" butonuna basar -> RequestPetrifyRpc -> host state = Petrified
// - Oyuncu hareket eder -> owner NotifyOwnerMoved -> RequestUnpetrifyRpc
// - Host, hareket eden heykel görüş konisindeyse FreezeGrace tanır; donmazsa Exposure artar
// - Exposure >= 1 -> heykel tamamen renklenir (yakalanmış sayılmaz ama çıplak gözle bulunur)

using Unity.Netcode;
using UnityEngine;
using StatuePanic.Core;
using StatuePanic.Player;

namespace StatuePanic.Modes.Statue
{
    [RequireComponent(typeof(PlayerIdentity))]
    public class PetrifyController : NetworkBehaviour
    {
        [SerializeField] private Renderer[] bodyRenderers; // Karakter meshleri
        private static readonly int PetrifyAmountId = Shader.PropertyToID("_PetrifyAmount");
        private static readonly int ExposureId = Shader.PropertyToID("_Exposure");

        private PlayerIdentity _identity;
        private MaterialPropertyBlock _mpb;
        private float _visualPetrify; // 0 = normal, 1 = tam taş (yumuşak geçiş)

        // Host tarafı grace takibi
        private float _graceTimer;
        private bool _pendingMoveWhileSeen;

        private void Awake()
        {
            _identity = GetComponent<PlayerIdentity>();
            _mpb = new MaterialPropertyBlock();
        }

        private void Update()
        {
            UpdateVisuals();
            if (IsServer) TickGrace();
        }

        // ---------------- OWNER GİRDİLERİ ----------------

        /// <summary>HUD'daki "DON 🗿" butonu çağırır.</summary>
        public void OwnerRequestPetrify()
        {
            if (!IsOwner || !_identity.IsHider) return;
            RequestPetrifyRpc(true);
        }

        /// <summary>PlayerController hareket algıladığında çağırır.</summary>
        public void NotifyOwnerMoved()
        {
            if (!IsOwner) return;
            if (_identity.State.Value == HiderState.Petrified)
                RequestPetrifyRpc(false);
        }

        [Rpc(SendTo.Server)]
        private void RequestPetrifyRpc(bool petrify, RpcParams rpcParams = default)
        {
            if (rpcParams.Receive.SenderClientId != OwnerClientId) return; // sahte istek koruması
            if (!_identity.IsAliveHider) return;

            if (petrify)
            {
                _identity.State.Value = HiderState.Petrified;
                _pendingMoveWhileSeen = false;
            }
            else
            {
                // Heykel çözülüyor. Görülüyorsa grace penceresi başlat.
                bool observed = VisionConeSystem.Instance != null &&
                                VisionConeSystem.Instance.IsObserved(OwnerClientId);
                _identity.State.Value = observed ? HiderState.Exposed : HiderState.Free;
                if (observed)
                {
                    _graceTimer = GameConstants.FreezeGraceSeconds;
                    _pendingMoveWhileSeen = true;
                }
            }
        }

        // ---------------- HOST MANTIĞI ----------------

        private void TickGrace()
        {
            if (!_pendingMoveWhileSeen) return;
            _graceTimer -= Time.deltaTime;
            if (_graceTimer > 0f) return;

            // Grace doldu; hâlâ donmadıysa Exposed durumunda kalır (exposure VisionCone tick'inde artar)
            _pendingMoveWhileSeen = false;
        }

        /// <summary>VisionConeSystem her tick çağırır: görülürken donmamış heykelin exposure'ı artar.</summary>
        public void ServerTickExposure(float dt)
        {
            if (!IsServer) return;
            if (_identity.State.Value != HiderState.Exposed) return;

            _identity.Exposure.Value = Mathf.Clamp01(
                _identity.Exposure.Value + GameConstants.ExposureRatePerSecond * dt * 50f);
            // Not: 50x çarpan = ExposureRate %2/sn'yi "görülürken hareket" cezası olarak hissettirir.
            // Playtest'te ayarlanacak (bkz. HANDOFF.md - Tuning).
        }

        /// <summary>Host: güvenli noktada exposure yavaşça iyileşir (görülmüyorken).</summary>
        private void LateUpdate()
        {
            if (!IsServer || !_identity.IsAliveHider) return;
            bool observed = VisionConeSystem.Instance != null &&
                            VisionConeSystem.Instance.IsObserved(OwnerClientId);
            if (!observed && _identity.Exposure.Value > 0f)
                _identity.Exposure.Value = Mathf.Max(0f, _identity.Exposure.Value - 0.1f * Time.deltaTime);

            if (!observed && _identity.State.Value == HiderState.Exposed)
                _identity.State.Value = HiderState.Free;
        }

        // ---------------- GÖRSEL ----------------

        private void UpdateVisuals()
        {
            float target = _identity.State.Value == HiderState.Petrified ? 1f : 0f;
            _visualPetrify = Mathf.MoveTowards(_visualPetrify, target, Time.deltaTime * 4f);

            if (bodyRenderers == null) return;
            foreach (var r in bodyRenderers)
            {
                if (r == null) continue;
                r.GetPropertyBlock(_mpb);
                _mpb.SetFloat(PetrifyAmountId, _visualPetrify);
                _mpb.SetFloat(ExposureId, _identity.Exposure.Value);
                r.SetPropertyBlock(_mpb);
            }
        }
    }
}
