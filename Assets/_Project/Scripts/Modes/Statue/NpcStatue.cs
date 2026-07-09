// STATUE PANIC! - Gerçek (NPC) heykel
// Haritadaki tuzak heykeller. Yanlış dokunmada "utanç animasyonu" oynar (klip anı).
// Statik obje olduğu için NetworkObject GEREKMEZ — sahne başında deterministik ID alır.

using System.Collections.Generic;
using UnityEngine;

namespace StatuePanic.Modes.Statue
{
    public class NpcStatue : MonoBehaviour
    {
        private static readonly Dictionary<int, NpcStatue> Registry = new();

        [SerializeField] private Animator animator; // "Shame" trigger'lı animator (opsiyonel)
        public int StatueId { get; private set; }

        private void OnEnable()
        {
            // Deterministik ID: sahnedeki pozisyona göre hash (host & client aynı sonucu üretir)
            StatueId = Mathf.Abs(transform.position.GetHashCode() ^ name.GetHashCode());
            Registry[StatueId] = this;
        }

        private void OnDisable() => Registry.Remove(StatueId);

        public static NpcStatue Find(int id) => Registry.TryGetValue(id, out var s) ? s : null;

        public void PlayShameAnimation()
        {
            if (animator != null) animator.SetTrigger("Shame");
            else StartCoroutine(FallbackHeadShake());
        }

        // Animator yoksa basit prosedürel kafa sallama (graybox aşaması için yeterli)
        private System.Collections.IEnumerator FallbackHeadShake()
        {
            Quaternion start = transform.rotation;
            for (float t = 0; t < 1.2f; t += Time.deltaTime)
            {
                transform.rotation = start * Quaternion.Euler(0f, Mathf.Sin(t * 25f) * 8f, 0f);
                yield return null;
            }
            transform.rotation = start;
        }
    }
}
