// STATUE PANIC! - Anti-cheat ihlal sayacı
// Her hız ihlalini sayar; MaxViolations aşılınca kick sinyali verir.
// PlayerController ile aynı prefab'da durur.

using UnityEngine;

namespace StatuePanic.Player
{
    public class ViolationTracker : MonoBehaviour
    {
        [SerializeField] private int maxViolations = 5;
        [SerializeField] private float decayInterval = 30f; // Bu süre geçince sayaç sıfırlanır

        private int _count;
        private float _decayTimer;

        private void Update()
        {
            if (_count <= 0) return;
            _decayTimer += Time.deltaTime;
            if (_decayTimer >= decayInterval)
            {
                _count = 0;
                _decayTimer = 0f;
            }
        }

        /// <summary>Host: ihlali kaydeder. True döndürürse kick eşiği aşıldı.</summary>
        public bool RecordAndCheck()
        {
            _count++;
            _decayTimer = 0f;
            return _count >= maxViolations;
        }
    }
}
