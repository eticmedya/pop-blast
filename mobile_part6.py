#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Claude Code ile Mobil Uygulama Rehberi — Part 6
Bolum 10: Fikir Bulma ve Pazar Arastirmasi
Bolum 11: AdMob ile Reklam Geliri
Bolum 12: Adapty ile Abonelik Sistemi
Bolum 13: RevenueCat ile Abonelik Sistemi
Kapanis ve Kaynaklar
"""
from mobile_pdf_engine import Doc, PW, PH, ML, MR, MT, MB, CW, HDR_H
from mobile_pdf_engine import NAVY, ORANGE, WHITE, BLACK, GRAY_BG, GRAY_DARK


def bolum10_fikir_bulma(doc):
    """Bolum 10: Fikir Bulma ve Pazar Arastirmasi"""

    doc.section_cover(
        10,
        'Fikir Bulma ve Pazar Arastirmasi',
        'Hangi uygulamayi yapmaliyim?',
        'Bu bolumde kazandiran uygulama fikirlerini nasil bulacaginizi, '
        'rakip analizini trustmrr.com uzerinden nasil yapacaginizi ve '
        'fikrinizi dogrulama (validation) yontemlerini aciklıyoruz.',
    )

    # ── 10.1 Neden Fikir Bulmak Zor ──────────────────────────────
    doc.new_page('Bolum 10: Fikir Bulma ve Pazar Arastirmasi')
    doc.h1('10.1  "Hangi Uygulamayi Yapmaliyim?" Sorusu')
    doc.sp(4)
    doc.text(
        'Cok kisi Claude Code\'u ogrendikten sonra ilk soruyla karsilasir: '
        '"Ne yapayim?" Iyi haber: Bu sorunun cevabi yaraticilikta degil, '
        'ARASTIRMADADIR. En basarili bagimsiz gelistiriciler (indie '
        'developer) genellikle %100 orijinal bir fikir bulmaz; var olan '
        'bir ihtiyaca daha iyi, daha basit veya daha ucuz bir cozum '
        'sunarlar.'
    )
    doc.h2('Iyi Bir Uygulama Fikrinin Ozellikleri')
    doc.bullets([
        'Belirli, dar bir kullanici kitlesine hizmet eder (herkese hitap '
        'etmeye calismak genellikle basarisiz olur)',
        'Tekrarlanan bir problemi cozer (kullanici haftada birkac kez '
        'kullanir, bir kerelik degil)',
        'Basit bir MVP (Minimum Viable Product — asgari calisan urun) '
        'ile test edilebilir',
        'Net bir gelir modeli vardir (reklamlar, abonelik veya tek '
        'seferlik satin alma)',
    ])

    # ── 10.2 trustmrr.com ile Rakip Analizi ──────────────────────
    doc.new_page('Bolum 10: Fikir Bulma ve Pazar Arastirmasi')
    doc.h1('10.2  trustmrr.com — Kanitlanmis Gelir Verileriyle Fikir Bulma')
    doc.sp(4)
    doc.text(
        'trustmrr.com, bagimsiz gelistiricilerin (indie maker) '
        'uygulamalarinin DOGRULANMIS aylik gelirlerini (MRR — Monthly '
        'Recurring Revenue) gosteren bir platformdur. Marc Lou tarafindan '
        'gelistirilmistir ve "build in public" (yapim surecini acik '
        'paylasma) hareketinin bir parcasidir. Buradaki gelir rakamlari '
        'Stripe, Lemon Squeezy veya Polar gibi odeme saglayicilarina '
        'baglanarak dogrulanir — yani kullanicilarin kendi beyan ettigi '
        'rakamlar degil, gercek satis verileridir.'
    )
    doc.h2('trustmrr.com\'u Nasil Kullanmali?')
    doc.bullets([
        '1. Siteye girip kategori bazinda (mobil uygulama, SaaS, vs.) '
        'gelir siralamasina bakin',
        '2. Sizi ilgilendiren bir kategoride yuksek gelirli ama BASIT '
        'gorunen uygulamalari bulun — basitlik, sizin de yapabileceginiz '
        'anlamina gelir',
        '3. O uygulamanin App Store/Play Store sayfasina gidip ekran '
        'goruntulerini, yorumlarini ve ozellik listesini inceleyin',
        '4. "Bu uygulamayi nasil daha iyi/basit/ucuz yapabilirim?" '
        'sorusunu sorun',
        '5. Yorumlarda sikayet edilen noktalari not edin — bu sizin '
        'rekabet avantajiniz olabilir',
    ])
    doc.box(
        'trustmrr.com\'daki bir uygulamanin aylik 5.000$ kazandigini '
        'gormeniz, "ben de bu kategoride bir uygulama yapip benzer gelir '
        'elde edebilirim" anlamina gelmez — ama o kategoride GERCEK bir '
        'talep oldugunu kanitlar. Bu, kor bir fikirle baslamaktan cok '
        'daha guvenli bir baslangic noktasidir.',
        'tip'
    )

    # ── 10.3 Fikir Dogrulama ──────────────────────────────────────
    doc.new_page('Bolum 10: Fikir Bulma ve Pazar Arastirmasi')
    doc.h1('10.3  Fikrinizi Kodlamadan Once Dogrulama')
    doc.sp(4)
    doc.text(
        'Aylarca kod yazip kimsenin istemedigi bir uygulama yapmaktan '
        'kacinmak icin, kodlamaya baslamadan once fikrinizi ucretsiz '
        'yontemlerle test edin.'
    )
    doc.bullets([
        'Reddit\'te ilgili subreddit\'lerde ("hangi uygulamayi '
        'kullanirdiniz" gibi sorular) arastirma yapin',
        'App Store/Play Store\'da benzer uygulamalarin 1-3 yildizli '
        'yorumlarini okuyun — kullanicilarin neden sikayet ettigini '
        'gorun, bu sizin icin bir ozellik listesi olusturur',
        'Basit bir tek sayfalik tanitim (landing page) yapip e-posta '
        'toplayin — kimse e-posta birakmiyorsa talep yoktur',
        'Kucuk bir Facebook/Reddit/Discord toplulugunda fikrinizi '
        'paylasip geri bildirim isteyin',
    ])

    # ── 10.4 Gelir Modeli Secimi ────────────────────────────────
    doc.new_page('Bolum 10: Fikir Bulma ve Pazar Arastirmasi')
    doc.h1('10.4  Hangi Gelir Modelini Secmeliyim?')
    doc.sp(4)
    doc.table(
        ['Model',            'Ne Zaman Uygun',                        'Arac'],
        [
            ['Reklam (Ads)',     'Genis kullanici tabani, ucretsiz '
                                  'kullanim onemli',                  'AdMob'],
            ['Abonelik',         'Surekli deger sunan uygulamalar '
                                  '(fitness, uretkenlik, AI)',         'RevenueCat / Adapty'],
            ['Tek seferlik satin alma', 'Bir kerelik arac/oyun, '
                                          'tekrar odeme istemiyorsaniz', 'App Store / Play '
                                                                          'Store IAP'],
            ['Freemium + Abonelik', 'Temel ozellikler ucretsiz, '
                                     'premium ozellikler ucretli',     'RevenueCat / Adapty'],
        ],
        widths=[110, 211, 100]
    )
    doc.sp(6)
    doc.box(
        'Bu rehberin kalan bolumlerinde uc temel gelir aracini detayli '
        'inceleyecegiz: AdMob (reklam), Adapty ve RevenueCat (abonelik '
        'yonetimi). Cogu basarili uygulama bunlardan birini, bazen '
        'ikisini birden (reklam + abonelik) kullanir.',
        'info'
    )


def bolum11_admob(doc):
    """Bolum 11: AdMob ile Reklam Geliri"""

    doc.section_cover(
        11,
        'AdMob ile Reklam Geliri',
        'Google\'in reklam agi ile mobil uygulamanizdan para kazanin',
        'Bu bolumde AdMob\'un ne oldugunu, hesap acmayi, reklam birimi '
        'olusturmayi ve banner/interstitial/rewarded reklam turlerini '
        'Expo projesine entegre etmeyi adim adim aciklıyoruz.',
    )

    # ── 11.1 AdMob Nedir ───────────────────────────────────────
    doc.new_page('Bolum 11: AdMob ile Reklam Geliri')
    doc.h1('11.1  AdMob Nedir, Nasil Calisir?')
    doc.sp(4)
    doc.text(
        'Google AdMob, mobil uygulamalar icin Google\'in reklam agini '
        'kullanan bir reklam gosterim platformudur. Uygulamanizda reklam '
        'alani (ad unit) tanimlarsiniz, Google bu alanlara otomatik '
        'olarak alakali reklamlari doldurur ve siz goruntuleme/tiklama '
        'basina gelir kazanirsiniz.'
    )
    doc.h2('Reklam Turleri')
    doc.table(
        ['Tur',              'Aciklama',                              'Kullanim Yeri'],
        [
            ['Banner',           'Ekranin ust/alt kisminda kucuk, '
                                  'surekli gorunen reklam',            'Liste ekranlari'],
            ['Interstitial',     'Ekrani kaplayan, gecisler arasi '
                                  'tam sayfa reklam',                  'Seviye gecisi, '
                                                                         'ekran degisimi'],
            ['Rewarded',         'Kullanici izleyince odul kazanir '
                                  '(ekstra hak, kilit acma)',          'Oyunlar, ozellik '
                                                                         'kilidi acma'],
            ['Native',           'Uygulama tasarimina uyumlu, dogal '
                                  'gorunen reklam',                    'Icerik akislari'],
        ],
        widths=[90, 211, 120]
    )

    # ── 11.2 AdMob Hesap Acma ──────────────────────────────────
    doc.new_page('Bolum 11: AdMob ile Reklam Geliri')
    doc.h1('11.2  AdMob Hesabi Acma')
    doc.sp(4)
    doc.bullets([
        '1. admob.google.com adresine gidin, Google hesabinizla giris '
        'yapin',
        '2. Odeme bilgilerinizi (ulke: Turkiye, adres, banka hesabi) '
        'girin',
        '3. "Uygulama Ekle" diyerek uygulamanizi tanimlayin — eger henuz '
        'magazada yayinlanmadiysa "Henuz magazalarda listelenmiyor" '
        'secenegini isaretleyebilirsiniz',
        '4. Uygulama icin reklam birimleri (ad units) olusturun: bir '
        'banner, bir interstitial, bir rewarded',
        '5. Her reklam birimi icin size ozel bir Ad Unit ID verilir '
        '(ca-app-pub-xxxx/yyyy formatinda) — bunlari not edin',
    ])
    doc.box(
        'AdMob odemeleri belirli bir esigi (genellikle 100$) astiginizda '
        'aylik olarak banka hesabiniza yapilir. Turkiye\'deki '
        'gelistiriciler icin odeme suresi diger ulkelere gore biraz '
        'daha uzun surebilir (banka transfer islemleri nedeniyle).',
        'info'
    )

    # ── 11.3 Expo Projesine Entegrasyon ──────────────────────────
    doc.new_page('Bolum 11: AdMob ile Reklam Geliri')
    doc.h1('11.3  AdMob\'u Expo Projesine Entegre Etme')
    doc.sp(4)
    doc.text(
        'AdMob, native modul gerektirdigi icin Expo Go ile CALISMAZ. '
        'Bolum 6.4\'te belirttigimiz gibi Expo Dev Client veya EAS Build '
        'ile derlenmis bir test uygulamasi gereklidir.'
    )
    doc.code(
        '# Resmi Google Mobile Ads SDK kurulumu:\n'
        'npx expo install react-native-google-mobile-ads\n\n'
        '# app.json icine plugin ekleme:\n'
        '{\n'
        '  "expo": {\n'
        '    "plugins": [\n'
        '      [\n'
        '        "react-native-google-mobile-ads",\n'
        '        {\n'
        '          "androidAppId": "ca-app-pub-xxxx~yyyy",\n'
        '          "iosAppId": "ca-app-pub-xxxx~zzzz"\n'
        '        }\n'
        '      ]\n'
        '    ]\n'
        '  }\n'
        '}\n\n'
        '# Dev Client yeniden derleme gerekir (native kod degisti):\n'
        'eas build --profile development --platform android',
        'Terminal'
    )

    # ── 11.4 Claude Code ile Reklam Ekleme ────────────────────────
    doc.new_page('Bolum 11: AdMob ile Reklam Geliri')
    doc.h1('11.4  Claude Code ile Reklam Bilesenleri Olusturma')
    doc.sp(4)
    doc.code(
        '> "react-native-google-mobile-ads kullanarak ana ekranin\n'
        '>  altina sabit bir banner reklam ekle. Ad unit ID\'lerini\n'
        '>  .env dosyasindan oku, test modunda Google\'in test ID\'lerini\n'
        '>  kullan, production\'da gercek ID\'lere gec."\n\n'
        '> "Kullanici 3 gorev tamamladiginda bir interstitial reklam\n'
        '>  goster. Reklam cok sik gosterilmesin, ayni oturumda en\n'
        '>  fazla 2 interstitial reklam goster."\n\n'
        '> "Kullaniciya \'reklam izle, 7 gun premium kazan\' diyen bir\n'
        '>  rewarded reklam butonu ekle. Reklam basariyla tamamlaninca\n'
        '>  kullanicinin premium durumunu guncelle."',
        'Claude Code Prompt'
    )
    doc.box(
        'Test asamasinda HER ZAMAN Google\'in resmi test Ad Unit '
        'ID\'lerini kullanin. Kendi gercek reklam ID\'nizle kendi '
        'reklamlariniza tiklarsaniz Google hesabinizi askiya alabilir.',
        'warning'
    )

    # ── 11.5 Reklam Stratejisi ────────────────────────────────────
    doc.new_page('Bolum 11: AdMob ile Reklam Geliri')
    doc.h1('11.5  Kullanici Deneyimini Bozmayan Reklam Stratejisi')
    doc.sp(4)
    doc.bullets([
        'Interstitial reklamlari kullanicinin akisini kesintiye '
        'ugratmayacak doğal noktalarda gosterin (seviye sonu, kayit '
        'sonrasi), rastgele degil',
        'Ayni oturumda cok sik reklam gostermek kullanici kaybina '
        '(churn) yol acar — bir minimum bekleme suresi (örn. 60 saniye) '
        'koyun',
        'Rewarded reklamlari "zorunlu" degil "tercihe bagli odul" '
        'olarak sunun — kullanici kontrolde hissetsin',
        'Premium/abonelik satin alan kullanicilara reklam '
        'GOSTERMEYIN — bu en temel "reklamsiz deneyim" beklentisidir',
    ])


def bolum12_adapty(doc):
    """Bolum 12: Adapty ile Abonelik Sistemi"""

    doc.section_cover(
        12,
        'Adapty ile Abonelik Sistemi',
        'Kod yazmadan abonelik ekranlari ve A/B test',
        'Bu bolumde Adapty\'nin ne oldugunu, RevenueCat\'ten farkini, '
        'hesap acmayi ve mobil uygulamaniza abonelik sistemi entegre '
        'etmeyi adim adim aciklıyoruz.',
    )

    # ── 12.1 Adapty Nedir ──────────────────────────────────────
    doc.new_page('Bolum 12: Adapty ile Abonelik Sistemi')
    doc.h1('12.1  Adapty Nedir?')
    doc.sp(4)
    doc.text(
        'Adapty, mobil uygulamalarda abonelik (subscription) ve uygulama '
        'ici satin alma (IAP) yonetimini kolaylastiran bir platformdur. '
        'App Store ve Play Store\'un karmasik satin alma API\'lerini tek '
        'bir basit SDK arkasinda toplar; ayrica kod yazmadan abonelik '
        'satis ekranlari (paywall) tasarlama ve bunlari A/B test etme '
        'ozelligi sunar.'
    )
    doc.h2('Adapty\'nin Sundugu Temel Ozellikler')
    doc.bullets([
        'Cross-platform abonelik yonetimi (App Store + Play Store tek '
        'yerden)',
        'No-code Paywall Builder: Kod yazmadan surukle-birak ile satis '
        'ekrani tasarlama',
        'A/B Testing: Farkli fiyat/tasarimlarin hangisinin daha cok '
        'satis getirdigini otomatik test etme',
        'Detayli analitik: Donusum orani (conversion rate), churn '
        '(abonelik birakma) orani, gelir raporlari',
        'Sunucu tarafi makbuz dogrulama (receipt validation) — '
        'sahtekarligi onler',
    ])

    # ── 12.2 Adapty Hesabi Acma ─────────────────────────────────
    doc.new_page('Bolum 12: Adapty ile Abonelik Sistemi')
    doc.h1('12.2  Adapty Hesabi Acma ve Proje Kurma')
    doc.sp(4)
    doc.bullets([
        '1. app.adapty.io adresine gidin, ucretsiz kayit olun (aylik '
        '$10,000 gelire kadar ucretsiz plan mevcuttur)',
        '2. "Create App" ile uygulamanizi tanimlayin, iOS Bundle ID ve '
        'Android Package Name girin',
        '3. App Store Connect / Play Console ile entegrasyon icin API '
        'anahtarlarinizi Adapty paneline ekleyin (Bolum 2 ve 3\'te '
        'olusturdugunuz hesaplar)',
        '4. "Products" bolumunde abonelik urunlerinizi tanimlayin (orn. '
        'aylik, yillik plan) — bu urunler ayrica App Store Connect ve '
        'Play Console\'da da olusturulmalidir',
        '5. "Paywalls" bolumunde no-code builder ile satis ekraninizi '
        'tasarlayin',
    ])
    doc.box(
        'Abonelik urunlerini HER ZAMAN once App Store Connect ve Play '
        'Console\'da olusturmalisiniz (urun kimligi, fiyat). Adapty bu '
        'urunleri yonetir ama olusturmaz — magazalar urunun sahibidir.',
        'warning'
    )

    # ── 12.3 SDK Entegrasyonu ────────────────────────────────────
    doc.new_page('Bolum 12: Adapty ile Abonelik Sistemi')
    doc.h1('12.3  Adapty SDK\'sini Expo Projesine Ekleme')
    doc.sp(4)
    doc.code(
        '# Adapty React Native SDK kurulumu:\n'
        'npx expo install react-native-adapty\n\n'
        '# Dev Client gerekir (native modul):\n'
        'eas build --profile development --platform all\n\n'
        '# Uygulama baslangicinda Adapty\'yi aktif etme (App.tsx):\n'
        'import { adapty } from \'react-native-adapty\';\n\n'
        'adapty.activate(\'public_sdk_key_buraya\');',
        'Terminal / TypeScript'
    )
    doc.code(
        '> "Adapty SDK\'sini projeye entegre et. Uygulama acilista\n'
        '>  adapty.activate() cagrisi yap. Kullanicinin abonelik\n'
        '>  durumunu (premium mi degil mi) global bir Zustand store\'da\n'
        '>  tut ve uygulama her acildiginda Adapty\'den guncel durumu\n'
        '>  cek. Eger kullanici premium degilse, paywall ekranini\n'
        '>  Adapty panelinde tasarladigim haliyle goster."',
        'Claude Code Prompt'
    )

    # ── 12.4 Ne Zaman Adapty Secilmeli ───────────────────────────
    doc.new_page('Bolum 12: Adapty ile Abonelik Sistemi')
    doc.h1('12.4  Ne Zaman Adapty Secmeliyim?')
    doc.sp(4)
    doc.text(
        'Adapty, ozellikle paywall tasarimini sik sik degistirmek ve '
        'hangi fiyatin/tasarimin daha cok dönüştürdüğünü test etmek '
        'isteyen gelistiriciler icin guclu bir secimdir.'
    )
    doc.bullets([
        'No-code paywall builder\'a onem veriyorsaniz Adapty avantajli',
        'A/B test ozelligini aktif olarak kullanmayi planliyorsaniz '
        'Adapty\'nin bu konudaki araclari daha gelismis',
        'Eger zaten RevenueCat ekosistemine asinaysaniz (cok daha '
        'yaygin topluluk) RevenueCat\'i tercih edebilirsiniz — Bolum '
        '13\'te detaylandiriyoruz',
    ])
    doc.box(
        'Hem Adapty hem RevenueCat benzer temel sorunu cozer: magaza '
        'abonelik API\'lerinin karmasikligini basitlestirmek. Ikisini '
        'ayni anda kullanmaniza gerek yoktur — projenize birini secip '
        'devam edin.',
        'tip'
    )


def bolum13_revenuecat(doc):
    """Bolum 13: RevenueCat ile Abonelik Sistemi"""

    doc.section_cover(
        13,
        'RevenueCat ile Abonelik Sistemi',
        'Sektorun en yaygin kullanilan abonelik altyapisi',
        'Bu bolumde RevenueCat\'in ne oldugunu, hesap acmayi, urun '
        'tanimlamayi ve Claude Code ile Expo projesine entegrasyonu '
        'adim adim aciklıyoruz.',
    )

    # ── 13.1 RevenueCat Nedir ────────────────────────────────────
    doc.new_page('Bolum 13: RevenueCat ile Abonelik Sistemi')
    doc.h1('13.1  RevenueCat Nedir?')
    doc.sp(4)
    doc.text(
        'RevenueCat, mobil abonelik altyapisi konusunda piyasanin en '
        'yaygin kullanilan platformudur — binlerce uygulama tarafindan '
        'kullanilir ve buyuk bir topluluk/dokumantasyon destegi vardir. '
        'App Store ve Play Store\'un satin alma sistemlerini tek bir API '
        'arkasinda birlestirir, makbuz dogrulamasini sunucu tarafinda '
        'sizin yerinize yapar.'
    )
    doc.h2('RevenueCat\'in Temel Ozellikleri')
    doc.bullets([
        'Cross-platform abonelik/IAP yonetimi (tek SDK, iki magaza)',
        'Sunucu tarafi makbuz dogrulama ve dolandiriciliga karsi koruma',
        'Detayli gelir analitikleri (MRR, churn, LTV — kullanici basina '
        'yasam boyu deger)',
        'Webhook destegi: Abonelik durumu degistiginde kendi backend\'inize '
        '(Supabase Edge Function) bildirim gonderme',
        'Cok genis entegrasyon ekosistemi (Superwall gibi paywall '
        'araclariyla uyumlu)',
    ])

    # ── 13.2 RevenueCat Hesabi Acma ───────────────────────────────
    doc.new_page('Bolum 13: RevenueCat ile Abonelik Sistemi')
    doc.h1('13.2  RevenueCat Hesabi Acma ve Proje Kurma')
    doc.sp(4)
    doc.bullets([
        '1. app.revenuecat.com adresine gidin, ucretsiz kayit olun '
        '(aylik $2,500 gelire kadar ucretsiz "Free" plan)',
        '2. "Create new project" ile projenizi olusturun',
        '3. "Apps" bolumunde iOS ve Android uygulamalarinizi ekleyin, '
        'Bundle ID/Package Name girin',
        '4. App Store Connect icin "App-Specific Shared Secret" '
        'degerini, Play Console icin servis hesabi (service account) '
        'JSON dosyasini RevenueCat\'e yukleyin',
        '5. "Products" bolumunde abonelik urunlerinizi (App Store '
        'Connect/Play Console\'da onceden olusturulmus olmalari gerekir) '
        'RevenueCat\'e baglayın',
        '6. "Entitlements" tanimlayin (orn. "premium" yetkisi) — bu, '
        'kodunuzda kontrol edecek oldugunuz tek deger olacak',
        '7. "Offerings" ile kullaniciya sunulacak paket kombinasyonlarini '
        'belirleyin (orn. aylik + yillik birlikte sunum)',
    ])

    # ── 13.3 SDK Entegrasyonu ──────────────────────────────────────
    doc.new_page('Bolum 13: RevenueCat ile Abonelik Sistemi')
    doc.h1('13.3  RevenueCat SDK\'sini Expo Projesine Ekleme')
    doc.sp(4)
    doc.code(
        '# RevenueCat React Native SDK kurulumu:\n'
        'npx expo install react-native-purchases\n\n'
        '# Dev Client gerekir (native modul):\n'
        'eas build --profile development --platform all\n\n'
        '# Uygulama baslangicinda yapilandirma (App.tsx):\n'
        'import Purchases from \'react-native-purchases\';\n\n'
        'Purchases.configure({ apiKey: \'public_sdk_key_buraya\' });',
        'Terminal / TypeScript'
    )
    doc.code(
        '> "react-native-purchases SDK\'sini projeye entegre et.\n'
        '>  Uygulama acilista Purchases.configure() cagrisi yap.\n'
        '>  customerInfo.entitlements.active icinde \'premium\' anahtari\n'
        '>  varsa kullaniciyi premium say ve global store\'da tut.\n'
        '>  Bir \'Premium Ol\' ekrani olustur: RevenueCat\'ten offerings\n'
        '>  cek, paketleri kartlar halinde listele, her birinde fiyat\n'
        '>  ve sure goster, \'Satin Al\' butonuna basinca\n'
        '>  Purchases.purchasePackage() cagir."',
        'Claude Code Prompt'
    )

    # ── 13.4 Webhook ve Backend Entegrasyonu ─────────────────────
    doc.new_page('Bolum 13: RevenueCat ile Abonelik Sistemi')
    doc.h1('13.4  Webhook ile Backend\'i Senkronize Tutma')
    doc.sp(4)
    doc.text(
        'Kullanicinin abonelik durumu (yeni satin alma, yenileme, iptal) '
        'degistiginde, bu bilgiyi kendi Supabase veritabaninizda da '
        'guncel tutmaniz gerekir — orn. AI istek limitini abonelik '
        'durumuna gore kontrol etmek icin.'
    )
    doc.code(
        '> "RevenueCat panelinde bir webhook URL\'i tanimlamam\n'
        '>  gerekiyor. Supabase\'de bir Edge Function olustur, bu\n'
        '>  fonksiyon RevenueCat\'in gonderdigi event\'i (INITIAL_\n'
        '>  PURCHASE, RENEWAL, CANCELLATION) okuyup ilgili kullanicinin\n'
        '>  veritabanindaki \'premium\' alanini guncellesin."',
        'Claude Code Prompt'
    )
    doc.box(
        'Sadece mobil uygulama icindeki SDK durumuna guvenmek riskli '
        'olabilir (offline durumlar, eski cache). Webhook ile backend\'i '
        'de senkron tutmak, ozellikle AI kullanim limiti gibi kritik '
        'kontroller icin ek bir guvenlik katmani saglar.',
        'tip'
    )

    # ── 13.5 RevenueCat vs Adapty Karsilastirma ───────────────────
    doc.new_page('Bolum 13: RevenueCat ile Abonelik Sistemi')
    doc.h1('13.5  RevenueCat vs Adapty: Hangisini Secmeliyim?')
    doc.sp(4)
    doc.table(
        ['Kriter',            'RevenueCat',                    'Adapty'],
        [
            ['Topluluk/dokumantasyon', 'Cok buyuk, en yaygin',     'Buyuyen, daha kucuk'],
            ['Ucretsiz plan siniri',   '$2,500 MRR\'a kadar',      '$10,000 MRR\'a kadar'],
            ['No-code paywall',        'Var (Paywalls v2)',        'Daha gelismis builder'],
            ['A/B Test',                'Var',                      'Daha detayli'],
            ['Ogrenme kaynagi',         'Cok fazla ornek/tutorial', 'Daha az ornek'],
        ],
        widths=[120, 161, 100]
    )
    doc.sp(6)
    doc.box(
        'Yeni baslayanlar icin RevenueCat onerilir — daha fazla ornek '
        'proje, Claude Code\'un egitim verisinde daha fazla referans '
        've daha genis topluluk destegi bulunur. Ileri seviyede A/B '
        'test ve no-code paywall onceliginiz varsa Adapty\'yi '
        'deneyebilirsiniz.',
        'tip'
    )


def kapanis(doc):
    """Kapanis ve Kaynaklar"""

    doc.new_page('Kapanis')
    doc.h1('Kapanis: Simdi Sira Sizde')
    doc.sp(4)
    doc.text(
        'Bu rehberde sifirdan basliyarak bir mobil uygulamayi nasil '
        'tasarlayacaginizi, kodlayacaginizi, backend\'ini kuracaginizi ve '
        'magazalarda yayinlayip gelir elde edecegini detayli olarak '
        'islediik. Artik elinizde Claude Code ile calisma yontemini, '
        'React Native/Expo ekosistemini, Supabase backend\'ini, tasarim '
        'surecini ve AdMob/Adapty/RevenueCat gelir modellerini kapsayan '
        'tam bir yol haritasi var.'
    )

    doc.h2('Hatirlamaniz Gereken Temel Ilkeler')
    doc.bullets([
        'Kucuk baslayin: Ilk uygulamaniz mukemmel olmak zorunda degil, '
        'TAMAMLANMIS olmasi onemlidir',
        'trustmrr.com gibi kaynaklarla fikrinizi kanitlanmis taleple '
        'destekleyin',
        'CLAUDE.md dosyanizi her zaman guncel tutun — Claude Code\'un '
        'tutarli calismasinin anahtari budur',
        'Guvenligi asla ihmal etmeyin: API anahtarlari her zaman '
        'backend\'de, RLS politikalari her zaman aktif',
        'Kullanici deneyimini gelir modelinin onune koyun — asiri '
        'reklam/agresif paywall kisa surede kullanici kaybettirir',
    ])

    doc.h2('Sonraki Adimlariniz')
    doc.table(
        ['Adim',  'Aciklama'],
        [
            ['1', 'Bolum 10\'daki yontemlerle bir uygulama fikri belirleyin'],
            ['2', 'Google Play ve/veya Apple Developer hesabinizi acin '
                   '(Bolum 2-3)'],
            ['3', 'Gelistirme ortaminizi kurun (Bolum 4-5)'],
            ['4', 'Bolum 7\'deki adimlari takip ederek ilk MVP\'nizi '
                   'Claude Code ile kodlayin'],
            ['5', 'Backend ve tasarimi tamamlayin (Bolum 8-9)'],
            ['6', 'Gelir modelinizi entegre edin (Bolum 11-13)'],
            ['7', 'EAS Build ile derleyip magazalara gonderin (Bolum 6)'],
        ],
        widths=[40, 331]
    )

    doc.sp(8)
    doc.box(
        'Sorulariniz oldugunda Claude Code\'a dogrudan sorun — bu '
        'rehberdeki her komut ve kod ornegi, gercek bir Claude Code '
        'oturumunda kullanilabilir sekilde yazilmistir. Basarilar!',
        'tip'
    )

    doc.sp(10)
    doc.h2('Kaynaklar')
    doc.bullets([
        'expo.dev — Resmi Expo dokumantasyonu',
        'reactnative.dev — Resmi React Native dokumantasyonu',
        'supabase.com/docs — Supabase dokumantasyonu',
        'revenuecat.com/docs — RevenueCat dokumantasyonu',
        'adapty.io/docs — Adapty dokumantasyonu',
        'apps.admob.com — AdMob paneli',
        'trustmrr.com — Kanitlanmis gelir verileriyle rakip/fikir '
        'arastirmasi',
        'mobbin.com — Tasarim ilhami arsivi',
        'claude.com/claude-code — Claude Code resmi dokumantasyonu',
    ])

    doc.sp(12)
    doc.h2('Yazar')
    doc.text('Aykut Uces  |  @aykutuces  |  EticMedya  |  vibecodingex.com')
