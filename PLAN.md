# Pop Blast - Uygulama Plani

## Oyun Konsepti
Match-3 grid + Bubble Shooter atisi hibrit bulmaca oyunu.
Renkli toplari kaydirarak eslestir, combo metre doldur, cannon ile ozel top firlat.

---

## Teknik Stack

| Katman | Kutuphane | Amac |
|--------|-----------|------|
| Framework | Expo SDK 52+ | Build, dev, deploy |
| Rendering | @shopify/react-native-skia | Canvas, grid, toplar, efektler |
| Animasyon | react-native-reanimated v3 | Tile hareketi, cascade, patlama |
| Dokunma | react-native-gesture-handler | Tap (match-3), Pan (cannon nisan) |
| Ses | expo-audio | Pop, match, atama ses efektleri |
| State | zustand | Oyun durumu, skor, seviye |
| Navigation | expo-router | Ekranlar arasi gecis |

---

## Ekran Yapisi

```
app/
  (tabs)/
    index.tsx          -> Ana menu (Play, Settings)
  game/
    index.tsx          -> Seviye secim ekrani
    [level].tsx        -> Oyun ekrani
  components/
    Board.tsx          -> Match-3 grid canvas
    Tile.tsx           -> Tek top/tile
    Cannon.tsx         -> Bubble shooter cannon
    ScoreBar.tsx       -> Skor + combo metre
    PowerUpBar.tsx     -> Guc-up butonlari
    LevelComplete.tsx  -> Seviye bitti modal
    GameOver.tsx       -> Oyun bitti modal
  game-engine/
    grid.ts            -> Grid veri yapisi + match algoritmasi
    matcher.ts         -> BFS ile eslestirme bulma
    gravity.ts         -> Yer cekimi / cascade
    cannon.ts          -> Top firlatma fizigi
    levels.ts          -> Seviye tanimlari (JSON)
    scoring.ts         -> Skor hesaplama
    powerups.ts        -> Guc-up tanimlari + etkileri
  stores/
    gameStore.ts       -> Zustand game state
  constants/
    colors.ts          -> Top renkleri
    dimensions.ts      -> Grid boyutlari
    levels/            -> Seviye JSON dosyalari
  assets/
    sounds/            -> Ses dosyalari
    images/            -> Gorseller
```

---

## Gelistirme Adimlari

### Adim 1: Proje Kurulumu
- Expo projesi olustur (TypeScript)
- Bagimliliklari yukle (skia, reanimated, gesture-handler, zustand, expo-audio, expo-router)
- Temel dizin yapisini olustur

### Adim 2: Oyun Grid Motoru (Logic)
- Grid veri yapisi (8x8 2D array)
- Renk tipleri (6 renk: kirmizi, mavi, yesil, sari, mor, turuncu)
- Rastgele grid olusturma (baslangicta match olmayan)
- BFS eslestirme algoritmasi (3+ ayni renk)
- Yer cekimi sistemi (eslesen toplar kaldirilinca ustler duser)
- Yeni top spawn (ustten)
- Hamle gecerliligi kontrolu (sadece komsu swap, en az 1 match olusacak)

### Adim 3: Grid Render (Skia Canvas)
- 8x8 grid cizimi (Skia Circle/RRect)
- Renk kodlari ile top cizimi
- Tap ile top secimi (gesture-handler)
- Swap animasyonu (reanimated)
- Eslestirme patlama animasyonu
- Cascade (dusme) animasyonu
- Yeni top spawn animasyonu

### Adim 4: Combo & Cannon Sistemi
- Combo metre (her eslestirme dolduruyor)
- Cannon UI (ekranin altinda)
- Nisan sistemi (pan gesture ile aci)
- Top firlatma fizigi (trajectory hesaplama)
- Grid'e carptigi anda patlama efekti
- Ozel top tipleri (bomba, lazer, gokkusagi)

### Adim 5: Seviye Sistemi
- Seviye tanimi yapisi (hedef skor, hamle limiti, ozel bloklar)
- 20 baslangic seviyesi
- Artan zorluk (daha az hamle, daha yuksek hedef)
- Seviye secim ekrani
- Yildiz sistemi (1-3 yildiz)
- Seviye kilidi (oncekini gecmeden sonraki acilmaz)

### Adim 6: UI & Menuler
- Ana menu ekrani
- Seviye secim grid'i
- Oyun ici skor bari
- Seviye tamamlandi modali
- Oyun bitti modali
- Ayarlar (ses ac/kapa)

### Adim 7: Ses & Efektler
- Top patlatma sesi
- Eslestirme sesi
- Combo sesi
- Cannon atisi sesi
- Seviye tamamlama sesi
- Arka plan muzigi

### Adim 8: Polish & Test
- Performans optimizasyonu
- Tum seviyeleri test et
- Hata duzeltmeleri
- App icon ve splash screen

---

## Oncelik: Adim 1-3 ilk hedef (oynanabilir temel oyun)
