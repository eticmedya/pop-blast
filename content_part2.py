#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Icerik Part 2 — Sayfa 20-40
Bolum 2 devami + Bolum 3: Claude Ekosistemi
"""
from pdf_engine import Doc, PW, PH, ML, MR, CW
from pdf_engine import NAVY, ORANGE, WHITE, BLACK, GRAY_BG, GRAY_DARK

# ── Part 1 fonksiyonlarını içe aktar ───────────────────────
from content_part1 import kapak_sayfasi, icindekiler, bolum1_giris
from content_part1 import bolum1_ek_ve_bolum2_baslangic


def bolum2_devami(doc):
    """Bolum 2 devami: Gemini, Grok, acık kaynak, gorsel, video, ses, kod AI"""

    # ── Gemini ─────────────────────────────────────────────
    doc.new_page('Bolum 2: 2026 da Hangi AI ile Ne Yapilir?')
    doc.h2('Gemini — Google DeepMind')
    doc.text(
        'Google\'ın Gemini ailesi, 2024\'te Bard\'ın yerini alarak Google\'ın yapay zeka '
        'stratejisinin merkezi haline geldi. 2026 itibarıyla Gemini 2.0 Ultra, ozellikle '
        'Google Workspace entegrasyonu ve inanılmaz uzun context window kapasitesiyle one '
        'cıkmaktadır. Gmail, Google Docs, Sheets ve Drive ile sıkı entegrasyon, kurumsal '
        'kullanıcılar icin buyuk avantaj saglamaktadır.'
    )
    doc.table(
        ['Kriter', 'Detay'],
        [
            ['Model',          'Gemini 2.0 Flash / Pro / Ultra (2026)'],
            ['Context Window', '1M - 2M token — en uzun context (2026 itibarıyla)'],
            ['Guclu Yonleri',  'Multimodal (goruntu+ses+video), Google entegrasyonu, uzun context'],
            ['Zayıf Yonleri',  'Kimi gorevlerde Claude ve GPT-4\'e kıyasla daha az yaratıcı'],
            ['Fiyat (2026)',   'Google One AI Premium $19.99/ay, API ayrı fiyatlandırma'],
            ['Kim Icin',       'Google ekosistemi kullanıcıları, kurumsal, arastırmacılar'],
            ['Ornek Kullanım', 'Google Docs\'ta belgelerle sohbet, YouTube transkrip analizi'],
        ],
        widths=[130, 341]
    )
    doc.sp(6)
    doc.box(
        'Gemini\'nin en buyuk silahı NotebookLM uygulamasıdır. PDF, web sitesi veya '
        'YouTube videosu yukleyerek kaynaklarla sohbet edebilir, ozet cıkarabilir ve '
        'podcast formatında ses icerik uretebilirsiniz. Arastırma is akısları icin '
        'vazgecilmez bir arac haline gelmistir.',
        'tip'
    )
    doc.sp(4)

    # ── Grok ───────────────────────────────────────────────
    doc.h2('Grok — xAI (Elon Musk)')
    doc.text(
        'Elon Musk\'ın kuruculardan biri oldugu xAI tarafından gelistirilen Grok, X '
        '(eski Twitter) platformuyla dogrudan entegrasyon sayesinde gercek zamanli '
        'internet ve sosyal medya verisine erisim saglayabilen nadir modellerden biridir. '
        '2026\'da Grok 3 ile ciddi performans atlaması yasamıstır.'
    )
    doc.table(
        ['Kriter', 'Detay'],
        [
            ['Model',          'Grok 3, Grok 3 mini (2026)'],
            ['Context Window', '128K token'],
            ['Guclu Yonleri',  'Gercek zamanli X verisi, daha az sansur, haber takibi'],
            ['Zayıf Yonleri',  'Uzun doc analizi ve kod kalitesinde rakiplerinin gerisinde'],
            ['Fiyat (2026)',   'X Premium+ aboneligiyle ($22/ay) veya API ayrı'],
            ['Kim Icin',       'Gazeteciler, sosyal medya takipcileri, trend arastırmacıları'],
            ['Ornek Kullanım', 'X\'teki son dakika haberlerin analizi, trend tespiti'],
        ],
        widths=[130, 341]
    )
    doc.sp(6)

    # ── Acık Kaynak Modeller ───────────────────────────────
    doc.h2('Acık Kaynak Modeller: DeepSeek, Qwen, Llama')
    doc.text(
        'Kapalı kaynak ticari modellerin hakim oldugu AI pazarında acık kaynak modeller '
        'giderek guclenisyor. 2025\'te DeepSeek R1\'in piyasaya surulmesi ile birlikte '
        'acık kaynak modellerin ticari modellere yakın performans sunabildigı kanıtlandı. '
        'Bu gelisme hem maliyetleri dusuruyor hem de yerel (local) AI kullanımını '
        'mumkun kılıyor.'
    )
    doc.table(
        ['Model',          'Sirket', 'Parametre', 'Ozellik',                     'Kullanım'],
        [
            ['Llama 4',        'Meta',    '400B+',    'Cok dilli, guclu reasoning',  'Local, fine-tuning'],
            ['DeepSeek R2',    'DeepSeek','~236B MoE','Maliyet etkin muhakeme',      'API veya local'],
            ['Qwen 2.5 72B',   'Alibaba', '72B',      'Cok dilli, Asya odaklı',      'Local deploy'],
            ['Mistral Large 3','Mistral', '123B',     'Avrupa gizlilik uyumu',       'Kurumsal'],
            ['Phi-4',          'Microsoft','14B',      'Kucuk ama guclu',             'Edge/mobile AI'],
            ['Gemma 3',        'Google',  '27B',      'Google acık kaynak',          'Fine-tuning'],
        ],
        widths=[95, 65, 60, 135, 116]
    )
    doc.sp(4)
    doc.h3('Local AI Ne Zaman Tercih Edilmeli?')
    doc.bullets([
        'Gizli kurumsal verilerle calısırken (veri dısarı cıkmamalı)',
        'API maliyetlerini sıfıra indirmek istedigınizde',
        'Internet baglantısı olmadan calısmanız gerektiginde',
        'Modeli kendi veri setinizle fine-tune etmek istedigınizde',
        'GDPR/KVKK kapsamında veri isleme kısıtlaması olan projelerde',
    ])
    doc.box(
        'Local AI icin Ollama aracı kullanımını siddetle onerilir. Ollama ile Llama, '
        'DeepSeek, Qwen gibi modelleri tek komutla indirip calıstırabilirsiniz: '
        '"ollama run llama4" — bu kadar basit.',
        'tip'
    )

    # ── Gorsel AI ──────────────────────────────────────────
    doc.new_page('Bolum 2: 2026 da Hangi AI ile Ne Yapilir?')
    doc.h1('2.2  Gorsel AI Araclari Detayli')
    doc.sp(4)
    doc.text(
        '2026\'da gorsel AI araclari profesyonel tasarımcıların is akısını kökten '
        'degistirmistir. Bir konsept gorsel uretmek artık saatler degil saniyeler '
        'almaktadır. Stok fotograf sektorü ciddi bir donusum icindedir. Asagıda '
        'onde gelen gorsel AI araçlarını detaylıca inceliyoruz.'
    )
    doc.h2('Midjourney v7')
    doc.text(
        'Midjourney, gorsel AI alanında sanatsal kalite standartlarını belirleyen '
        'referans platformdur. Discord uzerinden calısmaya baslayan platform, 2025\'te '
        'web arayuzune gecis yapmıstır. v7 ile birlikte fotogercekcilik ve tutarlı '
        'karakter olusturma kapasitesi cok artmıstır.'
    )
    doc.bullets([
        'Guclı yonleri: En sanatsal cıktılar, genis stil yelpazesi, aktif topluluk',
        'Zayif yonleri: Gorseldeki metin yazımı hala sorunlu, tam kontrol zor',
        'Fiyat: $10/ay (200 gorsel/ay) — $120/ay (sınırsız, ticari lisans)',
        'Kim icin: Tasarımcılar, marka gosel uretimi, sanatsal projeler',
        'Ornek: /imagine a futuristic Turkish city at sunset, cinematic lighting',
    ])
    doc.h2('Flux 1.1 Pro — Black Forest Labs')
    doc.text(
        'Flux, 2024 sonunda piyasaya cıkarak fotogercekcilik konusunda devrim yarattı. '
        'Stable Diffusion\'ın kurucularından olustupulan Black Forest Labs\'in urunudur. '
        'fal.ai uzerinden kolayca API erisimine sahip olması, gelisitriciler icin '
        'en tercih edilen gorsel AI\'si yapmıstır.'
    )
    doc.bullets([
        'Guclı yonleri: Fotografik gercekcilik, hızlı API, fal.ai entegrasyonu kolay',
        'Zayif yonleri: Sanatsal stillerde Midjourney kadar esnek degil',
        'Fiyat: fal.ai uzerinden kredi bazlı (~$0.05/gorsel)',
        'Kim icin: Gelisitirciler, e-ticaret gorsel uretimi, otomatik pipeline\'lar',
        'Ornek: Urun fotograf arka planı degistirme, model fotografi',
    ])
    doc.h2('Ideogram 2.5')
    doc.text(
        'Goruntu icinde metin yazımı, AI gorsel araçlarının en zor sorunlarından biri '
        'olageldi. Ideogram bu sorunu cozen platform olarak one cıktı. Poster, banner '
        've logo gibi metin iceren tasarımlarda rakipsizdir.'
    )
    doc.bullets([
        'Guclı yonleri: Goruntu icinde kusursuz metin, logo ve tipografi',
        'Zayif yonleri: Fotogercekcilik Flux kadar guclu degil',
        'Fiyat: $7/ay (800 gorsel) — $25/ay (3200 gorsel)',
        'Kim icin: Grafik tasarımcılar, sosyal medya banner uretimi',
    ])
    doc.table(
        ['Araç',         'En Iyi Oldugu Alan',    'Hız',    'Fiyat/Gorsel', 'API?'],
        [
            ['Midjourney v7',    'Sanatsal kalite',       'Orta',   '$0.05-0.50',   'Evet'],
            ['Flux 1.1 Pro',     'Fotogercekcilik',       'Hızlı',  '$0.04-0.06',   'Evet'],
            ['Ideogram 2.5',     'Metin+gorsel',          'Hızlı',  '$0.009-0.03',  'Evet'],
            ['DALL-E 4',         'Prompt hassasiyeti',    'Hızlı',  '$0.04-0.12',   'Evet'],
            ['Adobe Firefly 4',  'Ticari guvenli gorsel', 'Orta',   'CC abonelig',  'Evet'],
            ['Stable Diff. 4',   'Local/fine-tune',       'Degisir','Ucretsiz',     'Self'],
        ],
        widths=[105, 130, 55, 85, 96]
    )

    # ── Video AI ───────────────────────────────────────────
    doc.new_page('Bolum 2: 2026 da Hangi AI ile Ne Yapilir?')
    doc.h1('2.3  Video AI Araclari')
    doc.sp(4)
    doc.text(
        'Video AI, 2024\'de Sora\'nın duyurulmasıyla ana akıma girdi ve 2026\'da inanılmaz '
        'bir olgunluk seviyesine ulasti. Artık 60 saniyeye kadar fotogercekcilik kalitesinde '
        'video metin komutundan uretilmektedir. Reklam ajanları, sosyal medya icerigi '
        'olusturanlar ve film yapımcıları bu teknolojiyi aktif olarak kullanmaktadır.'
    )
    doc.h2('Veo 3 — Google DeepMind')
    doc.text(
        'Google DeepMind\'ın Veo 3\'u, 2026 itibarıyla en uzun ve en kaliteli AI videoları '
        'uretiyor. 4K cozunurluge kadar desteklemesi, fizik simulasyonunun gercekciligı '
        've kamera hareketi kontrolu onu sektorun lideri yapıyor. Google One AI Premium '
        'abonelerine sunuluyor.'
    )
    doc.bullets([
        'Maksimum sure: 60 saniye (4K)',
        'Kamera kontrolu: Pan, zoom, tracking shots tamamen kontrol edilebilir',
        'Fizik: Su, alev, kumas fiziği inandırıcı sekilde simule ediliyor',
        'Ses: Video ile senkronize AI ses uretimi destekleniyor (Veo 3 ile)',
        'Fiyat: Google One AI Premium ($19.99/ay)',
    ])
    doc.h2('Sora 2 — OpenAI')
    doc.text(
        'OpenAI\'nın Sora 2\'si, sinematik kalite ve tutarlı karakter olusturma konusunda '
        'rakiplerinden one gecmektedir. Ozelllikle insan yuzlerini ve hareketlerini gercekci '
        'sekilde canlandırma kapasitesi one cıkmaktadır. ChatGPT Pro abonelerine sunuluyor.'
    )
    doc.h2('Kling 2.0 — Kuaishou')
    doc.text(
        'Cin merkezli Kuaishou firmasının Kling 2.0 modeli, fiyat-performans dengesi '
        'acısından cok tercih edilen bir secenektir. Turkce prompt destegi oldukca '
        'iyidir ve fal.ai uzerinden API erisimine de sahiptir.'
    )
    doc.table(
        ['Araç',        'Max Sure', 'Cozunurluk', 'En Iyi Alan',          'Fiyat'],
        [
            ['Veo 3',       '60 sn',    '4K',        'Fizik gercekcilik',    'Google One AI'],
            ['Sora 2',      '60 sn',    '1080p',     'Sinematik, insan',     'ChatGPT Pro'],
            ['Kling 2.0',   '30 sn',    '1080p',     'Fiyat/perf. dengesi',  'Freemium/API'],
            ['Runway Gen-4','16 sn',    '4K',        'Stil transferi, edit', '$15-95/ay'],
            ['Hailuo 2',    '10 sn',    '720p',      'Karakter tutarlılıgı', 'API/Kredi'],
            ['Wan 2.1',     '15 sn',    '720p',      'Acık kaynak, local',   'Ucretsiz'],
        ],
        widths=[80, 60, 70, 140, 121]
    )
    doc.sp(6)
    doc.box(
        'Video AI kullanırken dikkat edilmesi gereken kritik nokta: Gercek kisiler '
        'iceren deepfake videoları uretmek hem etik hem de hukuki acıdan sorunludur. '
        'Turkiye Cumhuriyeti mevzuatında bu tur iceriklerin uretimi veya yayılması '
        'ciddi yaptırımlara yol acabilir. Her zaman etik ve yasal sinırlar icinde kalin.',
        'warning'
    )

    # ── Ses AI ─────────────────────────────────────────────
    doc.new_page('Bolum 2: 2026 da Hangi AI ile Ne Yapilir?')
    doc.h1('2.4  Ses AI ve Muzik Uretimi')
    doc.sp(4)
    doc.text(
        'Ses yapay zekası iki ana kategoride hızla gelisiyor: Metin-ses donusumu (TTS) '
        've muzik uretimi. ElevenLabs, ses klonlama teknolojisiyle piyasada devrim '
        'yaratmıstır. Artık 1 dakikalık ses orneginden saatler boyunca konusabilecek '
        'yapay bir ses klonu olusturmak mumkundur.'
    )
    doc.h2('ElevenLabs — Ses Klonlama ve TTS')
    doc.text(
        'ElevenLabs, 2026 itibarıyla TTS (text-to-speech) ve ses klonlama alanında '
        'tartısmasız liderdir. 29 dil destegi, gercekci duygusal ifade kapasitesi ve '
        'kolay API entegrasyonu ile ozellikle podcast, video seslendirme ve e-ogrenme '
        'sektorlerinde vazgecilmez bir arac haline gelmistir.'
    )
    doc.bullets([
        'Turkce dil destegi: Evet, dogal aksanla',
        'Ses klonlama: 1 dakika ses orneginden klon olusturma',
        'Duygusal kontrol: Heyecan, udukluk, ciddiyet gibi duygular ayarlanabilir',
        'API: Kolay entegrasyon, Node.js ve Python SDK\'lar mevcut',
        'Fiyat: Ucretsiz (10K karakter/ay) — $5/ay (30K) — $22/ay (100K)',
    ])
    doc.h2('Muzik Uretimi: Suno v4 ve Udio 2')
    doc.text(
        'Suno ve Udio, metin komutundan vokal ve enstru muzik uretebilen platformlardır. '
        '"80\'ler tarzında Turkce pop sevgi sarkısı" gibi bir prompt ile tam bir sarki '
        'uretmek artık dakikalar suren bir islemdir. Reklam jingle, egitim materyali '
        'muzigi ve sosyal medya arkaplan muzigi icin ideal araclardır.'
    )
    doc.table(
        ['Araç',          'Kategori',      'Ozellik',                 'Fiyat'],
        [
            ['ElevenLabs',    'TTS/Klonlama',  '29 dil, duygusal TTS',    'Freemium / $5+/ay'],
            ['Suika',         'TTS Turkce',    'Turkce optimize',         'API/Kredi'],
            ['Suno v4',       'Muzik uretimi', 'Vokal+enstru tam sarki',  '$8-24/ay'],
            ['Udio 2',        'Muzik uretimi', 'Studio kalitesi',         '$10-30/ay'],
            ['Whisper API',   'STT (tanıma)',  'OpenAI, 50+ dil',         'API token bazlı'],
            ['AssemblyAI',    'STT+Analiz',    'Transkripsiyon+duygu',    'API/Dakika'],
        ],
        widths=[95, 95, 145, 136]
    )

    # ── Kod AI ─────────────────────────────────────────────
    doc.new_page('Bolum 2: 2026 da Hangi AI ile Ne Yapilir?')
    doc.h1('2.5  Kod AI Araclari: IDE\'den Terminale')
    doc.sp(4)
    doc.text(
        'Kod yazmaya yardımcı AI araçları, gelistirici verimliligini dogrudan etkileyen '
        've son yıllarda en hızlı buyuyen AI segmentini olusturuyor. Bu araçları iki '
        'ana kategoride inceleyebiliriz: IDE\'ye entegre calisan yardımcılar ve terminal '
        'uzerinden calısan otonom ajanlar.'
    )
    doc.h2('IDE Entegre Araçlar')
    doc.h3('Cursor — AI-First IDE')
    doc.text(
        'Cursor, VS Code\'u temel alarak tum IDE deneyimini AI etrafında yeniden tasarlayan '
        'bir editordur. Claude ve GPT-4o ile calısmaktadır. En guclu ozelligi, tum kod '
        'tabanını anlayıp baglamsal oneriler sunabilmesidir. 2026\'da yazılım gelistiricilerin '
        'en cok kullandıgı AI IDE olma ozelligini koruyor.'
    )
    doc.bullets([
        'Cmd+K: Satır icinde kod degistirme ve yazma',
        'Cmd+L: Sag tarafta chat paneli ile kod tabanı hakkında soru',
        'Composer: Birden fazla dosyada degisiklik yapan ajan modu',
        'Codebase indexing: Tum proje dosyalarını analiz eder',
        'Fiyat: Ucretsiz (200 istek/ay) — Pro $20/ay — Business $40/kullanıcı/ay',
    ])
    doc.h3('GitHub Copilot')
    doc.text(
        'GitHub\'ın resmi AI asistanı Copilot, VS Code, JetBrains ve diger populer IDE\'lere '
        'entegre calısır. 2026\'da Copilot Workspace ozelligi ile pull request acmadan '
        'tum issue\'yu otonom olarak cozme kapasitesine kavusmustur.'
    )
    doc.h3('Windsurf — Codeium')
    doc.text(
        'Codeium\'un gelistirdigi Windsurf, "agentic flows" konseptiyle one cıkıyor. '
        'Gelistiriciyle birlikte adım adım dusunebilen, terminal komutları calıstırabilen '
        've dosya degisikliklerini acıklayan ajansal bir yapısı var. Claude Code ile '
        'benzer yeteneklere sahiptir.'
    )
    doc.h2('Terminal Ajanları')
    doc.h3('Claude Code (Anthropic)')
    doc.text(
        'Claude Code, terminalde calısan ve dosya sistemiyle dogrudan etkilesim kuran '
        'guclu bir AI ajanıdır. Dosya okuma/yazma, bash komutları calıstırma, git '
        'islemleri yapma ve buyuk kod tabanlarını anlama yetenekleriyle diger araçlardan '
        'ayrılır. Bu rehberin odak noktasıdır — Bolum 4\'te detaylıca inceleyecegiz.'
    )
    doc.h3('OpenAI Codex CLI')
    doc.text(
        'OpenAI\'nın terminal ajani Codex CLI, 2026\'da Claude Code\'a rakip olarak '
        'piyasaya suruldu. GPT-4o ve o3 modelleriyle calısmaktadır. OpenAI ekosistemi '
        'kullanıcıları icin dogal bir secenektir.'
    )
    doc.table(
        ['Araç',             'Tür',           'Model',         'Fiyat',           'En Iyi Alan'],
        [
            ['Claude Code',      'Terminal ajan', 'Claude Sonnet 4.6', 'Max plan ile',    'Buyuk proje, otonom gorev'],
            ['Cursor',           'AI IDE',        'Claude/GPT-4o', '$20/ay Pro',       'Gunluk gelistirme'],
            ['GitHub Copilot',   'IDE eklenti',   'GPT-4o/Claude', '$10/ay',          'GitHub entegrasyonu'],
            ['Windsurf',         'AI IDE/ajan',   'Claude/GPT',    '$15/ay Pro',      'Agentic flows'],
            ['Bolt.new',         'Web IDE',       'Claude',        'Freemium',         'Web prototip (hızlı)'],
            ['v0 by Vercel',     'UI uretici',    'Claude',        'Freemium',         'React/Next.js UI'],
            ['Codex CLI',        'Terminal ajan', 'GPT-4o/o3',     'API bazlı',       'OpenAI ekosistemi'],
        ],
        widths=[96, 68, 80, 78, 149]
    )
    doc.sp(6)
    doc.box(
        'Tavsiye: Gunluk IDE kullanımı icin Cursor\'u, buyuk ve karmasık projeler '
        'veya otonom gorevler icin Claude Code\'u tercih edin. İkisini birlikte '
        'kullanmak en verimli is akısını saglar.',
        'tip'
    )

    # ── Bolum 2 Ozet ───────────────────────────────────────
    doc.new_page('Bolum 2: 2026 da Hangi AI ile Ne Yapilir?')
    doc.h1('Bolum 2 Ozet — Hangi AI Ne Icin?')
    doc.sp(4)
    doc.text(
        'Bu bolumde 2026\'nın onde gelen AI araçlarını kategorilere gore inceledik. '
        'Asagıdaki karar rehberi, kullanım senaryonuza gore hangi araci secmeniz '
        'gerektigini hızlıca belirlemenizi saglar.'
    )
    doc.table(
        ['Gorev',                              'Tavsiye Edilen Araç',   'Alternatif'],
        [
            ['Uzun belge analizi / hukuk / finans', 'Claude Sonnet 4.6',     'Gemini 2.0 Pro'],
            ['Genel sohbet ve sorular',            'ChatGPT / Claude',       'Gemini Flash'],
            ['Kod yazma (IDE)',                    'Cursor + Claude',         'GitHub Copilot'],
            ['Otonom proje gelistirme',            'Claude Code',             'Windsurf'],
            ['Gercek zamanli haber takibi',        'Grok 3',                  'Perplexity'],
            ['Fotogercekci gorsel',                'Flux 1.1 Pro',            'DALL-E 4'],
            ['Sanatsal gorsel',                    'Midjourney v7',           'Adobe Firefly'],
            ['Goruntu icerisinde metin',           'Ideogram 2.5',            'Canva AI'],
            ['Video uretimi',                      'Veo 3 / Kling 2.0',      'Runway Gen-4'],
            ['Ses seslendirme',                    'ElevenLabs',              'Suika (Turkce)'],
            ['Muzik uretimi',                      'Suno v4',                 'Udio 2'],
            ['Yerel / gizli veri',                 'Llama 4 (Ollama ile)',    'DeepSeek R2'],
            ['Google Workspace entegrasyonu',      'Gemini 2.0',              'Notebooklm'],
            ['Web uygulaması prototipi',           'Bolt.new',                'v0 by Vercel'],
        ],
        widths=[175, 130, 166]
    )
    doc.sp(6)
    doc.box(
        'Unutmayin: En iyi araç, is akısınıza en uygun olandır. Buyuk AI sirketleri '
        'surekli guncelleme yapıyor. Bu rehber 2026 basına ait verileri icermektedir. '
        'Araçların guncel fiyat ve ozelliklerini resmi web sitelerinden kontrol edin.',
        'note'
    )


def bolum3_claude_ekosistemi(doc):
    """Bolum 3: Claude Ekosistemi Detayli"""

    # ── Section Cover ──────────────────────────────────────
    doc.section_cover(
        3,
        'Claude Ekosistemi Detayli',
        'Anthropic, Claude ve Claude Code\'u derinlemesine tanıyın',
        'Bu bolumde Anthropic\'i, Claude\'un farklı versiyonlarını, Claude Code\'u ve '
        'MCP gibi ileri duzey ozellikleri kapsamlı sekilde inceliyoruz.'
    )

    # ── 3.1 Anthropic Kimdir? ──────────────────────────────
    doc.new_page('Bolum 3: Claude Ekosistemi')
    doc.h1('3.1  Anthropic Kimdir?')
    doc.sp(4)
    doc.text(
        'Anthropic, 2021 yılında Dario Amodei, Daniela Amodei ve OpenAI\'dan ayrılan '
        'bir grup arastırmacı tarafından San Francisco\'da kuruldu. Sirketin odak '
        'noktası "AI guvenliği" (AI safety) alanındaki arastırmalar ve bu prensipleri '
        'uygulayan modeller gelistirmektir. 2023\'te Amazon\'dan 4 milyar dolar, '
        'Google\'dan 300 milyon dolar yatırım aldı. 2026 itibarıyla sektorun en '
        'saygın AI guvenlik arastırma sirketlerinden biri olarak kabul goruyor.'
    )
    doc.h3('Anthropic\'in Temel Degerleri')
    doc.bullets([
        'AI Safety First: Guclu AI sistemleri gelistirmeden once guvenligini sagla',
        'Constitutional AI: Modele etik ilkeler ogret, kural listesi yapma',
        'Seffaflık: Arastırma sonucllarını acık yayınla (Interpretability calısmaları)',
        'Uzun vadeli guvenlik: AGI gelisiminde insanlıgın cıkarlarını on planda tut',
    ])
    doc.h3('Claude Ailesi — 2026 Model Yelpazesi')
    doc.table(
        ['Model',              'Hız',     'Kapasite',  'Ideal Kullanım',              'API Fiyatı*'],
        [
            ['Claude Haiku 4.5',    'En Hızlı', 'Orta',     'Chatbot, basit gorevler',     '$0.8/M token'],
            ['Claude Sonnet 4.6',  'Hızlı',    'Yuksek',   'Genel AI, kod, analiz',       '$3/M token'],
            ['Claude Opus 4.7',    'Yavas',    'En Yuksek', 'Karmasık muhakeme, arastırma','$15/M token'],
        ],
        widths=[110, 55, 65, 155, 86]
    )
    doc.sp(4)
    doc.text(
        '* Fiyatlar 2026 Q1 itibarıyla input/output token basuına dolardır. API '
        'fiyatlandırması degisebilir, guncel bilgi icin console.anthropic.com adresini '
        'kontrol edin.'
    )
    doc.sp(6)

    # ── 3.2 Claude vs Claude Code ─────────────────────────
    doc.h1('3.2  Claude vs Claude Code — Net Karsilastırma')
    doc.sp(4)
    doc.text(
        'En sık karıstırılan konulardan biri "Claude" ile "Claude Code" arasındaki farktır. '
        'İkisi de aynı AI modelini kullanır fakat calisma sekilleri ve yetenekleri '
        'birbirinden temelden farklıdır.'
    )
    doc.table(
        ['Ozellik',               'Claude (Web/App)',              'Claude Code (Terminal)'],
        [
            ['Erisim sekli',          'Tarayıcı, mobil uygulama',      'Terminal (npm ile kurulur)'],
            ['Dosya sistemi',         'Sadece yukledikleriniz',         'Bilgisayardaki tum dosyalar'],
            ['Komut calıstırma',      'Hayır',                          'Evet — bash, git, npm vb.'],
            ['Proje hafızası',        'Sohbet bazlı',                   'CLAUDE.md ile kalıcı'],
            ['Cok dosya duzenleme',   'Sınırlı (1-2 dosya)',           'Evet — onlarca dosya aynı anda'],
            ['Web arama',             'Evet (Pro+)',                    'MCP ile evet'],
            ['MCP destegi',           'Sınırlı',                       'Tam destek'],
            ['Otonom gorev',          'Manuel adımlar',                'Saatler surebilen otonom calisma'],
            ['Kim icin',              'Herkes — basit gorevler',        'Gelisitriciler, power user'],
            ['Fiyat',                 'Ucretsiz/Pro $20/Max $100',     'Claude Max ile ($100/ay)'],
        ],
        widths=[130, 160, 181]
    )
    doc.sp(6)
    doc.box(
        'Ozet: Claude.ai\'yi kullanmak bir akıllı asistanla sohbet etmek gibidir. '
        'Claude Code kullanmak ise deneyimli bir yazılımcıyı bilgisayarınızın basına '
        'oturtup "su projeyi bitis" demek gibidir. Ikisi farklı araclar, farklı '
        'kullanım senaryoları.',
        'info'
    )

    # ── 3.3 Claude Desktop Kurulum ────────────────────────
    doc.new_page('Bolum 3: Claude Ekosistemi')
    doc.h1('3.3  Claude Desktop Uygulaması')
    doc.sp(4)
    doc.text(
        'Claude Desktop, masaustu bilgisayarınızda dogal AI asistan deneyimi sunan '
        'uygulamadır. Web tarayıcısına ihtiyac duymadan Claude ile calısmanızı saglar. '
        'Windows ve macOS icin mevcuttur.'
    )
    doc.h2('Windows\'ta Kurulum')
    doc.bullets([
        '1. claude.ai/download adresine gidin',
        '2. "Download for Windows" butonuna tıklayın',
        '3. Claude-Setup.exe dosyasını indirin ve calıstırın',
        '4. Kurulum tamamlandıgında masaustune kısayol olusur',
        '5. Anthropic hesabınızla giris yapın veya yeni hesap acın',
    ])
    doc.h2('macOS\'ta Kurulum')
    doc.bullets([
        '1. claude.ai/download adresine gidin',
        '2. "Download for Mac" butonuna tıklayın',
        '3. Claude.dmg dosyasını indirin',
        '4. DMG\'yi acın, Claude.app ikonunu Applications klasorune suruklleyin',
        '5. Spotlight (Cmd+Space) ile "Claude" yazarak acın',
        '6. Anthropic hesabınızla giris yapın',
    ])
    doc.h3('Claude Desktop Ozel Ozellikleri')
    doc.bullets([
        'MCP entegrasyonu: Desktop uygulama MCP server baglantısını destekler',
        'Dosya surukle-birak: Belge ve goruntu dogrudan suruklenebilir',
        'Klavye kısayolu: Cmd/Ctrl+Shift+C ile hızlı acma',
        'Sistem entegrasyonu: Bildirimler, tray icon destegi',
        'Cevrimdısı not: Bazı ozellikler internet baglantısı gerektirmez',
    ])
    doc.box(
        'Claude Desktop, MCP (Model Context Protocol) destegi ile en guclu '
        'sekilde kullanılabilir. Bolum 3.5\'te MCP\'yi detaylıca anlattıktan '
        'sonra Claude Desktop\'a MCP server baglamayı da gosterecegiz.',
        'info'
    )

    # ── 3.4 Plan Karsilastırması ───────────────────────────
    doc.h1('3.4  Claude Planlari ve Fiyatlandırma 2026')
    doc.sp(4)
    doc.text(
        'Anthropic 2026\'da bircok plan sunmaktadır. Hangi planın size uygun oldugunu '
        'belirlemek icin kullanım younuzü, mesaj limitlerini ve Claude Code ihtiyacını '
        'degerlendiriniz.'
    )
    doc.table(
        ['Plan',     'Fiyat/Ay',  'Mesaj Limiti',        'Claude Code', 'Ozellikleri'],
        [
            ['Ucretsiz', '$0',       'Kısıtlı, yavaslıyor', 'Hayır',       'Temel Claude, sinirli'],
            ['Pro',      '$20',      'Yüksek limit',        'Sinirli',     'Oncelikli erisim, Projects'],
            ['Max 5x',   '$100',     '5x Pro limiti',       'Evet',        'Claude Code, MCP, Artifacts'],
            ['Max 20x',  '$200',     '20x Pro limiti',      'Evet',        'En yuksek limit, beta'],
            ['Team',     '$30/kisi', 'Pro+  paylaşım',      'Hayır',       'Ekip calısması, Admin'],
            ['Enterprise','Teklif',  'Ozel',                'Ozel',        'SSO, veri guv., SLA'],
        ],
        widths=[65, 70, 100, 65, 171]
    )
    doc.sp(6)
    doc.box(
        'Claude Code kullanmak icin minimum Max 5x planı ($100/ay) gereklidir. '
        'Bu yatırım, profesyonel gelistirici verimliligi acısından genellikle kendini '
        'fazlasıyla geri odemektedir. Gunluk saatler gecebilecek isler dakikalara iner.',
        'tip'
    )
    doc.sp(4)
    doc.h3('API Planları — Gelisitriciler Icin')
    doc.text(
        'Uygulama gelistirmek isteyenler icin Claude API ayrı bir secenektir. '
        'console.anthropic.com uzerinden API key alarak pay-as-you-go modelinde '
        'calisabilirsiniz. Yeni hesaplar icin $5 ucretsiz kredi verilmektedir.'
    )
    doc.code(
        '# API key almak icin:\n'
        '# 1. console.anthropic.com adresine gidin\n'
        '# 2. "Get API Keys" butonuna tıklayın\n'
        '# 3. Yeni bir API key olusturun\n'
        '# 4. Guvenli bir yerde saklayın (.env dosyasına)\n\n'
        '# Python ile test:\n'
        'import anthropic\n'
        'client = anthropic.Anthropic(api_key="sk-ant-...")\n'
        'message = client.messages.create(\n'
        '    model="claude-sonnet-4-6",\n'
        '    max_tokens=1024,\n'
        '    messages=[{"role": "user", "content": "Merhaba Claude!"}]\n'
        ')\n'
        'print(message.content)',
        'Python'
    )

    # ── 3.5 MCP ───────────────────────────────────────────
    doc.new_page('Bolum 3: Claude Ekosistemi')
    doc.h1('3.5  MCP — Model Context Protocol')
    doc.sp(4)
    doc.text(
        'Model Context Protocol (MCP), Anthropic tarafından 2024 sonunda acık kaynak '
        'olarak duyurulan ve AI modellerinin harici araclara ve veri kaynaklarına '
        'standart bir sekilde baglanmasını saglayan protokoldur. Kısaca MCP, '
        'yapay zekayı "gerçek dunyaya" baglayan koprudur.'
    )
    doc.h3('MCP Neden Onemli?')
    doc.text(
        'Klasik bir LLM, size verilen bilgilerle sınırlıdır. MCP ile Claude, veritabanı '
        'sorgulama, dosya okuma, GitHub\'dan pull request acma, Slack mesajı gonderme, '
        'tarayıcı kontrol etme gibi gercek dunyadaki is akıslarını otomasyon edebilir. '
        'Cok sayıda MCP server yazılmıstır ve bu ekosistem hızla buyumektedir.'
    )
    doc.h3('MCP Mimarisi')
    doc.bullets([
        'MCP Host: Claude Desktop veya Claude Code — modeli calıstıran taraf',
        'MCP Server: Harici aracı (GitHub, Slack, Postgres vb.) saglayan kucuk uygulama',
        'MCP Client: Host ile Server arasındaki iletisimi yoneten protocol katmanı',
        'Transport: stdio (local) veya HTTP/SSE (uzak server) ile iletisim',
    ])
    doc.h3('Populer MCP Serverler (2026)')
    doc.table(
        ['MCP Server',       'Saglayan',   'Ne Yapar?'],
        [
            ['@modelcontextprotocol/server-filesystem', 'Anthropic', 'Dosya sistemi okuma/yazma'],
            ['@modelcontextprotocol/server-github',     'Anthropic', 'GitHub repo, issue, PR islemleri'],
            ['@modelcontextprotocol/server-postgres',   'Anthropic', 'PostgreSQL sorgulama'],
            ['@modelcontextprotocol/server-brave-search','Anthropic','Web arama (Brave API)'],
            ['@modelcontextprotocol/server-slack',      'Anthropic', 'Slack mesajlasma'],
            ['@modelcontextprotocol/server-puppeteer',  'Topluluk',  'Tarayıcı otomasyonu'],
            ['@modelcontextprotocol/server-memory',     'Anthropic', 'Kalıcı hafıza (Knowledge Graph)'],
        ],
        widths=[200, 70, 201]
    )
    doc.sp(6)
    doc.h3('Claude Desktop\'a MCP Server Baglama')
    doc.text(
        'Claude Desktop config dosyasını duzenleyerek MCP server ekleyebilirsiniz. '
        'Config dosyasının yolu:'
    )
    doc.bullets([
        'macOS: ~/Library/Application Support/Claude/claude_desktop_config.json',
        'Windows: %APPDATA%\\Claude\\claude_desktop_config.json',
    ])
    doc.code(
        '// claude_desktop_config.json ornegi\n'
        '{\n'
        '  "mcpServers": {\n'
        '    "filesystem": {\n'
        '      "command": "npx",\n'
        '      "args": [\n'
        '        "-y",\n'
        '        "@modelcontextprotocol/server-filesystem",\n'
        '        "/Users/kullaniciadi/Desktop",\n'
        '        "/Users/kullaniciadi/Documents"\n'
        '      ]\n'
        '    },\n'
        '    "github": {\n'
        '      "command": "npx",\n'
        '      "args": ["-y", "@modelcontextprotocol/server-github"],\n'
        '      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_..." }\n'
        '    }\n'
        '  }\n'
        '}',
        'JSON'
    )
    doc.box(
        'MCP ekosistemi surekli buyuyor. mcpservers.org sitesinde 500\'den fazla '
        'topluluk yapımı MCP server bulunuyor. Notion, Jira, Figma, Supabase, '
        'MongoDB ve daha onlarcası icin hazır MCP serverlar mevcut.',
        'info'
    )

    # ── 3.6 Artifacts ve Projects ─────────────────────────
    doc.new_page('Bolum 3: Claude Ekosistemi')
    doc.h1('3.6  Artifacts, Projects ve Skills')
    doc.sp(4)
    doc.h2('Artifacts — Canli Icerik Uretimi')
    doc.text(
        'Artifacts, Claude\'un kod, HTML, SVG, React bilesenini veya diger icerikleri '
        'konusma akısından ayrı, interaktif bir pencerede gostermesini saglayan '
        'ozelliktir. Ornegin Claude\'a bir web sayfası tasarlattigınızda sonucu hemen '
        'tarayıcıda onizleyebilirsiniz.'
    )
    doc.bullets([
        'HTML/CSS/JS: Canlı tarayıcı onizlemesi',
        'React bileseni: Interaktif UI prototipi',
        'SVG grafigi: Vektör gorsel anında gozter',
        'Mermaid diyagramı: Akıs seması, mimari diyagram',
        'Kod (tum diller): Soz dizimi vurgulamalı gosterim',
    ])
    doc.h2('Projects — Uzun Vadeli Hafıza')
    doc.text(
        'Projects ozelligi, Claude\'a bir projeye ozgu kalıcı baglam saglar. Proje '
        'icine dosya yukleyebilir, talimatlar ekleyebilir ve her yeni sohbetin o projeyi '
        'hatırlamasını saglayabilirsiniz. Aynı proje uzerinde defalarca calısırken her '
        'defasında baglam tekrar sağlamak zorunda kalmazsınız.'
    )
    doc.bullets([
        'Dosya yukleme: PDF, kod dosyası, Excel — kalıcı proje hafızasında',
        'Proje talimatları: "Bu proje React kullaniyor, Turkce cevapla" gibi',
        'Sohbet gecmisi: Proje kapsamındaki tum konusmalar saklanır',
        'Ekip paylasımı: Team planlarda projeyi ekiple paylas',
    ])
    doc.h2('Skills — Otomatik Calısan Yetenekler')
    doc.text(
        'Skills (Beceriler), Claude Code\'un otomatik olarak yukleyebilecegi kucuk '
        'Markdown dokumanlardır. Bir skill dosyası, Claude\'a belirli bir gorevi nasıl '
        'yapacagını ogretir. Ornegin bir "pdf-olustur" skill dosyası Claude Code\'a '
        'her zaman WeasyPrint kullanarak PDF olusturmasını soylleyebilir. '
        'Bolum 10\'da Skills konusunu derinlemesine inceleyecegiz.'
    )
    doc.box(
        'Bolum 3 Ozeti: Anthropic guvenlik odaklı bir AI sirketi, Claude ailesi '
        'Haiku/Sonnet/Opus ile farkli ihtiyaclara hitap ediyor. Claude Code icin '
        'Max plan gerekli. MCP ile Claude gercek dunyadaki araclara baglanabiliyor. '
        'Sonraki bolumde Claude Code kurulumunu adım adım yapıyoruz.',
        'info'
    )


def main():
    doc = Doc()
    print("Icerik olusturuluyor — Sayfa 20-40...")

    # Part 1 icerigini de dahil et
    kapak_sayfasi(doc)
    icindekiler(doc)
    bolum1_giris(doc)
    bolum1_ek_ve_bolum2_baslangic(doc)

    # Part 2 icerik
    bolum2_devami(doc)
    bolum3_claude_ekosistemi(doc)

    pages = doc.save('yapay_zeka_ogreniyorum_p1_40.pdf')
    print(f"\nTamamlandi! Toplam {pages} sayfa uretildi.")
    print("Dosya: yapay_zeka_ogreniyorum_p1_40.pdf")


if __name__ == '__main__':
    main()
