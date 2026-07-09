// STATUE PANIC! - Oyuncu hareket kontrolcüsü
// Owner-authoritative hareket + HOST tarafında hız doğrulaması (anti-cheat sanity check).
// PC: WASD + mouse bakış (New Input System). Mobil: UI joystick (MobileInputBridge).
// Prefab gereksinimleri: CharacterController, NetworkObject, NetworkTransform (owner authoritative),
//   ViolationTracker, PlayerIdentity.

using Unity.Netcode;
using UnityEngine;
using StatuePanic.Core;

#if ENABLE_INPUT_SYSTEM
using UnityEngine.InputSystem;
#endif

namespace StatuePanic.Player
{
    [RequireComponent(typeof(CharacterController), typeof(PlayerIdentity), typeof(ViolationTracker))]
    public class PlayerController : NetworkBehaviour
    {
        [Header("Refs")]
        [SerializeField] private Transform cameraPivot; // Kafa hizası; Cinemachine bağlanır

        [Header("Tuning")]
        [SerializeField] private float rotationSpeed = 120f;
        [SerializeField] private float gravity = -20f;

        private CharacterController _cc;
        private PlayerIdentity _identity;
        private ViolationTracker _violations;
        private float _verticalVelocity;

        // Mobil joystick köprüsü (MobileJoystick UI scripti bu statik değerleri yazar)
        public static Vector2 MobileMove;
        public static Vector2 MobileLook;

#if ENABLE_INPUT_SYSTEM
        private StatuePanicInputActions _input;
#endif

        // Host doğrulama
        private Vector3 _lastValidatedPos;
        private float _validateTimer;
        private const float ValidateInterval = 0.5f;

        private void Awake()
        {
            _cc = GetComponent<CharacterController>();
            _identity = GetComponent<PlayerIdentity>();
            _violations = GetComponent<ViolationTracker>();

#if ENABLE_INPUT_SYSTEM
            _input = new StatuePanicInputActions();
#endif
        }

        public override void OnNetworkSpawn()
        {
            _lastValidatedPos = transform.position;

            if (IsOwner)
            {
#if ENABLE_INPUT_SYSTEM
                _input.Gameplay.Enable();
#endif
                // Cinemachine 3.x: cameraPivot'u takip eden vcam'i owner'da aktifleştir.
                // CinemachineCamera Player prefab'ında cameraPivot'un altında disabled olarak durur;
                // burada sadece owner'ı için enable edilir (diğer clientlar için pasif kalır).
                if (cameraPivot != null)
                {
                    var vcam = cameraPivot.GetComponentInChildren<Unity.Cinemachine.CinemachineCamera>(true);
                    if (vcam != null)
                    {
                        vcam.Follow = cameraPivot;
                        vcam.LookAt = cameraPivot;
                        vcam.enabled = true;
                    }
                }
            }
        }

        public override void OnNetworkDespawn()
        {
#if ENABLE_INPUT_SYSTEM
            if (IsOwner) _input?.Gameplay.Disable();
#endif
        }

        private void OnDestroy()
        {
#if ENABLE_INPUT_SYSTEM
            _input?.Dispose();
#endif
        }

        private void Update()
        {
            if (IsOwner) HandleOwnerInput();
            if (IsServer) ValidateMovement();
        }

        // ---------------- OWNER ----------------

        private void HandleOwnerInput()
        {
            if (_identity.IsHider && _identity.State.Value == HiderState.Caught) return;

            Vector2 move = ReadMoveInput();
            Vector2 look = ReadLookInput();

            transform.Rotate(0f, look.x * rotationSpeed * Time.deltaTime, 0f);

            Vector3 dir = transform.forward * move.y + transform.right * move.x;
            if (dir.sqrMagnitude > 1f) dir.Normalize();

            _verticalVelocity = _cc.isGrounded ? -1f : _verticalVelocity + gravity * Time.deltaTime;
            _cc.Move((dir * GameConstants.MoveSpeed + Vector3.up * _verticalVelocity) * Time.deltaTime);

            if (_identity.IsHider && dir.sqrMagnitude > 0.01f)
                GetComponent<Modes.Statue.PetrifyController>()?.NotifyOwnerMoved();
        }

        private Vector2 ReadMoveInput()
        {
#if UNITY_ANDROID || UNITY_IOS
            return MobileMove;
#elif ENABLE_INPUT_SYSTEM
            return _input.Gameplay.Move.ReadValue<Vector2>();
#else
            return new Vector2(Input.GetAxisRaw("Horizontal"), Input.GetAxisRaw("Vertical"));
#endif
        }

        private Vector2 ReadLookInput()
        {
#if UNITY_ANDROID || UNITY_IOS
            return MobileLook;
#elif ENABLE_INPUT_SYSTEM
            return _input.Gameplay.Look.ReadValue<Vector2>();
#else
            return new Vector2(Input.GetAxis("Mouse X"), Input.GetAxis("Mouse Y"));
#endif
        }

        // ---------------- HOST ANTI-CHEAT ----------------

        private void ValidateMovement()
        {
            _validateTimer += Time.deltaTime;
            if (_validateTimer < ValidateInterval) return;

            float dist = Vector3.Distance(transform.position, _lastValidatedPos);
            float maxDist = GameConstants.MaxAllowedSpeed * _validateTimer * 1.25f;

            if (dist > maxDist)
            {
                Debug.LogWarning($"[AntiCheat] Client {OwnerClientId} hız ihlali: {dist:F1}m/{_validateTimer:F1}s");
                if (IsServer && !IsOwner)
                {
                    transform.position = _lastValidatedPos;

                    // Tekrarlanan ihlal: ViolationTracker eşiği aşarsa kick.
                    if (_violations != null && _violations.RecordAndCheck())
                    {
                        Debug.LogWarning($"[AntiCheat] Client {OwnerClientId} kick ediliyor (ihlal limiti).");
                        Networking.SessionManager.Instance?.KickPlayer(OwnerClientId,
                            "Hız hilesi tespit edildi.");
                    }
                }
            }

            _lastValidatedPos = transform.position;
            _validateTimer = 0f;
        }
    }
}
