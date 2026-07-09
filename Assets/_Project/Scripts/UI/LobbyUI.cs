// STATUE PANIC! - Ana menü / Lobi UI (minimal Faz 1 sürümü)
// Oda kur + kodla katıl + maçı başlat akışı.

using TMPro;
using UnityEngine;
using UnityEngine.UI;
using StatuePanic.Core;
using StatuePanic.Networking;

namespace StatuePanic.UI
{
    public class LobbyUI : MonoBehaviour
    {
        [Header("Ana Menü")]
        [SerializeField] private Button createRoomButton;
        [SerializeField] private Button joinRoomButton;
        [SerializeField] private TMP_InputField roomCodeInput;
        [SerializeField] private Toggle privateToggle;

        [Header("Lobi Paneli")]
        [SerializeField] private GameObject lobbyPanel;
        [SerializeField] private TMP_Text roomCodeLabel;
        [SerializeField] private Button startMatchButton; // sadece host'ta aktif
        [SerializeField] private TMP_Text statusLabel;

        private void Start()
        {
            createRoomButton?.onClick.AddListener(OnCreateRoom);
            joinRoomButton?.onClick.AddListener(OnJoinRoom);
            startMatchButton?.onClick.AddListener(OnStartMatch);

            var sm = SessionManager.Instance;
            if (sm != null)
            {
                sm.OnRoomCreated += code => ShowLobby(code, isHost: true);
                sm.OnJoinedRoom += () => ShowLobby(sm.RoomCode, isHost: false);
                sm.OnSessionError += msg => SetStatus(msg);
            }
        }

        private async void OnCreateRoom()
        {
            SetStatus("Oda kuruluyor...");
            bool isPrivate = privateToggle == null || privateToggle.isOn;
            await SessionManager.Instance.CreateRoomAsync("StatuePanic Odası", isPrivate, GameMode.Statue);
        }

        private async void OnJoinRoom()
        {
            if (roomCodeInput == null || string.IsNullOrWhiteSpace(roomCodeInput.text))
            { SetStatus("Oda kodunu gir."); return; }
            SetStatus("Katılınıyor...");
            await SessionManager.Instance.JoinRoomByCodeAsync(roomCodeInput.text);
        }

        private void OnStartMatch()
        {
            MatchManager.Instance?.RequestStartMatchRpc();
        }

        private void ShowLobby(string code, bool isHost)
        {
            if (lobbyPanel != null) lobbyPanel.SetActive(true);
            if (roomCodeLabel != null) roomCodeLabel.text = $"ODA KODU: {code}";
            if (startMatchButton != null) startMatchButton.gameObject.SetActive(isHost);
            SetStatus(isHost ? "Arkadaşlarına kodu gönder!" : "Host'un maçı başlatması bekleniyor...");
        }

        private void SetStatus(string msg)
        {
            if (statusLabel != null) statusLabel.text = msg;
            Debug.Log($"[LobbyUI] {msg}");
        }
    }
}
