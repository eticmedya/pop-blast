// STATUE PANIC! - Maç yöneticisi (host-otoriter durum makinesi)
// Faz akışı: Lobby -> Preparation -> Hunt -> RoundEnd -> PoseGallery -> (5 tur) -> MatchEnd
// Rol dağıtımı rotasyonludur: herkes en az bir kez Arayan olur.
// Sahnedeki tek bir NetworkObject üzerinde durur, NetworkManager ile spawn edilir.

using System.Collections.Generic;
using System.Linq;
using Unity.Netcode;
using UnityEngine;
using StatuePanic.Modes.Statue;

namespace StatuePanic.Core
{
    public class MatchManager : NetworkBehaviour
    {
        public static MatchManager Instance { get; private set; }

        // --- Senkron durum (herkes okur, sadece host yazar) ---
        public NetworkVariable<MatchPhase> Phase = new(MatchPhase.Lobby);
        public NetworkVariable<float> PhaseTimeRemaining = new(0f);
        public NetworkVariable<int> CurrentRound = new(0);

        // Rotasyon takibi: hangi clientId'ler arayanlık yaptı
        private readonly HashSet<ulong> _hasBeenSeeker = new();
        private float _phaseTimer;

        public override void OnNetworkSpawn()
        {
            Instance = this;
            if (IsServer)
                NetworkManager.Singleton.OnClientDisconnectCallback += HandleClientDisconnect;
        }

        public override void OnNetworkDespawn()
        {
            if (IsServer && NetworkManager.Singleton != null)
                NetworkManager.Singleton.OnClientDisconnectCallback -= HandleClientDisconnect;
        }

        private void Update()
        {
            if (!IsServer || Phase.Value == MatchPhase.Lobby || Phase.Value == MatchPhase.MatchEnd) return;

            _phaseTimer -= Time.deltaTime;
            PhaseTimeRemaining.Value = Mathf.Max(0f, _phaseTimer);
            if (_phaseTimer <= 0f) AdvancePhase();
        }

        // ---------------- HOST API ----------------

        /// <summary>Lobiden maçı başlatır (sadece host UI'ı çağırır).</summary>
        [Rpc(SendTo.Server)]
        public void RequestStartMatchRpc(RpcParams rpcParams = default)
        {
            // Sadece host'un kendi isteği kabul edilir
            if (rpcParams.Receive.SenderClientId != NetworkManager.ServerClientId) return;
            if (Phase.Value != MatchPhase.Lobby) return;

            int playerCount = NetworkManager.Singleton.ConnectedClientsIds.Count;
            if (playerCount < GameConstants.MinPlayers)
            {
                Debug.LogWarning("[Match] Yetersiz oyuncu.");
                return;
            }

            _hasBeenSeeker.Clear();
            CurrentRound.Value = 0;
            StartNextRound();
        }

        private void StartNextRound()
        {
            CurrentRound.Value++;
            AssignRoles();
            ScoreSystem.Instance?.ResetRoundState();
            SetPhase(MatchPhase.Preparation, GameConstants.PrepDuration);
        }

        private void AdvancePhase()
        {
            switch (Phase.Value)
            {
                case MatchPhase.Preparation:
                    SetPhase(MatchPhase.Hunt, GameConstants.HuntDuration);
                    break;

                case MatchPhase.Hunt:
                    EndHunt(seekersWin: false); // Süre doldu -> heykeller kazandı
                    break;

                case MatchPhase.RoundEnd:
                    SetPhase(MatchPhase.PoseGallery, GameConstants.PoseGalleryDuration);
                    break;

                case MatchPhase.PoseGallery:
                    if (CurrentRound.Value >= GameConstants.RoundsPerMatch)
                        SetPhase(MatchPhase.MatchEnd, 0f);
                    else
                        StartNextRound();
                    break;
            }
        }

        /// <summary>Hunt fazını bitirir. VisionCone/SeekerTouch sistemleri tüm heykeller yakalanınca çağırır.</summary>
        public void EndHunt(bool seekersWin)
        {
            if (!IsServer || Phase.Value != MatchPhase.Hunt) return;
            ScoreSystem.Instance?.ApplyRoundEndBonuses(seekersWin);
            SetPhase(MatchPhase.RoundEnd, GameConstants.RoundEndDuration);
        }

        private void SetPhase(MatchPhase phase, float duration)
        {
            Phase.Value = phase;
            _phaseTimer = duration;
            PhaseTimeRemaining.Value = duration;
            Debug.Log($"[Match] Faz: {phase} (tur {CurrentRound.Value})");
        }

        // ---------------- ROL DAĞITIMI ----------------

        private void AssignRoles()
        {
            var clientIds = NetworkManager.Singleton.ConnectedClientsIds.ToList();
            int seekerCount = RoleBalance.SeekerCountFor(clientIds.Count);

            // Önce henüz arayan olmamışlar, sonra rastgele — herkes sırasını alır
            var pool = clientIds.OrderBy(id => _hasBeenSeeker.Contains(id) ? 1 : 0)
                                .ThenBy(_ => Random.value)
                                .ToList();

            var seekers = pool.Take(seekerCount).ToHashSet();
            foreach (var id in seekers) _hasBeenSeeker.Add(id);
            if (_hasBeenSeeker.Count >= clientIds.Count) _hasBeenSeeker.Clear(); // Rotasyon sıfırla

            foreach (var client in NetworkManager.Singleton.ConnectedClientsList)
            {
                var identity = client.PlayerObject != null
                    ? client.PlayerObject.GetComponent<Player.PlayerIdentity>() : null;
                if (identity == null) continue;
                identity.Role.Value = seekers.Contains(client.ClientId) ? PlayerRole.Seeker : PlayerRole.Hider;
                identity.ResetForRound();
            }
        }

        private void HandleClientDisconnect(ulong clientId)
        {
            // Basit dayanıklılık: Hunt sırasında tüm heykeller düştüyse turu bitir.
            if (Phase.Value != MatchPhase.Hunt) return;
            bool anyHiderAlive = NetworkManager.Singleton.ConnectedClientsList.Any(c =>
            {
                var pi = c.PlayerObject != null ? c.PlayerObject.GetComponent<Player.PlayerIdentity>() : null;
                return pi != null && pi.Role.Value == PlayerRole.Hider && pi.State.Value != HiderState.Caught;
            });
            if (!anyHiderAlive) EndHunt(seekersWin: true);
        }
    }
}
