// STATUE PANIC! - Unity Gaming Services bootstrap
// UGS init + anonim auth. İlk sahnede tek bir GameObject'e ekle (DontDestroyOnLoad).
// Faz 2'de Steam / Apple / Google sign-in buraya bağlanacak (bkz. Docs/HANDOFF.md).

using System;
using System.Threading.Tasks;
using Unity.Services.Authentication;
using Unity.Services.Core;
using UnityEngine;

namespace StatuePanic.Networking
{
    public class ServicesBootstrap : MonoBehaviour
    {
        public static ServicesBootstrap Instance { get; private set; }
        public bool IsReady { get; private set; }
        public string PlayerId => AuthenticationService.Instance?.PlayerId;

        public event Action OnServicesReady;

        private async void Awake()
        {
            if (Instance != null) { Destroy(gameObject); return; }
            Instance = this;
            DontDestroyOnLoad(gameObject);
            await InitializeAsync();
        }

        public async Task InitializeAsync()
        {
            if (IsReady) return;
            try
            {
                if (UnityServices.State != ServicesInitializationState.Initialized)
                    await UnityServices.InitializeAsync();

                if (!AuthenticationService.Instance.IsSignedIn)
                    await AuthenticationService.Instance.SignInAnonymouslyAsync();

                IsReady = true;
                Debug.Log($"[Services] Hazır. PlayerId: {PlayerId}");
                OnServicesReady?.Invoke();
            }
            catch (Exception e)
            {
                Debug.LogError($"[Services] Başlatma hatası: {e.Message}");
                // UI katmanı bu durumu yakalayıp "çevrimdışı / tekrar dene" göstermeli.
            }
        }
    }
}
