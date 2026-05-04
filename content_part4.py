#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Icerik Part 4 — Sayfa 60-80
Bolum 5 devami: Mobil (Win/Mac) + Desktop
Bolum 6: App Store ve Google Play
"""
from pdf_engine import Doc
from pdf_engine import NAVY, ORANGE, WHITE, BLACK, GRAY_BG, GRAY_DARK

from content_part1 import kapak_sayfasi, icindekiler, bolum1_giris, bolum1_ek_ve_bolum2_baslangic
from content_part2 import bolum2_devami, bolum3_claude_ekosistemi
from content_part3 import bolum4_claude_code, bolum5_projeler_baslangic


def bolum5_mobil_windows(doc):
    """5.2 Mobil Uygulama — Windows'ta"""

    doc.new_page('Bolum 5: Claude Code ile Gercek Projeler')
    doc.h1('5.2  Mobil Uygulama — Windows\'ta Gelistirme')
    doc.sp(4)
    doc.text(
        'Windows\'ta mobil uygulama gelistirmek icin en pratik yol React Native + Expo '
        'kombinasyonudur. Expo, React Native\'in kurulum karmasikligini ortadan kaldirir '
        've Claude Code ile birlikte kullanildiginda gercek bir mobil uygulama saatler '
        'icinde hazir olabilir.'
    )

    doc.h2('Gerekli Kurulumlar')
    doc.bullets([
        'Node.js LTS (onceki bolumde kuruldu)',
        'Expo CLI: npm install -g @expo/cli',
        'Telefonunuza Expo Go uygulamasi (App Store / Play Store\'dan ucretsiz)',
        'Opsiyonel: Android Studio (emulator icin)',
    ])
    doc.code(
        '# Expo CLI\'yi global kur:\n'
        'npm install -g @expo/cli\n\n'
        '# Dogrula:\n'
        'expo --version\n'
        '# 0.x.x',
        'PowerShell'
    )

    doc.h2('Yeni Expo Projesi Olusturma')
    doc.code(
        '# Yeni proje olustur:\n'
        'npx create-expo-app benim-uygulamam\n'
        'cd benim-uygulamam\n\n'
        '# Claude Code\'u baslat:\n'
        'claude\n\n'
        '# Projeyi tanimla:\n'
        '> "Bu bir React Native + Expo projesi.\n'
        '>  Bana bir gunluk not tutma uygulamasi yap.\n'
        '>  Ozellikler: Not ekleme, listeleme, silme, arama.\n'
        '>  Tasarim: Minimalist, beyaz arkaplan, mavi aksanlar.\n'
        '>  AsyncStorage ile yerel kayit."',
        'Terminal'
    )

    doc.h2('Expo Go ile Telefonda Test')
    doc.text(
        'Expo Go, gelistirme surecinde uygulamanizi gercek telefonunuzda ani olarak '
        'gormek icin kullanilan resmi test uygulamasidir. Wi-Fi uzerinden calisir.'
    )
    doc.bullets([
        '1. Telefonunuza Expo Go\'yu App Store veya Play Store\'dan yukleyin',
        '2. Bilgisayar ve telefon ayni Wi-Fi aginda olmali',
        '3. Proje klasorunde terminale "npx expo start" yazin',
        '4. QR kod ekrana cikacak — Expo Go ile okutun',
        '5. Uygulama telefonunuzda aninda acilir',
        '6. Kodda degisiklik yapildiginda otomatik guncellenir (Hot Reload)',
    ])
    doc.code(
        '# Expo dev server baslatma:\n'
        'npx expo start\n\n'
        '# Alternatifler:\n'
        'npx expo start --android   # Android emulator\n'
        'npx expo start --web       # Web tarayici',
        'Terminal'
    )
    doc.box(
        'Expo Go kullanirken bazen QR kod okunmuyor olabilir. Bu durumda '
        'Expo Go uygulamasinda "Enter URL manually" secenegiyle '
        '"exp://192.168.x.x:8081" adresini manuel girin.',
        'warning'
    )

    doc.h2('EAS Build ile Gercek APK/IPA Uretme')
    doc.text(
        'Expo Go sadece gelistirme icin kullanilir. Uygulamayi Play Store veya '
        'App Store\'a yuklemek icin EAS (Expo Application Services) Build kullanilir. '
        'EAS Build, bulut sunucularda derleme yaparak size hazir APK/IPA dosyasi verir.'
    )
    doc.code(
        '# EAS CLI kur:\n'
        'npm install -g eas-cli\n\n'
        '# Expo hesabina giris:\n'
        'eas login\n\n'
        '# Projeyi EAS\'e bagla:\n'
        'eas init\n\n'
        '# Android APK/AAB derle:\n'
        'eas build --platform android --profile preview\n\n'
        '# iOS IPA derle (Mac gerekmez, bulutta derlenir):\n'
        'eas build --platform ios',
        'Terminal'
    )
    doc.box(
        'Windows\'ta iOS uygulamasi DERLEYEMEZSINIZ cunku Apple, iOS derlemelerinin '
        'sadece macOS uzerinde yapilmasini zorunlu kilar. Ancak EAS Build ile '
        'bu kisitlami asabilirsiniz: EAS\'in bulut Mac sunuculari derlemeyi yapar, '
        'size hazir IPA dosyasini gonderir. Apple Developer hesabi ($99/yil) gereklidir.',
        'warning'
    )

    doc.h2('Expo Dev Client — Gelismis Yerel Modüller')
    doc.text(
        'Expo Go, tum React Native kutuphanelerini desteklemez. Kamera, Bluetooth, '
        'push bildirim gibi yerel (native) modüller icin Expo Dev Client gerekir. '
        'Bu, Expo Go\'nun projeye ozel ozellestirilmis versiyonudur.'
    )
    doc.code(
        '# Expo Dev Client ekle:\n'
        'npx expo install expo-dev-client\n\n'
        '# Ozel dev client derle:\n'
        'eas build --profile development --platform android\n\n'
        '# Indirilen APK\'yi telefona yukle ve kullan',
        'Terminal'
    )

    # ── 5.3 Mobil — MacBook ───────────────────────────────
    doc.new_page('Bolum 5: Claude Code ile Gercek Projeler')
    doc.h1('5.3  Mobil Uygulama — MacBook\'ta Gelistirme')
    doc.sp(4)
    doc.text(
        'MacBook\'ta gelistirme yapmanin en buyuk avantaji: iOS uygulamasini local olarak '
        'derleyebilir, Xcode Simulator\'da test edebilir ve App Store\'a dogrudan '
        'yukleyebilirsiniz. Windows\'ta EAS cloud build ile yapilan islemleri '
        'MacBook\'ta yerel olarak yapabilirsiniz.'
    )

    doc.h2('Xcode Kurulumu')
    doc.bullets([
        '1. App Store\'u acin, "Xcode" aratip indirin (15+ GB, sabir gerektirir)',
        '2. Xcode acildiktan sonra "Install Additional Components" onaylayin',
        '3. Xcode Command Line Tools: xcode-select --install',
        '4. CocoaPods: sudo gem install cocoapods',
        '5. Xcode versiyonunu kontrol: xcodebuild -version',
    ])
    doc.code(
        '# Xcode CLI tools kur:\n'
        'xcode-select --install\n\n'
        '# CocoaPods kur:\n'
        'sudo gem install cocoapods\n\n'
        '# Dogrula:\n'
        'pod --version\n'
        '# 1.15.x',
        'Terminal (macOS)'
    )

    doc.h2('Apple Developer Hesabi')
    doc.text(
        'iOS uygulamasi yayinlamak icin Apple Developer Program\'a uye olmaniz gerekir. '
        'Yillik $99 ucreti olan bu program size gercek cihazda test ve App Store '
        'yayinlama hakki verir.'
    )
    doc.bullets([
        'developer.apple.com adresine gidin',
        'Apple ID ile giris yapin (yoksa olusturun)',
        '"Enroll" butonuna tiklayin',
        'Bireysel veya sirket hesabi secin',
        '$99 odeme yapin (kredi karti veya PayPal)',
        'Dogrulama 24-48 saat surebilir',
    ])
    doc.box(
        'Apple Developer hesabi olmadan da Xcode Simulator\'da test yapabilirsiniz. '
        'Simulator, gercek cihaza gerek duymadan iOS uygulamanizi masaustunuzde '
        'calistirmanizi saglar. Yayinlama asamasina gelince hesap acabilirsiniz.',
        'info'
    )

    doc.h2('iOS Simulator\'da Test')
    doc.code(
        '# Expo projesinde iOS calistir:\n'
        'npx expo start --ios\n\n'
        '# Veya dogrudan Simulator sec:\n'
        'npx expo run:ios\n\n'
        '# Belirli bir cihaz modeli sec:\n'
        'npx expo run:ios --device "iPhone 16 Pro"\n\n'
        '# Xcode\'dan simulator ac:\n'
        '# Xcode → Window → Devices and Simulators',
        'Terminal (macOS)'
    )

    doc.h2('Provisioning Profile ve Certificates')
    doc.text(
        'Gercek cihazda test veya App Store\'a yukleme icin Xcode\'un '
        '"Signing & Capabilities" ayarlarinizi yapilandirmaniz gerekir.'
    )
    doc.bullets([
        'Xcode\'da projenizi acin',
        'Sol panelden proje adina tiklayin',
        '"Signing & Capabilities" sekmesine gecin',
        '"Automatically manage signing" kutusunu isaretleyin',
        'Team\'den Apple Developer hesabinizi secin',
        'Xcode otomatik olarak certificate ve profile olusturur',
    ])
    doc.code(
        '# EAS ile local iOS build (Mac gerektirir):\n'
        'eas build --platform ios --local\n\n'
        '# Dogrudan Xcode ile archive:\n'
        '# Product → Archive → Distribute App → App Store Connect',
        'Terminal (macOS)'
    )

    # ── 5.4 Desktop Uygulama ──────────────────────────────
    doc.new_page('Bolum 5: Claude Code ile Gercek Projeler')
    doc.h1('5.4  Masaustu Uygulama: Electron ve Tauri')
    doc.sp(4)
    doc.text(
        'Masaustu uygulamasi gelistirmek icin iki modern secenek var: Electron ve Tauri. '
        'Electron daha olgun ve yaygın kullanilan bir teknoloji iken Tauri daha yeni, '
        'cok daha hafif ve hizli bir alternatiftir. Ikisi de HTML/CSS/JS bilgisiyle '
        'Windows, Mac ve Linux uygulamasi gelistirmenize olanak tanir.'
    )

    doc.h2('Electron vs Tauri Karsilastirmasi')
    doc.table(
        ['Kriter',          'Electron',                    'Tauri'],
        [
            ['Teknoloji',       'Node.js + Chromium',          'Rust + sistem WebView'],
            ['Kurulum buyuklugu','~150-200 MB',                '~5-10 MB'],
            ['Bellek kullanimi','Yuksek (~200MB+)',            'Dusuk (~30-50MB)'],
            ['Performans',      'Orta',                        'Cok yuksek'],
            ['Ogrenme egrisi',  'Kolay (JS bilgisi yeterli)',  'Orta (biraz Rust)'],
            ['Ekosistem',       'Cok genis, olgun',            'Buyuyor, aktif'],
            ['Ornekler',        'VS Code, Slack, Discord',     'Gitbutler, Spacedrive'],
            ['Onerim',          'Hizli prototip, mevcut web',  'Uretim kalitesi, kucuk boyut'],
        ],
        widths=[100, 170, 201]
    )
    doc.sp(6)

    doc.h2('Electron ile Not Alma Uygulamasi')
    doc.code(
        '# Claude Code\'a sorun:\n'
        '> "Electron ile bir not alma uygulamasi yap.\n'
        '>  Ozellikler:\n'
        '>  - Not ekleme, duzenleme, silme\n'
        '>  - Markdown destegi\n'
        '>  - Klasor / etiket sistemi\n'
        '>  - Yerel dosya sistemi kaydi (JSON)\n'
        '>  - Karanlik mod destegi\n'
        '>  Teknoloji: Electron + React + electron-store"',
        'Terminal'
    )
    doc.code(
        '# Claude asagidaki adimlari otomatik atar:\n'
        'npm init -y\n'
        'npm install electron electron-store react react-dom\n'
        'npm install --save-dev @electron-forge/cli\n'
        'npx electron-forge init\n\n'
        '# Gelistirme modunda calistirma:\n'
        'npm run start\n\n'
        '# Dagitim paketi olusturma (exe/dmg/deb):\n'
        'npm run make',
        'Terminal'
    )

    doc.h2('Tauri ile Uygulama')
    doc.code(
        '# Tauri kurulumu (Rust gerektirir):\n'
        '# Once Rust kur: rustup.rs\n'
        'curl --proto \'=https\' --tlsv1.2 -sSf https://sh.rustup.rs | sh\n\n'
        '# Tauri CLI kur:\n'
        'npm install -g @tauri-apps/cli\n\n'
        '# Yeni Tauri projesi:\n'
        'npm create tauri-app@latest benim-app\n'
        'cd benim-app\n'
        'npm install\n\n'
        '# Gelistirme:\n'
        'npm run tauri dev\n\n'
        '# Dagitim:\n'
        'npm run tauri build',
        'Terminal'
    )
    doc.box(
        'Claude Code, Electron ve Tauri projelerini cok iyi yonetir. '
        '"Bana bir not alma uygulamasi yap" gibi basit bir prompt bile '
        'tam calisan, paketlenebilir bir masaustu uygulamasi ortaya cikarir. '
        'Denemeye korkmayin!',
        'tip'
    )


def bolum6_store(doc):
    """Bolum 6: App Store ve Google Play Yayinlama"""

    doc.section_cover(
        6,
        'App Store ve Google Play Yayinlama',
        'Uygulamanizi milyonlara ulastirin',
        'Bu bolumde Google Play Console ve App Store Connect arayuzlerini adim adim '
        'inceliyor, test sureclerini, store listing hazirligini ve sikca karsilasilan '
        'red nedenlerini ve cozumlerini ele aliyoruz.'
    )

    # ── Google Play ───────────────────────────────────────
    doc.new_page('Bolum 6: App Store ve Google Play Yayinlama')
    doc.h1('6.1  Google Play Console — Adim Adim')
    doc.sp(4)
    doc.text(
        'Google Play Console, Android uygulamalarinizi Google Play Store\'a yuklemek, '
        'yonetmek ve analiz etmek icin kullanilan gelistirici panelidir. Tek seferlik '
        '$25 kayit ucreti odenince hesap omur boyu kullanilabilir.'
    )

    doc.h2('Hesap Acma ve Dogrulama')
    doc.bullets([
        '1. play.google.com/console adresine gidin',
        '2. Google hesabinizla giris yapin',
        '3. "Gelistirici hesabi olustur" butonuna tiklayin',
        '4. Gelistirici adi, e-posta ve telefon girin',
        '5. $25 kayit ucretini kredi karti ile odeyin',
        '6. Kimlik dogrulama: Kimlik belgesi veya telefon dogrulamasi',
        '7. Hesap onay suresi: 24-48 saat',
    ])
    doc.box(
        'Google Play Console hesabinizi kisisel veya sirket olarak acabilirsiniz. '
        'Ticari amacli uygulamalar icin sirket hesabi (kurumsal dogrulama gerekir) '
        'daha profesyonel goruntu saglar. Kisisel hesapla baslayip sonra donusturmek '
        'de mumkundur.',
        'info'
    )

    doc.h2('Yeni Uygulama Olusturma')
    doc.bullets([
        '1. Console ana sayfasinda "Uygulama olustur" butonuna tiklayin',
        '2. Uygulama adi, varsayilan dil ve uygulama turu secin (uygulama / oyun)',
        '3. Ucretsiz mi odeme mi? (ilerleyen sureclerde degistirilemez)',
        '4. Google Play Gelistirici Dagitim Anlasmasi\'ni kabul edin',
        '5. Uygulama paneli acilir — sol menuden tum ayarlara ulasabilirsiniz',
    ])

    doc.h2('AAB Dosyasi Hazirlama ve Yukleme')
    doc.text(
        'Google Play, APK yerine AAB (Android App Bundle) formatini tercih eder. '
        'AAB, Google\'in her cihaza optimize APK uretmesini saglar ve uygulama '
        'boyutunu dusurebilir.'
    )
    doc.code(
        '# Expo EAS ile AAB uretme:\n'
        'eas build --platform android --profile production\n\n'
        '# Veya React Native CLI ile:\n'
        'cd android\n'
        './gradlew bundleRelease\n'
        '# Cikti: android/app/build/outputs/bundle/release/app-release.aab\n\n'
        '# Play Console\'da:\n'
        '# Uretim → Yeni surum olustur → AAB yukle → Incele ve yayinla',
        'Terminal'
    )

    doc.h2('Store Listing Hazirlama')
    doc.text(
        'Store listing, kullanicilarin uygulamanizi Play Store\'da gordugu sayfadir. '
        'Kaliteli bir listing, indirme sayilarini dogrudan etkiler.'
    )
    doc.table(
        ['Alan',                 'Gereksinim',                   'Ipucu'],
        [
            ['Uygulama adi',         'Maks. 30 karakter',            'Anahtar kelime icerir olmali'],
            ['Kisa aciklama',        'Maks. 80 karakter',            'En onemli ozelligi one cikarin'],
            ['Uzun aciklama',        'Maks. 4000 karakter',          'AI ile yazin, SEO\'ya dikkat'],
            ['Ekran goruntuleri',    'Min. 2, maks. 8 gorsel',       'Her ekrani goster, aciklama ekle'],
            ['Ozellik grafigi',      '1024x500 px',                  'Dikkat cekici, marka renkleri'],
            ['Uygulama ikonu',       '512x512 px PNG',               'Temiz, basit, tanimlayici'],
            ['Tanitim videosu',      'Opsiyonel, YouTube linki',     'Varsa indirme artar'],
        ],
        widths=[110, 130, 231]
    )
    doc.sp(6)
    doc.box(
        'Store listing icin Claude\'u kullanin! "Benim uygulamam [X] yapiyor, '
        'Play Store icin etkileyici bir aciklama yaz, anahtar kelimeleri icerikle '
        'harmanla" prompt\'uyla profesyonel bir aciklama dakikalar icinde hazir olur.',
        'tip'
    )

    doc.h2('Test Asamalari')
    doc.text(
        'Google Play, uygulamanizi Uretim\'e gecirmeden once test etmenizi gerektirir. '
        'Uc test asamas mevcuttur ve sirasiyla gecilmesi onerilir.'
    )
    doc.table(
        ['Asama',           'Kapsam',                 'Amac'],
        [
            ['Ic Test',          'Maks. 100 tester',       'Takim ve yakin cevre testi'],
            ['Kapali Test (Alpha)', 'Davetli kullanicilar', 'Secilmis kullanici grubu'],
            ['Acik Test (Beta)', 'Herkese acik',           'Genis kullanici kitlesi geri bildirim'],
            ['Uretim',           'Tum dunya',              'Gercek yayinlama'],
        ],
        widths=[115, 130, 226]
    )
    doc.sp(4)
    doc.box(
        'Google Play, Uretim\'e gecmeden once en az 20 dahili tester\'in 14 gun boyunca '
        'uygulamanizi test etmesini zorunlu kilar (yeni hesaplar icin). '
        'Bu sureci atlamak icin arkadas cevrenizdeki 20 kisiyi tester olarak ekleyin.',
        'warning'
    )

    doc.h2('Veri Guvenligi Formu')
    doc.text(
        'Google Play, hangi kullanici verilerini topladığınızı aciklamanizi ister. '
        'Bu form doldurulmazsa uygulamaniz yayinlanamaz.'
    )
    doc.bullets([
        'Konum verisi toplanıyor mu? (GPS, aglarindan)',
        'Kisisel bilgiler: Ad, e-posta, telefon',
        'Finansal bilgiler: Kredi karti, satin alma gecmisi',
        'Saglik ve fitness verisi',
        'Uygulamada analitik / reklam SDK var mi? (AdMob, Firebase)',
        'Ucuncu taraf veri paylasimi var mi?',
    ])

    # ── App Store ─────────────────────────────────────────
    doc.new_page('Bolum 6: App Store ve Google Play Yayinlama')
    doc.h1('6.2  App Store Connect — Adim Adim')
    doc.sp(4)
    doc.text(
        'App Store Connect, Apple\'in iOS/macOS uygulama yonetim panelidir. '
        'Google Play\'e kiyasla daha kati inceleme sureci ve daha uzun bekleme '
        'sureleri icermektedir. Ancak iOS kullanicilari genellikle daha fazla '
        'harcama yaptigindan gelir potansiyeli yuksektir.'
    )

    doc.h2('Apple Developer Program Kaydi')
    doc.bullets([
        '1. developer.apple.com adresine gidin',
        '2. Apple ID ile giris yapin',
        '3. "Enroll" butonuna tiklayin',
        '4. Bireysel ($99/yil) veya Sirket hesabi secin',
        '5. Kredi karti ile odeme yapin',
        '6. Dogrulama: Kimlik belgesi + adres kaniti (sirket icin)',
        '7. Onay: 24-72 saat (bazen daha uzun surebilir)',
    ])

    doc.h2('App Store Connect\'te Uygulama Olusturma')
    doc.bullets([
        '1. appstoreconnect.apple.com adresine gidin',
        '2. "Uygulamalarim" → "+" → "Yeni Uygulama" tiklayin',
        '3. Platform secin: iOS, macOS, tvOS',
        '4. Uygulama adi, birincil dil, Bundle ID girin',
        '5. SKU (benzersiz tanimlayici): orneg. com.sirketadi.uygulamaadi',
        '6. Kullanici erisimi: Tam erisim veya sinirli erisim',
    ])

    doc.h2('Bundle ID ve App ID Olusturma')
    doc.text(
        'Bundle ID, uygulamanizin Apple ekosistemindeki benzersiz kimligidir. '
        'Bir kez belirlendikten sonra degistirilemez. "com.sirketadi.uygulamaadi" '
        'formatinda olmasi onerilir.'
    )
    doc.code(
        '# Expo ile Bundle ID ayarlama (app.json):\n'
        '{\n'
        '  "expo": {\n'
        '    "ios": {\n'
        '      "bundleIdentifier": "com.eticmedya.notapp",\n'
        '      "buildNumber": "1"\n'
        '    },\n'
        '    "android": {\n'
        '      "package": "com.eticmedya.notapp",\n'
        '      "versionCode": 1\n'
        '    }\n'
        '  }\n'
        '}',
        'JSON'
    )

    doc.h2('TestFlight ile Beta Test')
    doc.text(
        'TestFlight, App Store\'a yukleme yapmadan once uygulamanizi test '
        'kullanicilarina dagitin platformdur. Dahili ve harici testerlar '
        'olarak iki grup vardir.'
    )
    doc.bullets([
        'Dahili testerlar: Maks. 100 kisi, App Store Connect kullanicilari',
        'Harici testerlar: Maks. 10.000 kisi, e-posta daveti ile',
        'Harici test icin Apple incelemesi gerekir (~24-48 saat)',
        'TestFlight linkleri 90 gun gecerlidir',
        'Build yukleme: Xcode Archive veya EAS Build ile',
    ])
    doc.code(
        '# EAS ile TestFlight\'a yukleme:\n'
        'eas submit --platform ios\n\n'
        '# Bu komut:\n'
        '# 1. En son build\'i App Store Connect\'e yukler\n'
        '# 2. TestFlight\'ta otomatik olarak gorunur\n'
        '# 3. Testerlar e-posta daveti alir',
        'Terminal'
    )

    doc.h2('App Privacy Declarations')
    doc.text(
        'Apple, her uygulamanin kullanici gizliligi konusunda seffaf olmasini gerektirir. '
        'App Store Connect\'te "Uygulama Gizliligi" bolumunu doldurmak zorunludur.'
    )
    doc.bullets([
        'Hangi veri toplanıyor? (Konum, kimlik, kullanim verileri vb.)',
        'Bu veri ne amacla kullaniliyor? (Analitik, urun ozellestirme vb.)',
        'Veri kullaniciya bagli mi? (Hesap veya kimlikle iliskilendiriliyor mu?)',
        'ATT framework: Izleme yapiyorsaniz kullanicidan izin almaniz gerekir',
    ])

    doc.h2('ATT Framework — Kullanici Takibi')
    doc.code(
        '// React Native\'de ATT permission isteme:\n'
        'import { requestTrackingPermissionsAsync }\n'
        '  from "expo-tracking-transparency";\n\n'
        'const { status } = await requestTrackingPermissionsAsync();\n'
        'if (status === "granted") {\n'
        '  // AdMob veya analitik izleme aktif et\n'
        '} else {\n'
        '  // Anonim mod, izleme yapma\n'
        '}',
        'JavaScript'
    )
    doc.box(
        'ATT framework\'u kullanan uygulamalar, kullanicidan "Bu uygulama sizi '
        'diger uygulamalarda takip etmek istiyor" dialog\'u ile izin istemek '
        'zorundadır. Izin alinmadan AdMob veya Facebook Pixel gibi araclarin '
        'kullanici bazli hedefleme yapmasina izin verilmez.',
        'warning'
    )

    doc.new_page('Bolum 6: App Store ve Google Play Yayinlama')
    doc.h1('6.3  Inceleme Sureci ve Red Nedenleri')
    doc.sp(4)
    doc.text(
        'App Store inceleme sureci, Google Play\'e gore cok daha kati ve uzundur. '
        'Ortalama inceleme suresi 24-48 saattir, ancak bazen daha uzun surebilir. '
        'Asagida en sik karsilasilan red nedenleri ve cozumleri yer almaktadir.'
    )

    doc.h2('En Sik Red Nedenleri ve Cozumleri')
    doc.table(
        ['Kural',           'Red Nedeni',                           'Cozum'],
        [
            ['Guideline 2.1',   'Cokme / hata / eksik islevsellik',    'Testleri tam yap, test hesabi ekle'],
            ['Guideline 4.3',   'Spam / kopya uygulama',               'Benzersiz deger onerisi sunun'],
            ['Guideline 5.1.1', 'Gizlilik ihlali / veri toplama',      'Privacy manifest ekle, ATT kullan'],
            ['Guideline 3.1',   'IAP atlama / harici odeme',           'Sadece Apple IAP kullan'],
            ['Guideline 1.1',   'Zararli icerik',                      'Icerik denetimi ekle'],
            ['Guideline 4.0',   'Tasarim / UI sorunlari',              'HIG\'e uyun, native gorunum saglayin'],
            ['Metadata 1.3',    'Yaniltici ekran goruntuleri',         'Gercek uygulama ekranlari kullanin'],
        ],
        widths=[90, 185, 196]
    )
    doc.sp(6)

    doc.h2('Inceleme Surecini Hizlandirma')
    doc.bullets([
        'Demo hesabi ekleyin: Inceleyici icin hazir kullanici adi/sifre birakin',
        'Review notlari yazin: Ozellikleri ve nasil test edilecegini aciklayin',
        'Accelerated Review talep edin: Cok kritik bir hata duzeltmesi ise',
        'Tam islevsel uygulamayin: Bos butonlar, placeholder icerik redde yol acar',
        'Test tum cihazlarda: iPhone SE\'den Pro Max\'e kadar test edin',
    ])

    doc.h2('Red Sonrasi Ne Yapilmali?')
    doc.text(
        'Uygulamaniz reddedildiginde paniklemeyim. Red mesaji genellikle sorunun '
        'ne oldugunu acikca belirtir. Sorunu duzeltip yeni bir build yukleyin.'
    )
    doc.bullets([
        'Red mesajini dikkatlice okuyun — genellikle cok net',
        'Apple ile iletisime gecin: Resolution Center\'dan mesaj gonderin',
        'Sorunu duzeltip "Reply to Apple" butonuyla yanit verin',
        'Gerekirse Appeal (itiraz) basvurusu yapin',
        'Claude\'a red mesajini verin: "Bu red nedenini coz" deyin',
    ])
    doc.box(
        'Buyuk tuy! Claude Code\'a App Store red mesajini kopyalayin ve '
        '"Bu red nedenini coz, gerekli degisiklikleri yap" deyin. '
        'Cogu zaman Claude kodu duzeltip Privacy manifest, entitlement veya '
        'code signing sorunlarini otomatik cozer.',
        'tip'
    )

    doc.h2('Google Play vs App Store Karsilastirmasi')
    doc.table(
        ['Kriter',          'Google Play',               'App Store'],
        [
            ['Kayit Ucreti',    '$25 tek seferlik',          '$99/yil'],
            ['Inceleme Suresi', '~3-7 gun (ilk surum)',       '~24-72 saat'],
            ['Red Orani',       'Dusuk (~%5)',                'Yuksek (~%30-40 ilk surum)'],
            ['Esneklik',        'Daha esnek politikalar',     'Cok kati kurallar'],
            ['Gelir Potansiyeli','Genis kullanici kitlelesi', 'Daha yuksek harcama yapan kullanicilar'],
            ['Test Sureci',     'Dahili test zorunlu degil',  'TestFlight onerilen'],
            ['Guncelleme',      'Hizli (~saatler)',           'Her surum inceleme gerektirir'],
        ],
        widths=[110, 155, 206]
    )


def bolum5_mobil_mac(doc):
    """5.3 Mac bolumu zaten bolum5_mobil_windows icinde islendi — stub."""
    pass


def bolum5_desktop(doc):
    """5.4 Desktop bolumu zaten bolum5_mobil_windows icinde islendi — stub."""
    pass


def main():
    doc = Doc()
    print("Icerik olusturuluyor — Sayfa 60-80...")

    kapak_sayfasi(doc)
    icindekiler(doc)
    bolum1_giris(doc)
    bolum1_ek_ve_bolum2_baslangic(doc)
    bolum2_devami(doc)
    bolum3_claude_ekosistemi(doc)
    bolum4_claude_code(doc)
    bolum5_projeler_baslangic(doc)
    bolum5_mobil_windows(doc)
    bolum5_mobil_mac(doc)
    bolum5_desktop(doc)
    bolum6_store(doc)

    pages = doc.save('yapay_zeka_ogreniyorum_p1_80.pdf')
    print(f"\nTamamlandi! Toplam {pages} sayfa uretildi.")
    print("Dosya: yapay_zeka_ogreniyorum_p1_80.pdf")


if __name__ == '__main__':
    main()
