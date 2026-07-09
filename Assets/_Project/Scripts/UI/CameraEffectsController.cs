// STATUE PANIC! - Kamera Efektleri Kontrolcüsü
// "YANLIŞ HEYKEL!" shake + "GÖRÜLÜYORSUN!" vinyet + yakalama reveal zoom.
// Player prefab'ındaki CinemachineCamera ile aynı objeye eklenir (sadece owner için aktif).
// HudEvents olaylarını dinler; ağ bağlantısı yoktur.

using System.Collections;
using UnityEngine;
using Unity.Cinemachine;

namespace StatuePanic.UI
{
    [RequireComponent(typeof(CinemachineCamera))]
    public class CameraEffectsController : MonoBehaviour
    {
        [Header("Shake (Cinemachine Impulse)")]
        [SerializeField] private CinemachineImpulseSource impulseSource;
        [SerializeField] private float wrongTouchShakeForce = 1.5f;

        [Header("Reveal Zoom")]
        [SerializeField] private float revealFovNarrow = 30f;   // zoom-in
        [SerializeField] private float revealFovNormal = 60f;   // normal
        [SerializeField] private float revealDuration = 1.5f;

        [Header("HUD Overlay")]
        [SerializeField] private GameObject wrongTouchOverlay;  // "YANLIŞ HEYKEL!" paneli
        [SerializeField] private float overlayDuration = 2f;

        private CinemachineCamera _vcam;
        private Coroutine _revealRoutine;
        private Coroutine _overlayRoutine;

        private void Awake() => _vcam = GetComponent<CinemachineCamera>();

        private void OnEnable()
        {
            HudEvents.WrongTouchOccurred += OnWrongTouch;
            HudEvents.HiderCaughtReveal += OnReveal;
        }

        private void OnDisable()
        {
            HudEvents.WrongTouchOccurred -= OnWrongTouch;
            HudEvents.HiderCaughtReveal -= OnReveal;
        }

        // ── YANLIŞ HEYKEL! ──────────────────────────────────────

        private void OnWrongTouch()
        {
            // Cinemachine Impulse ile kamera sallantısı
            if (impulseSource != null)
                impulseSource.GenerateImpulse(wrongTouchShakeForce);

            // "YANLIŞ HEYKEL!" overlay
            if (_overlayRoutine != null) StopCoroutine(_overlayRoutine);
            _overlayRoutine = StartCoroutine(ShowOverlay(wrongTouchOverlay, overlayDuration));
        }

        private IEnumerator ShowOverlay(GameObject overlay, float duration)
        {
            if (overlay == null) yield break;
            overlay.SetActive(true);
            yield return new WaitForSeconds(duration);
            overlay.SetActive(false);
        }

        // ── YAKALAMA REVEAL ──────────────────────────────────────

        private void OnReveal(Vector3 hiderWorldPos)
        {
            if (_revealRoutine != null) StopCoroutine(_revealRoutine);
            _revealRoutine = StartCoroutine(RevealZoom(hiderWorldPos));
        }

        private IEnumerator RevealZoom(Vector3 targetPos)
        {
            if (_vcam == null) yield break;

            // Kamerayı hedef yönüne çevir (heykel tarafına bak)
            var lookAt = _vcam.LookAt;
            var originalLookAt = lookAt;

            // Geçici bir hedef noktası oluştur
            var tempTarget = new GameObject("RevealTarget").transform;
            tempTarget.position = targetPos;
            _vcam.LookAt = tempTarget;

            float elapsed = 0f;
            float halfDuration = revealDuration * 0.5f;
            float startFov = _vcam.Lens.FieldOfView;

            // Zoom in
            while (elapsed < halfDuration)
            {
                elapsed += Time.deltaTime;
                float t = elapsed / halfDuration;
                _vcam.Lens.FieldOfView = Mathf.Lerp(startFov, revealFovNarrow, t);
                yield return null;
            }

            yield return new WaitForSeconds(0.3f);

            // Zoom out
            elapsed = 0f;
            while (elapsed < halfDuration)
            {
                elapsed += Time.deltaTime;
                float t = elapsed / halfDuration;
                _vcam.Lens.FieldOfView = Mathf.Lerp(revealFovNarrow, revealFovNormal, t);
                yield return null;
            }

            _vcam.Lens.FieldOfView = revealFovNormal;
            _vcam.LookAt = originalLookAt;
            Destroy(tempTarget.gameObject);
        }
    }
}
