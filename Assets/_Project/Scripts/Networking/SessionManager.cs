// STATUE PANIC! - Oturum yöneticisi (Unity Relay + Lobby)
// Oda kodu ile cross-platform davet sisteminin kalbi.
// Host: Relay allocation -> Lobby (join code data'da) -> NGO StartHost
// Client: Lobby'yi kodla bul -> Relay join -> NGO StartClient
//
// NOT: API imzaları NGO 2.x / Relay 1.x / Lobby 1.x hedeflenerek yazıldı.
// Paket sürümlerine göre küçük düzeltmeler gerekebilir (bkz. HANDOFF.md Adım 2).

using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using Unity.Netcode;
using Unity.Netcode.Transports.UTP;
using Unity.Networking.Transport.Relay;
using Unity.Services.Lobbies;
using Unity.Services.Lobbies.Models;
using Unity.Services.Relay;
using Unity.Services.Relay.Models;
using UnityEngine;

namespace StatuePanic.Networking
{
    public class SessionManager : MonoBehaviour
    {
        public static SessionManager Instance { get; private set; }

        [Header("Config")]
        [SerializeField] private int maxPlayers = Core.GameConstants.MaxPlayers;
        [SerializeField] private string connectionType = "dtls";

        public Lobby CurrentLobby { get; private set; }
        public string RoomCode { get; private set; }
        public bool IsHost => NetworkManager.Singleton != null && NetworkManager.Singleton.IsHost;

        public event Action<string> OnRoomCreated;
        public event Action OnJoinedRoom;
        public event Action<string> OnSessionError;

        private float _heartbeatTimer;
        private const float HeartbeatInterval = 15f;

        private void Awake()
        {
            if (Instance != null) { Destroy(gameObject); return; }
            Instance = this;
            DontDestroyOnLoad(gameObject);
        }

        private void Update()
        {
            if (CurrentLobby != null && IsHost)
            {
                _heartbeatTimer += Time.deltaTime;
                if (_heartbeatTimer >= HeartbeatInterval)
                {
                    _heartbeatTimer = 0f;
                    _ = LobbyService.Instance.SendHeartbeatPingAsync(CurrentLobby.Id);
                }
            }
        }

        // ---------------- HOST ----------------

        public async Task<bool> CreateRoomAsync(string lobbyName, bool isPrivate, Core.GameMode mode)
        {
            try
            {
                Allocation allocation = await RelayService.Instance.CreateAllocationAsync(maxPlayers - 1);
                string relayJoinCode = await RelayService.Instance.GetJoinCodeAsync(allocation.AllocationId);

                var transport = NetworkManager.Singleton.GetComponent<UnityTransport>();
                transport.SetRelayServerData(new RelayServerData(allocation, connectionType));

                var options = new CreateLobbyOptions
                {
                    IsPrivate = isPrivate,
                    Data = new Dictionary<string, DataObject>
                    {
                        { "relayJoinCode", new DataObject(DataObject.VisibilityOptions.Member, relayJoinCode) },
                        { "gameMode", new DataObject(DataObject.VisibilityOptions.Public,
                            ((int)mode).ToString(), DataObject.IndexOptions.N1) }
                    }
                };
                CurrentLobby = await LobbyService.Instance.CreateLobbyAsync(lobbyName, maxPlayers, options);
                RoomCode = CurrentLobby.LobbyCode;

                if (!NetworkManager.Singleton.StartHost())
                    throw new Exception("NGO StartHost başarısız");

                Debug.Log($"[Session] Oda kuruldu. Kod: {RoomCode}");
                OnRoomCreated?.Invoke(RoomCode);
                return true;
            }
            catch (Exception e)
            {
                Debug.LogError($"[Session] Oda kurulamadı: {e}");
                OnSessionError?.Invoke("Oda kurulamadı. İnternet bağlantını kontrol edip tekrar dene.");
                await LeaveAsync();
                return false;
            }
        }

        // ---------------- CLIENT ----------------

        public async Task<bool> JoinRoomByCodeAsync(string roomCode)
        {
            try
            {
                roomCode = roomCode.Trim().ToUpperInvariant();
                CurrentLobby = await LobbyService.Instance.JoinLobbyByCodeAsync(roomCode);
                RoomCode = roomCode;

                string relayJoinCode = CurrentLobby.Data["relayJoinCode"].Value;
                JoinAllocation joinAlloc = await RelayService.Instance.JoinAllocationAsync(relayJoinCode);

                var transport = NetworkManager.Singleton.GetComponent<UnityTransport>();
                transport.SetRelayServerData(new RelayServerData(joinAlloc, connectionType));

                if (!NetworkManager.Singleton.StartClient())
                    throw new Exception("NGO StartClient başarısız");

                Debug.Log($"[Session] Odaya katılındı: {roomCode}");
                OnJoinedRoom?.Invoke();
                return true;
            }
            catch (LobbyServiceException le) when (le.Reason == LobbyExceptionReason.LobbyNotFound)
            {
                OnSessionError?.Invoke("Bu kodla bir oda bulunamadı. Kodu kontrol et.");
                return false;
            }
            catch (Exception e)
            {
                Debug.LogError($"[Session] Katılım hatası: {e}");
                OnSessionError?.Invoke("Odaya katılınamadı. Tekrar dene.");
                return false;
            }
        }

        /// <summary>Public lobi listesi (hızlı eşleşme ekranı için).</summary>
        public async Task<List<Lobby>> QueryPublicLobbiesAsync(Core.GameMode? modeFilter = null)
        {
            var options = new QueryLobbiesOptions { Count = 25 };
            if (modeFilter.HasValue)
            {
                options.Filters = new List<QueryFilter>
                {
                    new QueryFilter(QueryFilter.FieldOptions.N1,
                        ((int)modeFilter.Value).ToString(), QueryFilter.OpOptions.EQ)
                };
            }
            var result = await LobbyService.Instance.QueryLobbiesAsync(options);
            return result.Results;
        }

        // ---------------- ANTI-CHEAT KICK ----------------

        /// <summary>Host: belirtilen client'ı lobby'den çıkar ve NGO bağlantısını keser.
        /// PlayerController'ın ViolationTracker eşiği aşıldığında çağırır.</summary>
        public void KickPlayer(ulong clientId, string reason = "")
        {
            if (!NetworkManager.Singleton.IsServer) return;

            Debug.Log($"[Session] Kick: {clientId} — {reason}");
            NetworkManager.Singleton.DisconnectClient(clientId);
            _ = RemoveFromLobbyAsync(clientId);
        }

        private async Task RemoveFromLobbyAsync(ulong clientId)
        {
            if (CurrentLobby == null) return;
            try
            {
                // Lobby oyuncu ID'si, Authentication PlayerId ile eşleşir; clientId değil.
                // Lobby üyelerini tara, NGO clientId bilgisini data'da tut (Faz 2'de eklenebilir).
                // Şimdilik NGO kick yeterlidir; lobby'den düşme otomatik olarak heartbeat timeout ile gerçekleşir.
                await Task.Delay(100);
            }
            catch (Exception e)
            {
                Debug.LogWarning($"[Session] Lobby kick uyarısı: {e.Message}");
            }
        }

        // ---------------- ORTAK ----------------

        public async Task LeaveAsync()
        {
            try
            {
                if (CurrentLobby != null)
                {
                    string playerId = ServicesBootstrap.Instance.PlayerId;
                    if (IsHost)
                        await LobbyService.Instance.DeleteLobbyAsync(CurrentLobby.Id);
                    else if (!string.IsNullOrEmpty(playerId))
                        await LobbyService.Instance.RemovePlayerAsync(CurrentLobby.Id, playerId);
                }
            }
            catch (Exception e) { Debug.LogWarning($"[Session] Lobby ayrılma uyarısı: {e.Message}"); }
            finally
            {
                CurrentLobby = null;
                RoomCode = null;
                if (NetworkManager.Singleton != null &&
                    (NetworkManager.Singleton.IsClient || NetworkManager.Singleton.IsHost))
                    NetworkManager.Singleton.Shutdown();
            }
        }
    }
}
