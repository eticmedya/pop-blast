// STATUE PANIC! - Oyun içi HUD (minimal Faz 1 sürümü)
// Rol bazlı buton görünürlüğü + faz sayacı + "GÖRÜLÜYORSUN" uyarısı + dokunma hakkı.
// TODO(ClaudeCode): UI Toolkit veya uGUI prefab'ı kur, referansları bağla.

using TMPro;
using Unity.Netcode;
using UnityEngine;
using UnityEngine.UI;
using StatuePanic.Core;
using StatuePanic.Modes.Statue;
using StatuePanic.Player;

namespace StatuePanic.UI
{
    public class GameHud : MonoBehaviour
    {
        [Header("Ortak")]
        [SerializeField] private TMP_Text phaseLabel;
        [SerializeField] private TMP_Text timerLabel;
        [SerializeField] private TMP_Text scoreLabel;

        [Header("Heykel (Hider)")]
        [SerializeField] private GameObject hiderPanel;
        [SerializeField] private Button petrifyButton;   // "DON 🗿"
        [SerializeField] private Button tauntButton;     // "TAUNT 🎵"
        [SerializeField] private Button poseButton;      // Poz editörünü açar
        [SerializeField] private GameObject observedWarning; // "GÖRÜLÜYORSUN!"

        [Header("Arayan (Seeker)")]
        [SerializeField] private GameObject seekerPanel;
        [SerializeField] private Button touchButton;     // "DOKUN ✋"
        [SerializeField] private TMP_Text touchBudgetLabel;

        private PlayerIdentity _localIdentity;

        private void OnEnable() => HudEvents.ObservedChanged += OnObservedChanged;
        private void OnDisable() => HudEvents.ObservedChanged -= OnObservedChanged;

        private void Start()
        {
            petrifyButton?.onClick.AddListener(() =>
                Local<PetrifyController>()?.OwnerRequestPetrify());
            tauntButton?.onClick.AddListener(() =>
                Local<TauntSystem>()?.OwnerTaunt());
            touchButton?.onClick.AddListener(() =>
                Local<SeekerTouch>()?.OwnerTryTouch());
            // poseButton -> PoseEditorUI.Open() (Faz 1.5)
        }

        private void Update()
        {
            var mm = MatchManager.Instance;
            if (mm == null) return;

            if (timerLabel != null)
                timerLabel.text = Mathf.CeilToInt(mm.PhaseTimeRemaining.Value).ToString();
            if (phaseLabel != null)
                phaseLabel.text = PhaseNameTR(mm.Phase.Value, mm.CurrentRound.Value);

            var id = LocalIdentity();
            if (id == null) return;

            if (scoreLabel != null) scoreLabel.text = $"Puan: {id.MatchScore.Value}";
            bool isHider = id.IsHider;
            if (hiderPanel != null) hiderPanel.SetActive(isHider);
            if (seekerPanel != null) seekerPanel.SetActive(id.IsSeeker);
            if (id.IsSeeker && touchBudgetLabel != null)
                touchBudgetLabel.text = $"✋ {id.TouchBudget.Value}";
        }

        private void OnObservedChanged(bool observed)
        {
            if (observedWarning != null) observedWarning.SetActive(observed);
        }

        private PlayerIdentity LocalIdentity()
        {
            if (_localIdentity != null) return _localIdentity;
            var nm = NetworkManager.Singleton;
            if (nm == null || nm.LocalClient == null || nm.LocalClient.PlayerObject == null) return null;
            _localIdentity = nm.LocalClient.PlayerObject.GetComponent<PlayerIdentity>();
            return _localIdentity;
        }

        private T Local<T>() where T : Component
        {
            var id = LocalIdentity();
            return id != null ? id.GetComponent<T>() : null;
        }

        private static string PhaseNameTR(MatchPhase phase, int round) => phase switch
        {
            MatchPhase.Lobby => "Lobi",
            MatchPhase.Preparation => $"Tur {round} — Saklan ve Poz Ver!",
            MatchPhase.Hunt => $"Tur {round} — AVLANMA",
            MatchPhase.RoundEnd => "Tur Bitti",
            MatchPhase.PoseGallery => "Poz Galerisi 📸",
            MatchPhase.MatchEnd => "Maç Bitti!",
            _ => ""
        };
    }
}
