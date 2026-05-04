#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Icerik Part 5 — Sayfa 74-103
Bolum 7: AdMob Reklam Entegrasyonu
Bolum 8: SaaS / Abonelik Sistemleri
Bolum 9: GitHub ve Faydali Repolar
"""
from pdf_engine import Doc
from pdf_engine import NAVY, ORANGE, WHITE, BLACK, GRAY_BG, GRAY_DARK

from content_part1 import kapak_sayfasi, icindekiler, bolum1_giris, bolum1_ek_ve_bolum2_baslangic
from content_part2 import bolum2_devami, bolum3_claude_ekosistemi
from content_part3 import bolum4_claude_code, bolum5_projeler_baslangic
from content_part4 import bolum5_mobil_windows, bolum5_mobil_mac, bolum5_desktop, bolum6_store


def bolum7_admob(doc):
    """Bolum 7: AdMob Reklam Entegrasyonu"""

    doc.section_cover(
        7,
        'AdMob Reklam Entegrasyonu',
        'Uygulamanizdan pasif gelir elde edin',
        'Bu bolumde Google AdMob platformunu, React Native / Expo uygulamalarina '
        'reklam eklemeyi ve Claude Code yardimiyla entegrasyonu adim adim inceliyoruz.',
    )

    # ── 7.1 AdMob Nedir? ───────────────────────────────────────
    doc.new_page('Bolum 7: AdMob Reklam Entegrasyonu')
    doc.h1('7.1  AdMob Nedir?')
    doc.sp(4)
    doc.text(
        'Google AdMob, mobil uygulamalara reklam entegre etmenizi saglayan Google\'in '
        'ucretsiz platformudur. Uygulamaniza Banner, Interstitial (tam ekran) veya '
        'Rewarded (odullu) reklamlar ekleyerek para kazanabilirsiniz. '
        'Ozellikle ucretsiz uygulamalar icin en yaygin monetizasyon yontemidir.'
    )

    doc.h2('Reklam Turleri')
    doc.table(
        ['Tur',           'Gosterim Zamani',                 'Doluluk Orani', 'Tavsiye'],
        [
            ['Banner',        'Sayfa altinda / ustunde surekli', 'Dusuk',          'Basit uygulamalar'],
            ['Interstitial',  'Ekran gecislerinde tam ekran',    'Yuksek',         'Oyun, okuma arasi'],
            ['Rewarded',      'Kullanici izniyle, odul karsilig.','Cok yuksek',    'Oyun, premium icerik'],
            ['Native',        'Icerige entegre gorsel reklam',   'Orta',           'Haber, sosyal app'],
            ['App Open',      'Uygulama acilisinda',             'Orta-Yuksek',    'Her tur uygulama'],
        ],
        widths=[80, 160, 100, 131]
    )
    doc.sp(6)
    doc.box(
        'Rewarded reklamlar en yuksek CPM (1000 gosterim basina kazanc) degerine sahiptir. '
        '"30 saniye reklam izle, premium ozellik kazan" modeli kullanici memnuniyetini '
        'artirirken geliri de maksimize eder.',
        'tip'
    )

    # ── 7.2 AdMob Hesabi ───────────────────────────────────────
    doc.new_page('Bolum 7: AdMob Reklam Entegrasyonu')
    doc.h1('7.2  AdMob Hesabi Olusturma')
    doc.sp(4)
    doc.bullets([
        'admob.google.com adresine gidin',
        'Google hesabinizla giris yapin',
        '"Basla" butonuna tiklayin',
        'Ulke ve zaman dilimi secin (Turkiye / Istanbul)',
        'Odeme bilgilerini girin (banka hesabi veya Google Pay)',
        'Uygulamanizi AdMob\'e ekleyin: "Uygulama ekle" → platform secin',
        'Uygulama ID\'sini (ca-app-pub-XXXX~YYYY) not alin',
        'Her reklam turu icin reklam birimi olusturun, Ad Unit ID\'lerini kopyalayin',
    ])
    doc.box(
        'Test sirasinda gercek reklam ID\'leri kullanmak hesabinizin banlanmasina '
        'yol acabilir. Her zaman test reklam ID\'lerini kullanin, '
        'sadece uretim surumunde gercek ID\'lere gecin.',
        'warning'
    )

    doc.h2('Test Reklam ID\'leri')
    doc.code(
        '// Android Test Reklam ID\'leri:\n'
        'Banner:        ca-app-pub-3940256099942544/6300978111\n'
        'Interstitial:  ca-app-pub-3940256099942544/1033173712\n'
        'Rewarded:      ca-app-pub-3940256099942544/5224354917\n\n'
        '// iOS Test Reklam ID\'leri:\n'
        'Banner:        ca-app-pub-3940256099942544/2934735716\n'
        'Interstitial:  ca-app-pub-3940256099942544/4411468910\n'
        'Rewarded:      ca-app-pub-3940256099942544/1712485313',
        'JavaScript'
    )

    # ── 7.3 React Native Entegrasyon ──────────────────────────
    doc.new_page('Bolum 7: AdMob Reklam Entegrasyonu')
    doc.h1('7.3  React Native\'e AdMob Entegrasyonu')
    doc.sp(4)
    doc.text(
        'React Native uygulamasina AdMob eklemek icin en yaygin kutuphane '
        'react-native-google-mobile-ads\'dir. Claude Code\'a kurulum ve entegrasyon '
        'icin talimat vermeniz yeterlidir.'
    )

    doc.h2('Claude Code ile Kurulum')
    doc.code(
        '# Claude Code\'a sorun:\n'
        '> "React Native projeme AdMob ekle.\n'
        '>  - Paket: react-native-google-mobile-ads\n'
        '>  - Reklam turleri: Banner ve Rewarded\n'
        '>  - Android App ID: ca-app-pub-XXXX~YYYY\n'
        '>  - iOS App ID: ca-app-pub-XXXX~ZZZZ\n'
        '>  - Test modunda calis, test ID\'lerini kullan\n'
        '>  - Banner reklamini HomeScreen altina ekle\n'
        '>  - Rewarded reklamini premium ozelliklerde tetikle"',
        'Terminal'
    )
    doc.code(
        '# Claude asagidaki adimlari atar:\n'
        'npm install react-native-google-mobile-ads\n\n'
        '# android/build.gradle icine ekler:\n'
        '# classpath("com.google.gms:google-services:4.4.0")\n\n'
        '# android/app/build.gradle icine ekler:\n'
        '# apply plugin: "com.google.gms.google-services"\n\n'
        '# android/app/src/main/AndroidManifest.xml icine ekler:\n'
        '# <meta-data android:name="com.google.android.gms.ads.APPLICATION_ID"\n'
        '#            android:value="ca-app-pub-XXXX~YYYY"/>',
        'Terminal'
    )

    doc.h2('Banner Reklam Kodu')
    doc.code(
        'import { BannerAd, BannerAdSize, TestIds } from\n'
        '  "react-native-google-mobile-ads";\n\n'
        'const adUnitId = __DEV__\n'
        '  ? TestIds.ADAPTIVE_BANNER\n'
        '  : "ca-app-pub-XXXX/YYYY"; // gercek ID\n\n'
        'export function HomeScreen() {\n'
        '  return (\n'
        '    <View style={styles.container}>\n'
        '      {/* icerik */}\n'
        '      <BannerAd\n'
        '        unitId={adUnitId}\n'
        '        size={BannerAdSize.ANCHORED_ADAPTIVE_BANNER}\n'
        '        requestOptions={{ requestNonPersonalizedAdsOnly: true }}\n'
        '      />\n'
        '    </View>\n'
        '  );\n'
        '}',
        'JavaScript'
    )

    # ── 7.4 Rewarded Reklam ───────────────────────────────────
    doc.new_page('Bolum 7: AdMob Reklam Entegrasyonu')
    doc.h1('7.4  Rewarded Reklam Implementasyonu')
    doc.sp(4)
    doc.code(
        'import {\n'
        '  RewardedAd, RewardedAdEventType, TestIds\n'
        '} from "react-native-google-mobile-ads";\n'
        'import { useEffect, useState } from "react";\n\n'
        'const rewarded = RewardedAd.createForAdRequest(\n'
        '  __DEV__ ? TestIds.REWARDED : "ca-app-pub-XXXX/ZZZZ",\n'
        '  { requestNonPersonalizedAdsOnly: true }\n'
        ');\n\n'
        'export function PremiumFeature() {\n'
        '  const [loaded, setLoaded] = useState(false);\n\n'
        '  useEffect(() => {\n'
        '    const unsubLoad = rewarded.addAdEventListener(\n'
        '      RewardedAdEventType.LOADED, () => setLoaded(true)\n'
        '    );\n'
        '    const unsubEarn = rewarded.addAdEventListener(\n'
        '      RewardedAdEventType.EARNED_REWARD, (reward) => {\n'
        '        console.log("Odullendirildi:", reward.amount, reward.type);\n'
        '        unlockPremiumContent(); // kendi fonksiyonunuz\n'
        '      }\n'
        '    );\n'
        '    rewarded.load();\n'
        '    return () => { unsubLoad(); unsubEarn(); };\n'
        '  }, []);\n\n'
        '  return (\n'
        '    <Button\n'
        '      title="Reklam izle - Premium ac"\n'
        '      onPress={() => loaded && rewarded.show()}\n'
        '      disabled={!loaded}\n'
        '    />\n'
        '  );\n'
        '}',
        'JavaScript'
    )
    doc.box(
        'Rewarded reklamlarda kullanicinin gercekten odullendirildiginden emin olun. '
        'Reklami yari kapatan kullanicilara odul vermeyin; '
        'EARNED_REWARD eventi sadece reklam tamamen izlendiginde tetiklenir.',
        'info'
    )

    # ── 7.5 IDFA / ATT (iOS) ──────────────────────────────────
    doc.new_page('Bolum 7: AdMob Reklam Entegrasyonu')
    doc.h1('7.5  iOS ATT Izin Ekrani (IDFA)')
    doc.sp(4)
    doc.text(
        'iOS 14.5\'ten itibaren Apple, uygulamalarin kullanicilari takip etmeden once '
        'App Tracking Transparency (ATT) izni almasini zorunlu kildi. '
        'Bu izni almadan kisisellestirilmis reklam gosteremezsiniz ve '
        'reklamlarin deger dusebilir. ATT izin ekrani gostermek icin '
        'react-native-tracking-transparency kullanabilirsiniz.'
    )
    doc.code(
        'npm install react-native-tracking-transparency\n\n'
        '// Info.plist icine ekleyin (Xcode):\n'
        '// NSUserTrackingUsageDescription: "Kisisel reklamlar icin...',
        'Terminal'
    )
    doc.code(
        'import {\n'
        '  requestTrackingPermissionsAsync\n'
        '} from "react-native-tracking-transparency";\n\n'
        'async function requestATT() {\n'
        '  const { status } = await requestTrackingPermissionsAsync();\n'
        '  if (status === "authorized") {\n'
        '    // kisisellestirilmis reklam goster\n'
        '  } else {\n'
        '    // non-personalized reklam goster\n'
        '    mobileAds().setRequestConfiguration({\n'
        '      maxAdContentRating: MaxAdContentRating.PG,\n'
        '      tagForChildDirectedTreatment: false,\n'
        '      tagForUnderAgeOfConsent: false,\n'
        '    });\n'
        '  }\n'
        '}',
        'JavaScript'
    )
    doc.box(
        'ATT izin oranini artirmak icin kullaniciya neden izin istediginizi aciklayin. '
        '"Sizi ilgilendiren reklamlar gostermek icin" gibi net bir mesaj '
        'kullanicinin kabul etme ihtimalini arttirir.',
        'tip'
    )


def bolum8_saas(doc):
    """Bolum 8: SaaS / Abonelik Sistemleri"""

    doc.section_cover(
        8,
        'SaaS / Abonelik Sistemleri',
        'Tekrar eden gelir modeli kurun',
        'Bu bolumde In-App Purchase, RevenueCat, Adapty gibi abonelik '
        'cozumlerini ve Claude Code ile entegrasyon yontemlerini inceliyoruz.',
    )

    # ── 8.1 IAP'a Giris ───────────────────────────────────────
    doc.new_page('Bolum 8: SaaS / Abonelik Sistemleri')
    doc.h1('8.1  In-App Purchase (IAP) Nedir?')
    doc.sp(4)
    doc.text(
        'In-App Purchase (IAP), uygulama icerisinden yapilan satin alimlardir. '
        'Tek seferlik satin alimlar (consumable/non-consumable) veya tekrar eden '
        'abonelikler (subscriptions) seklinde olabilir. '
        'App Store %30, Google Play %15-30 komisyon alir.'
    )

    doc.h2('IAP Turleri')
    doc.table(
        ['Tur',               'Aciklama',                            'Ornekler'],
        [
            ['Consumable',        'Bir kez kullanilir, tekrar satin alinir','Oyun parasi, kredi'],
            ['Non-Consumable',    'Kalici acilis, bir kez satin alinir',    'Reklam kaldirma, tema'],
            ['Auto-Renewable',    'Otomatik yenilenen abonelik',            'Netflix, Spotify tipi'],
            ['Non-Renewing',      'Belirli sureli, elle yenilenir',         'Sezonluk erisim'],
        ],
        widths=[115, 200, 156]
    )
    doc.sp(6)
    doc.text(
        'Modern SaaS uygulamalar genellikle Auto-Renewable Subscription modelini kullanir. '
        'Bu model MRR (Monthly Recurring Revenue) ve ARR (Annual Recurring Revenue) '
        'metriklerini takip etmenizi saglar ve yalintilik olcmeye uyundur.'
    )

    # ── 8.2 RevenueCat ────────────────────────────────────────
    doc.new_page('Bolum 8: SaaS / Abonelik Sistemleri')
    doc.h1('8.2  RevenueCat ile Abonelik Yonetimi')
    doc.sp(4)
    doc.text(
        'RevenueCat, App Store ve Google Play aboneliklerini tek platformda yonetmenizi '
        'saglayan en populer SDK\'dir. Ucretsiz plan ayda 2.500 dolara kadar geliri kapsar. '
        'Webhook, entitlement sistemi ve gercek zamanli analitik sunar.'
    )

    doc.h2('Claude Code ile RevenueCat Kurulumu')
    doc.code(
        '# Claude Code\'a sorun:\n'
        '> "React Native projeme RevenueCat ekle.\n'
        '>  - SDK: react-native-purchases\n'
        '>  - iOS API key: appl_XXXX\n'
        '>  - Android API key: goog_YYYY\n'
        '>  - Paketler: monthly ($9.99), annual ($79.99)\n'
        '>  - Paywall ekrani olustur: ucretsiz vs premium karsilastirma\n'
        '>  - Entitlement: premium_access\n'
        '>  - Restore purchases butonu ekle"',
        'Terminal'
    )
    doc.code(
        'npm install react-native-purchases\n\n'
        '// App.tsx veya index.js icinde:\n'
        'import Purchases from "react-native-purchases";\n\n'
        'Purchases.configure({\n'
        '  apiKey: Platform.OS === "ios"\n'
        '    ? "appl_XXXX"\n'
        '    : "goog_YYYY",\n'
        '});\n\n'
        '// Mevcut entitlements kontrol:\n'
        'const customerInfo = await Purchases.getCustomerInfo();\n'
        'const isPremium =\n'
        '  customerInfo.entitlements.active["premium_access"];\n\n'
        '// Satin alma:\n'
        'const { customerInfo: info } =\n'
        '  await Purchases.purchasePackage(selectedPackage);\n'
        'if (info.entitlements.active["premium_access"]) {\n'
        '  // premium icerigi ac\n'
        '}',
        'JavaScript'
    )

    # ── 8.3 Adapty ────────────────────────────────────────────
    doc.new_page('Bolum 8: SaaS / Abonelik Sistemleri')
    doc.h1('8.3  Adapty — Alternatif Abonelik Platformu')
    doc.sp(4)
    doc.text(
        'Adapty, RevenueCat\'e iyi bir alternatiftir. Daha uygun fiyatli '
        've A/B testing ile paywall optimizasyonu konusunda daha guclüdür. '
        'Kodu degistirmeden farkli paywall tasarimlarini test edebilirsiniz.'
    )
    doc.bullets([
        'Ucretsiz plan: ayda $10.000\'e kadar gelir (RevenueCat\'ten cok daha yuksek)',
        'No-code paywall builder: surukleme-birakma ile tasarim',
        'A/B testing: hangi fiyatlandirma daha cok donusiyor?',
        'Analitik: LTV, Churn Rate, MRR dashboard',
        'Webhook: Stripe, Amplitude, Mixpanel entegrasyonu',
    ])
    doc.code(
        'npm install react-native-adapty\n\n'
        'import { adapty } from "react-native-adapty";\n\n'
        '// Baslangic:\n'
        'await adapty.activate("PUBLIC_SDK_KEY");\n\n'
        '// Paywall goster:\n'
        'const paywall = await adapty.getPaywall("premium_paywall");\n'
        'const products = await adapty.getPaywallProducts(paywall);\n\n'
        '// Profil kontrolu:\n'
        'const profile = await adapty.getProfile();\n'
        'const isPremium =\n'
        '  profile.accessLevels["premium"]?.isActive ?? false;',
        'JavaScript'
    )

    doc.h2('RevenueCat vs Adapty Karsilastirmasi')
    doc.table(
        ['Kriter',           'RevenueCat',                  'Adapty'],
        [
            ['Ucretsiz limit',   '$2.500/ay gelire kadar',       '$10.000/ay gelire kadar'],
            ['A/B Testing',      'Temel',                         'Gelismis, no-code'],
            ['Paywall builder',  'Yok (kod gerekir)',             'Var, surukleme-birakma'],
            ['Analitik',         'Detayli dashboard',             'Detayli + cohort analizi'],
            ['Entegrasyon',      'Cok genis ekosistem',           'Buyuyor'],
            ['Dokumanlar',       'Cok kapsamli',                  'Iyi'],
            ['Onerim',           'Mevcut ekosistem/SDK yayginl.', 'Buyuk paywall optimizasyonu'],
        ],
        widths=[100, 180, 191]
    )

    # ── 8.4 Stripe Web ────────────────────────────────────────
    doc.new_page('Bolum 8: SaaS / Abonelik Sistemleri')
    doc.h1('8.4  Web SaaS: Stripe ile Abonelik')
    doc.sp(4)
    doc.text(
        'Web tabanli SaaS urunler icin Stripe, dunyanin en yaygin odeme altyapisini sunar. '
        'Stripe, komisyonlardan muaf tutar (App Store/%30\'a karsilik %2.9+30 cent). '
        'Claude Code, tam bir Stripe abonelik sistemi kurabilir.'
    )
    doc.code(
        '# Claude Code\'a sorun:\n'
        '> "Next.js projeme Stripe abonelik sistemi ekle:\n'
        '>  - Paketler: Baslangic ($19/ay), Pro ($49/ay), Kurumsal ($149/ay)\n'
        '>  - Stripe Checkout sayfasi\n'
        '>  - Webhook: odeme basarili / basarisiz / iptal\n'
        '>  - Kullanici dashboardinda abonelik durumu\n'
        '>  - Iptal ve yenileme akisi\n'
        '>  - Veritabani: Supabase (users, subscriptions tablosu)"',
        'Terminal'
    )
    doc.code(
        'npm install stripe @stripe/stripe-js\n\n'
        '// API route: pages/api/create-checkout-session.ts\n'
        'import Stripe from "stripe";\n'
        'const stripe = new Stripe(process.env.STRIPE_SECRET_KEY!);\n\n'
        'export default async function handler(req, res) {\n'
        '  const session = await stripe.checkout.sessions.create({\n'
        '    mode: "subscription",\n'
        '    payment_method_types: ["card"],\n'
        '    line_items: [{ price: req.body.priceId, quantity: 1 }],\n'
        '    success_url: `${process.env.NEXT_PUBLIC_URL}/success`,\n'
        '    cancel_url: `${process.env.NEXT_PUBLIC_URL}/pricing`,\n'
        '    customer_email: req.body.email,\n'
        '  });\n'
        '  res.json({ url: session.url });\n'
        '}',
        'JavaScript'
    )
    doc.box(
        'Stripe, Turkiye\'den kayitli sirketlere destek vermektedir. '
        'Bireysel kayit icin vergi numarasi ve banka hesabi gereklidir. '
        'Alternatif olarak Paddle veya LemonSqueezy merchant of record olarak '
        'vergi yukümlülüklerinizi devralabilir.',
        'info'
    )


def bolum9_github(doc):
    """Bolum 9: GitHub ve Faydali Repolar"""

    doc.section_cover(
        9,
        'GitHub ve Faydali Repolar',
        'Omuzlara basarak daha uzaga gorun',
        'Bu bolumde GitHub\'in temel kullanimini, Claude Code ile git entegrasyonunu '
        've yapay zeka projeleriniz icin en faydali acik kaynak repolarini inceliyoruz.',
    )

    # ── 9.1 GitHub Temel ──────────────────────────────────────
    doc.new_page('Bolum 9: GitHub ve Faydali Repolar')
    doc.h1('9.1  GitHub Temelleri')
    doc.sp(4)
    doc.text(
        'GitHub, dunya genelinde 100 milyondan fazla gelistiricinin kodlarini '
        'sakladigi ve paylastigi bir platformdur. Acik kaynak projelerin merkezi olmanin '
        'otesinde CI/CD, issue takibi ve kod inceleme araclari da sunar. '
        'Claude Code, dogrudan git ve GitHub ile entegre calisir.'
    )

    doc.h2('Temel Git Komutlari')
    doc.code(
        '# Yeni repo olustur ve baglanti kur:\n'
        'git init\n'
        'git remote add origin https://github.com/kullanici/repo.git\n\n'
        '# Degisiklikleri commit et ve gonder:\n'
        'git add .\n'
        'git commit -m "feat: ilk commit"\n'
        'git push -u origin main\n\n'
        '# Yeni ozellik dali ac:\n'
        'git checkout -b feature/yeni-ozellik\n\n'
        '# Guncel kodu cek:\n'
        'git pull origin main\n\n'
        '# Birlesim:\n'
        'git merge feature/yeni-ozellik',
        'Terminal'
    )

    doc.h2('Claude Code ile Git')
    doc.code(
        '# Claude Code git islemlerini otomatik yapar:\n'
        '> "Degisiklikleri commit et ve push et"\n'
        '> "Yeni bir feature branch ac: kullanici-profili"\n'
        '> "Son 5 commit\'i goster"\n'
        '> "Bu PR\'i merge et"\n'
        '> ".gitignore\'a node_modules, .env ekle"',
        'Terminal'
    )

    # ── 9.2 GitHub Actions CI/CD ──────────────────────────────
    doc.new_page('Bolum 9: GitHub ve Faydali Repolar')
    doc.h1('9.2  GitHub Actions ile CI/CD')
    doc.sp(4)
    doc.text(
        'GitHub Actions, kod degisikliklerinde otomatik test, build ve deploy '
        'islemi yapmanizi saglar. Her push veya PR\'da testlerin otomatik calismasini '
        'saglamak kod kalitesini korur. Claude Code, Actions workflow dosyalari yazabilir.'
    )
    doc.code(
        '# Claude Code\'a sorun:\n'
        '> "GitHub Actions workflow ekle:\n'
        '>  - Her push\'ta ESLint ve TypeScript kontrol\n'
        '>  - main branch\'e merge\'de Vercel\'e deploy\n'
        '>  - PR\'larda preview deploy\n'
        '>  - Test coverage raporu"',
        'Terminal'
    )
    doc.code(
        '# .github/workflows/ci.yml\n'
        'name: CI/CD\n'
        'on:\n'
        '  push:\n'
        '    branches: [main, develop]\n'
        '  pull_request:\n'
        '    branches: [main]\n\n'
        'jobs:\n'
        '  lint-and-test:\n'
        '    runs-on: ubuntu-latest\n'
        '    steps:\n'
        '      - uses: actions/checkout@v4\n'
        '      - uses: actions/setup-node@v4\n'
        '        with:\n'
        '          node-version: 20\n'
        '          cache: npm\n'
        '      - run: npm ci\n'
        '      - run: npm run lint\n'
        '      - run: npm run type-check\n'
        '      - run: npm test -- --coverage',
        'YAML'
    )

    # ── 9.3 Faydali Repolar ───────────────────────────────────
    doc.new_page('Bolum 9: GitHub ve Faydali Repolar')
    doc.h1('9.3  AI Gelistiricileri icin Faydali Repolar')
    doc.sp(4)

    doc.h2('Hazir Starter Sablonlar')
    doc.bullets([
        'vercel/ai — AI SDK: streaming, tool use, multi-modal destekli Next.js starter',
        'mckaywrigley/chatbot-ui — ChatGPT benzeri arayuz, OpenAI/Claude destekli',
        'lobehub/lobe-chat — Modern chatbot UI, eklenti sistemi, cok model destegi',
        'open-webui/open-webui — Ollama icin web arayuzu, yerel LLM calistirma',
        'langchain-ai/langchainjs — LangChain JavaScript, agent ve chain frameworku',
    ])

    doc.h2('Uretkenlik ve Otomasyon')
    doc.bullets([
        'n8n-io/n8n — No-code otomasyon, Zapier alternatifi, AI node\'lari var',
        'browserbase/stagehand — AI ile tarayici otomasyonu (Playwright + LLM)',
        'microsoft/markitdown — Her dosyayi (PDF, Word, Excel) Markdown\'a cevirir',
        'xyflow/xyflow — React Flow, akis diyagrami UI bileşeni',
        'shadcn-ui/ui — Kopyala-yapistir React UI bileşenleri, Tailwind tabanli',
    ])

    doc.h2('Veritabani ve Backend')
    doc.bullets([
        'supabase/supabase — Acik kaynak Firebase alternatifi, PostgreSQL + Auth + Storage',
        'prisma/prisma — TypeScript ORM, tum SQL veritabanlari destekli',
        'trpc/trpc — End-to-end type-safe API, NextJS ile mukemmel uyum',
        'drizzle-team/drizzle-orm — Hafif TypeScript ORM, Edge destekli',
        'lucia-auth/lucia — Esnek authentication kutuphanesi',
    ])

    # ── 9.4 GitHub Arama Ipuclari ─────────────────────────────
    doc.new_page('Bolum 9: GitHub ve Faydali Repolar')
    doc.h1('9.4  GitHub\'da Arama Ipuclari')
    doc.sp(4)

    doc.h2('Gelismis Arama Operatorleri')
    doc.code(
        '# Dil ve yildiz sayisina gore filtrele:\n'
        'language:typescript stars:>1000 react native admob\n\n'
        '# Son 1 yil icinde guncellenenler:\n'
        'pushed:>2025-01-01 topic:ai-agent\n\n'
        '# Belirli bir dosyayi ara:\n'
        'filename:CLAUDE.md\n\n'
        '# Kod icinde ara:\n'
        'path:*.tsx useState useEffect\n\n'
        '# Sahip veya org ile:\n'
        'org:vercel stars:>500 language:typescript',
        'Terminal'
    )

    doc.h2('Trending Repolar Takip Etme')
    doc.bullets([
        'github.com/trending — gunluk/haftalik en cok yildizlanan repolar',
        'github.com/trending/typescript — dil bazli filtre',
        'github.com/explore — ilgi alanlarina gore kesfet',
        'Twitter/X\'te #buildinpublic, #indiedev, #shipit etiketleri',
        'producthunt.com — yeni AI araclari ve SaaS urunleri',
    ])

    doc.h2('Claude Code ile Repo Analizi')
    doc.code(
        '# Yeni bir repo klonladiginda Claude Code\'a sorun:\n'
        '> "Bu repoyu analiz et:\n'
        '>  - Ne is yapiyor?\n'
        '>  - Teknoloji stack nedir?\n'
        '>  - Baslangic noktam neresi olmali?\n'
        '>  - Benim projem icin nasil kullanabilirim?"\n\n'
        '# Veya dogrudan:\n'
        '> "Bu kodu kendi projeme entegre et, gerekli '
        'adaptasyonlari yap"',
        'Terminal'
    )
    doc.box(
        'Acik kaynak kod kullanirken lisans turunu kontrol edin. '
        'MIT ve Apache 2.0 lisanslari ticari kullanim icin serbesttir. '
        'GPL lisansi ise projenizin de acik kaynak olmasini gerektirebilir. '
        'Claude Code\'a "Bu reponun lisansi ticari kullanim icin uygun mu?" diye sorabilirsiniz.',
        'warning'
    )


def main():
    doc = Doc()
    print("Icerik olusturuluyor — Sayfa 74-103...")

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
    bolum7_admob(doc)
    bolum8_saas(doc)
    bolum9_github(doc)

    pages = doc.save('yapay_zeka_ogreniyorum_p1_103.pdf')
    print(f"\nTamamlandi! Toplam {pages} sayfa uretildi.")
    print("Dosya: yapay_zeka_ogreniyorum_p1_103.pdf")


if __name__ == '__main__':
    main()
