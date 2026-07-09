// STATUE PANIC! - Mobil sanal joystick (sol: hareket, sağ yarı ekran: bakış)
// PlayerController.MobileMove / MobileLook statik değerlerini besler.
// Basit ama iş gören Faz 1 sürümü; Faz 2'de Input System On-Screen Controls'a taşınabilir.

using UnityEngine;
using UnityEngine.EventSystems;
using StatuePanic.Player;

namespace StatuePanic.UI
{
    public class MobileJoystick : MonoBehaviour, IDragHandler, IPointerDownHandler, IPointerUpHandler
    {
        public enum Kind { Move, Look }
        [SerializeField] private Kind kind = Kind.Move;
        [SerializeField] private RectTransform handle;
        [SerializeField] private float radius = 90f;
        [SerializeField] private float lookSensitivity = 0.12f;

        private Vector2 _startPos;
        private Vector2 _lastDrag;

        public void OnPointerDown(PointerEventData e)
        {
            _startPos = e.position;
            _lastDrag = e.position;
        }

        public void OnDrag(PointerEventData e)
        {
            if (kind == Kind.Move)
            {
                Vector2 delta = Vector2.ClampMagnitude(e.position - _startPos, radius);
                if (handle != null) handle.anchoredPosition = delta;
                PlayerController.MobileMove = delta / radius;
            }
            else
            {
                Vector2 frameDelta = e.position - _lastDrag;
                _lastDrag = e.position;
                PlayerController.MobileLook = frameDelta * lookSensitivity;
            }
        }

        public void OnPointerUp(PointerEventData e)
        {
            if (handle != null) handle.anchoredPosition = Vector2.zero;
            if (kind == Kind.Move) PlayerController.MobileMove = Vector2.zero;
            else PlayerController.MobileLook = Vector2.zero;
        }

        private void LateUpdate()
        {
            // Look joystick'i sürükleme yokken sıfırlanır (delta tabanlı)
            if (kind == Kind.Look) PlayerController.MobileLook = Vector2.zero;
        }
    }
}
