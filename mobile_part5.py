#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Claude Code ile Mobil Uygulama Rehberi — Part 5
Bolum 8: Backend Tasarimi
Bolum 9: UI/UX Tasarim Sureci
"""
from mobile_pdf_engine import Doc, PW, PH, ML, MR, MT, MB, CW, HDR_H
from mobile_pdf_engine import NAVY, ORANGE, WHITE, BLACK, GRAY_BG, GRAY_DARK


def bolum8_backend_tasarimi(doc):
    """Bolum 8: Backend Tasarimi"""

    doc.section_cover(
        8,
        'Backend Tasarimi',
        'Mobil uygulamaniz icin veritabani ve sunucu tarafi',
        'Bu bolumde mobil uygulamalar icin en uygun backend secenegi olan '
        'Supabase\'i, veritabani tasarimini, kimlik dogrulamayi ve Claude '
        'Code ile backend gelistirmeyi detayli olarak inceliyoruz.',
    )

    # ── 8.1 Backend Neden Gerekli ──────────────────────────────
    doc.new_page('Bolum 8: Backend Tasarimi')
    doc.h1('8.1  Mobil Uygulamada Backend Neden Gerekli?')
    doc.sp(4)
    doc.text(
        'Bolum 7\'deki GorevTakip ornegimizde veriler telefonun yerel '
        'hafizasinda (AsyncStorage) tutuluyordu. Bu basit uygulamalar icin '
        'yeterlidir, ama kullanicinin verilerini baska bir telefonda '
        'gormesi, birden fazla kullanicinin ayni veriyi paylasmasi (sosyal '
        'uygulama, sohbet, paylasimli liste) veya uzaktan bildirim '
        'gonderme gibi ihtiyaclar oldugunda bir BACKEND (sunucu tarafi) '
        'gereklidir.'
    )
    doc.h2('Backend Hangi Durumlarda Sart?')
    doc.bullets([
        'Kullanici hesabi sistemi (giris/kayit, sifre sifirlama)',
        'Verilerin bulutta saklanmasi (telefon degisse de veri kaybolmasin)',
        'Birden fazla kullanicinin ayni veriyi gormesi/duzenlemesi',
        'Push bildirim gonderme (sunucu tetiklemeli)',
        'Odeme/abonelik durumunun dogrulanmasi (sahtecilik onleme)',
        'Yapay zeka API\'lerine (OpenAI, Claude) guvenli istek gonderme — '
        'API anahtarlari ASLA mobil uygulama icine gomulmemeli',
    ])
    doc.box(
        'API anahtarlarini (OpenAI, Claude, vs.) dogrudan mobil uygulama '
        'kodunun icine yazmak buyuk bir guvenlik hatasidir — uygulamayi '
        'paketinden cikarip anahtarinizi calabilirler. Bu anahtarlar her '
        'zaman bir backend sunucusunda saklanmali, mobil uygulama sadece '
        'kendi backend\'inize istek atmalidir.',
        'warning'
    )

    # ── 8.2 Supabase Nedir ─────────────────────────────────────
    doc.new_page('Bolum 8: Backend Tasarimi')
    doc.h1('8.2  Supabase — Mobil Gelistiriciler Icin Ideal Backend')
    doc.sp(4)
    doc.text(
        'Supabase, acik kaynakli bir "Firebase alternatifi"dir. PostgreSQL '
        'veritabani, kimlik dogrulama, dosya depolama ve gercek zamanli '
        '(realtime) veri senkronizasyonunu tek bir platformda sunar. '
        'Claude Code ile en uyumlu calisan backend secenegidir cunku tum '
        'islemler JavaScript/TypeScript SDK\'si uzerinden yapilir — ayri '
        'bir backend dili (Python, Java, vs.) yazmaniza gerek kalmaz.'
    )
    doc.h2('Supabase\'in Sundugu Hizmetler')
    doc.table(
        ['Hizmet',          'Ne Ise Yarar'],
        [
            ['Database',        'PostgreSQL veritabani — kullanicilar, gorevler, '
                                 'mesajlar gibi tum veriler'],
            ['Auth',             'E-posta/sifre, Google, Apple ile giris-kayit sistemi'],
            ['Storage',          'Profil fotografi, dosya, video gibi medya depolama'],
            ['Realtime',         'Veri degistiginde tum cihazlara aninda guncelleme'],
            ['Edge Functions',   'Sunucu tarafi kod (orn. AI API anahtarini gizli '
                                 'tutan fonksiyonlar)'],
        ],
        widths=[110, 271]
    )
    doc.sp(6)
    doc.box(
        'Supabase\'in ucretsiz plani: 500 MB veritabani, 1 GB dosya '
        'depolama, ayda 50,000 aktif kullanici. Kucuk ve orta olcekli '
        'uygulamalar icin uzun sure ucretsiz kalabilirsiniz.',
        'tip'
    )

    # ── 8.3 Supabase Projesi Olusturma ─────────────────────────
    doc.new_page('Bolum 8: Backend Tasarimi')
    doc.h1('8.3  Supabase Projesi Olusturma ve Baglanti')
    doc.sp(4)
    doc.bullets([
        '1. supabase.com adresine gidin, GitHub hesabinizla ucretsiz kayit '
        'olun',
        '2. "New Project" tiklayin, proje adi ve guclu bir veritabani '
        'sifresi belirleyin',
        '3. Bolge (region) olarak Avrupa\'ya en yakin bir sunucu secin '
        '(orn. Frankfurt)',
        '4. Proje olusturulduktan sonra "Project Settings > API" '
        'sayfasindan Project URL ve anon key degerlerini kopyalayin',
        '5. Bu iki degeri mobil projenizdeki .env dosyasina ekleyin',
    ])
    doc.code(
        '# Expo projesine Supabase SDK kurulumu:\n'
        'npx expo install @supabase/supabase-js\n'
        'npx expo install react-native-url-polyfill\n\n'
        '# .env dosyasi (proje kok dizininde):\n'
        'EXPO_PUBLIC_SUPABASE_URL=https://xxxx.supabase.co\n'
        'EXPO_PUBLIC_SUPABASE_ANON_KEY=eyJhbGc...',
        'Terminal'
    )
    doc.box(
        'Supabase\'in "anon key"i mobil uygulama icinde kullanilmasi '
        'guvenli bir anahtardir — ozel olarak tasarlanmistir ve Row Level '
        'Security (RLS) kurallariyla korunur. Ancak "service_role key" '
        'ASLA mobil uygulamaya konulmamalidir, sadece backend/Edge '
        'Functions icinde kullanilir.',
        'warning'
    )

    # ── 8.4 Veritabani Tasarimi ─────────────────────────────────
    doc.new_page('Bolum 8: Backend Tasarimi')
    doc.h1('8.4  Veritabani Semasi Tasarlama')
    doc.sp(4)
    doc.text(
        'Claude Code\'a uygulamanizin ihtiyaclarini anlatarak veritabani '
        'tablolarini birlikte tasarlayabilirsiniz. Ornek bir GorevTakip '
        'uygulamasi icin SQL semasi:'
    )
    doc.code(
        '-- Supabase SQL Editor\'de calistirilir\n\n'
        'create table gorevler (\n'
        '  id uuid default gen_random_uuid() primary key,\n'
        '  user_id uuid references auth.users not null,\n'
        '  baslik text not null,\n'
        '  tamamlandi boolean default false,\n'
        '  kategori text default \'genel\',\n'
        '  created_at timestamp with time zone default now()\n'
        ');\n\n'
        '-- Row Level Security: herkes sadece kendi verisini gorsun\n'
        'alter table gorevler enable row level security;\n\n'
        'create policy "Kullanicilar kendi gorevlerini gorebilir"\n'
        '  on gorevler for select\n'
        '  using (auth.uid() = user_id);\n\n'
        'create policy "Kullanicilar kendi gorev ekleyebilir"\n'
        '  on gorevler for insert\n'
        '  with check (auth.uid() = user_id);',
        'SQL'
    )
    doc.box(
        'Row Level Security (RLS), Supabase\'in en kritik guvenlik '
        'ozelligidir. RLS olmadan herhangi bir kullanici tum '
        'veritabanindaki verileri okuyabilir/degistirebilir. Claude '
        'Code\'a "RLS policy ekle" diyerek her tablo icin bu korumayi '
        'kurdurun.',
        'warning'
    )

    # ── 8.5 Auth Entegrasyonu ───────────────────────────────────
    doc.new_page('Bolum 8: Backend Tasarimi')
    doc.h1('8.5  Kimlik Dogrulama (Auth) Entegrasyonu')
    doc.sp(4)
    doc.text(
        'Claude Code\'a su sekilde talimat vererek tam bir giris/kayit '
        'sistemi kurdurabilirsiniz:'
    )
    doc.code(
        '> "Supabase Auth kullanarak e-posta/sifre ile giris ve kayit\n'
        '>  ekrani olustur. Basarili girişten sonra kullaniciyi ana\n'
        '>  ekrana yonlendir. Oturum bilgisini AsyncStorage\'da kalici\n'
        '>  tut, uygulama yeniden acildiginda otomatik giris yapsin."',
        'Claude Code Prompt'
    )
    doc.h2('Supabase Auth\'un Desteklediği Giris Yontemleri')
    doc.bullets([
        'E-posta + sifre (en yaygin, en basit)',
        'Magic Link (sifresiz, e-postaya gelen link ile giris)',
        'Google ile giris (Google OAuth)',
        'Apple ile giris (App Store kurallari geregi bazi uygulamalarda '
        'ZORUNLU — kullanici baska bir sosyal giris sunuyorsaniz Apple '
        'ile girisi de eklemelisiniz)',
    ])
    doc.box(
        'Apple App Store kurali: Eger uygulamaniz Google/Facebook gibi '
        'ucuncu parti giris secenekleri sunuyorsa, "Sign in with Apple" '
        'secenegini de sunmak ZORUNLUDUR. Bu kurali atlarsaniz uygulamaniz '
        'reddedilir.',
        'warning'
    )

    # ── 8.6 Edge Functions ──────────────────────────────────────
    doc.new_page('Bolum 8: Backend Tasarimi')
    doc.h1('8.6  Edge Functions — Sunucu Tarafi Mantik')
    doc.sp(4)
    doc.text(
        'Edge Functions, Supabase\'in sunucusuz (serverless) fonksiyon '
        'sistemidir. AI API cagirma, odeme dogrulama gibi gizli '
        'anahtar gerektiren islemler buraya yazilir.'
    )
    doc.code(
        '# Edge Function olusturma:\n'
        'npx supabase functions new ai-yanitla\n\n'
        '# Fonksiyonu deploy etme:\n'
        'npx supabase functions deploy ai-yanitla\n\n'
        '# Gizli anahtarlari sunucuya tanitma (asla mobil kodda olmaz):\n'
        'npx supabase secrets set OPENAI_API_KEY=sk-xxxx',
        'Terminal'
    )
    doc.text(
        'Mobil uygulamadan bu fonksiyona istek atildiginda, fonksiyon '
        'kendi icinde OpenAI/Claude API\'sini cagirir ve sonucu mobil '
        'uygulamaya geri doner. Boylece API anahtariniz hicbir zaman '
        'kullanicinin telefonuna ulasmaz.'
    )

    # ── 8.7 Alternatif Backend Secenekleri ──────────────────────
    doc.new_page('Bolum 8: Backend Tasarimi')
    doc.h1('8.7  Alternatif Backend Secenekleri')
    doc.sp(4)
    doc.table(
        ['Secenek',       'Avantaj',                           'Dezavantaj'],
        [
            ['Supabase',      'Acik kaynak, SQL, kolay RLS',       'Once ogrenme egrisi gerektirir'],
            ['Firebase',      'Google destegi, cok yayginlik',     'NoSQL, sorgular sinirli'],
            ['Appwrite',      'Self-hosted secenek',               'Topluluk daha kucuk'],
            ['Kendi backend\'iniz (Node.js)', 'Tam kontrol', 'Sunucu yonetimi, daha fazla is'],
        ],
        widths=[120, 161, 100]
    )
    doc.sp(6)
    doc.box(
        'Bu rehberde Supabase\'i oneriyoruz cunku Claude Code ile TypeScript '
        'tabanli tek bir SDK uzerinden hem mobil hem backend kodu '
        'yazabilirsiniz — context switch (dil/araç degistirme) en aza '
        'iner.',
        'tip'
    )


def bolum9_uiux_tasarim(doc):
    """Bolum 9: UI/UX Tasarim Sureci"""

    doc.section_cover(
        9,
        'UI/UX Tasarim Sureci',
        'Guzel ve kullanilabilir bir mobil arayuz tasarlamak',
        'Bu bolumde tasarim deneyimi olmayan birinin Claude Code ile '
        'profesyonel gorunumlu bir mobil arayuz nasil olusturabilecegini, '
        'tasarim sistemlerini ve hazir kaynaklari aniatiyoruz.',
    )

    # ── 9.1 Tasarim Deneyimi Olmadan Tasarim ────────────────────
    doc.new_page('Bolum 9: UI/UX Tasarim Sureci')
    doc.h1('9.1  Tasarim Deneyimim Yok, Ne Yapmaliyim?')
    doc.sp(4)
    doc.text(
        'Iyi haber: Profesyonel bir grafik tasarimci olmaniza gerek yok. '
        'Claude Code, dogru talimatlar verildiginde modern ve temiz '
        'arayuzler olusturabilir. Onemli olan dogru kaynaklardan ilham '
        'almak ve tutarli bir "tasarim dili" (design system) belirlemektir.'
    )
    doc.h2('Ilham Kaynaklari')
    doc.bullets([
        'Mobbin.com — binlerce gercek uygulamadan ekran goruntusu '
        'arsivi, kategori bazinda filtreleme',
        'Dribbble.com — tasarimci portfolyolarinda mobil UI konseptleri',
        'App Store / Play Store\'da kategori liderlerini inceleme — '
        'rakip uygulamalarin nasil tasarlandigina bakin',
        'trustmrr.com — gelir kanitlanmis uygulamalarin landing page ve '
        'uygulama tasarimlarini inceleyin (Bolum 10\'da detayli)',
    ])

    # ── 9.2 Tasarim Sistemi ─────────────────────────────────────
    doc.new_page('Bolum 9: UI/UX Tasarim Sureci')
    doc.h1('9.2  Tasarim Sistemi (Design System) Olusturma')
    doc.sp(4)
    doc.text(
        'Tasarim sistemi, uygulamanizda kullanacaginiz renkleri, '
        'fontlari, bosluklari ve bilesen stillerini onceden belirlemektir. '
        'Bu, Claude Code\'a her ekran icin ayri ayri tasarim talimati '
        'vermek zorunda kalmamanizi saglar.'
    )
    doc.code(
        '> "Uygulamamiz icin bir tasarim sistemi olustur:\n'
        '>  - Ana renk: #6366F1 (indigo)\n'
        '>  - Ikincil renk: #F59E0B (amber)\n'
        '>  - Arka plan: #FFFFFF (acik mod) / #0F172A (koyu mod)\n'
        '>  - Font: Inter veya sistem fontu\n'
        '>  - Kose yuvarlatma: butun kartlarda 16px radius\n'
        '>  - Bosluklar: 4, 8, 16, 24, 32 piksel olcekli sistem\n'
        '>  Bunu theme.ts dosyasinda merkezi olarak tanimla ve tum\n'
        '>  bilesenler bu dosyadan renk/font ceksin."',
        'Claude Code Prompt'
    )
    doc.box(
        'NativeWind (Tailwind CSS\'in React Native versiyonu) kullanmak, '
        'tasarim sistemini kod icinde tutarli uygulamayi kolaylastirir. '
        '"npx expo install nativewind" ile kurabilirsiniz.',
        'tip'
    )

    # ── 9.3 Hazir Bilesen Kutuphaneleri ──────────────────────────
    doc.new_page('Bolum 9: UI/UX Tasarim Sureci')
    doc.h1('9.3  Hazir Bilesen Kutuphaneleri')
    doc.sp(4)
    doc.text(
        'Sifirdan her butonu, karti, formu tasarlamak yerine hazir, test '
        'edilmis bilesen kutuphanelerini kullanmak hem zaman kazandirir '
        'hem de daha profesyonel bir gorunum saglar.'
    )
    doc.table(
        ['Kutuphane',         'Aciklama'],
        [
            ['React Native Paper', 'Material Design tabanli, hazir buton/kart/form bilesenleri'],
            ['Gluestack UI',       'Modern, ozellesti rilebilir, NativeWind ile uyumlu'],
            ['Tamagui',            'Performans odakli, animasyon destekli bilesen seti'],
            ['React Native Reanimated', 'Akici animasyonlar icin (sayfa geciscileri, '
                                          'jest efektleri)'],
            ['Expo Vector Icons',  'Binlerce hazir ikon (ucretsiz)'],
        ],
        widths=[140, 241]
    )
    doc.code(
        '> "Bu ekrana React Native Paper kullanarak modern bir kart\n'
        '>  tasarimi ekle. Kartin ustunde bir ikon, ortasinda baslik\n'
        '>  ve alt yazi, altta da bir buton olsun. Tum kartlar arasinda\n'
        '>  16px bosluk birak ve kenarlara hafif golge ver."',
        'Claude Code Prompt'
    )

    # ── 9.4 Figma ile Calisma ────────────────────────────────────
    doc.new_page('Bolum 9: UI/UX Tasarim Sureci')
    doc.h1('9.4  Figma Tasarimini Koda Donusturme')
    doc.sp(4)
    doc.text(
        'Eger Figma\'da hazir bir tasarim varsa (kendiniz yaptiniz veya '
        'bir tasarimciya yaptirdiniz), bu tasarimi Claude Code\'a '
        'aktarabilirsiniz.'
    )
    doc.bullets([
        'Figma ekran goruntusunu kaydedip Claude Code\'a dosya olarak '
        'verebilirsiniz — Claude Code goruntuyu analiz edip benzer bir '
        'arayuz kodu yazabilir',
        'Figma\'nin "Dev Mode" ozelligi ile CSS degerlerini (renk, '
        'boyut, bosluk) dogrudan kopyalayip Claude\'a iletebilirsiniz',
        'Karmaşık tasarimlar icin ekran goruntusunu parca parca '
        'paylasin (ust bar, orta icerik, alt navigasyon ayri ayri)',
    ])
    doc.box(
        'Claude Code goruntu (screenshot) analiz edebilen bir modeldir. '
        'Bir ekran goruntusu surukleyip "bu tasarimi React Native ile '
        'uygula" diyerek dogrudan kod uretebilirsiniz.',
        'info'
    )

    # ── 9.5 Karanlik Mod ve Erisilebilirlik ──────────────────────
    doc.new_page('Bolum 9: UI/UX Tasarim Sureci')
    doc.h1('9.5  Karanlik Mod ve Erisilebilirlik')
    doc.sp(4)
    doc.text(
        '2026 itibariyle kullanicilar karanlik mod (dark mode) destegini '
        'standart bir ozellik olarak bekliyor. Ayrica gorme zorlugu '
        'cekenler icin erisilebilirlik (accessibility) ayarlari da '
        'magaza degerlendirmelerinde olumlu etki yaratir.'
    )
    doc.code(
        '> "Uygulamaya tam karanlik mod destegi ekle. Sistem ayarini\n'
        '>  otomatik algilasin (useColorScheme hook\'u), ama kullanici\n'
        '>  isterse ayarlardan manuel olarak da degistirebilsin. Tum\n'
        '>  renkler theme.ts uzerinden gelsin, hicbir yerde sabit\n'
        '>  (hardcoded) renk kullanma."',
        'Claude Code Prompt'
    )
    doc.h2('Temel Erisilebilirlik Kontrol Listesi')
    doc.bullets([
        'Tum butonlarda accessibilityLabel tanimli olsun',
        'Yazi/arka plan renk kontrasti yeterli olsun (WCAG AA standardi)',
        'Dokunma alanlari en az 44x44 piksel olsun',
        'Font boyutlari kullanici sistem ayarina gore olceklenebilsin '
        '(Dynamic Type / Font Scaling destegi)',
    ])

    # ── 9.6 Onboarding ve Ilk Izlenim ─────────────────────────────
    doc.new_page('Bolum 9: UI/UX Tasarim Sureci')
    doc.h1('9.6  Onboarding Ekranlari — Ilk Izlenim Kritiktir')
    doc.sp(4)
    doc.text(
        'Kullanicilarin uygulamayi ilk actiginda gordugu 2-3 tanitim '
        'ekrani (onboarding), uygulamanin ne yaptigini hizlica anlatir '
        've kullaniciyi kayit/girise yonlendirir. Iyi tasarlanmis bir '
        'onboarding, kullanici tutma (retention) oranini belirgin '
        'sekilde yukseltir.'
    )
    doc.bullets([
        'En fazla 3 ekran kullanin — uzun onboarding kullaniciyi '
        'sikar ve uygulamayi terk etmesine sebep olur',
        'Her ekranda bir tek mesaj verin: "Ne yapar", "Nasil yardimci '
        'olur", "Nasil baslanir"',
        'Atla (Skip) butonu her zaman görünür olsun',
        'Son ekranda net bir "Basla" / "Kayit Ol" CTA (call-to-action) '
        'butonu koyun',
    ])
    doc.code(
        '> "3 ekranlik bir onboarding akisi olustur. Her ekranda buyuk\n'
        '>  bir ikon/illustrasyon, kalin bir baslik, kisa bir aciklama\n'
        '>  metni ve alt kisimda sayfa noktalari (dot indicator) olsun.\n'
        '>  Sag ust kosede her zaman \'Atla\' linki gorunsun. Son\n'
        '>  ekranda buyuk bir \'Hemen Basla\' butonu olsun."',
        'Claude Code Prompt'
    )
    doc.box(
        'Bir sonraki bolumde uygulama fikrinizi bulma, rakip analizi ve '
        'gelir modelini (AdMob, Adapty, RevenueCat) nasil kuracaginizi '
        'detayli olarak ele alacagiz.',
        'tip'
    )
