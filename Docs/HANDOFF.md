# STATUE PANIC! — CLAUDE CODE HANDOFF DOKÜMANI

> Bu paketteki her şey **Faz 0 + Faz 1'in kod temelidir** (bkz. STATUE_PANIC_SPEC.md).
> Aşağıdaki adımları sırayla uygula. Kodda `TODO(ClaudeCode)` etiketli noktalar senin işlerin.

## PAKETİN İÇİNDE NE VAR (hazır)

| Dosya | Ne yapıyor |
|---|---|
| `Scripts/Core/GameEnums.cs` | Tüm enum'lar + oyun sabitleri (tuning değerleri tek yerde) |
| `Scripts/Core/MatchManager.cs` | Host-otoriter maç durum makinesi: 5 turluk döngü, rol rotasyonu |
| `Scripts/Networking/ServicesBootstrap.cs` | UGS init + anonim auth |
| `Scripts/Networking/SessionManager.cs` | Relay + Lobby: oda kur / 6 haneli kodla katıl / public lobi listesi / heartbeat |
| `Scripts/Player/PlayerIdentity.cs` | Rol, durum, exposure, dokunma hakkı, skor NetworkVariable'ları |
| `Scripts/Player/PlayerController.cs` | PC+mobil hareket, host hız doğrulaması (anti-cheat) |
| `Scripts/Modes/Statue/VisionConeSystem.cs` | **Weeping Angels çekirdeği**: host-otoriter FOV+raycast, heykel kimliği client'a sızmaz |
| `Scripts/Modes/Statue/PetrifyController.cs` | Don/çöz, grace penceresi, exposure cezası, shader sürücüsü |
| `Scripts/Modes/Statue/SeekerTouch.cs` | Dokunma bütçesi, host menzil doğrulaması, NPC utanç cezası |
| `Scripts/Modes/Statue/NpcStatue.cs` | Tuzak heykeller + prosedürel kafa sallama fallback'i |
| `Scripts/Modes/Statue/ScoreSystem.cs` | Risk=ödül puanlaması, tur sonu bonusları |
| `Scripts/Modes/Statue/TauntSystem.cs` | Islık + 10 sn hayatta kalma bonusu |
| `Scripts/Modes/Statue/PoseController.cs` | Poz senkronu (preset v1 + serbest IK için PoseData hazır) |
| `Scripts/Modes/Statue/PosePresetLibrary.cs` | ScriptableObject, 8 poz kodda tanımlı (Düşünen Adam, Dab, T-Poz...) |
| `Scripts/UI/*` | LobbyUI, GameHud, MobileJoystick, HudEvents köprüsü |
| `Shaders/Petrify.shader` | URP taşlaşma shader'ı (_PetrifyAmount + _Exposure sızma efekti) |
| `Packages/manifest-additions.json` | Gerekli paket listesi |

## SENİN YAPACAKLARIN (sırayla)

### Adım 1 — Proje kurulumu
1. Unity Hub'dan **Unity 6 LTS** ile **URP (3D Universal)** template projesi oluştur: `StatuePanic`.
2. `Assets/_Project` klasörünü bu paketten projenin Assets'ine kopyala.
3. `Packages/manifest-additions.json` içindeki paketleri projenin `Packages/manifest.json`'ına ekle; Unity'nin paketleri çözmesini bekle.
4. Unity Dashboard'da proje oluştur, **Project Settings > Services**'ten bağla (Relay, Lobby, Authentication, Vivox, Leaderboards, Cloud Save'i etkinleştir). ⚠️ Bu adım Aykut'un Unity hesabını gerektirir — ondan Project ID iste.

### Adım 2 — Derleme düzeltmeleri
- Kod NGO 2.x / Relay 1.x / Lobby 1.x API'lerine göre yazıldı. Kurulan paket sürümlerinde imza farkları olabilir (özellikle `RelayServerData` constructor'ı ve `Rpc` attribute'ları). **Derle, hataları API dokümanına göre düzelt** — mimariyi değiştirme.
- `RpcTarget.Single(...)` kullanımı NGO 2.x gerektirir; eski sürümdeyse `ClientRpcParams`'a çevir.

### Adım 3 — Sahneler
1. `Boot` sahnesi: `ServicesBootstrap` + `SessionManager` + `NetworkManager` (UnityTransport ile) objeleri. NetworkManager'da PlayerPrefab'ı ata.
2. `MainMenu` sahnesi: `LobbyUI` Canvas'ı (oda kur / kodla katıl / lobi paneli).
3. `Museum_Graybox` sahnesi: ProBuilder ile müze graybox'ı (3 salon + koridorlar), 20-30 adet `NpcStatue` (capsule + küp kombinasyonları yeterli), spawn noktaları. Occlusion layer'ı oluştur (`Walls`) ve `VisionConeSystem.occlusionMask`'e ata.
4. Sahne akışı: maç başlayınca host `NetworkManager.SceneManager.LoadScene("Museum_Graybox")` çağırsın — `MatchManager.RequestStartMatchRpc`'ye ekle.

### Adım 4 — Player Prefab
- Capsule karakter: `CharacterController` + `NetworkObject` + `NetworkTransform`(owner authoritative) + `PlayerIdentity` + `PlayerController` + `PetrifyController` + `PoseController` + `SeekerTouch` + `TauntSystem`.
- Basit humanoid iskelet (boş Transform hiyerarşisi yeterli: Head/Spine/L_Arm/R_Arm/L_Leg/R_Leg) — `PoseController` referanslarına bağla.
- `Petrify.shader`'dan materyal oluştur, renderer'lara ata, `PetrifyController.bodyRenderers`'a bağla.
- Cinemachine 3rd person follow kamera — sadece owner'da aktif.

### Adım 5 — Input System geçişi
- `PlayerController.ReadMoveInput/ReadLookInput` eski Input Manager kullanıyor (hızlı test için). Yeni Input System action map'ine taşı: Move (WASD/sol stick), Look (mouse/sağ stick), Petrify (Space), Touch (E), Taunt (T). Mobil tarafta `MobileJoystick` köprüsü zaten hazır.

### Adım 6 — HUD prefab'ı
- `GameHud` scriptindeki SerializeField'lar için uGUI Canvas kur (mobil-öncelikli: butonlar sağ altta, başparmak erişiminde). "GÖRÜLÜYORSUN!" uyarısı: ekran kenarlarında kırmızı vinyet + titreşim (mobilde `Handheld.Vibrate`).

### Adım 7 — Kabul testi (Faz 0+1 tamam sayılır eğer:)
1. İki editör instance'ı (ParrelSync veya Multiplayer Play Mode) ile oda kur + kodla katıl çalışıyor.
2. Maç başlat → rol dağıtımı → Prep(45sn) → Hunt → tur döngüsü 5 tur akıyor.
3. Heykel donuyor, arayan görüş konisine girince "GÖRÜLÜYORSUN" çıkıyor, görülürken hareket = renklenme.
4. Dokunma: oyuncuya = yakalama, NPC'ye = hak kaybı + kafa sallama.
5. Skor HUD'da işliyor, tüm heykeller yakalanınca tur erken bitiyor.

### Sonraki fazlar (bu pakette YOK, spec'te detaylı)
- Poz Galerisi ekranı + oylama, serbest IK poz editörü (PoseData yapısı hazır)
- Leaderboards/CloudSave entegrasyonu, kozmetik sistemi
- Steamworks.NET, mobil build pipeline, Vivox (Echo modu)

## TUNING NOTLARI (playtest'te oyna)
- `GameConstants` içindeki tüm değerler tek dosyada — FOV 70°, mesafe 25m, grace 0.3sn başlangıç değerleridir.
- `PetrifyController.ServerTickExposure` içindeki 50x çarpan kasıtlı olarak serttir; ilk playtest'te hissiyata göre ayarla.
- `VisionConeSystem.tickRate = 10` mobil host için; PC-only lobide 20'ye çıkarılabilir.

## MİMARİ KURALLAR (değiştirme)
1. **Host otoritesi:** Rol, durum, skor, menzil, görüş hesabı SADECE host'ta yazılır/hesaplanır.
2. **Bilgi sızdırmama:** Heykel oyuncularının kimliği/durumu arayan client'larına gönderilmez.
3. **Tuning tek yerde:** Yeni sabitleri `GameConstants`'a ekle, magic number bırakma.
4. **UI ↔ Network gevşek bağlantı:** UI, network'e `HudEvents` ve public Owner* metodları üzerinden dokunur.
