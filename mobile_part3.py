#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Claude Code ile Mobil Uygulama Rehberi — Part 3
Bolum 6: React Native ve Expo Derinlemesine
"""
from mobile_pdf_engine import Doc, PW, PH, ML, MR, MT, MB, CW, HDR_H
from mobile_pdf_engine import NAVY, ORANGE, WHITE, BLACK, GRAY_BG, GRAY_DARK


def bolum6_react_native_expo(doc):
    """Bolum 6: React Native ve Expo Derinlemesine"""

    doc.section_cover(
        6,
        'React Native ve Expo Derinlemesine',
        'Tek kod tabaniyla Android + iOS',
        'Bu bolumde React Native\'in ne oldugunu, Expo\'nun nasil calistigini, '
        'Managed vs Bare workflow farkini ve EAS Build sistemini detayli '
        'olarak inceliyoruz.',
    )

    # ── 6.1 React Native Nedir ─────────────────────────────────
    doc.new_page('Bolum 6: React Native ve Expo')
    doc.h1('6.1  React Native Nedir?')
    doc.sp(4)
    doc.text(
        'React Native, Facebook (Meta) tarafindan gelistirilen, JavaScript '
        've React kullanarak hem Android hem iOS icin GERCEK native '
        'uygulamalar yazmanizi saglayan bir framework\'tur. "Gercek native" '
        'derken kastimiz: arayuzler tarayici icinde degil, isletim sisteminin '
        'kendi native bilesenleri uzerinden render edilir.'
    )

    doc.h2('React Native\'in Avantajlari')
    doc.bullets([
        'Tek kod tabani: Ayni kodu Android VE iOS icin yazarsiniz, %90+ kod '
        'paylasimi',
        'Hot Reload: Kodu kaydettiginizde uygulama anlik guncellenir, '
        'yeniden derleme gerekmez',
        'Buyuk ekosistem: npm uzerinde binlerce hazir kutuphane (kamera, '
        'harita, bildirim, vs.)',
        'Performans: Native bilesenler kullandigi icin web-tabanli '
        'cozumlerden (Cordova/Ionic) cok daha hizlidir',
        'Is gucu: Dunyada en cok kullanilan cross-platform framework, bol '
        'kaynak ve topluluk destegi',
    ])

    doc.h2('React Native vs Diger Secenekler')
    doc.table(
        ['Framework',       'Dil',              'Performans',  'Ogrenme Egrisi'],
        [
            ['React Native',    'JavaScript/TS',    'Cok iyi',      'Orta'],
            ['Flutter',         'Dart',             'Cok iyi',      'Orta'],
            ['Swift/Kotlin',    'Swift + Kotlin',   'En iyi',       'Yuksek (2 dil)'],
            ['Cordova/Ionic',   'JavaScript',        'Orta-Dusuk',   'Kolay'],
        ],
        widths=[120, 130, 110, 111]
    )
    doc.sp(6)
    doc.box(
        'Bu rehberde React Native + Expo kullaniyoruz cunku Claude Code ile '
        'en uyumlu, en hizli prototipleme yapabileceginiz ve tek kod '
        'tabaniyla iki platformu da kapsayabileceginiz secenektir.',
        'tip'
    )

    # ── 6.2 Expo Nedir ─────────────────────────────────────────
    doc.new_page('Bolum 6: React Native ve Expo')
    doc.h1('6.2  Expo Nedir ve Neden Kullaniyoruz?')
    doc.sp(4)
    doc.text(
        'Expo, React Native uzerine insa edilen bir araç ve hizmet setidir. '
        'Saf React Native ile calismanin en zor kismi olan native kurulum '
        'karmasikligini (Xcode/Android Studio yapilandirmasi, native '
        'kütüphaneleri elle baglama) ortadan kaldirir.'
    )

    doc.h2('Expo\'nun Sagladigi Kolaylik')
    doc.bullets([
        'Tek komutla proje olusturma: npx create-expo-app',
        'Expo Go uygulamasiyla telefonunuzda aninda test (derleme '
        'gerekmeden)',
        'EAS Build: Bulutta derleme — Windows\'tan iOS derleyebilme dahil',
        'Hazir modul kutuphanesi: kamera, konum, bildirim, dosya sistemi '
        'gibi yuzlerce native ozellik tek satirla kullanilabilir',
        'OTA (Over-The-Air) guncelleme: Magaza onayina gerek olmadan JS '
        'kod guncellemesi gonderebilme',
    ])

    # ── 6.3 Managed vs Bare ────────────────────────────────────
    doc.new_page('Bolum 6: React Native ve Expo')
    doc.h1('6.3  Managed Workflow vs Bare Workflow')
    doc.sp(4)
    doc.text(
        'Expo iki farkli calisma modeli sunar. Hangisini secmeniz gerektigi '
        'projenizin native ozellik ihtiyacina baglidir.'
    )
    doc.table(
        ['Kriter',           'Managed Workflow',              'Bare Workflow'],
        [
            ['Native klasor',    'Yok (Expo yonetir)',            'Var (android/, ios/ klasorleri)'],
            ['Kurulum karmasik.','Cok dusuk',                      'Yuksek (Xcode/Android Studio gerekir)'],
            ['Ozel native kod',  'Sinirli (Expo modulleri ile)',   'Tam ozgurluk'],
            ['EAS Build',        'Tam destek',                     'Tam destek'],
            ['Onerilen',         'Coğu uygulama icin (baslangic)', 'Cok ozel native entegrasyon gerektiginde'],
        ],
        widths=[110, 180, 181]
    )
    doc.sp(6)
    doc.box(
        'Yeni baslayanlar icin her zaman Managed Workflow ile baslayin. '
        'Expo, 2023\'ten itibaren "Continuous Native Generation" (CNG) '
        'sayesinde gerektiginde native klasorleri otomatik olusturabiliyor, '
        'bu yuzden Bare Workflow\'a gecis ihtiyaci eskisi kadar yaygin degil.',
        'tip'
    )

    # ── 6.4 Expo Go vs Dev Client ──────────────────────────────
    doc.new_page('Bolum 6: React Native ve Expo')
    doc.h1('6.4  Expo Go vs Expo Dev Client')
    doc.sp(4)
    doc.text(
        'Test sirasinda iki farkli uygulama kullanabilirsiniz: Expo Go '
        '(magazadan indirilen genel test uygulamasi) veya Expo Dev Client '
        '(sizin projenize ozel derlenen test uygulamasi).'
    )

    doc.h2('Ne Zaman Hangisi?')
    doc.bullets([
        'Expo Go: Basit projelerde, sadece Expo\'nun resmi SDK\'sindaki '
        'modulleri kullaniyorsaniz yeterlidir. Kurulum gerektirmez, '
        'Play Store/App Store\'dan direkt indirilir',
        'Expo Dev Client: Kamera, Bluetooth, ucuncu parti SDK (orn. '
        'RevenueCat, AdMob) gibi native modul gerektiren her durumda '
        'ZORUNLUDUR',
        'AdMob, RevenueCat, Adapty gibi bu rehberde anlatacagimiz hemen tum '
        'gelir araclari Expo Go\'da CALISMAZ — Dev Client gerektirir',
    ])
    doc.code(
        '# Expo Dev Client ekleme:\n'
        'npx expo install expo-dev-client\n\n'
        '# Ozel dev client derleme (Android):\n'
        'eas build --profile development --platform android\n\n'
        '# Derlenen APK\'yi indirip telefona kurun, ardindan:\n'
        'npx expo start --dev-client',
        'Terminal'
    )
    doc.box(
        'Bu rehberin sonunda AdMob, Adapty veya RevenueCat eklediginizde '
        'Expo Go ile test edemeyeceginizi unutmayin — Dev Client derlemesi '
        'gerekecek. Bu, projenin dogal bir asamasidir, hata degildir.',
        'warning'
    )

    # ── 6.5 EAS Build ──────────────────────────────────────────
    doc.new_page('Bolum 6: React Native ve Expo')
    doc.h1('6.5  EAS Build — Bulutta Derleme Sistemi')
    doc.sp(4)
    doc.text(
        'EAS (Expo Application Services) Build, uygulamanizi kendi '
        'bilgisayariniz yerine Expo\'nun bulut sunucularinda derler. '
        'Bu sayede Windows\'tan iOS uygulamasi derleyebilirsiniz — Apple\'in '
        'kurali iOS derlemesinin bir Mac\'te yapilmasini sart kilar, ama '
        'EAS bu Mac\'i bulutta sizin yerinize calistirir.'
    )
    doc.code(
        '# EAS CLI kurulumu:\n'
        'npm install -g eas-cli\n\n'
        '# Expo hesabiniza giris:\n'
        'eas login\n\n'
        '# Projeyi EAS\'e bagla:\n'
        'eas init\n\n'
        '# eas.json yapilandirma dosyasi olusturma:\n'
        'eas build:configure\n\n'
        '# Android APK/AAB derleme (test icin APK, yayinlamak icin AAB):\n'
        'eas build --platform android --profile preview\n\n'
        '# iOS IPA derleme (Apple Developer hesabi gerekir):\n'
        'eas build --platform ios --profile preview\n\n'
        '# Her ikisini birlikte derleme:\n'
        'eas build --platform all',
        'Terminal'
    )

    doc.h2('EAS Build Profilleri')
    doc.table(
        ['Profil',       'Kullanim',                          'Cikti'],
        [
            ['development',  'Dev Client ile gelistirme testi',    'APK / Simulator IPA'],
            ['preview',      'Beta test, ekip ici test',           'APK / Ad Hoc IPA'],
            ['production',   'Magaza yayinlamasi',                  'AAB / App Store IPA'],
        ],
        widths=[100, 220, 151]
    )
    doc.sp(6)
    doc.box(
        'EAS Build\'in ucretsiz plani ayda sinirli derleme hakki sunar. '
        'Sik derleme yapan projeler icin EAS\'in ucretli planlarini '
        'degerlendirin (aylik $29\'dan baslar).',
        'info'
    )

    # ── 6.6 EAS Submit ─────────────────────────────────────────
    doc.new_page('Bolum 6: React Native ve Expo')
    doc.h1('6.6  EAS Submit — Otomatik Magaza Yukleme')
    doc.sp(4)
    doc.text(
        'EAS Build ile derledikten sonra EAS Submit komutuyla dosyayi '
        'dogrudan Google Play Console veya App Store Connect\'e '
        'yukleyebilirsiniz — elle indirip yuklemenize gerek kalmaz.'
    )
    doc.code(
        '# Android icin Play Console\'a otomatik yukleme:\n'
        'eas submit --platform android --latest\n\n'
        '# iOS icin App Store Connect\'e otomatik yukleme:\n'
        'eas submit --platform ios --latest\n\n'
        '# Gerekli: Google Play service account JSON dosyasi\n'
        '# Gerekli: Apple App Store Connect API anahtari',
        'Terminal'
    )

    # ── 6.7 Claude Code ile Expo İş Akışı ──────────────────────
    doc.new_page('Bolum 6: React Native ve Expo')
    doc.h1('6.7  Claude Code ile Expo Calisma Akisi')
    doc.sp(4)
    doc.text(
        'Artik Expo\'nun temellerini anladığınıza gore, Claude Code\'a nasil '
        'talimat vereceğinizin pratik akisina bakalim.'
    )
    doc.code(
        '# 1. Yeni proje olusturma:\n'
        'npx create-expo-app benim-uygulamam --template\n'
        'cd benim-uygulamam\n\n'
        '# 2. Claude Code\'u baslatin:\n'
        'claude\n\n'
        '# 3. Claude\'a projeyi tanitin:\n'
        '> "Bu bos bir Expo projesi. TypeScript kullaniyoruz.\n'
        '>  Navigasyon icin expo-router kuralim. Tab bar ile\n'
        '>  3 sekme olsun: Ana Sayfa, Kesfet, Profil."\n\n'
        '# 4. Claude paketleri kurar, dosyalari olusturur\n'
        '# 5. Test icin:\n'
        'npx expo start\n'
        '# QR kodu telefonunuzdaki Expo Go ile okutun',
        'Terminal'
    )
    doc.box(
        'Claude Code\'a her zaman "TypeScript kullaniyoruz" gibi proje '
        'tercihlerinizi en basta CLAUDE.md dosyasina yazdırın. Boylece her '
        'oturumda bu tercihler hatirlanir ve tutarli kod uretilir.',
        'tip'
    )
