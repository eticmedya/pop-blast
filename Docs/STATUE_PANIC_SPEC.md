# STATUE PANIC! (MÜTHİŞ HEYKEL) — Detaylı Proje Prompt'u / Teknik Spesifikasyon

> Bu dosyayı Claude Code'a doğrudan verebilirsin. Proje: Steam (PC) + iOS/Android cross-play destekli, 3 modlu online parti oyunu.

---

## 1. OYUN ÖZETİ

**İsim:** STATUE PANIC! (TR pazarlama adı: Müthiş Heykel)
**Tür:** Online asimetrik parti oyunu (hide & seek + sosyal aldatmaca)
**Oyuncu sayısı:** 4–10 (2–16 teknik destek, 4–10 önerilen)
**Platformlar:** Steam (Windows), iOS, Android — tam cross-play
**Fiyat modeli:** Steam $5.99 premium / Mobil free-to-play (kozmetik IAP + ödüllü reklam)
**Referans oyunlar:** Meccha Chameleon (saklanma yaratıcılığı), Scam Line (sosyal aldatmaca), Among Us (cross-play F2P/premium hibrit modeli)
**Sanat yönü:** Low-poly, pastel renkli, "cozy ama gerilimli" müze/restoran ortamları. Karakterler yumuşak hatlı, komik oranlı (büyük kafa, kısa bacak) — klip'lenebilirlik için abartılı animasyonlar.

**Tek cümlelik pitch:** "Heykel gibi don, ses gibi saklan, garson gibi yalan söyle — arkadaşlarını kandırabilen kazanır."

---

## 2. TEKNOLOJİ YIĞINI (ZORUNLU KARARLAR)

| Katman | Seçim | Gerekçe |
|---|---|---|
| Engine | **Unity 6 (LTS)** | Tek codebase'den Steam + iOS + Android export, olgun mobil pipeline |
| Netcode | **Netcode for GameObjects (NGO)** | Unity resmi, 10 oyunculu oda ölçeği için yeterli |
| Relay/NAT | **Unity Relay** | Host migration olmadan P2P sorunlarını çözer, cross-play'i basitleştirir |
| Lobby | **Unity Lobby Service** | Oda kodu ile arkadaş daveti + public lobi listesi |
| Auth | **Unity Authentication** | Anonim + Steam + Apple/Google Sign-In birleşik hesap |
| Sesli sohbet | **Vivox (UGS)** | Mod 2 (Echo) için pozisyonel ses ZORUNLU; ayrıca yakınlık tabanlı voice chat |
| Leaderboard | **UGS Leaderboards + Cloud Save** | Cross-platform sıralama |
| Steam entegrasyonu | **Steamworks.NET** | Achievements, Rich Presence, arkadaş daveti overlay |
| Mobil IAP | **Unity IAP** | Kozmetik satışı |
| Mobil reklam | **AdMob (ödüllü reklam)** | Aykut'un mevcut AdMob deneyimiyle uyumlu |
| Analitik | **Unity Analytics** | Funnel + mod popülerliği ölçümü |

**Kritik mimari kural:** Sunucu otoritesi host'ta (listen-server + Relay). Bakış açısı kontrolü (Mod 1) ve vurma/dokunma doğrulaması HOST tarafında yapılır — Meccha Chameleon'un yaşadığı aimbot/wallhack sorununa karşı temel önlem. Pozisyon ve "kim kime bakıyor" verisi client'a minimum gönderilir (görünmeyen heykel oyuncularının kimliği client'a hiç gitmez, sadece pozisyon + poz verisi gider).

---

## 3. MOD 1 — HEYKEL (STATUE) 🗿 [LANSMANIN YILDIZI]

### Konsept
Müze haritasında Saklananlar kendini gri taş dokulu heykele dönüştürür ve gerçek (NPC) heykellerin arasına karışır. Arayanlar müzeyi gezerek sahte heykelleri bulmaya çalışır.

### Roller
- **Arayan (Seeker):** 1–3 kişi (oyuncu sayısına göre otomatik). El feneri + sınırlı "dokunma hakkı" var.
- **Heykel (Hider):** Kalan herkes.

### Tur akışı
1. **Hazırlık (45 sn):** Heykeller haritada yer seçer ve POZ EDİTÖRÜ ile pozunu ayarlar. Arayanlar karanlık lobide bekler, harita önizlemesi GÖREMEZ.
2. **Avlanma (4 dk):** Arayanlar müzeye girer. Heykeller taş dokusuna bürünür ve donar.
3. **Weeping Angels mekaniği:** Bir heykel, HİÇBİR arayanın görüş konisinde (FOV ~70°, mesafe ~25m, raycast ile duvar arkası hariç) değilse hareket edebilir. Görüş konisine girdiği anda 0.3 sn içinde donmazsa vücudu %2/sn hızla renklenir (taş → gerçek renk) = görsel ele verme. Ekranda "GÖRÜLÜYORSUN" uyarısı çıkar (sadece kendine).
4. **Dokunma hakkı:** Arayan başına 5 dokunma. Sahte heykele dokunma = yakalama (+puan). Gerçek NPC heykele dokunma = 1 hak kaybı + 5 sn "utanç" stun animasyonu (heykel arayana kafa sallar — klip anı).
5. **Tur sonu:** Süre bitince hayatta kalan heykeller kazanır; tüm heykeller yakalanırsa arayanlar kazanır. Roller rotasyonla değişir, maç = 5 tur.

### Poz Editörü (oyunun viral kalbi)
- 12 eklem noktalı basit IK sistemi: kollar, bacaklar, kafa, gövde eğimi.
- **PC:** Mouse ile eklem sürükle. **Mobil:** Dokunmatik sürükle + hazır poz kütüphanesi (20 preset: Düşünen Adam, Diskobol, dab, T-pose, tavuk dansı...).
- Pozlar tur sonunda "Poz Galerisi" ekranında herkese gösterilir + en komik poz oylaması (+bonus puan). Bu ekran ekran görüntüsü paylaşımı için tasarlanır (oyun logosu + otomatik watermark).

### Puanlama (Meccha'nın dahiyane "görünür ol" mekaniği uyarlanmış)
- Arayanın görüş konisinde geçirilen her saniye: +2 puan (risk = ödül; köşeye saklanmak puan kazandırmaz)
- "Taunt" (ıslık/heykel gıcırtısı sesi çıkarma): arayan 10 sn içinde seni bulamazsa +50
- Hayatta kalma bonusu: +100
- Yakalama (arayan): +75/heykel, yanlış dokunma: −25

### Haritalar (lansman: 3)
1. **Sanat Müzesi:** Klasik heykeller, sütunlar, geniş salonlar.
2. **Balmumu Müzesi:** İnsan formunda NPC'ler → en zor/en komik harita.
3. **Heykel Bahçesi:** Açık hava, gün batımı ışığı, çeşmeler.

---

## 4. MOD 2 — ECHO (SES TAKLİDİ) 🔊

### Konsept
Saklananlar %90 şeffaf (hayalet). Arayanlar onları GÖREREK değil DUYARAK bulur. Twist: saklananlar her 15 saniyede bir "ses görevi" yapmak ZORUNDA.

### Mekanik
- **Ses görevi:** Her 15 sn'de oyuncuya rastgele ortam sesi kartı gelir: "kapı gıcırtısı", "kuş", "damla", "rüzgar", "tahta çıtırtısı". Oyuncu MİKROFONLA bu sesi taklit eder. Ses, Vivox pozisyonel audio ile o noktadan 3D olarak yayınlanır.
- Görevi yapmazsa: konumu 3 sn boyunca haritada arayanlara işaretlenir (ceza).
- **Mikrofonsuz fallback (mobil için kritik):** Mikrofon izni yoksa "soundboard modu" — oyuncu 3 hazır ses arasından seçer ama hazır sesler hafif robotik/dijital tınlar = taklitten daha kolay ayırt edilir (mikrofon kullanmaya teşvik).
- **Arayan aracı:** "Sonar puls" (10 sn cooldown) — yakındaki sesin geldiği yönü kısa bir dalga ile gösterir.
- Haritada gerçek ortam sesleri de rastgele çalar (gerçek kapı gıcırtıları vb.) → oyuncu taklidi ile gerçek ses karışır.

### Neden viral
Yayıncı mikrofona "gıcırt gıcırt" yaparken izleyici kırılır. Tur sonunda "Ses Tekrarı" ekranı: en iyi/en kötü taklitler herkese dinletilir + oylanır.

### Teknik notlar
- Vivox positional channels + ses aktivite tespiti (VAD). Ses kaydı SAKLANMAZ, sadece tur içi replay buffer'ı (RAM, tur sonunda silinir) — KVKK/GDPR notu ayarlar ekranında.
- Küfür/istismar önlemi: replay oynatma host tarafından kapatılabilir, oyuncu bazlı mute her zaman erişilebilir.

---

## 5. MOD 3 — SAHTE GARSON (FAKE WAITER) 🍽️

### Konsept
Scam Line tarzı sosyal aldatmaca ama fiziksel mini-görevlerle: Herkes bir restoranda garson. İçlerinden biri (veya 8+ oyuncuda ikisi) SAHTEKAR — müşterileri sabote ediyor.

### Among Us'tan ayrışma noktaları (kritik!)
1. **Öldürme yok** → sabotaj var: Sahtekar sipariş tabaklarına gizlice "acı sos" ekler, müşteri yediğinde restoran puanı düşer ve komik kusma animasyonu oynar.
2. **Sürekli hareket:** Toplantı/oylama ekranı YOK. Suçlama gerçek zamanlı: bir garson diğerini "ŞİKAYET" edebilir (tepsisini yere atma animasyonu ile) → 10 sn'lik hızlı el kaldırma oylaması OYUN DURMADAN yapılır. Yanlış suçlama = suçlayan 15 sn bulaşık yıkama cezası.
3. **Beceri katmanı:** Tabak taşıma fiziği (tepsi dengesi — telefonda jiroskop/PC'de mouse dengesi). Herkes sakarlaşabildiği için sahtekarın sabotajı kazalara karışır — mükemmel şüphe sisi.

### Tur akışı
- 6 dk servis. Garsonlar sipariş alır → mutfaktan tabak taşır → doğru masaya bırakır. Restoran puanı hedefi tutarsa garsonlar kazanır.
- Sahtekar hedefi: restoran puanını sıfıra indirmek VEYA süre sonunda hedefin altında tutmak.
- Sahtekar araçları: acı sos (cooldown 30 sn), ışık söndürme, kayganlaştırıcı dökme (kayan garsonlar = klip), sipariş defterini karıştırma.

---

## 6. META SİSTEMLER (TÜM MODLAR ORTAK)

### Lobi & Arkadaş Sistemi
- **Oda kodu:** 6 haneli kod (ör. "PANIK1") — cross-platform davet. Mobilde deep link (`statuepanic://join/PANIK1`), Steam'de overlay arkadaş daveti + Rich Presence "Arkadaşının odasına katıl".
- **Public matchmaking:** Mod seçimi + bölge → hızlı eşleşme. Lobi listesi (isim, mod, harita, doluluk).
- **Lobi içi:** Karakter kozmetik önizleme, mod oylaması, hazır butonu, yakınlık tabanlı sesli sohbet.

### Sıralama & Rekabet
- **Kasual playlist:** Puan sadece kozmetik XP'ye gider.
- **Dereceli playlist (min. seviye 5):** Mod bazlı MMR (Elo benzeri, glicko-lite). Ligler: Çamur → Kil → Mermer → Bronz → Altın Heykel → GRANİT (top 500, isimli global sıralama).
- **Leaderboard'lar (UGS):** Global / arkadaşlar / haftalık; ayrıca eğlence tabloları: "En çok oylanan poz", "En iyi ses taklitçisi", "En çok yanlış heykele dokunan" (utanç tablosu — paylaşım mıknatısı).
- Sezonlar: 8 haftalık, sezon sonu kozmetik ödül + sıfırlama (soft reset).

### Progression & Kozmetik (pay-to-win YASAK)
- Karakter skinleri (heykel dokuları: mermer, altın, lego, peynir...), taunt sesleri, poz preset paketleri, tabak/tepsi skinleri, isim plakası çerçeveleri.
- Kazanım: seviye XP + haftalık görevler + sezon ödülleri + IAP.

### Monetizasyon
- **Steam ($5.99):** Tüm oyun + "Kurucu" kozmetik paketi. IAP mağazası da açık (Among Us modeli).
- **Mobil (ücretsiz):** 3 mod da açık, günde reklamsız 5 maç → sonrası maç başı 1 ödüllü reklam VEYA tek seferlik $4.99 "Reklamları Kaldır + Kurucu Paketi". Kozmetik IAP her iki platformda ortak (Cloud Save ile senkron).
- Cross-play lobilerinde platform ikonu gösterilir; mobil oyuncular için aim-assist yok (bu oyunda gerek yok, dokunma/poz mekanikleri platform-nötr).

### Güvenlik & Anti-cheat (Meccha'nın dersleri)
- Host-otoriter doğrulama: dokunma menzili, hareket hızı, görüş konisi hesapları host'ta.
- Sunucu tarafı sanity check: ışınlanma, hız hilesi, duvar içi pozisyon tespiti → otomatik kick.
- Oda içi oy ile kick (host + %50 oy), oyuncu raporlama, mute/block listesi (Cloud Save).
- Duvar içine saklanma engeli: geçerli saklanma noktaları navmesh + collision doğrulaması ile sınırlanır.

---

## 7. UI/UX PRENSİPLERİ

- **Mobil öncelikli HUD:** Tüm etkileşimler tek elle erişilebilir; sanal joystick + bağlamsal aksiyon butonu. PC'de WASD + mouse, tam gamepad desteği (Steam Deck hedefi!).
- Poz editörü her iki platformda 60 saniyede öğrenilebilir olmalı — onboarding: ilk açılışta 90 saniyelik interaktif tutorial (bot'larla mini tur).
- **Diller (lansman):** Türkçe, İngilizce, İspanyolca, Portekizce (BR), Rusça, Japonca, Korece, Çince (Basit). (Meccha ve Scam Line'ın TR dahil geniş dil desteği tesadüf değil.)
- Renk körü modu, ses altyazıları (Echo modunda "kapı gıcırtısı ↖" gibi opsiyonel görsel ipucu — dereceli modda kapalı).
- Yayıncı modu: oda kodunu gizle butonu, izleyici katılım kuyruğu (public odada "yayıncı odası" etiketi).

---

## 8. GELİŞTİRME FAZLARI (Claude Code için yol haritası)

### Faz 0 — İskelet (1. hafta)
- Unity 6 proje kurulumu, NGO + Relay + Lobby + Auth entegrasyonu.
- 2 oyuncu aynı odada birbirini görüyor (capsule karakterler), oda kodu ile katılım çalışıyor.
- Platform buildleri: Windows + Android + iOS boş build pipeline (CI: GitHub Actions + Unity Cloud Build).

### Faz 1 — Heykel MVP (2–5. hafta)
- Karakter kontrolcüsü (mobil joystick + PC WASD), müze haritası #1 (graybox).
- Poz editörü v1 (preset'ler önce, serbest IK sonra), taşlaşma shader'ı (gri doku geçişi).
- Görüş konisi sistemi (host-otoriter), donma/renklenme cezası, dokunma hakkı, puanlama, tur döngüsü.
- Poz Galerisi + oylama ekranı.
- **Bu fazın sonunda oyun arkadaşlarla test edilebilir olmalı.**

### Faz 2 — Meta + Lansman hazırlığı (6–8. hafta)
- Matchmaking, leaderboard, seviye/XP, 5 kozmetik skin, ayarlar, lokalizasyon (TR+EN).
- Sanat geçişi: graybox → final low-poly asset'ler (asset store hızlandırması serbest — Meccha felsefesi: "önce var olsun, sonra mükemmelleşsin").
- Steam sayfası + Early Access lansmanı (SADECE Heykel modu ile çık! Scam Line gibi roadmap yayınla).

### Faz 3 — Echo modu (EA güncellemesi #1)
- Vivox pozisyonel ses, ses görev sistemi, soundboard fallback, sonar, Ses Tekrarı ekranı.

### Faz 4 — Sahte Garson (EA güncellemesi #2)
- Restoran haritası, tepsi fiziği, sabotaj araçları, gerçek zamanlı şikayet/oylama.

### Faz 5 — Mobil lansman
- Steam'de topluluk oturduktan sonra iOS/Android çıkışı (cross-play günü = ikinci viral dalga fırsatı).
- AdMob + Unity IAP + Adapty benzeri abonelik YOK (kozmetik-only).

---

## 9. KLASÖR YAPISI ÖNERİSİ

```
Assets/
  _Project/
    Scripts/
      Core/            # GameManager, ModeManager, SceneFlow
      Networking/      # RelayManager, LobbyManager, NetworkPlayer
      Modes/
        Statue/        # VisionCone, PoseEditor, PetrifyShaderCtrl, TouchBudget
        Echo/          # SoundTaskSystem, VivoxPositional, SonarPulse
        Waiter/        # TrayPhysics, SabotageSystem, ComplaintVote
      Meta/            # Leaderboards, Progression, Cosmetics, IAP, Ads
      UI/              # HUD, Lobby, PoseGallery, Results
    Art/  Audio/  Prefabs/  Scenes/  Shaders/
```

---

## 10. BAŞARI KRİTERLERİ / KABUL TESTLERİ

1. 6 oyuncu (2 PC + 4 mobil karışık) tek odada 5 turluk Heykel maçını tamamlayabiliyor, desync yok.
2. Poz editöründe yeni oyuncu 60 sn içinde özgün poz oluşturabiliyor.
3. Görüş konisi hilesi client tarafından yapılamıyor (host doğrulaması test edilmiş).
4. Oda kodu ile mobil → Steam odasına katılım < 10 sn.
5. Leaderboard cross-platform senkron.
6. Android alt segment cihazda (4GB RAM) 30+ FPS, PC'de 60+ FPS.
7. Bir tur içinde en az 1 "klip anı" üretiliyor (poz galerisi, utanç stun'ı, ses tekrarı) — bu bir tasarım kriteri, her güncelleme buna göre değerlendirilir.
