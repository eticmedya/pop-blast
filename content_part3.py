#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Icerik Part 3 — Sayfa 38-60
Bolum 4: Claude Code Kurulum ve Kullanim (tam)
Bolum 5: Claude Code ile Gercek Projeler (baslangic)
"""
from pdf_engine import Doc, PW, PH, ML, MR, CW
from pdf_engine import NAVY, ORANGE, WHITE, BLACK, GRAY_BG, GRAY_DARK

from content_part1 import kapak_sayfasi, icindekiler, bolum1_giris, bolum1_ek_ve_bolum2_baslangic
from content_part2 import bolum2_devami, bolum3_claude_ekosistemi


def bolum4_claude_code(doc):
    """Bolum 4: Claude Code Kurulum ve Kullanim"""

    doc.section_cover(
        4,
        'Claude Code Kurulum ve Kullanim',
        'Terminal\'den AI destekli yazilim gelistirme',
        'Bu bolumde Node.js kurulumundan baslayarak Claude Code\'u adim adim '
        'kuruyoruz. Temel komutlar, CLAUDE.md, slash komutlari, MCP server '
        'baglama, hooks ve subagentlari detaylica inceliyoruz.'
    )

    # ── 4.1 Node.js Kurulumu ───────────────────────────────
    doc.new_page('Bolum 4: Claude Code Kurulum ve Kullanim')
    doc.h1('4.1  Node.js Kurulumu')
    doc.sp(4)
    doc.text(
        'Claude Code, Node.js uzerinde calisan bir npm paketidir. Kurulum yapmadan once '
        'sisteminizde Node.js\'in yuklu olmasi gerekir. Node.js hem Windows hem de '
        'macOS icin resmi yukleyicilerle kolayca kurulabilir.'
    )

    doc.h2('Windows\'ta Node.js Kurulumu')
    doc.bullets([
        '1. nodejs.org adresine gidin',
        '2. "LTS" (Long Term Support) surum butonuna tiklayin — ornegin Node 22 LTS',
        '3. Indirilen .msi dosyasini calistirin',
        '4. Kurulum sihirbazinda "Next" diyerek devam edin, tum secenekleri varsayilan birakin',
        '5. Kurulum bittikten sonra PowerShell\'i yonetici olarak acin',
        '6. "node --version" yazin — v22.x.x gibi bir cikti gormelisiniz',
        '7. "npm --version" yazin — 10.x.x gibi bir cikti gormelisiniz',
    ])
    doc.code(
        '# PowerShell\'de dogrulama\n'
        'node --version\n'
        '# v22.13.0\n\n'
        'npm --version\n'
        '# 10.9.2',
        'PowerShell'
    )
    doc.box(
        'Windows\'ta PowerShell\'i her zaman "Yonetici Olarak Calistir" secenegiyle acin. '
        'Aksi takdirde global npm paketleri kurarken izin hatasi alabilirsiniz. '
        'Baslatma menusu → PowerShell → Sag tik → Yonetici Olarak Calistir.',
        'warning'
    )

    doc.h2('macOS\'ta Node.js Kurulumu')
    doc.text(
        'macOS\'ta Node.js kurmanin iki yolu var: Resmi yukleyici veya Homebrew. '
        'Homebrew kullananlar icin ikinci yol daha pratiktir.'
    )
    doc.h3('Yol 1: Resmi Yukleyici')
    doc.bullets([
        '1. nodejs.org adresine gidin',
        '2. macOS LTS butonuna tiklayin',
        '3. Indirilen .pkg dosyasini calistirin',
        '4. Kurulum tamamlandiktan sonra Terminal\'i acin',
        '5. "node --version" ile dogrulayin',
    ])
    doc.h3('Yol 2: Homebrew (Onerilir)')
    doc.code(
        '# Homebrew yoksa once bunu kurun:\n'
        '/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"\n\n'
        '# Node.js kurulumu:\n'
        'brew install node\n\n'
        '# Dogrulama:\n'
        'node --version   # v22.x.x\n'
        'npm --version    # 10.x.x',
        'Terminal (macOS)'
    )
    doc.h3('NVM ile Surum Yonetimi (Pro Ipucu)')
    doc.text(
        'Birden fazla Node.js surumu ile calismak isteyenler icin NVM '
        '(Node Version Manager) kullanmak en iyi pratiktir.'
    )
    doc.code(
        '# NVM kurulumu (Mac/Linux)\n'
        'curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash\n\n'
        '# Terminal\'i yeniden acin, ardindan:\n'
        'nvm install 22        # Node 22 LTS kur\n'
        'nvm use 22            # Node 22\'yi aktif et\n'
        'nvm alias default 22  # Varsayilan yap\n'
        'node --version        # v22.x.x',
        'Terminal'
    )

    # ── 4.2 Terminal Nedir? ────────────────────────────────
    doc.new_page('Bolum 4: Claude Code Kurulum ve Kullanim')
    doc.h1('4.2  Terminal Nedir? Temel Kullanim')
    doc.sp(4)
    doc.text(
        'Terminal (veya komut satirı), bilgisayarinizla metin komutlari araciligiyla '
        'iletisim kurdugunuz arabirimdir. Claude Code tamamen terminal uzerinde calisir. '
        'Terminal\'den korkmayın — gunluk birkac komut yeterlidir.'
    )

    doc.h2('Windows: PowerShell ve Windows Terminal')
    doc.text(
        'Windows\'ta iki secenek var: Eski CMD (Komut Istemi) ve modern PowerShell. '
        'Claude Code icin PowerShell veya Windows Terminal kullanin. '
        'Windows 11\'de Windows Terminal varsayilan olarak gelir.'
    )
    doc.bullets([
        'Acmak icin: Win+X → Windows Terminal (Yonetici)',
        'Ya da: Baslatma menusu → "powershell" yaz → Yonetici olarak calistir',
        'WSL (Windows Subsystem for Linux) kullaniyorsaniz Ubuntu terminali de calisir',
    ])

    doc.h2('macOS: Terminal ve iTerm2')
    doc.bullets([
        'Varsayilan: Uygulamalar → Yardimci Programlar → Terminal',
        'Hizli acmak: Cmd+Space → "terminal" yaz → Enter',
        'Profesyonel alternatif: iTerm2 (iterm2.com — cok daha guclu)',
        'Zsh: macOS\'un varsayilan shell\'i, .zshrc dosyasiyla yapilandirilir',
    ])

    doc.h2('En Cok Kullanilan Terminal Komutlari')
    doc.table(
        ['Komut', 'Aciklama', 'Ornek'],
        [
            ['ls / dir',    'Klasor icerigini listele',     'ls -la (Mac) / dir (Win)'],
            ['cd',          'Klasor degistir',              'cd Desktop/projem'],
            ['cd ..',       'Ust klasore don',              'cd ..'],
            ['pwd',         'Bulundugun yolu goster',       'pwd → /Users/aykut/Desktop'],
            ['mkdir',       'Yeni klasor olustur',          'mkdir yeni-proje'],
            ['rm -rf',      'Klasor/dosya sil (dikkat!)',   'rm -rf node_modules'],
            ['cp',          'Dosya kopyala',                'cp dosya.txt kopya.txt'],
            ['cat',         'Dosya icerigini goster',       'cat CLAUDE.md'],
            ['clear',       'Terminal ekranini temizle',    'clear'],
            ['Ctrl+C',      'Calisani durdur',              'Sonsuz dongu durdurma'],
        ],
        widths=[75, 155, 241]
    )
    doc.sp(6)
    doc.box(
        'Claude Code kullanirken en cok ihtiyac duyacaginiz komutlar: '
        '"cd" (proje klasorune gecmek) ve "claude" (Claude Code\'u baslatmak). '
        'Geri kalan her seyi Claude Code sizin icin yapar.',
        'tip'
    )

    doc.h2('Proje Klasorune Gecmek')
    doc.code(
        '# Mac\'te masaustundeki "projem" klasorune gecmek:\n'
        'cd ~/Desktop/projem\n\n'
        '# Windows\'ta masaustundeki klasore gecmek:\n'
        'cd C:\\Users\\KullaniciAdi\\Desktop\\projem\n\n'
        '# Ipucu: Klasoru terminal\'e suruklersen yolunu otomatik yazar!\n'
        '# Mac: Klasoru Terminal penceresine suruklleyin\n'
        '# Win: Explorer\'da klasore sag tik → "Terminalde Ac"',
        'Terminal'
    )

    # ── 4.3 Claude Code Kurulumu ───────────────────────────
    doc.new_page('Bolum 4: Claude Code Kurulum ve Kullanim')
    doc.h1('4.3  Claude Code Kurulumu')
    doc.sp(4)
    doc.text(
        'Node.js kurulduktan sonra Claude Code\'u kurmak tek bir komutla olur. '
        'Bu komut Claude Code\'u global olarak kurar, yani herhangi bir klasorden '
        '"claude" yazarak calistirabilirsizin.'
    )

    doc.h2('Kurulum Komutu')
    doc.code(
        '# Claude Code\'u global olarak kur:\n'
        'npm install -g @anthropic-ai/claude-code\n\n'
        '# Kurulumu dogrula:\n'
        'claude --version\n'
        '# Claude Code 1.x.x',
        'Terminal'
    )
    doc.box(
        'Kurulum sirasinda "permission denied" hatasi aliyorsaniz Mac\'te '
        '"sudo npm install -g @anthropic-ai/claude-code" komutunu deneyin. '
        'Windows\'ta PowerShell\'i yonetici olarak acip tekrar deneyin.',
        'warning'
    )

    doc.h2('Ilk Giris ve Authentication')
    doc.text(
        'Claude Code\'u ilk kez calistirdiginizdaAnthropicHesabinizla oturum '
        'acmaniz gerekir. Hesabinizda Claude Max plani olmasi zorunludur.'
    )
    doc.code(
        '# Herhangi bir klasorde Claude Code\'u baslatin:\n'
        'claude\n\n'
        '# Ilk calistirmada tarayici acilir ve giris yapmanizi ister.\n'
        '# Anthropic hesabinizla giris yapin.\n'
        '# Giris basarili oldugunda terminale doner ve hazir olur:\n\n'
        '# Claude Code v1.x.x\n'
        '# > (buraya prompt yazabilirsiniz)',
        'Terminal'
    )
    doc.h3('API Key ile Kullanim (Alternatif)')
    doc.text(
        'Claude Max plani yerine API key ile de kullanabilirsiniz. '
        'Bu yontem ozellikle otomasyon ve CI/CD ortamlari icin uygundur.'
    )
    doc.code(
        '# .env dosyasina veya ortam degiskenine API key ekleyin:\n'
        'export ANTHROPIC_API_KEY="sk-ant-api..."\n\n'
        '# Windows PowerShell:\n'
        '$env:ANTHROPIC_API_KEY = "sk-ant-api..."\n\n'
        '# Ardindan Claude Code\'u normal baslatin:\n'
        'claude',
        'Terminal'
    )

    doc.h2('Model Secimi')
    doc.text(
        '2026 itibarıyla Claude Code birden fazla modeli destekler. '
        'Varsayilan model Claude Sonnet 4.6\'dir. Daha guclu muhakeme icin '
        'Opus 4.7, daha hizli ve ucuz isler icin Haiku 4.5 secebilirsiniz.'
    )
    doc.code(
        '# Oturum sirasinda model degistir:\n'
        '/model claude-opus-4-7\n\n'
        '# Veya baslatirken:\n'
        'claude --model claude-opus-4-7\n\n'
        '# Mevcut modeller (2026):\n'
        '# claude-sonnet-4-6   → Varsayilan, dengeli\n'
        '# claude-opus-4-7     → En guclu, yavas\n'
        '# claude-haiku-4-5    → Hizli ve ucuz',
        'Terminal'
    )

    # ── 4.4 Temel Komutlar ────────────────────────────────
    doc.new_page('Bolum 4: Claude Code Kurulum ve Kullanim')
    doc.h1('4.4  Temel Slash Komutlari')
    doc.sp(4)
    doc.text(
        'Claude Code oturum icerisinde "/" ile baslayan ozel komutlar destekler. '
        'Bu slash komutlari oturumu yonetmenizi, modeli degistirmenizi ve '
        'proje baglam dosyalarini yuklemenizi saglar.'
    )
    doc.table(
        ['Komut', 'Aciklama'],
        [
            ['/help',           'Tum slash komutlarini listeler'],
            ['/init',           'Projeyi analiz ederek CLAUDE.md olusturur'],
            ['/clear',          'Oturum gecmisini (context) sifirlar'],
            ['/compact',        'Uzun konusmalari ozetleyerek context\'i kucultur'],
            ['/model',          'Aktif modeli degistirir (sonnet/opus/haiku)'],
            ['/cost',           'Mevcut oturumun token maliyetini gosterir'],
            ['/status',         'Baglanti durumu ve oturum bilgilerini gosterir'],
            ['/review',         'Git diff\'ini inceleyip kod review yapar'],
            ['/bug',            'Hata raporunu formatlayarak sunar'],
            ['/pr',             'Pull request ozeti olusturur'],
            ['/memory',         'CLAUDE.md ve skill dosyalarini yeniden yukler'],
            ['/permissions',    'Izin listesini gosterir ve duzenler'],
        ],
        widths=[120, 351]
    )
    doc.sp(6)

    doc.h2('Claude Code\'u Nasil Kullanirsiniz?')
    doc.text(
        'Claude Code\'u bir proje klasorunun icerisinden baslatmaniz en verimli '
        'yoldur. Boylece Claude kodunuzu, dosyalarinizi ve proje yapisini '
        'otomatik olarak gorebilir.'
    )
    doc.code(
        '# 1. Proje klasorune gec:\n'
        'cd ~/Desktop/benim-projem\n\n'
        '# 2. Claude Code\'u baslat:\n'
        'claude\n\n'
        '# 3. Ilk is olarak projeyi tanittin:\n'
        '> Bu proje bir React e-ticaret sitesi. Sepet sayfasinda bug var,\n'
        '>  urun silindikten sonra toplam fiyat guncellenmiyor. Duzelter misin?\n\n'
        '# Claude projenizi okur, hatanin kaynagini bulur ve duzelter.',
        'Terminal'
    )
    doc.box(
        'Claude Code ile ilk kez calismaya basliyorsaniz su altın kurali unUtmayin: '
        '"Ne istedigini acik ve spesifik yaz." Ornegin "bu projeyi duzelт" yerine '
        '"src/cart.js dosyasindaki removeItem fonksiyonunda, urun '
        'silindikten sonra totalPrice state\'i guncellenmiyor, duzelt" deyin.',
        'tip'
    )

    doc.h2('/init Komutu — Proje Baslangici')
    doc.text(
        '/init komutu, Claude Code\'un projenizi otomatik olarak analiz ederek '
        'CLAUDE.md dosyasi olusturmasini saglar. Bu dosya, '
        'her oturumda projeye ozgu baglamlari otomatik yukler.'
    )
    doc.code(
        '# Proje klasorunde /init calistirin:\n'
        '> /init\n\n'
        '# Claude projeyi tarar:\n'
        '# - package.json, README, dosya yapisi\n'
        '# - Kullanilan teknoloji stack\'i tespit eder\n'
        '# - CLAUDE.md dosyasini olusturur\n\n'
        '# Ornek cikti:\n'
        '# CLAUDE.md olusturuldu. Icerik:\n'
        '# - React 18 + TypeScript projesi\n'
        '# - Tailwind CSS kullaniliyor\n'
        '# - npm ile paket yonetimi\n'
        '# - Testler: Vitest',
        'Terminal'
    )

    # ── 4.5 CLAUDE.md ─────────────────────────────────────
    doc.new_page('Bolum 4: Claude Code Kurulum ve Kullanim')
    doc.h1('4.5  CLAUDE.md — Proje Hafizasi')
    doc.sp(4)
    doc.text(
        'CLAUDE.md, projenizin "biyografisi" gibidir. Claude Code her oturumda '
        'bu dosyayi otomatik okur ve icerigindeki talimatlara uygun davranir. '
        'Proje standartlarinizi, kullanilan teknolojileri, yasakli uygulamalari '
        've tercih ettiginiz kod stilini buraya yazarsiniz.'
    )

    doc.h2('CLAUDE.md Neden Onemlidir?')
    doc.bullets([
        'Her sohbette ayni baglami tekrar aciklamak zorunda kalmazsiniz',
        'Takim calismalarinda tum gelistiriciler ayni standartlari paylasir',
        'Claude\'un yanlis teknoloji secmesinin onune gecer',
        'Proje kurallarini, yasakli kutuphaneleri ve kod stilini belirler',
        'Surekli hata yaptiginda bir kuralı CLAUDE.md\'ye ekleyerek cozersizin',
    ])

    doc.h2('Ornek CLAUDE.md Dosyasi')
    doc.code(
        '# Proje: E-Ticaret Sitesi\n\n'
        '## Teknoloji Stack\n'
        '- Frontend: Next.js 15, TypeScript, Tailwind CSS\n'
        '- Backend: Supabase (PostgreSQL + Auth + Storage)\n'
        '- Odeme: iyzico entegrasyonu\n'
        '- Deploy: Vercel\n\n'
        '## Kod Standartlari\n'
        '- TypeScript strict mode aktif, "any" kullanimayin\n'
        '- Fonksiyonlar icin arrow function tercih edin\n'
        '- Her component icin ayr .tsx dosyasi\n'
        '- Componentler PascalCase, fonksiyonlar camelCase\n\n'
        '## Yasaklar\n'
        '- class component kullanma, sadece functional component\n'
        '- Redux kullanma, Zustand veya Context API yeterli\n'
        '- console.log birakma, kaldirilmali\n\n'
        '## Onemli Klasor Yapisi\n'
        '- /src/components  → UI bilesenleri\n'
        '- /src/lib         → Yardimci fonksiyonlar\n'
        '- /src/app         → Next.js App Router sayfalar\n'
        '- /supabase        → DB migration dosyalari\n\n'
        '## Cevap Dili\n'
        'Turkce konustuğumda Turkce, Ingilizce konustuğumda Ingilizce cevapla.',
        'Markdown'
    )
    doc.box(
        'CLAUDE.md icin altin kural: Kisa ve oze yonelik tutun. '
        '100-200 satirlik bir dosya idealdir. Cok uzun CLAUDE.md dosyalari '
        'context penceresi doldurur ve Claude\'un performansini dusurebilir.',
        'info'
    )

    doc.h2('Hiyerarsik CLAUDE.md Sistemi')
    doc.text(
        'Claude Code birden fazla CLAUDE.md dosyasini destekler. '
        'Farkli klasorlere farkli kurallar koyabilirsiniz:'
    )
    doc.bullets([
        '~/.claude/CLAUDE.md → Global kurallar (tum projeler icin)',
        '/proje-koku/CLAUDE.md → Proje geneli kurallar',
        '/proje-koku/src/CLAUDE.md → Sadece src klasoru icin kurallar',
        '/proje-koku/tests/CLAUDE.md → Test klasorune ozel kurallar',
    ])
    doc.code(
        '# Global CLAUDE.md ornegi (~/.claude/CLAUDE.md)\n'
        '# Her projede gecerli genel tercihler\n\n'
        '## Genel Tercihler\n'
        '- Her zaman Turkce konusmanin Turkce yaniت ver\n'
        '- Kod yazarken yorum satirlari ekleme\n'
        '- Commit mesajlari Ingilizce yaz\n'
        '- Dosya olusturmadan once mevcut dosyalari kontrol et\n\n'
        '## Guvenlik\n'
        '- .env dosyalarini asla oku veya duzenleme\n'
        '- API keylerini kod icine yazma',
        'Markdown'
    )

    # ── 4.6 Hooks Sistemi ─────────────────────────────────
    doc.new_page('Bolum 4: Claude Code Kurulum ve Kullanim')
    doc.h1('4.6  Hooks Sistemi')
    doc.sp(4)
    doc.text(
        'Hooks, Claude Code\'un belirli olaylar gerceklestiginde otomatik olarak '
        'kabuk komutlari calistirmasini saglayan guclu bir ozelliktir. '
        'Ornegin her dosya kaydedildiginde lint calistirabilir, her commit oncesinde '
        'testleri otomatik calistirabililirsiniz.'
    )

    doc.h2('Hook Turleri')
    doc.table(
        ['Hook Turu', 'Ne Zaman Tetiklenir?', 'Kullanim Ornegi'],
        [
            ['PreToolUse',   'Araç cagrilmadan ONCE',       'Izin kontrolu, loglama'],
            ['PostToolUse',  'Araç cagrilmasından SONRA',   'Lint, format, test'],
            ['Stop',         'Claude cevap vermeden ONCE',  'Bildirim, rapor'],
            ['Notification', 'Bildirim gonderileceginde',   'Slack/mail entegrasyonu'],
        ],
        widths=[90, 160, 221]
    )
    doc.sp(6)

    doc.h2('Hook Yapilandirmasi — settings.json')
    doc.text(
        'Hook\'lar .claude/settings.json veya global ~/.claude/settings.json '
        'dosyasina yazilir.'
    )
    doc.code(
        '// .claude/settings.json\n'
        '{\n'
        '  "hooks": {\n'
        '    "PostToolUse": [\n'
        '      {\n'
        '        "matcher": "Write",\n'
        '        "hooks": [\n'
        '          {\n'
        '            "type": "command",\n'
        '            "command": "npm run lint --fix"\n'
        '          }\n'
        '        ]\n'
        '      }\n'
        '    ],\n'
        '    "Stop": [\n'
        '      {\n'
        '        "hooks": [\n'
        '          {\n'
        '            "type": "command",\n'
        '            "command": "echo \'Claude gorevi tamamladi\'"\n'
        '          }\n'
        '        ]\n'
        '      }\n'
        '    ]\n'
        '  }\n'
        '}',
        'JSON'
    )
    doc.h3('Populer Hook Kullanim Senaryolari')
    doc.bullets([
        'Dosya yazildiktan sonra otomatik Prettier ile formatlama',
        'Python dosyasi degistiginde Black + isort calistirma',
        'Git commit oncesinde test suite calistirma',
        'Gorev bittiginde Discord/Slack\'e bildirim gonderme',
        'Her araç cagrisini log dosyasina kaydetme',
        'Hassas dosyalara erisimi engelleyen guvenlik hook\'u',
    ])
    doc.box(
        'Hooks, Claude Code\'u tamamen ozellestirilmis bir gelistirme ortamina '
        'donusturur. disler/claude-code-hooks-mastery GitHub reposu, gercek '
        'dunya hook orneklerini icermektedir — mutlaka inceleyin.',
        'tip'
    )

    # ── 4.7 MCP Server Baglama ────────────────────────────
    doc.new_page('Bolum 4: Claude Code Kurulum ve Kullanim')
    doc.h1('4.7  Claude Code\'a MCP Server Baglama')
    doc.sp(4)
    doc.text(
        'Claude Code, MCP server\'lari araciligiyla harici servislerle entegrasyon '
        'kurar. GitHub, Postgres, Slack, tarayici otomasyonu ve daha fazlasini '
        'Claude Code\'a baglamak mumkundur.'
    )

    doc.h2('MCP Server Ekleme Komutu')
    doc.code(
        '# Tek satir ile MCP server ekle:\n'
        'claude mcp add <server-adi> -- <komut> [arguman...]\n\n'
        '# Ornek: Filesystem MCP server ekle\n'
        'claude mcp add filesystem -- npx -y @modelcontextprotocol/server-filesystem /home/user\n\n'
        '# Ornek: GitHub MCP server ekle\n'
        'claude mcp add github -- npx -y @modelcontextprotocol/server-github\n\n'
        '# Ornek: Postgres MCP server ekle\n'
        'claude mcp add postgres -- npx -y @modelcontextprotocol/server-postgres \\\n'
        '  postgresql://localhost/mydb\n\n'
        '# Mevcut MCP serverlari listele:\n'
        'claude mcp list\n\n'
        '# MCP server sil:\n'
        'claude mcp remove filesystem',
        'Terminal'
    )

    doc.h2('GitHub MCP ile Gercek Ornek')
    doc.text(
        'GitHub MCP server\'i bagladiktan sonra Claude Code\'a dogal dille '
        'GitHub islemleri yaptirrabilirsiniz:'
    )
    doc.code(
        '# Ortam degiskenini ayarla:\n'
        'export GITHUB_PERSONAL_ACCESS_TOKEN="ghp_xxxxx"\n\n'
        '# GitHub MCP\'yi ekle:\n'
        'claude mcp add github -- npx -y @modelcontextprotocol/server-github\n\n'
        '# Simdi Claude Code\'a sorebilirsiniz:\n'
        '> "eticmedya/pop-blast reposundaki son 5 issue\'yu listele"\n'
        '> "main branch\'ine PR ac, baslik: Fix cart bug"\n'
        '> "gecen hafta acilan tum bug etiketli issue\'lari goster"',
        'Terminal'
    )
    doc.box(
        'MCP server\'lar otomatik olarak baslayip durur, arka planda surekli '
        'calismaz. Claude bir araci kullanmaya ihtiyac duyduğunda server\'i '
        'baslatirak islemi yapar, bitince kapatir. Bu yuzden sistem kaynaklarini '
        'az tuketir.',
        'info'
    )

    # ── 4.8 Subagents ─────────────────────────────────────
    doc.new_page('Bolum 4: Claude Code Kurulum ve Kullanim')
    doc.h1('4.8  Subagents ve Paralel Calisma')
    doc.sp(4)
    doc.text(
        'Subagents, Claude Code\'un bir gorevi paralel alt gorevlere boldugu ve '
        'her birini bagimsiz bir "alt ajan" olarak calistirdigi gelismis bir '
        'ozelliktir. Buyuk ve karmasik projelerde ciddi hiz kazanimi saglar.'
    )

    doc.h2('Subagent Nasil Calisir?')
    doc.text(
        'Subagent, ana Claude oturumunun "alt calisan" olarak dusunulebilir. '
        'Ana Claude bir gorevi alt gorevlere boler ve bunlari birer subagent\'e '
        'deleye eder. Her subagent kendi bagimsiz context\'inde calisir. '
        'Gorevler bitince sonuclar ana ajana raporlanir.'
    )
    doc.bullets([
        'Buyuk test suite\'lerini paralel calistirmak',
        'Birden fazla dosyayi ayni anda analiz etmek',
        'Farkli modulleri bagimsiz olarak refactor etmek',
        'Kod dokumantasyonu uretirken herbir modulu ayri subagent\'e vermek',
    ])

    doc.h2('Subagent Ornegi')
    doc.code(
        '# Claude Code\'a sorun:\n'
        '> "Bu projedeki tum React componentlerini incele ve\n'
        '>  her birinin TypeScript interface\'lerini ekle.\n'
        '>  Componentleri paralel olarak isle, hizli bitirmek istiyorum."\n\n'
        '# Claude otomatik olarak:\n'
        '# 1. Tum .tsx dosyalarini tespit eder\n'
        '# 2. Her dosya icin bir subagent olusturur\n'
        '# 3. Paralel olarak calistirir\n'
        '# 4. Sonuclari birlestirir',
        'Terminal'
    )

    doc.h2('Ozel Subagent Tanimlama (wshobson/agents)')
    doc.text(
        'GitHub\'da wshobson/agents reposu, hazir subagent tanimlari icermektedir. '
        'Bu tanimlari .claude/agents/ klasorune koyarak Claude Code\'un '
        'otomatik yuklemesini saglayabilirsiniz.'
    )
    doc.code(
        '# Ornek subagent tanimi: .claude/agents/code-reviewer.md\n\n'
        '---\n'
        'name: code-reviewer\n'
        'description: Kod kalitesi ve guvenlik denetimi\n'
        '---\n\n'
        '# Kod Inceleyici Agent\n\n'
        'Gorundugunde:\n'
        '- OWASP Top 10 guvenlik aciklari icin tara\n'
        '- Performance sorunlarini tespit et\n'
        '- DRY ilkesine uyumu kontrol et\n'
        '- Her bulgu icin somut duzeltme onerisi sun',
        'Markdown'
    )
    doc.box(
        'Subagents ozellikle buyuk refactor ve migration islerinde mukemmeldir. '
        '"Bu projeyi JavaScript\'ten TypeScript\'e migreye et" gibi dev gorevlerde '
        'Claude paralel subagentlerle saatler yerine dakikalarda bitirebilir.',
        'tip'
    )

    # ── 4.9 Pratik Is Akisi ───────────────────────────────
    doc.new_page('Bolum 4: Claude Code Kurulum ve Kullanim')
    doc.h1('4.9  Pratik Claude Code Is Akisi')
    doc.sp(4)
    doc.text(
        'Claude Code\'u verimli kullanmanin sirri dogru is akisi kurmaktir. '
        'Asagida deneyimli Claude Code kullanicilarin benimsedigi is akisi '
        'adim adim aciklanmistir.'
    )

    doc.h2('Yeni Proje Baslatma')
    doc.code(
        '# 1. Proje klasoru olustur ve gir\n'
        'mkdir benim-saas-projem && cd benim-saas-projem\n\n'
        '# 2. Claude Code\'u baslat\n'
        'claude\n\n'
        '# 3. Projeyi tanimla\n'
        '> "Supabase ve Next.js kullanan bir SaaS uygulama kurmak istiyorum.\n'
        '>  Kullanici kayit/giris, dashboard ve abonelik sistemi olacak.\n'
        '>  Once proje yapisini olustur, CLAUDE.md yaz, sonra\n'
        '>  Next.js projesini kur."\n\n'
        '# 4. Claude:\n'
        '# - CLAUDE.md olusturur\n'
        '# - npx create-next-app calistirir\n'
        '# - Supabase baglantisini kurar\n'
        '# - Auth sayfalarini yazar',
        'Terminal'
    )

    doc.h2('Mevcut Projede Calisma')
    doc.code(
        '# Var olan projeye git:\n'
        'cd ~/projelerim/mevcut-proje\n\n'
        '# Proje yoksa Claude\'a analiz ettir:\n'
        'claude\n'
        '> /init\n\n'
        '# Gorev ver:\n'
        '> "Odeme sayfasinda kullanicinin kart bilgilerini\n'
        '>  girdiginde form validasyonu calismiyor.\n'
        '>  Hatayi bul ve duzelt, sonra test yaz."\n\n'
        '# Context dolmaya baslarsa:\n'
        '> /compact\n'
        '# veya\n'
        '> /clear',
        'Terminal'
    )

    doc.h2('Uzun Gorevlerde Context Yonetimi')
    doc.bullets([
        '/compact: Oturumu ozetler, context\'i kucultur ama hafizayi korur',
        '/clear: Tamamen sifirlar — yeni bir konu baslarken kullanin',
        'Buyuk gorevleri parcalara bolun: once mimari, sonra implementasyon',
        'CLAUDE.md\'ye kritik kararlar ekleyin ki /clear sonrasi da hatirlasin',
        '--resume: Son kaydedilen oturumu yuklemek icin "claude --resume"',
    ])
    doc.box(
        'Altin kural: Claude Code bir gorevi yaparken cok fazla mudahale etmeyin. '
        'Gorevi acikca tanimlayin ve Claude\'un calistirmasini izleyin. Bittikten '
        'sonra sonucu inceleyin ve gerekirse duzeltme isteyin. Bu "vibe coding" '
        'zihniyetinin temelidir.',
        'tip'
    )

    doc.h2('Bolum 4 Ozeti')
    doc.bullets([
        'Node.js kurulumu: nodejs.org\'dan LTS indir, "node --version" ile dogrula',
        'Claude Code kurulumu: npm install -g @anthropic-ai/claude-code',
        'Ilk giris: "claude" yaz, tarayici acilir, Anthropic hesabiyla giris yap',
        'Temel komutlar: /init, /clear, /compact, /model, /cost',
        'CLAUDE.md: Proje hafizasi — her oturumda otomatik yuklenir',
        'Hooks: Dosya degisimlerinde otomatik lint/test — settings.json\'da yonetilir',
        'MCP: "claude mcp add" ile GitHub, Postgres gibi servislere baglan',
        'Subagents: Buyuk gorevleri paralel alt ajanlara bol, hizlan',
    ])


def bolum5_projeler_baslangic(doc):
    """Bolum 5: Claude Code ile Gercek Projeler — baslangic"""

    doc.section_cover(
        5,
        'Claude Code ile Gercek Projeler',
        'Web, mobil ve masaustu — sifirdan uygulamaya',
        'Bu bolumde Claude Code kullanarak gercek projeler gelistiriyoruz: '
        'Modern web sitesi, React Native mobil uygulama (Windows ve Mac) '
        've Electron/Tauri masaustu uygulamasi.'
    )

    # ── 5.1 Web Sitesi ────────────────────────────────────
    doc.new_page('Bolum 5: Claude Code ile Gercek Projeler')
    doc.h1('5.1  Claude Code ile Web Sitesi Yapma')
    doc.sp(4)
    doc.text(
        'Claude Code ile web sitesi yapmak, HTML/CSS bilmeden de mumkundur. '
        'Sadece ne istedigini aciklayarak tam calisan, modern bir web sitesi '
        'olusturabilirsiniz. Bu bolumde adim adim bir landing page projesi yapiyoruz.'
    )

    doc.h2('Adim 1: Proje Klasoru Olusturun')
    doc.code(
        '# Terminal\'de:\n'
        'mkdir landing-page && cd landing-page\n'
        'claude\n\n'
        '# Claude Code baslar. Simdi projeyi tanimlayalim:',
        'Terminal'
    )

    doc.h2('Adim 2: Projeyi Tanimlayin')
    doc.code(
        '> "Benim icin modern bir SaaS landing page olustur.\n'
        '>  Urun: AI destekli musteri hizmetleri botu.\n'
        '>  Sayfa bolumleri: Hero, Ozellikler (3 kart), Fiyatlandirma\n'
        '>  (3 plan), Musteri yorumlari, CTA, Footer.\n'
        '>  Renk paleti: Lacivert ve turuncu.\n'
        '>  Tamamen responsive olmali, mobile-first tasarim.\n'
        '>  Teknoloji: Sade HTML, CSS, minimal JavaScript.\n'
        '>  Animasyonlar: Scroll ile gorunen fade-in efekti."',
        'Terminal'
    )
    doc.text(
        'Claude bu prompt\'u aldiginda su adimlari otomatik olarak atar: '
        'index.html, style.css ve script.js dosyalarini olusturur, '
        'tum bolumlerle birlikte tam calisan bir sayfa yazar.'
    )

    doc.h2('Adim 3: Sonucu Inceleyin')
    doc.code(
        '# Claude dosyalari olusturduktan sonra:\n'
        '# Projenizin icindeki index.html dosyasina cift tiklayin\n'
        '# Tarayicida acilacak, canli onizleme goreceksiniz.\n\n'
        '# Begenmediginiz bir sey varsa:\n'
        '> "Hero bolumundeki baslik daha buyuk olsun, rengi beyaz yap"\n'
        '> "Fiyatlandirma kartlarinda en populer plani vurgula"\n'
        '> "Footer\'a sosyal medya ikonlari ekle: Twitter, LinkedIn, GitHub"',
        'Terminal'
    )

    doc.h2('Adim 4: Vercel ile Yayina Alma')
    doc.text(
        'Sitenizi internette yayinlamak icin Vercel\'i kullanabilirsiniz. '
        'Ucretsiz plan kisisel projeler icin yeterlidir.'
    )
    doc.bullets([
        '1. vercel.com\'a gidin, GitHub hesabinizla kayit olun',
        '2. "Add New Project" tiklayin',
        '3. GitHub reponuzu secin (once "git init && git push" yapmaniz gerekir)',
        '4. "Deploy" tiklayin — 30 saniyede canli!',
        '5. Otomatik https://projeniz.vercel.app adresi alinirsiniz',
    ])
    doc.code(
        '# Terminal\'de git ile yukleme:\n'
        'git init\n'
        'git add .\n'
        'git commit -m "Initial landing page"\n'
        'git remote add origin https://github.com/kullaniciadi/landing-page.git\n'
        'git push -u origin main\n\n'
        '# Vercel otomatik olarak deploy eder (GitHub entegrasyonu aktifse)',
        'Terminal'
    )
    doc.box(
        'Netlify de Vercel\'e cok iyi bir alternatiftir. netlify.com\'a gidin, '
        '"Deploy from GitHub" secin ve reponuzu baglayın. Her iki platform da '
        'custom domain, HTTPS ve CI/CD\'yi ucretsiz saglar.',
        'info'
    )

    doc.h2('Next.js ile Daha Guclu Web Sitesi')
    doc.text(
        'Basit HTML yerine Next.js kullanmak, SEO, performans ve genis ekosistem '
        'acisından cok daha avantajlidir. Claude Code, Next.js projelerini de '
        'kolayca olusturabilir.'
    )
    doc.code(
        '# Claude Code\'a sorun:\n'
        '> "Next.js 15 ve Tailwind CSS ile bir blog sitesi olustur.\n'
        '>  MDX ile markdown icerik destegi olsun.\n'
        '>  Ana sayfa, blog listesi ve tek yazi sayfasi.\n'
        '>  SEO meta taglari ve sitemap otomatik olusturulsun."',
        'Terminal'
    )


def main():
    doc = Doc()
    print("Icerik olusturuluyor — Sayfa 38-60...")

    kapak_sayfasi(doc)
    icindekiler(doc)
    bolum1_giris(doc)
    bolum1_ek_ve_bolum2_baslangic(doc)
    bolum2_devami(doc)
    bolum3_claude_ekosistemi(doc)
    bolum4_claude_code(doc)
    bolum5_projeler_baslangic(doc)

    pages = doc.save('yapay_zeka_ogreniyorum_p1_60.pdf')
    print(f"\nTamamlandi! Toplam {pages} sayfa uretildi.")
    print("Dosya: yapay_zeka_ogreniyorum_p1_60.pdf")


if __name__ == '__main__':
    main()
