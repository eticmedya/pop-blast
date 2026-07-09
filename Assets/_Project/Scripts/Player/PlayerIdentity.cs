// STATUE PANIC! - Oyuncu kimliği ve tur içi durumu
// Player prefab'ının kökünde durur. Rol/durum sadece host tarafından yazılır.

using Unity.Collections;
using Unity.Netcode;
using StatuePanic.Core;

namespace StatuePanic.Player
{
    public class PlayerIdentity : NetworkBehaviour
    {
        public NetworkVariable<FixedString32Bytes> DisplayName =
            new(writePerm: NetworkVariableWritePermission.Owner);

        public NetworkVariable<PlayerRole> Role = new(PlayerRole.None);
        public NetworkVariable<HiderState> State = new(HiderState.Free);

        // Görülürken hareket cezası: 0 = tam taş, 1 = tamamen renklenmiş (ele verilmiş)
        public NetworkVariable<float> Exposure = new(0f);

        // Arayan için kalan dokunma hakkı
        public NetworkVariable<int> TouchBudget = new(GameConstants.TouchBudgetPerSeeker);

        // Bu tur toplanan puan (skor tablosu HUD'u için)
        public NetworkVariable<int> RoundScore = new(0);
        public NetworkVariable<int> MatchScore = new(0);

        public bool IsSeeker => Role.Value == PlayerRole.Seeker;
        public bool IsHider => Role.Value == PlayerRole.Hider;
        public bool IsAliveHider => IsHider && State.Value != HiderState.Caught;

        public override void OnNetworkSpawn()
        {
            if (IsOwner && DisplayName.Value.IsEmpty)
                DisplayName.Value = $"Oyuncu{OwnerClientId}";
        }

        /// <summary>Host: yeni tur başında durumu sıfırlar.</summary>
        public void ResetForRound()
        {
            if (!IsServer) return;
            State.Value = HiderState.Free;
            Exposure.Value = 0f;
            TouchBudget.Value = GameConstants.TouchBudgetPerSeeker;
            RoundScore.Value = 0;
        }

        /// <summary>Host: puan ekler (negatif olabilir).</summary>
        public void AddScore(int amount)
        {
            if (!IsServer) return;
            RoundScore.Value += amount;
            MatchScore.Value += amount;
        }
    }
}
