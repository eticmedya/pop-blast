#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Claude Code ile Mobil Uygulama Rehberi — Part 4
Bolum 7: Claude Code ile Sifirdan Mobil Uygulama (tam tutorial)
"""
from mobile_pdf_engine import Doc, PW, PH, ML, MR, MT, MB, CW, HDR_H
from mobile_pdf_engine import NAVY, ORANGE, WHITE, BLACK, GRAY_BG, GRAY_DARK


def bolum7_claude_code_tutorial(doc):
    """Bolum 7: Claude Code ile Sifirdan Mobil Uygulama"""

    doc.section_cover(
        7,
        'Claude Code ile Sifirdan Mobil Uygulama',
        'Tek bir fikirden calisan uygulamaya',
        'Bu bolumde "Gorev Takip" adli ornek bir uygulamayi en bastan sona '
        'Claude Code ile birlikte gelistiriyoruz. Her adim, hic kod bilmeyen '
        'birinin takip edebilecegi sekilde aciklanmistir.',
    )

    # ── 7.1 Proje Fikrini Netlestirme ───────────────────────────
    doc.new_page('Bolum 7: Claude Code ile Sifirdan Mobil Uygulama')
    doc.h1('7.1  Adim 1: Proje Fikrini Netlestirme')
    doc.sp(4)
    doc.text(
        'Kod yazmaya baslamadan once uygulamanizin TAM olarak ne yaptigini '
        'tarif edebilmelisiniz. Bu rehberde ornek olarak basit ama gercekci '
        'bir "Gorev Takip" (to-do list) uygulamasi yapacagiz; ayni mantik '
        'her turlu uygulamaya uygulanabilir.'
    )
    doc.box(
        'Ornek proje: GorevTakip — Kullanicilarin gorev ekleyebildigi, '
        'tamamlandi olarak isaretleyebildigi, kategorilere ayirabildigi ve '
        'bulutta senkron edebildigi bir mobil uygulama.',
        'note'
    )

    doc.h2('Proje Tanimi Sablonu')
    doc.text(
        'Claude Code\'a vermeden once asagidaki sablonu kendi projeniz icin '
        'doldurun. Bu, projenizin "anayasasi" gibi calisacak ve CLAUDE.md '
        'dosyasinin temelini olusturacak.'
    )
    doc.code(
        'UYGULAMA ADI: GorevTakip\n\n'
        'NE YAPAR: Kullanicilarin gunluk gorevlerini ekleyip, '
        'tamamlayip,\n'
        'takip edebilecegi basit bir uretkenlik uygulamasi.\n\n'
        'HEDEF KULLANICI: Gunluk islerini organize etmek isteyen herkes\n\n'
        'TEMEL OZELLIKLER:\n'
        '- Gorev ekleme, duzenleme, silme\n'
        '- Gorevi tamamlandi olarak isaretleme\n'
        '- Kategoriler (Is, Kisisel, Alisveris)\n'
        '- Tarih/saat hatirlaticisi\n'
        '- Bulut senkronizasyonu (Supabase)\n'
        '- Karanlik mod destegi\n\n'
        'TEKNOLOJI: React Native + Expo + TypeScript + Supabase',
        'Metin'
    )

    # ── 7.2 Projeyi Olusturma ──────────────────────────────────
    doc.new_page('Bolum 7: Claude Code ile Sifirdan Mobil Uygulama')
    doc.h1('7.2  Adim 2: Bos Projeyi Olusturma')
    doc.sp(4)
    doc.code(
        '# Terminal/PowerShell acin, proje klasoru olusturun:\n'
        'npx create-expo-app gorev-takip --template blank-typescript\n'
        'cd gorev-takip\n\n'
        '# Projenin calistigini test edin:\n'
        'npx expo start\n'
        '# Telefonunuzda Expo Go ile QR kodu okutun, bos bir ekran\n'
        '# gormelisiniz - bu basariyla calistigi anlamina gelir\n\n'
        '# Claude Code\'u baslatin:\n'
        'claude',
        'Terminal'
    )
    doc.box(
        'QR kod calismiyorsa telefonunuzun ve bilgisayarinizin AYNI Wi-Fi '
        'agina bagli oldugundan emin olun. Hala calismiyorsa terminalde '
        '"npx expo start --tunnel" deneyin (daha yavas ama agdan bagimsiz '
        'calisir).',
        'warning'
    )

    # ── 7.3 CLAUDE.md Yazma ────────────────────────────────────
    doc.new_page('Bolum 7: Claude Code ile Sifirdan Mobil Uygulama')
    doc.h1('7.3  Adim 3: CLAUDE.md Dosyasini Olusturma')
    doc.sp(4)
    doc.text(
        'Claude Code\'a proje baglamini ezberletmek icin proje klasorunuzun '
        'kokunde bir CLAUDE.md dosyasi olusturun. Bunu Claude\'a yazdırabilirsiniz.'
    )
    doc.code(
        '# Claude Code\'a sorun:\n'
        '> "Bu proje icin bir CLAUDE.md dosyasi olustur.\n'
        '>  Uygulama: GorevTakip - gorev yonetim uygulamasi\n'
        '>  Stack: Expo + TypeScript + expo-router + Supabase\n'
        '>  Stil: NativeWind (Tailwind for React Native) kullan\n'
        '>  Klasor yapisi: app/ (router), components/, lib/, hooks/\n'
        '>  Kurallar: any tipi kullanma, her component icin tip tanimla,\n'
        '>  fonksiyonel component + hooks kullan, class component yok"',
        'Terminal'
    )
    doc.text(
        'Claude bu talimatı okuyup detaylı bir CLAUDE.md dosyasi yazacaktir. '
        'Bu dosya, projenizdeki HER oturumda otomatik olarak okunur.'
    )

    # ── 7.4 Navigasyon Kurulumu ─────────────────────────────────
    doc.new_page('Bolum 7: Claude Code ile Sifirdan Mobil Uygulama')
    doc.h1('7.4  Adim 4: Navigasyon (Sekme Yapisi) Kurulumu')
    doc.sp(4)
    doc.code(
        '# Claude Code\'a sorun:\n'
        '> "expo-router kur ve 3 sekmeli bir navigasyon yapisi olustur:\n'
        '>  1. Gorevler (ana sayfa, liste ikonu)\n'
        '>  2. Kategoriler (klasor ikonu)\n'
        '>  3. Profil (kullanici ikonu)\n'
        '>  Alt sekme cubugu (tab bar) NativeWind ile turuncu vurgu\n'
        '>  renginde olsun. Her sekme icin bos bir placeholder sayfa yaz."',
        'Terminal'
    )
    doc.text(
        'Claude bu adimda: expo-router\'i kuracak, app/_layout.tsx ve '
        'app/(tabs)/ klasorunu olusturacak, her sekme icin sayfa dosyasi '
        'yazacak ve tab bar stilini ayarlayacaktir. Islem bittiginde '
        'Expo Go\'da uygulamanizi yenileyip 3 sekmenin gorundugunu '
        'kontrol edin.'
    )
    doc.box(
        'Her buyuk adimdan sonra MUTLAKA telefonunuzda test edin. '
        '"Calisiyor mu?" sorusunu kendinize sik sorun. Hata gorurseniz '
        'hata mesajinin TAMAMINI kopyalayip Claude\'a yapistirin ve '
        '"Bu hatayi coz" deyin.',
        'tip'
    )

    # ── 7.5 Veri Modeli ve State Yonetimi ──────────────────────
    doc.new_page('Bolum 7: Claude Code ile Sifirdan Mobil Uygulama')
    doc.h1('7.5  Adim 5: Veri Modeli ve Yerel State Yonetimi')
    doc.sp(4)
    doc.text(
        'Backend\'i kurmadan once uygulamanizin sadece kendi telefonunuzda '
        '(yerel hafizada) calisan bir versiyonunu yapmak iyi bir baslangictir. '
        'Bu, "once basit calistir, sonra karmasiklastir" prensibidir.'
    )
    doc.code(
        '# Claude Code\'a sorun:\n'
        '> "Gorev veri modelini tanimla:\n'
        '>  interface Gorev {\n'
        '>    id: string;\n'
        '>    baslik: string;\n'
        '>    tamamlandi: boolean;\n'
        '>    kategori: \'is\' | \'kisisel\' | \'alisveris\';\n'
        '>    olusturmaTarihi: Date;\n'
        '>  }\n'
        '>\n'
        '>  Zustand kullanarak bir gorev store\'u olustur:\n'
        '>  - gorevEkle, gorevSil, gorevTamamla fonksiyonlari\n'
        '>  - AsyncStorage ile cihazda kalici sakla (uygulama\n'
        '>    kapatilip acildiginda veri kaybolmasin)"',
        'Terminal'
    )
    doc.box(
        'Zustand, React uygulamalarinda durum (state) yonetimi icin Redux\'a '
        'gore cok daha basit bir kutuphanedir. Claude Code, projenize en '
        'uygun state yonetim aracını secip kuracaktır; siz sadece ne '
        'istediginizi tarif edin.',
        'info'
    )

    # ── 7.6 UI: Gorev Ekleme Ekrani ─────────────────────────────
    doc.new_page('Bolum 7: Claude Code ile Sifirdan Mobil Uygulama')
    doc.h1('7.6  Adim 6: Gorev Ekleme ve Listeleme Ekrani')
    doc.sp(4)
    doc.code(
        '# Claude Code\'a sorun:\n'
        '> "Gorevler sekmesini doldur:\n'
        '>  - Ust kisimda baslik: \'Gorevlerim\'\n'
        '>  - Altinda bir metin kutusu + \'Ekle\' butonu (yeni gorev icin)\n'
        '>  - Asagida gorev listesi: her satirda checkbox + baslik +\n'
        '>    kategori etiketi (renkli badge) + silme ikonu\n'
        '>  - Tamamlanan gorevler ustu cizili ve solgun gorunsun\n'
        '>  - Liste bossa \'Henuz gorev yok, ilk gorevini ekle!\' mesaji goster\n'
        '>  - FlatList kullan, performansli render olsun"',
        'Terminal'
    )
    doc.text(
        'Bu tek prompt ile Claude Code, fonksiyonel bir gorev listesi '
        'ekranini sizin icin yazar: checkbox bileseni, swipe-to-delete '
        'jesti, bos durum (empty state) tasarimi dahil. Test edip '
        'begenmediginiz bir detay varsa "checkbox\'in rengini turuncu yap" '
        'gibi kucuk duzeltme istekleri verebilirsiniz.'
    )

    # ── 7.7 Kategoriler Ekrani ──────────────────────────────────
    doc.new_page('Bolum 7: Claude Code ile Sifirdan Mobil Uygulama')
    doc.h1('7.7  Adim 7: Kategoriler ve Filtreleme')
    doc.sp(4)
    doc.code(
        '# Claude Code\'a sorun:\n'
        '> "Kategoriler sekmesini yap:\n'
        '>  - 3 buyuk kart goster: Is, Kisisel, Alisveris\n'
        '>  - Her kartta o kategorideki toplam/tamamlanan gorev sayisi\n'
        '>  - Karta tiklayinca o kategoriye filtrelenmis gorev listesine\n'
        '>    gecsin (Gorevler sekmesine yonlendir, filtre parametresiyle)\n'
        '>  - Her kategori icin farkli renk: Is=mavi, Kisisel=yesil,\n'
        '>    Alisveris=turuncu"',
        'Terminal'
    )

    # ── 7.8 Hata Ayiklama Pratigi ────────────────────────────────
    doc.new_page('Bolum 7: Claude Code ile Sifirdan Mobil Uygulama')
    doc.h1('7.8  Adim 8: Hata Ayiklama — Gercek Bir Senaryo')
    doc.sp(4)
    doc.text(
        'Gelistirme sirasinda hatalarla karsilasmaniz tamamen normaldir. '
        'Onemli olan, hatayi nasil Claude Code\'a ileteceğinizi bilmek.'
    )
    doc.code(
        '# Telefonunuzda kirmizi bir hata ekrani gorduyseniz:\n'
        '# 1. Ekrandaki TAM hata mesajini fotograflayin veya kopyalayin\n'
        '# 2. Terminaldeki hata logunu da kopyalayin\n'
        '# 3. Claude Code\'a yapistirin:\n\n'
        '> "Su hatayi aliyorum:\n'
        '>\n'
        '>  [BURAYA TAM HATA MESAJINI YAPISTIRIN]\n'
        '>\n'
        '>  Bu hata gorev ekleme butonuna tikladigimda olusuyor.\n'
        '>  Bunu coz."',
        'Terminal'
    )
    doc.box(
        'Hata mesajinin TAMAMINI vermek cok onemlidir. "Bir hata aldim, '
        'coz" gibi belirsiz bir talep Claude\'un tahmin yurutmesine yol '
        'acar. Ne kadar spesifik olursaniz, cozum o kadar hizli gelir.',
        'warning'
    )

    # ── 7.9 Tasarim Cilalama ────────────────────────────────────
    doc.new_page('Bolum 7: Claude Code ile Sifirdan Mobil Uygulama')
    doc.h1('7.9  Adim 9: Tasarimi Cilalama (Polish)')
    doc.sp(4)
    doc.text(
        'Uygulamanizin temel ozellikleri calistiktan sonra, kullanicilarin '
        'gercekten begenecegi bir gorunum icin tasarim detaylarina '
        'odaklanin.'
    )
    doc.bullets([
        'Animasyonlar: "Gorev tamamlandiginda kucuk bir konfeti animasyonu '
        'ekle" gibi istekler verebilirsiniz (react-native-reanimated)',
        'Karanlik mod: "Sistem temasina gore otomatik karanlik/aydinlik '
        'mod destegi ekle"',
        'Bos durumlar (empty states): Her liste/ekran icin anlamli bos '
        'durum mesajlari ve illustrasyonlari',
        'Yukleme durumlari (loading states): Veriler yuklenirken iskelet '
        '(skeleton) animasyonu',
        'Haptic feedback: Butona basildiginda telefonun hafifce '
        'titremesi (expo-haptics)',
    ])
    doc.code(
        '# Claude Code\'a sorun:\n'
        '> "Tum uygulamada haptic feedback ekle: her butona basildiginda\n'
        '>  hafif titresim olsun (expo-haptics kullan). Ayrica karanlik\n'
        '>  mod destegi ekle, sistem temasini otomatik algilasin."',
        'Terminal'
    )

    # ── 7.10 Genel Ozet ─────────────────────────────────────────
    doc.new_page('Bolum 7: Claude Code ile Sifirdan Mobil Uygulama')
    doc.h1('7.10  Bu Bolumun Ozeti: Tekrarlanabilir Sablon')
    doc.sp(4)
    doc.text(
        'Yukaridaki adimlar herhangi bir mobil uygulama icin tekrarlanabilir '
        'bir sablondur. Kendi fikrinize uygularken su sirayi takip edin:'
    )
    doc.table(
        ['Adim',  'Eylem',                                           'Anahtar Komut'],
        [
            ['1',     'Fikri net tarif et (ne yapar, kim icin)',         'Kagit uzerinde planla'],
            ['2',     'Bos Expo projesi olustur',                        'create-expo-app'],
            ['3',     'CLAUDE.md yaz (Claude\'a yazdirilabilir)',         '"CLAUDE.md olustur"'],
            ['4',     'Navigasyon iskeletini kur',                       '"Sekme yapisi kur"'],
            ['5',     'Veri modelini ve yerel state\'i tanimla',          '"Store olustur"'],
            ['6',     'Ekranlari sirayla doldur',                        '"Bu ekrani yap"'],
            ['7',     'Her adimda test et, hatalari Claude\'a bildir',    '"Bu hatayi coz"'],
            ['8',     'Tasarim detaylarini cilala',                      '"Animasyon/tema ekle"'],
            ['9',     'Backend ekle (Bolum 8)',                          'Supabase entegrasyonu'],
            ['10',    'Gelir modeli ekle (Bolum 11-13)',                  'AdMob/Adapty/RevenueCat'],
        ],
        widths=[35, 250, 186]
    )
    doc.sp(6)
    doc.box(
        'Bu donguyu kucuk parcalara bolerek ilerlemek en onemli prensiptir: '
        'her seferinde TUM uygulamayi istemek yerine bir ekrani, bir '
        'ozelligi isteyin. Boylece hatalari kolayca izole eder, Claude\'un '
        'her adimini kontrol edebilirsiniz.',
        'tip'
    )
