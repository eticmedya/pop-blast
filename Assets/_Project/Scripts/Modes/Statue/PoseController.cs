// STATUE PANIC! - Poz Sistemi v1 (preset tabanlı)
// Faz 1: 20 hazır poz, ağda sadece poz index'i senkronlanır (ultra hafif).
// Faz 1.5 (Claude Code): serbest IK editörü — eklem offset'leri PoseData struct'ı ile
// senkronlanacak (yapı hazır, aşağıda).

using Unity.Netcode;
using UnityEngine;
using StatuePanic.Core;
using StatuePanic.Player;

namespace StatuePanic.Modes.Statue
{
    /// <summary>Serbest poz için eklem offset paketi (Faz 1.5). INetworkSerializable = tek RPC'de gider.</summary>
    public struct PoseData : INetworkSerializable
    {
        public byte PresetIndex;          // 255 = özel poz
        public Vector3 HeadEuler;
        public Vector3 SpineEuler;
        public Vector3 LeftArmEuler, RightArmEuler;
        public Vector3 LeftLegEuler, RightLegEuler;

        public void NetworkSerialize<T>(BufferSerializer<T> serializer) where T : IReaderWriter
        {
            serializer.SerializeValue(ref PresetIndex);
            serializer.SerializeValue(ref HeadEuler);
            serializer.SerializeValue(ref SpineEuler);
            serializer.SerializeValue(ref LeftArmEuler);
            serializer.SerializeValue(ref RightArmEuler);
            serializer.SerializeValue(ref LeftLegEuler);
            serializer.SerializeValue(ref RightLegEuler);
        }
    }

    [RequireComponent(typeof(PlayerIdentity))]
    public class PoseController : NetworkBehaviour
    {
        [Header("İskelet referansları (humanoid rig)")]
        [SerializeField] private Transform head;
        [SerializeField] private Transform spine;
        [SerializeField] private Transform leftArm, rightArm;
        [SerializeField] private Transform leftLeg, rightLeg;

        [SerializeField] private PosePresetLibrary presetLibrary; // ScriptableObject (Data/)

        public NetworkVariable<PoseData> CurrentPose = new(
            new PoseData { PresetIndex = 0 },
            writePerm: NetworkVariableWritePermission.Owner);

        private PlayerIdentity _identity;

        private void Awake() => _identity = GetComponent<PlayerIdentity>();

        public override void OnNetworkSpawn()
        {
            CurrentPose.OnValueChanged += (_, newPose) => ApplyPose(newPose);
            ApplyPose(CurrentPose.Value);
        }

        /// <summary>Poz editörü UI'ı çağırır (owner). Preparation ve Hunt fazlarında serbest
        /// (Meccha dersi: avlanma sırasında da boyamaya/poza devam edebilmek oyunu derinleştiriyor).</summary>
        public void OwnerSetPreset(byte presetIndex)
        {
            if (!IsOwner || !_identity.IsHider) return;
            var pose = presetLibrary != null ? presetLibrary.GetPose(presetIndex)
                                             : new PoseData { PresetIndex = presetIndex };
            pose.PresetIndex = presetIndex;
            CurrentPose.Value = pose;
        }

        /// <summary>Faz 1.5 serbest IK editörü bu metodu kullanacak.</summary>
        public void OwnerSetCustomPose(PoseData pose)
        {
            if (!IsOwner || !_identity.IsHider) return;
            pose.PresetIndex = 255;
            CurrentPose.Value = pose;
        }

        private void ApplyPose(PoseData pose)
        {
            // Sadece taşlaşınca poz kilitlenir; animator'ün üstüne LateUpdate'te yazılır.
            _applied = pose;
            _hasPose = true;
        }

        private PoseData _applied;
        private bool _hasPose;

        private void LateUpdate()
        {
            if (!_hasPose || _identity.State.Value != HiderState.Petrified) return;
            Set(head, _applied.HeadEuler);
            Set(spine, _applied.SpineEuler);
            Set(leftArm, _applied.LeftArmEuler);
            Set(rightArm, _applied.RightArmEuler);
            Set(leftLeg, _applied.LeftLegEuler);
            Set(rightLeg, _applied.RightLegEuler);
        }

        private static void Set(Transform t, Vector3 euler)
        {
            if (t != null) t.localRotation = Quaternion.Euler(euler);
        }
    }
}
