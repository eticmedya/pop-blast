#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Claude Code ile Mobil Uygulama Rehberi — Part 2
Bolum 4: Windows'ta Mobil Gelistirme Ortami Kurulumu
Bolum 5: Mac'te Mobil Gelistirme Ortami Kurulumu
"""
from mobile_pdf_engine import Doc, PW, PH, ML, MR, MT, MB, CW, HDR_H
from mobile_pdf_engine import NAVY, ORANGE, WHITE, BLACK, GRAY_BG, GRAY_DARK


def bolum4_windows_ortam(doc):
    """Bolum 4: Windows'ta Mobil Gelistirme Ortami Kurulumu"""

    doc.section_cover(
        4,
        'Windows\'ta Mobil Gelistirme Ortami Kurulumu',
        'Windows bilgisayarinizdan mobil uygulama gelistirme',
        'Bu bolumde Windows\'ta Node.js, Android Studio, emulator ve Expo CLI '
        'kurulumunu adim adim, hic deneyimi olmayan biri icin aciklıyoruz.',
    )

    # ── 4.1 Node.js ────────────────────────────────────────────
    doc.new_page('Bolum 4: Windows\'ta Mobil Gelistirme Ortami')
    doc.h1('4.1  Node.js Kurulumu')
    doc.sp(4)
    doc.text(
        'Node.js, JavaScript kodunu bilgisayarinizda calistiran bir programdir. '
        'Claude Code, React Native, Expo — hepsi Node.js uzerine kuruludur. '
        'Bu yuzden ilk adim her zaman Node.js kurulumudur.'
    )
    doc.bullets([
        '1. nodejs.org adresine gidin',
        '2. "LTS" (Long Term Support) etiketli surumu indirin — en kararli '
        'surumdur',
        '3. Indirilen .msi dosyasini calistirin, "Next" diyerek ilerleyin',
        '4. Kurulum bittiginde bilgisayarinizi yeniden baslatin',
        '5. PowerShell veya CMD\'yi acin, asagidaki komutlarla dogrulayin',
    ])
    doc.code(
        'node --version\n'
        '# v20.x.x veya benzeri bir surum gormeli\n\n'
        'npm --version\n'
        '# 10.x.x veya benzeri',
        'PowerShell'
    )
    doc.box(
        'PowerShell\'i Baslat menusunden aratip acabilirsiniz. Yonetici '
        'olarak calistirmaniz gerekmez, normal kullanici yetkisi yeterlidir.',
        'info'
    )

    # ── 4.2 Claude Code Kurulumu ───────────────────────────────
    doc.new_page('Bolum 4: Windows\'ta Mobil Gelistirme Ortami')
    doc.h1('4.2  Claude Code Kurulumu (Windows)')
    doc.sp(4)
    doc.code(
        '# Claude Code\'u global olarak kurun:\n'
        'npm install -g @anthropic-ai/claude-code\n\n'
        '# Kurulumu dogrulayin:\n'
        'claude --version\n\n'
        '# Proje klasoru olusturun ve icine girin:\n'
        'mkdir benim-mobil-uygulamam\n'
        'cd benim-mobil-uygulamam\n\n'
        '# Claude Code\'u baslatin:\n'
        'claude\n'
        '# Ilk calistirmada Anthropic hesabinizla giris yapmaniz istenir',
        'PowerShell'
    )

    # ── 4.3 Android Studio ─────────────────────────────────────
    doc.new_page('Bolum 4: Windows\'ta Mobil Gelistirme Ortami')
    doc.h1('4.3  Android Studio ve Emulator Kurulumu')
    doc.sp(4)
    doc.text(
        'Android Studio, Google\'in resmi Android gelistirme aracidir. '
        'Telefon emulatoru (sanal Android telefon) icin gereklidir; gercek '
        'bir Android telefonunuz varsa Expo Go uygulamasiyla emulator '
        'gerekmeden de test edebilirsiniz, ama emulator kurmak yine de '
        'tavsiye edilir.'
    )
    doc.bullets([
        '1. developer.android.com/studio adresinden Android Studio\'yu indirin',
        '2. Kurulum sirasinda "Standard" kurulum tipini secin',
        '3. Kurulum bitince Android Studio\'yu acin, SDK\'larin inmesini '
        'bekleyin (birkac GB, internet hizina gore 10-30 dakika)',
        '4. "More Actions" > "Virtual Device Manager" acin',
        '5. "Create Device" tiklayin, Pixel 8 veya benzeri bir model secin',
        '6. Sistem imaji (system image) olarak en guncel Android surumunu '
        'indirin',
        '7. Emulatoru baslatip sanal telefonun acildiginindan emin olun',
    ])
    doc.code(
        '# Ortam degiskenlerini kontrol edin (PowerShell):\n'
        '# ANDROID_HOME degiskeni otomatik ayarlanir, kontrol icin:\n'
        '$env:ANDROID_HOME\n'
        '# C:\\Users\\KullaniciAdi\\AppData\\Local\\Android\\Sdk gibi\n'
        'bir yol gormelisiniz',
        'PowerShell'
    )
    doc.box(
        'Android Studio kurulumu en az 8 GB bos disk alani gerektirir ve '
        'emulator calisirken bilgisayarinizin en az 8 GB RAM\'e sahip olmasi '
        'onerilir. Eski/dusuk donanimli bilgisayarlarda emulator yerine '
        'gercek telefon + Expo Go kullanin.',
        'warning'
    )

    # ── 4.4 Expo CLI ───────────────────────────────────────────
    doc.new_page('Bolum 4: Windows\'ta Mobil Gelistirme Ortami')
    doc.h1('4.4  Expo CLI Kurulumu')
    doc.sp(4)
    doc.code(
        '# Expo CLI global kurulum:\n'
        'npm install -g @expo/cli\n\n'
        '# Dogrulama:\n'
        'expo --version\n\n'
        '# Telefonunuza Expo Go uygulamasini indirin:\n'
        '# Play Store\'dan "Expo Go" aratip yukleyin (ucretsiz)',
        'PowerShell'
    )
    doc.text(
        'Expo Go, gelistirme sirasinda telefonunuzda QR kod okutarak '
        'uygulamanizi anlik test etmenizi saglayan bir uygulamadir. '
        'Bilgisayar ve telefon ayni Wi-Fi agina bagli olmalidir.'
    )

    # ── 4.5 VS Code ────────────────────────────────────────────
    doc.new_page('Bolum 4: Windows\'ta Mobil Gelistirme Ortami')
    doc.h1('4.5  VS Code Kurulumu (Opsiyonel Ama Onerilir)')
    doc.sp(4)
    doc.text(
        'Claude Code, terminal uzerinden calisir; bir kod editorune ihtiyaciniz '
        'olmaz. Ancak dosyalarinizi gozle gormek, kodu okumak isterseniz '
        'Visual Studio Code kullanmaniz iyi bir alistirmadir.'
    )
    doc.bullets([
        'code.visualstudio.com adresinden indirin ve kurun',
        'Kurulum sirasinda "Add to PATH" ve "Open with Code" secimlerini '
        'isaretleyin',
        'Claude Code\'un Claude Code uzantisi (extension) VS Code icinden de '
        'kullanilabilir; terminal panelinde "claude" yazarak baslatin',
    ])
    doc.box(
        'Windows\'ta tum kurulum islemleri tamamlandiginda Bolum 6\'daki '
        '"React Native ve Expo Derinlemesine" bolumune gecebilirsiniz. '
        'Mac kullanmiyorsaniz Bolum 5\'i atlayabilirsiniz.',
        'tip'
    )


def bolum5_mac_ortam(doc):
    """Bolum 5: Mac'te Mobil Gelistirme Ortami Kurulumu"""

    doc.section_cover(
        5,
        'Mac\'te Mobil Gelistirme Ortami Kurulumu',
        'MacBook ile hem Android hem iOS gelistirme',
        'Bu bolumde macOS\'ta Node.js, Xcode, Android Studio ve Expo CLI '
        'kurulumunu adim adim aciklıyoruz. Mac, iOS derlemesi yapabilen tek '
        'platformdur.',
    )

    # ── 5.1 Node.js (Mac) ──────────────────────────────────────
    doc.new_page('Bolum 5: Mac\'te Mobil Gelistirme Ortami')
    doc.h1('5.1  Node.js Kurulumu (macOS)')
    doc.sp(4)
    doc.text(
        'Mac\'te Node.js kurmanin en kolay yolu Homebrew paket yoneticisidir. '
        'Homebrew, macOS icin bir "uygulama magazasi" gibi calisir; terminal '
        'uzerinden tek satirla program kurmanizi saglar.'
    )
    doc.code(
        '# Once Homebrew\'u kurun (Terminal uygulamasini acin):\n'
        '/bin/bash -c "$(curl -fsSL '
        'https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"\n\n'
        '# Homebrew ile Node.js LTS kurun:\n'
        'brew install node@20\n\n'
        '# Dogrulama:\n'
        'node --version\n'
        'npm --version',
        'Terminal (macOS)'
    )
    doc.box(
        'Homebrew kurulumu sirasinda terminalde Mac sifrenizi girmeniz '
        'istenecektir; bu normaldir ve yazdiginiz karakterler ekranda '
        'gorunmez.',
        'info'
    )

    # ── 5.2 Claude Code (Mac) ──────────────────────────────────
    doc.new_page('Bolum 5: Mac\'te Mobil Gelistirme Ortami')
    doc.h1('5.2  Claude Code Kurulumu (macOS)')
    doc.sp(4)
    doc.code(
        '# Claude Code\'u global kurun:\n'
        'npm install -g @anthropic-ai/claude-code\n\n'
        '# Dogrulayin:\n'
        'claude --version\n\n'
        '# Proje klasoru olusturup Claude Code\'u baslatin:\n'
        'mkdir ~/Projeler/benim-mobil-uygulamam\n'
        'cd ~/Projeler/benim-mobil-uygulamam\n'
        'claude',
        'Terminal (macOS)'
    )

    # ── 5.3 Xcode ──────────────────────────────────────────────
    doc.new_page('Bolum 5: Mac\'te Mobil Gelistirme Ortami')
    doc.h1('5.3  Xcode Kurulumu — iOS Gelistirmenin Kalbi')
    doc.sp(4)
    doc.text(
        'Xcode, Apple\'in resmi gelistirme aracidir ve iOS uygulamasi '
        'derlemenin TEK yoludur. Sadece Mac\'te calisir. Indirme boyutu '
        '15 GB+ oldugundan sabirli olun, hizli internet kullanin.'
    )
    doc.bullets([
        '1. App Store uygulamasini acin, "Xcode" aratin, indirin (ucretsiz)',
        '2. Indirme tamamlandiktan sonra Xcode\'u acin',
        '3. "Install Additional Components" penceresi cikarsa onaylayin',
        '4. Lisans sozlesmesini kabul edin',
        '5. Terminal\'den komut satiri araclarini kurun',
    ])
    doc.code(
        '# Xcode Command Line Tools kurulumu:\n'
        'xcode-select --install\n\n'
        '# CocoaPods kurulumu (iOS bagimliliklari icin):\n'
        'sudo gem install cocoapods\n\n'
        '# Dogrulamalar:\n'
        'xcodebuild -version\n'
        'pod --version',
        'Terminal (macOS)'
    )
    doc.box(
        'Xcode kurulumu ortalama 1-2 saat surebilir (indirme + kurulum). '
        'Bu sureyi Apple Developer hesap basvurunuzu yaptiginiz zamana '
        'denk getirebilirsiniz, boylece bekleme sureleri ust uste biner.',
        'tip'
    )

    # ── 5.4 iOS Simulator ──────────────────────────────────────
    doc.new_page('Bolum 5: Mac\'te Mobil Gelistirme Ortami')
    doc.h1('5.4  iOS Simulator Kullanimi')
    doc.sp(4)
    doc.text(
        'iOS Simulator, gercek bir iPhone\'a ihtiyac duymadan Mac '
        'ekraninizda iOS uygulamanizi calistirip test etmenizi saglar.'
    )
    doc.code(
        '# Xcode uzerinden simulator acma:\n'
        '# Xcode > Window > Devices and Simulators\n\n'
        '# Veya Expo projesinden direkt baslatma:\n'
        'npx expo start --ios\n\n'
        '# Belirli bir cihaz modeli secerek baslatma:\n'
        'npx expo run:ios --device "iPhone 16 Pro"',
        'Terminal (macOS)'
    )

    # ── 5.5 Android Studio (Mac) ───────────────────────────────
    doc.new_page('Bolum 5: Mac\'te Mobil Gelistirme Ortami')
    doc.h1('5.5  Android Studio Kurulumu (macOS)')
    doc.sp(4)
    doc.text(
        'Mac\'te de Android uygulamasi gelistirebilir ve test edebilirsiniz. '
        'Boylece tek bilgisayardan hem iOS hem Android\'i yonetebilirsiniz — '
        'bu Mac\'in en buyuk avantajidir.'
    )
    doc.bullets([
        '1. developer.android.com/studio adresinden Mac surumunu indirin '
        '(Apple Silicon veya Intel\'e gore secin)',
        '2. .dmg dosyasini acip Android Studio\'yu Applications klasorune '
        'surukleyin',
        '3. Ilk acilista SDK kurulum sihirbazini tamamlayin',
        '4. Virtual Device Manager\'dan bir emulator olusturun',
        '5. Expo CLI ile Android emulatorde test edin: npx expo run:android',
    ])
    doc.box(
        'Apple Silicon (M1/M2/M3/M4) Mac\'lerde Android emulator performansi '
        'cok iyidir. Intel Mac\'lerde biraz daha yavas calisabilir.',
        'info'
    )

    # ── 5.6 Karsilastirma ───────────────────────────────────────
    doc.new_page('Bolum 5: Mac\'te Mobil Gelistirme Ortami')
    doc.h1('5.6  Windows vs Mac: Hangisini Kullanmaliyim?')
    doc.sp(4)
    doc.table(
        ['Kriter',              'Windows',                       'Mac'],
        [
            ['Android gelistirme',  'Tam destek',                    'Tam destek'],
            ['iOS gelistirme',      'Sadece EAS cloud build',        'Yerel + Simulator + Xcode'],
            ['App Store yayinlama', 'EAS Build ile mumkun',          'Dogrudan, daha hizli'],
            ['Maliyet',             'Genelde daha ucuz donanim',     'Daha yuksek baslangic maliyeti'],
            ['Onerilen',            'Sadece Android hedefliyorsaniz','iOS + Android ikisi de hedefse'],
        ],
        widths=[110, 175, 186]
    )
    doc.sp(6)
    doc.box(
        'Eger bircaginiz hem App Store hem Google Play\'de yayinlamak '
        'istiyorsaniz, uzun vadede bir Mac (hatta ikinci el bir MacBook Air) '
        'edinmek size zaman kazandirir. Ancak Windows + EAS Build cloud '
        'derleme kombinasyonu da tamamen calisir cozumdurur, Mac sart degildir.',
        'tip'
    )
