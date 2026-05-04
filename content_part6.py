#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Icerik Part 6 — Sayfa 104-133
Bolum 10: Claude Code Skills ve MD Dosyalari
Bolum 11: SaaS Projesi Gelistirme
Bolum 12: fal.ai ve Gorsel/Video AI API
"""
from pdf_engine import Doc
from pdf_engine import NAVY, ORANGE, WHITE, BLACK, GRAY_BG, GRAY_DARK

from content_part1 import kapak_sayfasi, icindekiler, bolum1_giris, bolum1_ek_ve_bolum2_baslangic
from content_part2 import bolum2_devami, bolum3_claude_ekosistemi
from content_part3 import bolum4_claude_code, bolum5_projeler_baslangic
from content_part4 import bolum5_mobil_windows, bolum5_mobil_mac, bolum5_desktop, bolum6_store
from content_part5 import bolum7_admob, bolum8_saas, bolum9_github


def bolum10_skills(doc):
    """Bolum 10: Claude Code Skills ve MD Dosyalari"""

    doc.section_cover(
        10,
        'Claude Code Skills ve MD Dosyalari',
        'Claude\'u projenize ozgulestirin',
        'Bu bolumde CLAUDE.md, skills, hook\'lar ve MCP sunucularini kullanarak '
        'Claude Code\'u projenize tam anlamıyla adapte etmeyi ogreniyoruz.',
    )

    # ── 10.1 CLAUDE.md Derinlemesine ──────────────────────────
    doc.new_page('Bolum 10: Claude Code Skills ve MD Dosyalari')
    doc.h1('10.1  CLAUDE.md Derinlemesine')
    doc.sp(4)
    doc.text(
        'CLAUDE.md, Claude Code\'un calisma dizinini her actiginda okuduğu talimat '
        'dosyasidir. Projenize ozel kurallar, mimari kararlar, kod standartlari ve '
        'yasak listesi buraya yazilir. Iyi bir CLAUDE.md, sanki deneyimli bir '
        'gelistiriciyi projeye tanistiriyor gibi calisir.'
    )

    doc.h2('Etkili CLAUDE.md Yapisi')
    doc.code(
        '# Proje Adi ve Amaci\n'
        'Bu bir e-ticaret SaaS platformudur. Satici ve musteri\n'
        'iki farkli panel icermektedir.\n\n'
        '## Tech Stack\n'
        '- Frontend: Next.js 15, TypeScript, Tailwind, shadcn/ui\n'
        '- Backend: Next.js API routes, Prisma, PostgreSQL\n'
        '- Auth: NextAuth.js v5 (Auth.js)\n'
        '- Odeme: Stripe Subscriptions\n'
        '- Deploy: Vercel + Supabase\n\n'
        '## Dizin Yapisi\n'
        'src/app/          — Next.js App Router sayfalar\n'
        'src/components/   — Yeniden kullanilabilir bilesenleri\n'
        'src/lib/          — Yardimci fonksiyonlar\n'
        'src/server/       — Server actions ve API mantigi\n\n'
        '## Kurallar\n'
        '- TypeScript strict mod, tip hatasi kabul edilmez\n'
        '- Her server action icin Zod validasyonu yaz\n'
        '- Tailwind icin class-variance-authority kullan\n'
        '- console.log yazma, bunun yerine logger kullan\n'
        '- Test: Vitest + React Testing Library\n\n'
        '## YASAKLAR\n'
        '- any tipi kullanma\n'
        '- useEffect icinde async/await kullanma\n'
        '- Dogrudan DB sorgusu yazmak yerine repository pattern kullan',
        'Markdown'
    )

    doc.h2('Hiyerarsik CLAUDE.md')
    doc.text(
        'Claude Code, ic ice dizinlerdeki CLAUDE.md dosyalarini da okur ve birlestirir. '
        'Kok dizindeki genel kurallar her yerde gecerliyken alt dizinlerdeki '
        'CLAUDE.md dosyalari o modüle ozgu talimatlar icin kullanilabilir.'
    )
    doc.code(
        'proje/\n'
        '├── CLAUDE.md          # Genel kurallar\n'
        '├── src/\n'
        '│   ├── app/\n'
        '│   │   └── CLAUDE.md  # Sayfa yaratma kurallari\n'
        '│   ├── components/\n'
        '│   │   └── CLAUDE.md  # Bilesen standartlari\n'
        '│   └── server/\n'
        '│       └── CLAUDE.md  # Server action kurallari',
        'Terminal'
    )

    # ── 10.2 Skills ───────────────────────────────────────────
    doc.new_page('Bolum 10: Claude Code Skills ve MD Dosyalari')
    doc.h1('10.2  Skills (Slash Komutlari) Olusturma')
    doc.sp(4)
    doc.text(
        'Skills, Claude Code\'a ozel slash komutlari tanimlamanizi saglar. '
        '.claude/commands/ dizinine Markdown dosyalari koyarak /komudum seklinde '
        'cagirabileceginiz tekrar kullanilanabilir talimat setleri olusturabilirsiniz.'
    )
    doc.code(
        '# .claude/commands/pr-review.md\n'
        'Mevcut branch\'teki degisiklikleri incele:\n'
        '1. Tip guvenligi kontrolu yap\n'
        '2. Test eksiklerini belirle\n'
        '3. Guvenlik aciklari var mi kontrol et\n'
        '4. Performans sorunlari var mi?\n'
        '5. CLAUDE.md kurallarına uygunluk kontrolu\n'
        '6. Bulgulayi madde madde raporla\n\n'
        '# Kullanim:\n'
        '> /pr-review',
        'Markdown'
    )
    doc.code(
        '# .claude/commands/new-feature.md\n'
        'Arguman: $ARGUMENTS\n\n'
        'Yeni bir ozellik ekle: $ARGUMENTS\n\n'
        'Adimlar:\n'
        '1. src/types/ icinde gerekli tip tanimlarini ekle\n'
        '2. src/server/ icinde repository ve service yaz\n'
        '3. src/app/api/ icinde API route olustur\n'
        '4. src/components/ icinde UI bilesenlerini yaz\n'
        '5. src/app/ icinde sayfayi olustur\n'
        '6. Test dosyasini ekle\n'
        '7. CLAUDE.md kurallarini kontrol et\n\n'
        '# Kullanim:\n'
        '> /new-feature kullanici profil sayfasi',
        'Markdown'
    )
    doc.box(
        'Skills en cok tekrar eden is akislari icin degerlidir. '
        '"Her ozellik eklemede ayni adimlari takip et" seklindeki '
        'talimatlari bir skill haline getirin ve /new-feature ile cagirin. '
        'Bu kodlama standartlarinizin tutarli kalmasini saglar.',
        'tip'
    )

    # ── 10.3 Hooks ────────────────────────────────────────────
    doc.new_page('Bolum 10: Claude Code Skills ve MD Dosyalari')
    doc.h1('10.3  Hooks: Otomatik Tetikleyiciler')
    doc.sp(4)
    doc.text(
        'Hooks, belirli olaylar gerceklestiginde otomatik calistirilan komutlardir. '
        'Ornégin her dosya kaydedildiginde lint, her tool kullanimi oncesinde '
        'log alma veya bitis sonrasinda bildirim gonderme gibi islemler '
        '.claude/settings.json icindeki hooks yapilandirmasi ile saglanir.'
    )

    doc.h2('Hook Turleri')
    doc.table(
        ['Hook Turu',       'Ne Zaman Tetiklenir?',              'Kullanim Ornegi'],
        [
            ['PreToolUse',      'Bir arac kullanilmadan once',       'Log al, izin kontrol et'],
            ['PostToolUse',     'Arac kullanimi sonrasinda',         'Lint/format calistir'],
            ['Notification',   'Claude bildirim gonderdiginde',      'Sistem bildirimi'],
            ['Stop',           'Oturum sonunda',                     'Git push, ozet rapor'],
        ],
        widths=[110, 185, 176]
    )
    doc.code(
        '// .claude/settings.json\n'
        '{\n'
        '  "hooks": {\n'
        '    "PostToolUse": [\n'
        '      {\n'
        '        "matcher": "Write|Edit",\n'
        '        "hooks": [{\n'
        '          "type": "command",\n'
        '          "command": "npm run lint:fix 2>&1 | tail -5"\n'
        '        }]\n'
        '      }\n'
        '    ],\n'
        '    "Stop": [\n'
        '      {\n'
        '        "hooks": [{\n'
        '          "type": "command",\n'
        '          "command": "git add -A && git diff --stat HEAD"\n'
        '        }]\n'
        '      }\n'
        '    ]\n'
        '  }\n'
        '}',
        'JSON'
    )

    # ── 10.4 MCP Sunuculari ───────────────────────────────────
    doc.new_page('Bolum 10: Claude Code Skills ve MD Dosyalari')
    doc.h1('10.4  MCP Sunuculari ile Araclari Genisletme')
    doc.sp(4)
    doc.text(
        'Model Context Protocol (MCP), Claude Code\'un dis sistemlerle — veritabani, '
        'API\'lar, dosya sistemleri — konusmasini saglayan acik standarttir. '
        'Hazir MCP sunucularini kurarak Claude\'a yeni yetenekler kazandirabilirsiniz.'
    )

    doc.h2('Populer MCP Sunuculari')
    doc.bullets([
        '@anthropic/mcp-server-filesystem — Yerel dosya sistemi erisimi',
        '@modelcontextprotocol/server-github — GitHub repo, issue, PR islemleri',
        '@modelcontextprotocol/server-postgres — PostgreSQL sorgulari',
        '@modelcontextprotocol/server-brave-search — Brave Search ile web arama',
        '@modelcontextprotocol/server-puppeteer — Tarayici otomasyonu',
        'mcp-server-supabase — Supabase DB, Auth, Storage yonetimi',
    ])
    doc.code(
        '// .claude/settings.json\n'
        '{\n'
        '  "mcpServers": {\n'
        '    "github": {\n'
        '      "command": "npx",\n'
        '      "args": ["-y", "@modelcontextprotocol/server-github"],\n'
        '      "env": { "GITHUB_TOKEN": "ghp_XXXX" }\n'
        '    },\n'
        '    "supabase": {\n'
        '      "command": "npx",\n'
        '      "args": ["-y", "mcp-server-supabase"],\n'
        '      "env": {\n'
        '        "SUPABASE_URL": "https://xxx.supabase.co",\n'
        '        "SUPABASE_KEY": "eyJ..."\n'
        '      }\n'
        '    }\n'
        '  }\n'
        '}',
        'JSON'
    )
    doc.box(
        'MCP sunuculari Claude\'a gercek yetenekler katar. Supabase MCP kurulunca '
        '"Kullanicilar tablosuna bak, son 7 gunde kayit olanlar kac kisi?" gibi '
        'dogal dil sorularini dogrudan veritabanina yonlendirebilirsiniz.',
        'tip'
    )


def bolum11_saas_proje(doc):
    """Bolum 11: SaaS Projesi Gelistirme"""

    doc.section_cover(
        11,
        'SaaS Projesi Gelistirme',
        'Sifirdan gelir getiren urun',
        'Bu bolumde Claude Code yardimiyla sifirdan bir SaaS urun tasarlayip, '
        'gelistirip yayinlama surecini adim adim inceliyoruz.',
    )

    # ── 11.1 Fikir ve Validasyon ──────────────────────────────
    doc.new_page('Bolum 11: SaaS Projesi Gelistirme')
    doc.h1('11.1  Fikir Validasyonu')
    doc.sp(4)
    doc.text(
        'Kod yazmadan once fikrinizin gercek bir problemi cozup cozmedigini '
        'anlamak kritik oneme sahiptir. Aylar sonra "kimse istemiyor" '
        'kesifleri yapmamak icin ilk haftayi validasyona ayirin.'
    )

    doc.h2('Validasyon Adimlari')
    doc.bullets([
        '1. Problemi net tanimla: "Kim, ne zaman bu problemi yasIyor?"',
        '2. Reddit, Twitter, Hacker News\'de sorun hakkindaki tartismalari bul',
        '3. Rakipleri ara: alternativeto.net, Product Hunt, G2',
        '4. Landing page olustur (no-code), email listesi topla',
        '5. 10 potansiyel kullaniciya birebir gorüsme yap',
        '6. Hedef: kod yazmadan 5 on-siparis veya 50 email adresi topla',
    ])
    doc.box(
        'Claude Code\'a "Bu SaaS fikri icin musteri validasyon plani olustur" '
        'diyebilirsiniz. Size hedef kitle analizi, rekabet araştirmasi ve '
        'gorüsme sorulari hazirlayacaktir.',
        'tip'
    )

    # ── 11.2 Tech Stack ───────────────────────────────────────
    doc.new_page('Bolum 11: SaaS Projesi Gelistirme')
    doc.h1('11.2  SaaS icin Tech Stack Secimi')
    doc.sp(4)

    doc.h2('Onerilern Stack: Next.js + Supabase + Stripe')
    doc.text(
        'Tek kisilik veya kucuk takim SaaS\'lar icin en uretken stack:'
    )
    doc.table(
        ['Katman',      'Teknoloji',          'Neden?'],
        [
            ['Frontend',    'Next.js + TypeScript','SEO, SSR, full-stack tek repoda'],
            ['UI',          'Tailwind + shadcn/ui','Hizli prototipleme, guzel varsayilan'],
            ['Auth',        'Supabase Auth',       'Sosyal login, magic link, RLS hazir'],
            ['Veritabani',  'Supabase Postgres',   'Gercek zamanli, Row Level Security'],
            ['Odeme',       'Stripe',              'Abonelik, webhook, portal hazir'],
            ['Email',       'Resend',              'React Email ile guzel sablonlar'],
            ['Deploy',      'Vercel',              'Sifir yapilandirma, edge network'],
            ['Analitik',    'PostHog',             'Olay izleme, funnel, session replay'],
        ],
        widths=[80, 140, 251]
    )
    doc.sp(6)
    doc.h2('Alternatif Stack: T3')
    doc.code(
        '# T3 Stack (Next.js + tRPC + Prisma + NextAuth):\n'
        'npm create t3-app@latest benim-saas\n\n'
        '# Veya SaaS starter sablonlari:\n'
        '# - github.com/leerob/next-saas-starter\n'
        '# - github.com/boxyhq/saas-starter-kit\n'
        '# - github.com/mickasmt/next-saas-stripe-starter',
        'Terminal'
    )

    # ── 11.3 Proje Yapilandirma ───────────────────────────────
    doc.new_page('Bolum 11: SaaS Projesi Gelistirme')
    doc.h1('11.3  Claude Code ile Proje Kurulumu')
    doc.sp(4)
    doc.code(
        '# Claude Code\'a adim adim sorun:\n\n'
        '# 1. Proje iskeletini olustur:\n'
        '> "Next.js 15 + TypeScript + Tailwind + shadcn/ui projesini\n'
        '>  olustur. Supabase ile auth ekle (Google + email/sifre).\n'
        '>  Stripe abonelik sistemi kur (free/pro/enterprise planlari).\n'
        '>  Landing page, pricing sayfasi ve dashboard iskeletini yaz."\n\n'
        '# 2. Veritabani semasinii tanimla:\n'
        '> "Kullanicilarin proje olusturabileceği bir SaaS icin\n'
        '>  Supabase sema olustur: users, projects, subscriptions,\n'
        '>  usage_logs tablolari. RLS kurallarini ekle."\n\n'
        '# 3. Core ozellik:\n'
        '> "Kullanici proje olusturabilsin, duzenleyebilsin, silebilsin.\n'
        '>  CRUD islemleri server action ile yapilsin. Optimistic update ekle."',
        'Terminal'
    )

    doc.h2('Temel Dizin Yapisi')
    doc.code(
        'src/\n'
        '├── app/\n'
        '│   ├── (auth)/\n'
        '│   │   ├── login/page.tsx\n'
        '│   │   └── signup/page.tsx\n'
        '│   ├── (dashboard)/\n'
        '│   │   ├── layout.tsx        # Sidebar + header\n'
        '│   │   ├── dashboard/page.tsx\n'
        '│   │   └── projects/\n'
        '│   │       ├── page.tsx      # Liste\n'
        '│   │       └── [id]/page.tsx # Detay\n'
        '│   ├── api/\n'
        '│   │   └── webhooks/stripe/route.ts\n'
        '│   └── page.tsx              # Landing\n'
        '├── components/\n'
        '├── lib/\n'
        '│   ├── supabase/\n'
        '│   └── stripe/\n'
        '└── server/\n'
        '    └── actions/',
        'Terminal'
    )

    # ── 11.4 Launch Checklist ─────────────────────────────────
    doc.new_page('Bolum 11: SaaS Projesi Gelistirme')
    doc.h1('11.4  Launch Checklist')
    doc.sp(4)

    doc.h2('Teknik Kontroller')
    doc.bullets([
        'HTTPS zorunlu, HTTP\'yi HTTPS\'e yonlendir',
        'Environment variable\'lar .env.local\'da, .gitignore\'da kayitli',
        'Stripe webhook imzasi dogrulanıyor (stripe.webhooks.constructEvent)',
        'Supabase RLS politikalari aktif — kullanici sadece kendi verisini gorebilir',
        'Rate limiting eklendi (Upstash Redis + Ratelimit veya Vercel)',
        'Error tracking: Sentry veya Axiom',
        'Yükleme hizlari kabul edilebilir: Lighthouse skoru > 85',
        'Tum formlar server-side validasyona sahip (Zod)',
    ])

    doc.h2('Is Kontrolleri')
    doc.bullets([
        'Odeme akisi gercek kartla test edildi',
        'Iptal ve refund akisi calisıyor',
        'Webhook\'lar production ortaminda test edildi',
        'Hosgeldin emaili gonderiliyor',
        'Kullanim kosullari ve gizlilik politikasi sayfasi var',
        'Support kanali tanimli (email / Intercom / Crisp)',
        'Analytics kurulu: kullanicilari izleyebiliyorsunuz',
        'Yedekleme plani var: Supabase gunluk yedekleme aktif',
    ])

    doc.box(
        'Claude Code\'a "Launch checklist\'imi gozden gecir, eksikleri tamamla" '
        'diyebilirsiniz. Kodunuzu tarayip guvenlik aciklarini, eksik '
        'validasyonlari ve yapi hatalarini bildirecektir.',
        'tip'
    )

    # ── 11.5 Buyume Stratejisi ────────────────────────────────
    doc.new_page('Bolum 11: SaaS Projesi Gelistirme')
    doc.h1('11.5  Lansman Sonrasi Buyume')
    doc.sp(4)

    doc.h2('Ilk 100 Kullanici')
    doc.bullets([
        'Product Hunt lansmanı: PH Upcoming ile onceden duyuru toplayin',
        'Hacker News Show HN: pazartesi sabahi UTC 12:00\'de paylasin',
        'Twitter/X: building in public, haftalik ilerleme paylasimi',
        'Reddit: hedef kitlenizin oldugu subreddit\'lerde yardimci icerik',
        'YouTube: kurulumdan lansmana kadar seri video',
        'Cold email: potansiyel musterilere 50-100 adet kisisellestirilmis email',
    ])

    doc.h2('Metrikler')
    doc.table(
        ['Metrik',      'Formul',                         'Hedef (ilk 6 ay)'],
        [
            ['MRR',         'Aktif abonelik x aylik ucret',    '$1.000+'],
            ['Churn',       'Iptal / toplam abone',            '< %5/ay'],
            ['CAC',         'Pazarlama harcamasi / yeni mus.', '< 3 aylik LTV'],
            ['LTV',         'Ortalama abonelik suresi x ucret', 'CAC x 3+'],
            ['Activation',  'Kayit → kor ozellik kullanan',     '> %40'],
            ['NPS',         'Oneririm mi? 0-10 anketi',        '> 30'],
        ],
        widths=[80, 210, 181]
    )


def bolum12_falai(doc):
    """Bolum 12: fal.ai ve Gorsel/Video AI API"""

    doc.section_cover(
        12,
        'fal.ai ve Gorsel/Video AI API',
        'AI ile gorsel ve video uretimi',
        'Bu bolumde fal.ai platformunu, en guclü gorsel ve video AI modellerini '
        've bu API\'lari projelerinize entegre etmeyi inceliyoruz.',
    )

    # ── 12.1 fal.ai Nedir? ────────────────────────────────────
    doc.new_page('Bolum 12: fal.ai ve Gorsel/Video AI API')
    doc.h1('12.1  fal.ai Nedir?')
    doc.sp(4)
    doc.text(
        'fal.ai, gorsel, video ve ses AI modellerini API uzerinden sunduran bir '
        'inferans platformudur. Flux, Stable Diffusion, Kling, CogVideoX gibi '
        'guclu modellere tek bir API anahtariyla erisebilirsiniz. '
        'Olusturulan gorsel veya videolar CDN\'e otomatik yuklenir ve URL geri doner.'
    )

    doc.h2('fal.ai Avantajlari')
    doc.bullets([
        'Cok sayida model tek API: Flux Pro, Flux Dev, SDXL, Kling, CogVideoX...',
        'Cok hizli: Flux Schnell ile 0.6 saniyede gorsel uretimi',
        'CDN entegrasyonu: sonuc dosyalari otomatik depolanir ve URL verilir',
        'Webhook destegi: uzun video islemleri icin async kuyruk',
        'Typescript ve Python SDK\'lari hazir',
        'Ucretsiz kredi ile baslayin, kullandıginiz kadar odeyin',
    ])

    doc.h2('Hesap ve API Anahtari')
    doc.code(
        '# fal.ai\'de ucretsiz hesap olusturun:\n'
        '# fal.ai → Sign Up → API Keys → Create Key\n\n'
        '# SDK kurulumu:\n'
        'npm install @fal-ai/client\n\n'
        '# .env.local:\n'
        'FAL_KEY=your_fal_api_key_here\n\n'
        '# Veya ortam degiskeni olarak:\n'
        'export FAL_KEY="your_fal_api_key_here"',
        'Terminal'
    )

    # ── 12.2 Gorsel Uretimi ───────────────────────────────────
    doc.new_page('Bolum 12: fal.ai ve Gorsel/Video AI API')
    doc.h1('12.2  Gorsel Uretimi: Flux ile')
    doc.sp(4)
    doc.text(
        'Flux, 2024-2025 itibariyle en guclu acik gorsel uretim modeli haline gelmistir. '
        'fal.ai uzerinden Flux Pro (en kaliteli), Flux Dev (dengeli) ve '
        'Flux Schnell (en hizli, ucuz) versiyonlarina erisebilirsiniz.'
    )

    doc.h2('Temel Gorsel Uretimi')
    doc.code(
        'import { fal } from "@fal-ai/client";\n\n'
        'fal.config({ credentials: process.env.FAL_KEY });\n\n'
        'async function gorselUret(prompt: string) {\n'
        '  const result = await fal.subscribe("fal-ai/flux/dev", {\n'
        '    input: {\n'
        '      prompt,\n'
        '      image_size: "landscape_16_9",\n'
        '      num_inference_steps: 28,\n'
        '      guidance_scale: 3.5,\n'
        '      num_images: 1,\n'
        '    },\n'
        '    logs: true,\n'
        '    onQueueUpdate: (update) => {\n'
        '      if (update.status === "IN_PROGRESS") {\n'
        '        console.log("Islem:", update.logs);\n'
        '      }\n'
        '    },\n'
        '  });\n'
        '  return result.data.images[0].url;\n'
        '}',
        'TypeScript'
    )

    doc.h2('Flux Model Karsilastirmasi')
    doc.table(
        ['Model',          'Hiz',           'Kalite',  'Fiyat (1K gorsel)'],
        [
            ['Flux Schnell',   '0.6 saniye',    'Orta',    '~$0.30'],
            ['Flux Dev',       '3-5 saniye',    'Yuksek',  '~$2.50'],
            ['Flux Pro',       '5-10 saniye',   'En yüksek','~$5.00'],
            ['Flux Pro Ultra', '10-15 saniye',  'Ultra',    '~$8.00'],
        ],
        widths=[120, 100, 100, 151]
    )

    # ── 12.3 Gorsel-den-Gorsel ────────────────────────────────
    doc.new_page('Bolum 12: fal.ai ve Gorsel/Video AI API')
    doc.h1('12.3  Gorsel-den-Gorsel ve Inpainting')
    doc.sp(4)
    doc.text(
        'Sadece metin-den-gorsel degil; mevcut bir gorseli donusturmek, '
        'belirli bir alani degistirmek (inpainting) veya gorseli buyutmek '
        '(outpainting) de fal.ai ile mumkundur.'
    )
    doc.code(
        '// Gorsel-den-gorsel donusturme:\n'
        'const result = await fal.subscribe("fal-ai/flux/dev/image-to-image", {\n'
        '  input: {\n'
        '    prompt: "ayni sahne, gece ve neon isiklar altinda",\n'
        '    image_url: "https://cdn.ornekleri.com/fotograf.jpg",\n'
        '    strength: 0.75,  // 0=orijinal, 1=tamamen yeni\n'
        '    num_inference_steps: 28,\n'
        '  },\n'
        '});\n\n'
        '// Yuz degistirme / kimlik koruma:\n'
        'const faceSwap = await fal.subscribe("fal-ai/pulid", {\n'
        '  input: {\n'
        '    prompt: "profesyonel is portroesi, ofis ortami",\n'
        '    reference_images: [{ image_url: "yuz.jpg" }],\n'
        '  },\n'
        '});',
        'TypeScript'
    )

    # ── 12.4 Video Uretimi ────────────────────────────────────
    doc.new_page('Bolum 12: fal.ai ve Gorsel/Video AI API')
    doc.h1('12.4  Video Uretimi: Kling ve Veo')
    doc.sp(4)
    doc.text(
        'Video AI modelleri 2025 itibariyle inanilmaz bir kaliteye ulasti. '
        'fal.ai uzerinden Kling 1.6, CogVideoX ve diger modellere erisebilirsiniz. '
        'Video uretimi birkaç dakika surebileceginden webhook kullanimi onerilir.'
    )
    doc.code(
        '// Metin-den-video (Kling 1.6):\n'
        'const video = await fal.subscribe("fal-ai/kling-video/v1.6/standard/text-to-video", {\n'
        '  input: {\n'
        '    prompt: "Bir kadin sahil yukurugunde kosarken gulumsüyor,\n'
        '             altin saati fotografi, yavaş cekim",\n'
        '    duration: "5",   // 5 veya 10 saniye\n'
        '    aspect_ratio: "16:9",\n'
        '  },\n'
        '  logs: true,\n'
        '  onQueueUpdate: (update) => console.log(update.status),\n'
        '});\n'
        'console.log("Video URL:", video.data.video.url);',
        'TypeScript'
    )
    doc.code(
        '// Gorsel-den-video (statik gorseli hayata gecirir):\n'
        'const animated = await fal.subscribe(\n'
        '  "fal-ai/kling-video/v1.6/standard/image-to-video",\n'
        '  {\n'
        '    input: {\n'
        '      prompt: "kamera saga kayiyor, hafif ruzgar",\n'
        '      image_url: "https://ornekleri.com/sahne.jpg",\n'
        '      duration: "5",\n'
        '    },\n'
        '  }\n'
        ');',
        'TypeScript'
    )
    doc.box(
        'Video islemleri uzun surer (30 saniye - 5 dakika). '
        'Kullanicilara "Videonuz hazirlanıyor..." mesajı gosterin '
        've webhook ile tamamlaninca bildirin. '
        'fal.ai webhook URL\'ini kolayca yapilandirebilirsiniz.',
        'info'
    )

    # ── 12.5 EticPanel Case Study ─────────────────────────────
    doc.new_page('Bolum 12: fal.ai ve Gorsel/Video AI API')
    doc.h1('12.5  EticPanel.com Case Study')
    doc.sp(4)
    doc.text(
        'EticPanel.com, fal.ai API\'larini kullanarak gorsel AI uretimini SaaS '
        'urun haline getirmenin gercek bir ornegi olarak bu kitabin yazari Aykut Uces '
        'tarafindan insa edilmistir. Asagida gelistirme surecinden ogrenilen dersler '
        'paylasılmaktadir.'
    )

    doc.h2('Ogrenilenler')
    doc.bullets([
        'Rate limiting: Her kullanici icin ayri kuyruk sistemi kurulmalı',
        'Maliyet yonetimi: Kullanici basina aylik kredi sistemi (kullanim limiti)',
        'CDN: fal.ai CDN URL\'leri 24 saat sonra silinebilir; kendi S3\'unuze kopyalayin',
        'Hata yonetimi: Model zaman zaman "content policy" hatasi verir; retry + fallback',
        'UX: Gercek zamanli ilerleme cubugu (WebSocket veya Server-Sent Events)',
        'Prompt engineering: Farkli modeller farkli prompt formatlari ister',
    ])

    doc.h2('Mimarisi')
    doc.code(
        '// Genel yapi:\n'
        'Kullanici → Next.js API → Redis Queue → Worker\n'
        '                                          ↓\n'
        '                                       fal.ai API\n'
        '                                          ↓\n'
        '                                      Supabase Storage\n'
        '                                          ↓\n'
        '                              WebSocket → Kullanici bildirimi\n\n'
        '// Kredi kontrolu:\n'
        'const kullanici = await supabase\n'
        '  .from("users")\n'
        '  .select("credits")\n'
        '  .eq("id", userId)\n'
        '  .single();\n\n'
        'if (kullanici.data.credits < islemMaliyeti) {\n'
        '  return { error: "Yetersiz kredi" };\n'
        '}',
        'TypeScript'
    )


def main():
    doc = Doc()
    print("Icerik olusturuluyor — Sayfa 104-133...")

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
    bolum10_skills(doc)
    bolum11_saas_proje(doc)
    bolum12_falai(doc)

    pages = doc.save('yapay_zeka_ogreniyorum_p1_133.pdf')
    print(f"\nTamamlandi! Toplam {pages} sayfa uretildi.")
    print("Dosya: yapay_zeka_ogreniyorum_p1_133.pdf")


if __name__ == '__main__':
    main()
