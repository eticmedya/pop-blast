// STATUE PANIC! - Editor Kurulum Yardımcısı
// Menü: StatuePanic > Setup > ...
// HANDOFF.md Adım 3 (sahneler) ve Adım 6 (HUD) için hızlı kurulum menüleri.
// Bu script sadece Editor'da derlenir, dağıtılan build'e girmez.

#if UNITY_EDITOR
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace StatuePanic.Editor
{
    public static class StatuePanicSetup
    {
        // ── Adım 3: Boot sahnesi ────────────────────────────────

        [MenuItem("StatuePanic/Setup/1 - Boot Sahnesi Oluştur")]
        public static void CreateBootScene()
        {
            var scene = EditorSceneManager.NewScene(NewSceneSetup.EmptyScene, NewSceneMode.Single);

            // Temel objeler
            CreateGO("ServicesBootstrap",
                typeof(Networking.ServicesBootstrap));

            CreateGO("SessionManager",
                typeof(Networking.SessionManager));

            var nmGO = CreateGO("NetworkManager",
                typeof(Unity.Netcode.NetworkManager),
                typeof(Unity.Netcode.Transports.UTP.UnityTransport));

            Debug.Log("[Setup] Boot sahnesi oluşturuldu. " +
                "NetworkManager'a PlayerPrefab'ı ve SceneList'i manuel ata.");

            SaveScene(scene, "Assets/_Project/Scenes/Boot.unity");
        }

        // ── Adım 3: MainMenu sahnesi ────────────────────────────

        [MenuItem("StatuePanic/Setup/2 - MainMenu Sahnesi Oluştur")]
        public static void CreateMainMenuScene()
        {
            var scene = EditorSceneManager.NewScene(NewSceneSetup.DefaultGameObjects, NewSceneMode.Single);

            var canvasGO = new GameObject("LobbyCanvas");
            canvasGO.AddComponent<UnityEngine.Canvas>().renderMode = RenderMode.ScreenSpaceOverlay;
            canvasGO.AddComponent<UnityEngine.UI.CanvasScaler>();
            canvasGO.AddComponent<UnityEngine.UI.GraphicRaycaster>();
            canvasGO.AddComponent<StatuePanic.UI.LobbyUI>();

            Debug.Log("[Setup] MainMenu sahnesi oluşturuldu. " +
                "LobbyUI Canvas bileşenlerine TMP alanları ekle.");

            SaveScene(scene, "Assets/_Project/Scenes/MainMenu.unity");
        }

        // ── Adım 3: Museum_Graybox sahnesi ────────────────────

        [MenuItem("StatuePanic/Setup/3 - Museum_Graybox Sahnesi Oluştur")]
        public static void CreateMuseumScene()
        {
            var scene = EditorSceneManager.NewScene(NewSceneSetup.DefaultGameObjects, NewSceneMode.Single);

            // Zemin
            var floor = GameObject.CreatePrimitive(PrimitiveType.Plane);
            floor.name = "Floor";
            floor.transform.localScale = new Vector3(5f, 1f, 10f);
            SetLayerRecursive(floor, LayerMask.NameToLayer("Default"));

            // Duvar örnekleri (Walls layer'ı oluştur: Layer 8 önerisi)
            for (int i = 0; i < 4; i++)
            {
                var wall = GameObject.CreatePrimitive(PrimitiveType.Cube);
                wall.name = $"Wall_{i}";
                wall.layer = 8; // "Walls" layer — VisionConeSystem.occlusionMask'e ata
                float angle = i * 90f;
                wall.transform.position = new Vector3(
                    Mathf.Sin(angle * Mathf.Deg2Rad) * 20f, 2f,
                    Mathf.Cos(angle * Mathf.Deg2Rad) * 20f);
                wall.transform.localScale = new Vector3(40f, 4f, 0.5f);
                wall.transform.eulerAngles = new Vector3(0f, angle, 0f);
            }

            // 5 örnek NPC heykel (capsule + küp)
            for (int i = 0; i < 5; i++)
            {
                var npc = GameObject.CreatePrimitive(PrimitiveType.Capsule);
                npc.name = $"NpcStatue_{i}";
                npc.AddComponent<StatuePanic.Modes.Statue.NpcStatue>();
                npc.transform.position = new Vector3((i - 2) * 4f, 1f, 5f);
            }

            // Spawn noktaları
            for (int i = 0; i < 10; i++)
            {
                var spawn = new GameObject($"SpawnPoint_{i}");
                float angle = i * 36f * Mathf.Deg2Rad;
                spawn.transform.position = new Vector3(
                    Mathf.Sin(angle) * 12f, 0.5f, Mathf.Cos(angle) * 12f);
            }

            // MatchManager + sistem objeleri
            var systems = CreateGO("GameSystems",
                typeof(Core.MatchManager),
                typeof(Modes.Statue.VisionConeSystem),
                typeof(Modes.Statue.ScoreSystem));

            var netObj = systems.AddComponent<Unity.Netcode.NetworkObject>();

            Debug.Log("[Setup] Museum_Graybox sahnesi oluşturuldu. " +
                "VisionConeSystem.occlusionMask'e 'Walls' layer'ını ata. " +
                "ProBuilder ile 3 salon + koridor ekle (isteğe bağlı).");

            SaveScene(scene, "Assets/_Project/Scenes/Museum_Graybox.unity");
        }

        // ── Adım 4 / 6: GameHUD kurulum ipucu ─────────────────

        [MenuItem("StatuePanic/Setup/4 - HUD Canvas Kurulum Notları")]
        public static void ShowHudSetupNotes()
        {
            EditorUtility.DisplayDialog(
                "GameHUD Kurulum",
                "GameHud.cs için uGUI Canvas:\n\n" +
                "1. Hiyerarşide Canvas > CanvasScaler (Screen Space - Overlay, 1080p referans) oluştur.\n" +
                "2. Canvas'a GameHud scripti ekle.\n" +
                "3. PhaseLabel, TimerLabel, ScoreLabel: TMP Text objeler.\n" +
                "4. HiderPanel (alt): PetrifyButton, TauntButton, PoseButton butonları.\n" +
                "5. ObservedWarning: kırmızı yarı saydam tam ekran Image + 'GÖRÜLÜYORSUN!' TMP metni.\n" +
                "6. SeekerPanel (alt): TouchButton, TouchBudgetLabel.\n" +
                "7. WrongTouchOverlay: turuncu panel + 'YANLIŞ HEYKEL! ❌' TMP metni (başlangıçta kapalı).\n" +
                "8. CameraEffectsController scriptini owner'ın CinemachineCamera objesi üzerine ekle.\n" +
                "   CinemachineImpulseSource bileşenini de aynı objeye ekle.\n" +
                "9. MobileJoystick (Android/iOS): sol alt köşeye Move joystick, sağ yarıya Look alanı.",
                "Anladım");
        }

        // ── Yardımcı ────────────────────────────────────────────

        private static GameObject CreateGO(string name, params System.Type[] components)
        {
            var go = new GameObject(name);
            foreach (var t in components) go.AddComponent(t);
            return go;
        }

        private static void SetLayerRecursive(GameObject go, int layer)
        {
            go.layer = layer;
            foreach (Transform child in go.transform) SetLayerRecursive(child.gameObject, layer);
        }

        private static void SaveScene(Scene scene, string path)
        {
            System.IO.Directory.CreateDirectory(
                System.IO.Path.GetDirectoryName(path));
            EditorSceneManager.SaveScene(scene, path);
            AssetDatabase.Refresh();
            Debug.Log($"[Setup] Sahne kaydedildi: {path}");
        }
    }
}
#endif
