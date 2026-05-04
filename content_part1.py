#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Icerik - Bolum 1-20 sayfa
Kapak + Icindekiler + Bolum 1: Yapay Zeka Dunyasina Giris
"""
from pdf_engine import Doc, PW, PH, ML, MR, MT, MB, CW, HDR_H
from pdf_engine import NAVY, ORANGE, WHITE, BLACK, GRAY_BG, GRAY_DARK, NAVY_LIGHT

def kapak_sayfasi(doc):
    """Sayfa 1: Kapak"""
    doc.new_page('Yapay Zeka Ogreniyorum - 2026 Guncel Rehber')

    # Tam sayfa lacivert arkaplan
    doc._fill(*NAVY)
    doc._rect(0, 0, PW, PH, 'f')

    # Ust dekoratif serit
    doc._fill(*ORANGE)
    doc._rect(0, PH-6, PW, 6, 'f')

    # Orta buyuk beyaz panel
    doc._fill(*WHITE)
    doc._rect(ML-10, PH*0.38, CW+20, PH*0.48, 'f')

    # Sol turuncu aksent
    doc._fill(*ORANGE)
    doc._rect(ML-10, PH*0.38, 6, PH*0.48, 'f')

    # Ana baslik
    baslik1 = "YAPAY ZEKA"
    baslik2 = "OGRENIYORUM"
    doc._fill(*NAVY)
    b1w = doc.f['bold'].measure(baslik1, 46)
    b2w = doc.f['bold'].measure(baslik2, 46)
    doc._txy(baslik1, 'bold', 46, (PW - b1w)/2, PH*0.80)
    doc._fill(*ORANGE)
    doc._txy(baslik2, 'bold', 46, (PW - b2w)/2, PH*0.80 - 56)

    # Alt baslik
    alt = "2026 Guncel Rehber  -  Sifirdan Profesyonellige"
    doc._fill(*NAVY)
    aw = doc.f['reg'].measure(alt, 13)
    doc._txy(alt, 'reg', 13, (PW-aw)/2, PH*0.80 - 82)

    # Ayirici cizgi
    doc._stroke(*ORANGE)
    doc._lw(1.5)
    doc._line(ML+20, PH*0.80-96, PW-MR-20, PH*0.80-96)

    # Yazar bilgi kutusu
    doc._fill(*NAVY)
    doc._rect(ML, PH*0.38+14, CW, 72, 'f')
    doc._fill(*ORANGE)
    doc._rect(ML, PH*0.38+14, 5, 72, 'f')
    doc._fill(*WHITE)
    doc._txy("Hazirlayan:", 'bold', 10, ML+14, PH*0.38+68)
    doc._fill(0.9, 0.9, 0.9)
    doc._txy("Aykut Uces  |  x.com/aykutuces  |  EticMedya  |  vibecodingex.com",
             'bold', 11, ML+14, PH*0.38+50)
    doc._fill(0.75, 0.75, 0.8)
    tanitim = ("Bu egitim, yapay zeka alaninda pratik deneyime sahip girisimci ve")
    doc._txy(tanitim, 'reg', 9, ML+14, PH*0.38+32)
    tanitim2 = ("yazilimci Aykut Uces tarafindan hazirlanmistir. x.com/aykutuces")
    doc._txy(tanitim2, 'reg', 9, ML+14, PH*0.38+20)

    # Yil etiketi
    doc._fill(*ORANGE)
    doc._rect(PW-MR-60, MB+30, 55, 24, 'f')
    doc._fill(*WHITE)
    yilw = doc.f['bold'].measure('2026', 14)
    doc._txy('2026', 'bold', 14, PW-MR-60+(55-yilw)/2, MB+40)

    # Alt dekorasyon
    doc._fill(*ORANGE)
    doc._rect(0, MB+8, PW, 4, 'f')


def icindekiler(doc):
    """Sayfa 2-3: Icindekiler"""
    doc.new_page('Icindekiler')

    # Baslik
    doc._fill(*NAVY)
    doc._rect(ML-10, doc._y-38, CW+20, 48, 'f')
    doc._fill(*WHITE)
    basw = doc.f['bold'].measure('ICINDEKILER', 22)
    doc._txy('ICINDEKILER', 'bold', 22, (PW-basw)/2, doc._y-24)
    doc._y -= 56

    doc._fill(*ORANGE)
    doc._rect(ML, doc._y, CW, 1.5, 'f')
    doc._y -= 10

    bolumler = [
        ('Bolum 1', 'Yapay Zeka Dunyasina Giris',           '4'),
        ('',        '  Yapay zeka nedir ve tarihcesi',       '5'),
        ('',        '  2026 AI ekosistemi haritasi',         '6'),
        ('',        '  LLM (Large Language Model) kavrami',  '8'),
        ('',        '  AI turleri: Text, Image, Video, Audio, Code', '10'),
        ('Bolum 2', '2026 da Hangi AI ile Ne Yapilir?',     '12'),
        ('',        '  Claude, ChatGPT, Gemini, Grok karsilastirmasi', '13'),
        ('',        '  Gorsel AI: Midjourney, Flux, Ideogram','17'),
        ('',        '  Video AI: Veo 3, Sora, Runway, Kling', '19'),
        ('',        '  Ses ve Kod AI araclari',              '21'),
        ('Bolum 3', 'Claude Ekosistemi Detayli',             '24'),
        ('',        '  Anthropic kimdir, Claude nedir?',     '25'),
        ('',        '  Claude vs Claude Code karsilastirmasi','27'),
        ('',        '  Desktop uygulama ve planlar',         '30'),
        ('',        '  MCP, Artifacts, Projects, Skills',    '33'),
        ('Bolum 4', 'Claude Code Kurulum ve Kullanim',       '36'),
        ('',        '  Node.js kurulumu (Win/Mac)',           '37'),
        ('',        '  Kurulum ve authentication',           '40'),
        ('',        '  Temel komutlar ve CLAUDE.md',         '43'),
        ('',        '  Slash komutlari, MCP, Hooks, Subagents','47'),
        ('Bolum 5', 'Claude Code ile Gercek Projeler',       '52'),
        ('',        '  Web sitesi yapma',                    '53'),
        ('',        '  Mobil uygulama (Windows)',             '57'),
        ('',        '  Mobil uygulama (MacBook)',             '62'),
        ('',        '  Masaustu uygulama (Electron/Tauri)',   '66'),
        ('Bolum 6', 'App Store ve Google Play Yayinlama',    '70'),
        ('',        '  Google Play Console adimlari',        '71'),
        ('',        '  App Store Connect adimlari',          '75'),
        ('',        '  Test surecleri ve red nedenleri',     '79'),
        ('Bolum 7', 'AdMob Reklam Entegrasyonu',             '82'),
        ('Bolum 8', 'SaaS / Abonelik Sistemleri',            '88'),
        ('',        '  In-App Purchase ve Adapty',           '89'),
        ('',        '  RevenueCat, Qonversion alternatifler', '93'),
        ('Bolum 9', 'GitHub ve Faydali Repolar',             '96'),
        ('Bolum 10','Claude Code Skills ve MD Dosyalari',    '104'),
        ('Bolum 11','SaaS Projesi Gelistirme',               '112'),
        ('Bolum 12','fal.ai ve Gorsel/Video AI API',         '122'),
        ('',        '  EticPanel.com Case Study',            '128'),
        ('Bolum 13','Prompt Muhendisligi',                   '134'),
        ('Bolum 14','ChatGPT, Codex ve OpenAI Ekosistemi',   '144'),
        ('Bolum 15','AI ile Marketing',                      '152'),
        ('Bolum 16','Kritik Konular ve Gelecege Hazirlik',   '168'),
        ('',        'Kapanis ve Kaynaklar',                  '184'),
    ]

    for bno, ad, sayfa in bolumler:
        is_main = bno != ''
        fk = 'bold' if is_main else 'reg'
        sz = 10.5 if is_main else 10
        color = NAVY if is_main else GRAY_DARK
        lh = 18 if is_main else 14

        doc._need(lh + 2)

        if is_main:
            doc._fill(*ORANGE)
            doc._rect(ML, doc._y - lh + 8, CW, 1, 'f')
            doc._y -= 4

        doc._fill(*color)
        doc._txy(f'{bno}  {ad}' if bno else ad, fk, sz, ML + (0 if is_main else 10), doc._y)

        # Noktalama ve sayfa no
        pw = doc.f[fk].measure(sayfa, sz)
        txt_w = doc.f[fk].measure(f'{bno}  {ad}' if bno else ad, sz)
        dot_start = ML + (0 if is_main else 10) + txt_w + 4
        dot_end = PW - MR - pw - 4
        if dot_end > dot_start:
            dot_y = doc._y - 2
            doc._stroke(*GRAY_DARK if not is_main else NAVY)
            doc._lw(0.3)
            step = 4
            x = dot_start
            while x < dot_end:
                doc._line(x, dot_y, min(x+1, dot_end), dot_y)
                x += step
        doc._fill(*color)
        doc._txy(sayfa, fk, sz, PW-MR-pw, doc._y)
        doc._y -= lh

    doc._y -= 10
    doc.box(
        "Bu PDF, yapay zekayi sifirdan ogrenmek isteyen herkese yonelik kapsamli bir rehberdir. "
        "Her bolum bagimsiz olarak okunabilir. Bolumler arasindan size uygun konuyu secin.",
        'info'
    )


def bolum1_giris(doc):
    """Bolum 1: Yapay Zeka Dunyasina Giris (sayfa 4-15)"""

    # --- SECTION COVER ---
    doc.section_cover(
        1,
        'Yapay Zeka Dunyasina Giris',
        '2026 itibarıyla AI nedir, nasıl calisir?',
        'Bu bolumde yapay zekanin temel kavramlarini, tarihsel gelisimini, buyuk dil modellerinin '
        'nasil calistigini ve 2026 itibarıyla AI ekosisteminin haritasini oğreneceksiniz.'
    )

    # ── 1.1 Yapay Zeka Nedir? ──────────────────────────────
    doc.new_page('Bolum 1: Yapay Zeka Dunyasina Giris')
    doc.h1('1.1  Yapay Zeka Nedir?')
    doc.sp(4)
    doc.text(
        'Yapay zeka (Artificial Intelligence - AI), bilgisayar sistemlerinin normalde insan '
        'zekasinı gerektiren gorevleri yerine getirebilmesi icin tasarlanan bilim ve muhendislik '
        'dalıdır. Bu gorevler arasinda dil anlama, goruntu tanıma, problem cozme, ogrenme ve '
        'karar verme gibi yetenekler yer almaktadır.'
    )
    doc.text(
        '2026 yilına geldigimizde yapay zeka artık bir akademik kavram olmaktan cıkmıs, '
        'gunluk hayatımızın ayrılmaz bir parcasi haline gelmistir. Telefonunuzdaki asistan, '
        'e-postanızdaki spam filtresi, Netflix onerileri, Google Haritalar trafik tahminleri '
        've bir doktorun MRI taramasını analiz etmesine yardımcı olan sistem — bunların '
        'hepsi yapay zekanın farkli bicimleridır.'
    )
    doc.h3('Yapay Zekanın Temel Tanimı')
    doc.text(
        'John McCarthy, 1956 yilında Dartmouth Konferansı\'nda yapay zeka terimini ilk kez '
        'kullanmıstır. McCarthy\'nin tanımına gore yapay zeka, "makineyi akıllıca davranmasını '
        'saglayan bilim ve muhendisliktir." Bu tanım gunumuze kadar evrilmis olsa da ozunde '
        'aynı kalmaktadır: Makinelere insan benzeri zeka kazandırma cabası.'
    )
    doc.text(
        'Modern yapay zeka uc ana paradigma uzerine insaa edilmistir. Birincisi Sembolik AI, '
        'kural tabanlı sistemler ve mantık programlamasına dayanır. İkincisi Makine Ogrenmesi '
        '(Machine Learning), verilere dayalı olarak ogrenen algoritmalar kullanır. Ucuncusu '
        've gunumuzde en guclu olan Derin Ogrenme (Deep Learning) ise insan beyninin yapısından '
        'esinlenen yapay sinir agları kullanır.'
    )
    doc.box(
        'Yapay zeka "akıllı" degil, "istatistiksel olarak en uygun cevabı bulan" bir '
        'sistemdir. ChatGPT veya Claude yanıt uretirken anlayarak degil, buyuk veri uzerinde '
        'egitilmis olasılık hesaplamaları yaparak calisır. Bu ayrımı anlamak, AI araçlarını '
        'dogru kullanmak icin kritik oneme sahiptir.',
        'note'
    )
    doc.h3('Dar AI vs Genel AI vs Super AI')
    doc.text(
        'Yapay zekayı kapsam acisindan uc kategoriye ayırırız. Dar AI (Narrow AI), belirli '
        'bir goreve odaklanan sistemlerdir; ornegi yuz tanıma, ceviri veya satranc oynama. '
        'Gunumuzde kullandıgımız tum AI sistemleri bu kategoridedir. Genel AI (AGI - Artificial '
        'General Intelligence), insan duzeydinde herhangi bir zihinsel gorevi yerine '
        'getirebilecek sistemleri ifade eder; henuz mevcut degildir ancak 2030\'lar icin '
        'tahminler yapılmaktadır. Super AI ise insan zekasını tum boyutlarda asan, teorik '
        'bir kavramdır.'
    )
    doc.bullets([
        'Dar AI (Narrow AI): Tek goreve odaklı, gunumuzde mevcut — ChatGPT, Claude, Midjourney',
        'AGI (General AI): Her alanda insan duzeyi — 2030 sonrası tahmin ediliyor',
        'Super AI: İnsan zekasını asan — teorik, henuz yok',
        'Yapay Genel Zeka icin Anthropic, OpenAI ve DeepMind aktif arastırma yapıyor',
    ])

    doc.h3('Makine Ogrenmesi ve Derin Ogrenme Farkı')
    doc.text(
        'Makine ogrenmesi, bilgisayarın ornek verilerden ogrenmesini saglayan algoritmalar '
        'butunudur. Klasik programlamada kural → veri → cıktı mantıgı islerken, makine '
        'ogreniminde veri + cıktı → kural mantıgı calisır. Derin ogrenme ise makine '
        'ogreniminin bir alt dalıdır ve cok katmanlı yapay sinir agları kullanır. GPT-4, '
        'Claude Sonnet 4.6 ve Opus 4.7 gibi modeller derin ogrenme temelli buyuk dil modelleridir (LLM).'
    )
    doc.sp(6)

    # ── 1.2 Kısa Tarihce ───────────────────────────────────
    doc.h2('1.2  Yapay Zekanın Kısa Tarihcesi')
    doc.text(
        '1940\'lardan gunumuze uzanan AI yolculugu, birden fazla "kıs" ve "bahar" '
        'donemi gecirmistir. Asagıdaki tablo bu yolculugun kritik kilometre taslarını '
        'ozetlemektedir.'
    )
    doc.table(
        ['Yıl', 'Olay', 'Onemi'],
        [
            ['1950', 'Alan Turing — Turing Testi', 'Makine zekası icin ilk kriter'],
            ['1956', 'Dartmouth Konferansı', 'AI terimi resmi olarak dogdu'],
            ['1969', 'İlk AI kıs donemi', 'Finansman kesildi, umutlar azaldı'],
            ['1986', 'Geri Yayılım algoritması', 'Sinir agları tekrar ilgi gördü'],
            ['1997', 'Deep Blue satranc sampiyonu yendi', 'Dar AI\'nın gucu ispatlandı'],
            ['2006', 'Derin Ogrenme renaissance', 'Hinton ve arkadaşları yeniden alevlendirdi'],
            ['2012', 'AlexNet ImageNet yarısması', 'Goruntu tanımada devrim'],
            ['2017', 'Transformer mimarisi (Attention is All You Need)', 'Modern LLM\'lerin temeli'],
            ['2020', 'GPT-3 — 175B parametre', 'Dil modellerinde yeni cag'],
            ['2022', 'ChatGPT — 100M kullanıcı', 'AI ana akıma girdi'],
            ['2023', 'GPT-4, Claude 2, Gemini', 'Rekabet hızlandı'],
            ['2024', 'Claude 3.5 Sonnet, GPT-4o, Gemini 1.5', 'Multimodal ve uzun context'],
            ['2025', 'Claude Sonnet 4.6, Opus 4.7, GPT-5', 'Otonom AI cagi, guclu modeller'],
            ['2026', 'AGI tartısmaları, AI her yerde', 'Herkes AI ile calısıyor'],
        ],
        widths=[45, 180, 246]
    )
    doc.sp(6)
    doc.box(
        '2026 itibarıyla yapay zeka artic bir araştırma konusu degil, gunluk is '
        'aracınızdır. Bir programcının yanında Claude Code, bir icerik ureticisin yanında '
        'ChatGPT, bir tasarımcının yanında Midjourney bulunuyor. Bu araclari kullanmayı '
        'bilmek artık okur-yazarlık gibi temel bir beceridir.',
        'tip'
    )

    # ── 1.3 2026 AI Ekosistemi ─────────────────────────────
    doc.new_page('Bolum 1: Yapay Zeka Dunyasina Giris')
    doc.h1('1.3  2026 AI Ekosistemi Haritası')
    doc.sp(4)
    doc.text(
        '2026\'da yapay zeka ekosistemi inanılmaz derecede genis ve karmaşık bir yapıya '
        'kavuşmuştur. Temel kategorileri ve her kategorinin onde gelen oyuncularını '
        'anlamak, hangi araci ne icin kullanacagınıza karar vermenizi kolaylaştırır.'
    )
    doc.h3('Buyuk Dil Modelleri (LLM) Haritası')
    doc.table(
        ['Kategori', 'Sirket', 'Model', 'Guclu Oldugu Alan'],
        [
            ['Kapalı Kaynak', 'Anthropic', 'Claude Sonnet 4.6 / Opus 4.7', 'Kod, analiz, guvenlik'],
            ['Kapalı Kaynak', 'OpenAI', 'GPT-5, o3', 'Genel, goruntu, ses'],
            ['Kapalı Kaynak', 'Google', 'Gemini 2.0 Ultra', 'Multimodal, Workspace'],
            ['Kapalı Kaynak', 'xAI', 'Grok 3', 'Gercek zamanli X verisi'],
            ['Acık Kaynak', 'Meta', 'Llama 4', 'Local calistırma'],
            ['Acık Kaynak', 'Alibaba', 'Qwen 2.5', 'Cok dilli, Asya odaklı'],
            ['Acık Kaynak', 'DeepSeek', 'DeepSeek R2', 'Maliyet etkin muhakeme'],
            ['Acık Kaynak', 'Mistral', 'Mistral Large 3', 'Avrupa veri gizliligi'],
        ],
        widths=[95, 75, 130, 171]
    )
    doc.sp(8)
    doc.h3('Gorsel AI Ekosistemi')
    doc.table(
        ['Araç', 'Sirket', 'Guclu Alan', 'Fiyat'],
        [
            ['Midjourney v7', 'Midjourney', 'Sanatsal, cinematic', '$10-120/ay'],
            ['DALL-E 4', 'OpenAI', 'Prompt hassasiyeti', 'ChatGPT icinde'],
            ['Flux 1.1 Pro', 'Black Forest Labs', 'Fotogercekci', 'API/kredi'],
            ['Ideogram 2.5', 'Ideogram', 'Goruntude metin', '$7-25/ay'],
            ['Nano Banana 2', 'fal.ai', 'Hizli, API dostu', 'Kredi bazlı'],
            ['Stable Diffusion 4', 'Stability AI', 'Acık kaynak, local', 'Ucretsiz/self-host'],
            ['Adobe Firefly 4', 'Adobe', 'Ticari guvenli', 'Creative Cloud'],
            ['Recraft v3', 'Recraft', 'Vektor, UI tasarım', 'Freemium'],
        ],
        widths=[110, 110, 130, 121]
    )
    doc.sp(8)
    doc.h3('Video AI Ekosistemi')
    doc.table(
        ['Araç', 'Sirket', 'Ozellik', 'Fiyat'],
        [
            ['Veo 3', 'Google DeepMind', 'En uzun, en kaliteli', 'Google One AI'],
            ['Sora 2', 'OpenAI', 'Gercekci fizik simul.', 'ChatGPT Pro'],
            ['Kling 2.0', 'Kuaishou', 'Asya tarzı, hızlı', 'Freemium'],
            ['Runway Gen-4', 'Runway', 'Video duzenleme', '$15-95/ay'],
            ['Hailuo 2', 'MiniMax', 'Karakter tutarlılıgı', 'API/Kredi'],
            ['Wan 2.1', 'Alibaba', 'Acık kaynak video', 'Self-host'],
        ],
        widths=[100, 120, 145, 106]
    )
    doc.sp(8)
    doc.box(
        '2026 itibarıyla AI pazarında yuzlerce araç bulunmaktadır. Hepsini ogrenmeye '
        'calismak hem imkansız hem de gereksizdir. Odak noktanızı belirleyin: Yazılım '
        'gelistirecekseniz Claude Code, icerik uretecekseniz ChatGPT veya Claude, '
        'gorsel yaratacaksanız Midjourney veya Flux secin ve o araci derinlemesine '
        'ogrenin. Geri kalanını zaman icinde kesfedebilirsiniz.',
        'tip'
    )

    # ── 1.4 LLM Nedir? ─────────────────────────────────────
    doc.new_page('Bolum 1: Yapay Zeka Dunyasina Giris')
    doc.h1('1.4  LLM — Buyuk Dil Modeli Nedir?')
    doc.sp(4)
    doc.text(
        'Large Language Model (LLM), yani Buyuk Dil Modeli; internetten, kitaplardan ve '
        'cok sayıda belgeden derlenen dev veri setleri uzerinde egitilmis, dili anlayan '
        've ureten yapay zeka modellerdir. ChatGPT, Claude, Gemini — bunların hepsi birer LLM\'dir.'
    )
    doc.h3('LLM Nasıl Calısır?')
    doc.text(
        'LLM\'lerin calısma prensibi "bir sonraki tokeni tahmin etme" uzerine kuruludur. '
        'Token, bir modelin isledigı en kucuk anlam birimidir — bir hece, bir kelime veya '
        'bir noktalama isareti olabilir. GPT-4 gibi modeller, bir cumle verildiginde '
        'istatistiksel olarak en olası devamı uretir. Bu basit ilke, milyarlarca parametre '
        've devasa egitim verisiyle birlestirildignde inanılmaz derecede yetenekli sistemler '
        'ortaya cıkarır.'
    )
    doc.h3('Parametre Sayısı Ne Anlama Gelir?')
    doc.text(
        'Modelin "agırlıkları" olarak da bilinen parametreler, modelin egitim sırasında '
        'ogrendigi sayısal degerlerdir. GPT-3\'un 175 milyar, GPT-4\'un ise tahminlere gore '
        '1 trilyon ustunde parametresi vardır. Ancak 2025 sonrasında parametre sayısı tek '
        'basına kalitenin gostergesi olmaktan cıkmıstır — verimlilik ve egitim kalitesi '
        'en az buyukluk kadar onemli hale gelmistir. DeepSeek R1, GPT-4\'e yaklasan '
        'performansı cok daha az parametreyle elde etmistir.'
    )
    doc.h3('Context Window (Baglan Penceresi) Nedir?')
    doc.text(
        'Context window, modelin tek bir konusmada "hatirlayabildigi" maksimum token '
        'sayısıdır. 2022\'de GPT-3 icin bu deger sadece 4.096 tokendi. 2024\'te Gemini '
        '1.5 Pro, 1 milyon token context window ile tarihin en uzun baglam penceresi '
        'rekoru kırdı. 2026\'da standart modeller 200K-500K token context ile calısmaktadır. '
        'Bu, 300 ila 700 sayfalık bir kitabı tek seferde analiz edebilmek anlamına gelir.'
    )
    doc.table(
        ['Model', 'Context Window', 'Pratik Kullanim'],
        [
            ['GPT-3.5 Turbo', '16K token (~12K kelime)', 'Kısa sohbetler, basit gorevler'],
            ['GPT-4o', '128K token (~96K kelime)', 'Uzun belgeler, kod projeleri'],
            ['Claude Sonnet 4.6', '200K token (~150K kelime)', 'Dev kod tabanları, kitap analizi'],
            ['Gemini 2.0 Ultra', '1M token (~750K kelime)', 'Tam kitap serisi, buyuk kod repo'],
            ['Gemini 2.0 Pro', '2M token (~1.5M kelime)', 'En buyuk context (2026 itibarıyla)'],
        ],
        widths=[130, 140, 201]
    )
    doc.sp(6)
    doc.box(
        'Context window buyuk olması her zaman iyi degildir. Model context\'in sonlarina '
        'dogru dikkatini kaybedebilir (lost in the middle problemi). Pratik kural: '
        'Context\'in %60-70\'ini doldurun, geri kalanını bos bırakın.',
        'warning'
    )
    doc.sp(6)
    doc.h3('Transformer Mimarisi — AI\'nın Beyni')
    doc.text(
        '2017\'de Google Brain ekibinin "Attention is All You Need" makalesiyle tanıttıgı '
        'Transformer mimarisi, modern tum buyuk dil modellerinin temelini olusturur. '
        'Transformerin en onemli yeniligi "self-attention" mekanizmasıdır: Model, bir '
        'kelimenin anlamını belirlerken cumledeki diger tum kelimelere olan ilgisini '
        'hesaplar. Bu sayede "bank" kelimesinin "nehir kıyısı" mı yoksa "finans kurumu" '
        'mu oldugunu baglama gore anlayabilir.'
    )
    doc.text(
        'GPT (Generative Pre-trained Transformer) ailesi, sadece "decoder" bloklarını '
        'kullanan bir Transformer varyantıdır. BERT ise "encoder" bloklarını kullanır '
        've metin anlama gorevlerinde ustundur. Claude ve GPT-4 gibi modern modeller, '
        'milyonlarca GPU saati boyunca trilyonlarca token uzerinde pre-training yapılmıs, '
        'ardından RLHF (Reinforcement Learning from Human Feedback) ile ince ayar '
        'yapılmıstır.'
    )
    doc.box(
        'Transformer mimariyi ayrıntılı anlayamasanız da bu metaforu hatırlayın: '
        'LLM, olagan ustu bellekli, milyonlarca metin okumust, son derece zeki ama '
        'sahte bilgi uretebilen bir yardımcıdır. Bilgilerini her zaman cift kontrol edin.',
        'info'
    )

    # ── 1.5 AI Turleri ─────────────────────────────────────
    doc.new_page('Bolum 1: Yapay Zeka Dunyasina Giris')
    doc.h1('1.5  AI Turleri: Text, Image, Video, Audio, Code')
    doc.sp(4)
    doc.text(
        '2026 itibarıyla yapay zeka artık sadece metin uretmekten cok daha fazlasını '
        'yapabilmektedir. Modalite (mod) olarak adlandırılan bu farklı kategoriler, her '
        'biri kendi uzmanlasmıs modelleri ve kullanım senaryolarıyla gelismistir.'
    )
    doc.h2('Metin AI (Text)')
    doc.text(
        'Metin bazlı AI\'lar, 2026\'da en olgun ve kullanılan kategoridır. ChatGPT, Claude, '
        'Gemini bu kategorinin liderleridir. Kullanım alanları son derece genistir: yazı '
        'yazma, ozetleme, ceviri, soru-cevap, analiz, kod yazma ve daha fazlası.'
    )
    doc.bullets([
        'Guclu yonleri: En olgun teknoloji, en genis kullanım alanı, en iyi dokumantasyon',
        'Zayıf yonleri: Bazen yanılabilir (hallucination), gercek zamanli bilgiye erisim sınırlı',
        'Kullanım: Her turlu yazı, analiz, ogrenme, kod yazma, arastırma',
    ])

    doc.h2('Gorsel AI (Image)')
    doc.text(
        'Text-to-Image teknolojisi 2022\'de Stable Diffusion ve Midjourney v1 ile ana akıma '
        'girdi. 2026\'da gorsel AI\'lar artık fotografik gercekcilik, sanatsal stil ve '
        'metin gosterme konularında insan tasarımcılara meydan okuyacak seviyededir. '
        'Midjourney v7, tek bir prompt ile film afisi kalitesinde gorusel uretebilir.'
    )
    doc.bullets([
        'Midjourney — En sanatsal sonuclar, community destegi kuvvetli',
        'Flux 1.1 Pro — Fotogercekcilik, API erismesi kolay (fal.ai uzerinden)',
        'Adobe Firefly — Ticari kullanım icin guvenli, stok foto alternaitifi',
        'Ideogram — Goruntu icerisinde metin yerlesimi cok basarılı',
        'DALL-E 4 — ChatGPT ile entegre, anında kullanım kolaylıgı',
    ])

    doc.h2('Video AI')
    doc.text(
        'Video AI, 2024\'te Sora\'nın duyurulmasıyla devrim yaradı. 2026\'da 10-60 saniyelik '
        'videolar metin komutundan saniyeler icinde uretilmektedir. Reklamcılık, sosyal medya '
        'icerik uretimi ve film on-vizualizasyonu en buyuk kullanım alanlarıdır.'
    )
    doc.bullets([
        'Veo 3 (Google) — En uzun video, en gercekci fizik simulasyonu',
        'Sora 2 (OpenAI) — Sinematik kalite, kamera hareketleri kontrol edilebilir',
        'Kling 2.0 — Asya pazarında lider, turkce prompt destegi iyi',
        'Runway Gen-4 — Video duzenleme ve stil transferi konusunda cok guclu',
    ])

    doc.h2('Ses AI (Audio)')
    doc.text(
        'Ses AI\'lar iki ana kategoride guclu: Metin-konusma (TTS) ve muzik uretimi. '
        'ElevenLabs, 2026\'da yapay bir sesin gercek insan sesi ile ayırt edilemez '
        'oldugunu kanıtlamıstır. Muzik uretiminde Suno ve Udio ise profesyonel kalitede '
        'sarkilar uretebilmektedir.'
    )
    doc.table(
        ['Araç', 'Kategori', 'Ozellik', 'Kullanım'],
        [
            ['ElevenLabs', 'TTS / Voice Clone', 'Gercekci ses, 29 dil', 'Podcast, video seslendirme'],
            ['Suika (Suono)', 'TTS', 'Turkce optimizeli', 'Turkce icerik'],
            ['Suno v4', 'Muzik Uretimi', 'Vokal + enstru.', 'Reklam muzigi, jingle'],
            ['Udio 2', 'Muzik Uretimi', 'Studi kalitesi', 'Profesyonel muzik'],
            ['Whisper API', 'Ses Tanıma (STT)', 'OpenAI tabanlı', 'Transkripsiyon'],
        ],
        widths=[90, 95, 110, 176]
    )

    doc.h2('Kod AI (Code)')
    doc.text(
        'Kod AI\'lar, gelistiricilerin verimliligini 2-10x artırdıgı kanıtlanmıs araçlardır. '
        '2026\'da artık tum yazılım gelistiricilerinin %70\'inden fazlası AI kod asistanı '
        'kullandıgını bildirmektedir. Bu araçlar sadece kod tamamlama degil, tam proje '
        'olusturma, hata ayıklama ve mimarı tasarım konularında da yardım sunmaktadır.'
    )
    doc.table(
        ['Araç', 'Acıklama', 'Guclu Alan', 'Fiyat (2026)'],
        [
            ['Claude Code', 'Anthropic terminal ajani', 'Buyuk kod tabanları, otonom gorevler', 'Claude Max ile'],
            ['Cursor', 'VS Code bazlı AI IDE', 'Kod tamamlama, chat', '$20/ay Pro'],
            ['GitHub Copilot', 'GitHub resmi AI', 'IDE entegrasyonu', '$10/ay bireysel'],
            ['Windsurf', 'Codeium gelistirdi', 'Agentic coding, flows', '$15/ay Pro'],
            ['Bolt.new', 'StackBlitz web IDE', 'Web uygulaması prototip', 'Freemium'],
            ['v0 by Vercel', 'UI komponent uretici', 'React/Next.js UI', 'Freemium'],
            ['OpenAI Codex', 'CLI terminal ajani', 'OpenAI ekosistemi', 'API bazlı'],
        ],
        widths=[90, 130, 160, 91]
    )
    doc.sp(6)
    doc.box(
        'Bu rehberin odak noktasını Claude Code olusturmaktadır. Claude Code, terminal '
        'uzerinden calisarak dosya okuyup yazabilen, komut calıstırabilen ve buyuk projeleri '
        'otonom olarak gelisitrebilen guclu bir AI ajanıdır. Bolum 4\'te detaylı kurulum ve '
        'kullanım rehberini bulacaksınız.',
        'tip'
    )

    # ── 1.6 AI ve Insan Iliskisi ───────────────────────────
    doc.new_page('Bolum 1: Yapay Zeka Dunyasina Giris')
    doc.h1('1.6  AI ve İnsan: Doğru Zihniyet')
    doc.sp(4)
    doc.text(
        'Yapay zekayı dogru kullanabilmek icin once dogru zihniyet geliştirmeniz gerekir. '
        'AI araçları, ne sizi isssiz bırakacak dusman sistemler, ne de her seyi cozecek '
        'mucizeli artalardır. Gercek su: AI, sizi 10x daha verimli yapan bir kuvvet '
        'carpanıdır. Ama bu kuvveti yonlendiren hala sizsiniz.'
    )
    doc.h3('AI Hallucination (Yanılsama) Problemi')
    doc.text(
        'LLM\'lerin en buyuk zayıflıgı "hallucination" yani gerci olmayan bilgileri '
        'gercekmiş gibi sunmasıdır. Model, egitim verisinde gorduğu desenleri birleştirerek '
        'aslında var olmayan kaynaklar, isimler, tarihler veya istatistikler uretebilir. '
        '2026\'da bu sorun hala tamamen cozulmus degildir, ancak onceki yıllara kıyasla '
        'cok azalmıstır. Kritik bilgileri her zaman bagimsız kaynaklardan dogrulayin.'
    )
    doc.h3('AI\'yı Guclendiren Kaynaklar')
    doc.bullets([
        'Egitim verisi: Internet, kitaplar, akademik makaleler, kod — trilyonlarca token',
        'RLHF: İnsan geri bildirimiyle yapılan ince ayar — modeli yardımsever yapar',
        'Constitutional AI (Anthropic): Ahlaki ilkeleri olan AI egitimi — Claude\'a ozel',
        'Reinforcement Learning: Deneme-yanılma ile ogrenme — muhakeme gorevlerinde buyuk kazanım',
    ])

    doc.h3('2026\'da AI Kullanıcı Profilleri')
    doc.table(
        ['Profil', 'Nasıl Kullanıyor?', 'Elde Ettigi Avantaj'],
        [
            ['Yazılımcı', 'Claude Code ile proje geliştirme', '5-10x hızlı kod yazma'],
            ['Icerik Ureticisi', 'ChatGPT/Claude ile post ve video script', 'Gunluk 30+ icerik'],
            ['Girisimci', 'AI ile MVP olusturma', 'Teknik ekip olmadan urun'],
            ['Pazarlamacı', 'AI ile A/B test metinleri', 'Onlarca varyant saniyede'],
            ['Ogretmen/Akademisyen', 'AI ile ders materyali ve arastırma', 'Saatler yerine dakikalar'],
            ['Tasarımcı', 'Midjourney + Figma ile prototip', 'Konsept → gorsel saniyede'],
        ],
        widths=[100, 190, 181]
    )
    doc.sp(6)
    doc.box(
        '"AI, isimi elimden alacak mı?" sorusu yanlıs bir sorudur. Dogru soru su: '
        '"AI kullanan biri, kullanmayan birinin isini alabilir mi?" Yanıt: Evet. '
        'O yuzden bu rehberi okuyorsunuz ve dogru adımı atıyorsunuz.',
        'tip'
    )

    doc.text(
        'Bu bolumde yapay zekanın temel kavramlarını, tarihsel gelisimini ve 2026 '
        'ekosistem haritasını ogrendik. Sonraki bolumde her bir AI aracını ayrıntılı '
        'inceleyerek hangi aracın hangi is icin ideal oldugunu goreceğiz.'
    )


def bolum1_ek_ve_bolum2_baslangic(doc):
    """Bolum 1 tamamlama + Bolum 2 baslangıcı — sayfaları 20'ye tamamla"""

    # ── 1.7 AI Guvenlik ve Etik Temelleri ──────────────────
    doc.new_page('Bolum 1: Yapay Zeka Dunyasina Giris')
    doc.h1('1.7  AI Guvenlik ve Etik Temelleri')
    doc.sp(4)
    doc.text(
        'AI sistemlerinin guvenli ve etik sekilde kullanılması, 2026\'da hem bireyler hem '
        'de sirketler icin kritik bir konu haline gelmistir. Buyuk dil modellerinin '
        'olagan ustu yetenekleri, beraberinde ciddi sorumluluklar getirmektedir.'
    )
    doc.h3('Temel AI Guvenlik Kavramları')
    doc.bullets([
        'Alignment (Hizalama): AI sisteminin insan degerlerine uygun hareket etmesi',
        'Hallucination: Modelin yanlis ama gercekmiş gibi gorunen bilgi uretmesi',
        'Bias (Yanlılık): Egitim verisindeki onjargıların modele yansıması',
        'Jailbreak: Modelin guvenlik filtrelerini asan promtlar aracılıgıyla manipule edilmesi',
        'Prompt Injection: Kotu niyetli kullanıcıların sistem promptunu ezmesi',
        'Data Poisoning: Egitim verisinin kasıtlı sekilde bozulması',
    ])
    doc.h3('Anthropic\'in Constitutional AI Yaklasımı')
    doc.text(
        'Anthropic, Claude\'u gelistirirken "Constitutional AI" adlı yenilikci bir yaklasım '
        'kullanmıstır. Bu yontemde, modele belirli bir anayasa (kurallar seti) verilmekte '
        've modelin bu anayasaya uygun sekilde davranması icin kendi kendini degerlendirmesi '
        'saglanmaktadır. Sonuc olarak Claude, zararlı icerik uretme konusunda daha direncli, '
        'yardımseverlik konusunda ise daha tutarlı bir model haline gelmistir.'
    )
    doc.box(
        'Constitutional AI, modelin hem yardımsever (helpful) hem de zararsız (harmless) '
        'hem de donuk (honest) olmasını hedefler. Anthropic bu uc ilkeyi "HHH" olarak '
        'adlandırmaktadır. Claude\'un diger modellerden farkı buyuk olcude bu egitim '
        'metodolojisinden kaynaklanır.',
        'info'
    )
    doc.h3('Turkiye\'de AI Kullanımında Dikkat Edilecekler')
    doc.text(
        'KVKK (Kisisel Verilerin Korunması Kanunu) kapsamında AI araclara gonderilen '
        'veriler onem tasımaktadır. Musteri verileri, kisisel bilgiler veya gizli is '
        'bilgilerini AI araclara girerken dikkatli olunmalıdır. Enterprise planlar genellikle '
        'veri islememe garantisi sunarken, ucretsiz veya bireysel planlar bu garantiyi '
        'vermeyebilir. Bolum 16\'da bu konuyu daha ayrıntılı ele alacagız.'
    )
    doc.bullets([
        'Ucretsiz planlarda girilen veriler model egitiminde kullanılabilir',
        'Kurumsal verileri paylasirken Enterprise plan veya API kullanın',
        'API kullaniminda veriler modeli egitmek icin kullanılmaz (OpenAI ve Anthropic politikası)',
        'GDPR ve KVKK kapsamında AI araclarin gizlilik politikalarını okuyun',
    ])

    # ── 1.8 Makine Ogrenmesi Temelleri ─────────────────────
    doc.new_page('Bolum 1: Yapay Zeka Dunyasina Giris')
    doc.h1('1.8  Makine Ogrenmesinin Temelleri')
    doc.sp(4)
    doc.text(
        'AI araçlarını etkin kullanabilmek icin teknik mimarilerini derinlemesine anlamanız '
        'gerekmez; ancak temel kavramları bilmek, AI ile daha iyi iletisim kurmanızı ve '
        'sınırlarını daha iyi anlamanızı saglar.'
    )
    doc.h3('Supervised, Unsupervised ve Reinforcement Learning')
    doc.table(
        ['Ogrenme Turu', 'Nasıl Calısır?', 'Ornek Uygulama'],
        [
            ['Supervised (Denetimli)',
             'Etiketli veri → model egrenir',
             'Spam filtresi, goruntu sınıflandırma'],
            ['Unsupervised (Denetimsiz)',
             'Etiketsiz veri → patern bulur',
             'Musteri segmentasyonu, anomali tespiti'],
            ['Reinforcement (Pekistirmeli)',
             'Deneme-yanılma + odullendir',
             'Oyun oynayan AI, otonom araclar'],
            ['Self-supervised',
             'Veriyi kendi etiketler',
             'GPT, Claude — pre-training asaması'],
            ['RLHF',
             'İnsan geri bildirimiyle RL',
             'ChatGPT, Claude — fine-tuning asaması'],
        ],
        widths=[120, 160, 191]
    )
    doc.sp(6)
    doc.h3('Pre-training vs Fine-tuning vs RAG')
    doc.text(
        'Buyuk dil modellerinin gelistirme surecini uc asamada dusunebilirsiniz. '
        'Pre-training: Modelin devasa veri seti uzerinde "dil ogrenmesi" asaması, '
        'en pahalı asamadır (GPT-4 icin milyarlarca dolar). Fine-tuning: Onceden '
        'egitilmis bir modelin belirli bir gorev icin ince ayar yapılması; cok daha '
        'ucuz ve hızlıdır. RAG (Retrieval Augmented Generation): Modele harici bilgi '
        'tabanından veri ekleme teknigi; fine-tuning yerine tercih edilir cunku '
        'guncellenmesi daha kolaydır.'
    )
    doc.box(
        'Kendi AI uygulamanızı olusturuyorsanız genellikle RAG veya fine-tuning '
        'yapmanız gerekir. Sıfırdan model egitmek milyonlarca dolarlık bir yatırımdır '
        've neredeyse hic kimse bunu yapmaz. API uzerinden mevcut modelleri kullanın.',
        'tip'
    )
    doc.h3('Embedding ve Vektor Veritabanları')
    doc.text(
        'Embedding, metni sayısal vektore donusturme islemidir. "Kedi" ve "kedigiller" '
        'gibi anlam bakımından yaklın kelimeler, vektor uzayında da birbrine yaklın '
        'konumlarda yer alır. Bu mantık, RAG sistemlerinin temelini olusturur: Belgeleri '
        'embedding\'e cevir, sorguyu da embedding\'e cevir, en yaklın belgeleri bul ve '
        'modele bırak. Pinecone, Weaviate, Chroma ve pgvector populer vektor veritabanı '
        'cozumleridir.'
    )
    doc.h3('Promptun Teknik Yapısı')
    doc.text(
        'Bir LLM\'e gonderilen mesaj aslında uc katmandan olusur: System prompt (modele '
        'kim oldugunu ve nasıl davranacagını soyleyen talimat), user mesajı (kullanıcının '
        'sorusu veya gorevi) ve assistant mesajı (modelin onceki yanıtları, few-shot '
        'ornekleri). Bu yapıyı anlamak, prompt muhendisliginin temelidir. Bolum 13\'te '
        'bu konuyu derinlemesine inceleyecegiz.'
    )
    doc.code(
        '// Tipik LLM API Cagri Yapısı (Claude Ornegi)\n'
        '{\n'
        '  "model": "claude-sonnet-4-6",\n'
        '  "system": "Sen bir uzman yazılım mimarısın. Turkce yanıt ver.",\n'
        '  "messages": [\n'
        '    {"role": "user", "content": "REST API tasarımında best practice\'ler neler?"},\n'
        '    {"role": "assistant", "content": "..."},\n'
        '    {"role": "user", "content": "Pagination icin ne onerirsin?"}\n'
        '  ],\n'
        '  "max_tokens": 4096,\n'
        '  "temperature": 0.7\n'
        '}',
        'JSON/API'
    )

    # ── Bolum 1 Ozet ───────────────────────────────────────
    doc.new_page('Bolum 1: Yapay Zeka Dunyasina Giris')
    doc.h1('Bolum 1 Ozeti ve Kilit Noktalar')
    doc.sp(4)
    doc.text(
        'Yapay zeka dunyasına giris bolumunu tamamladınız. Bu bolumde ogrendiklerinizi '
        'pekistirmek icin en onemli kavramları aşagıda ozetliyoruz.'
    )
    doc.h3('Bu Bolumde Ogrendikleriniz')
    doc.bullets([
        'Yapay zekanın tanımı: İnsan zekasını gerektiren gorevleri yapan bilgisayar sistemleri',
        'AI turleri: Dar AI (gunumuzde), AGI (gelecekte), Super AI (teorik)',
        'LLM calısma prensibi: Token tahmini + transformer mimarisi + RLHF',
        'Context window: Modelin tek sohbette hatirlayabildiginin siniri',
        'AI modaliteleri: Text, Image, Video, Audio, Code — her birinin lider aracları',
        '2026 ekosistemi: Claude, GPT-5, Gemini 2.0, Grok 3 ana dil modelleri',
        'Hallucination tehlikesi: AI\'nın yanilis bilgiyi gercekmiş gibi sunması',
        'Constitutional AI: Anthropic\'in guvenli AI egitim yontemi',
        'Pre-training / Fine-tuning / RAG: AI gelistirme asamaları',
    ])
    doc.sp(6)
    doc.h3('Pratik Cıkarımlar')
    doc.table(
        ['Senaryo', 'Onerimiz'],
        [
            ['Metin yazma ve analiz',         'Claude Sonnet 4.6 veya GPT-4o'],
            ['Kod yazma ve debug',             'Claude Code veya Cursor'],
            ['Gorsel olusturma',               'Midjourney v7 veya Flux 1.1'],
            ['Video uretimi',                  'Veo 3 veya Kling 2.0'],
            ['Ses seslendirme',                'ElevenLabs'],
            ['Gercek zamanli bilgi',           'Grok 3 veya Perplexity'],
            ['Acık kaynak / local calistırma', 'Llama 4 veya DeepSeek R2'],
        ],
        widths=[160, 311]
    )
    doc.sp(8)
    doc.box(
        'Sonraki Bolum: "2026\'da Hangi AI ile Ne Yapilir?" — Her AI aracını karsilastırmalı '
        'tablolar ve gercek kullanım senaryolarıyla detaylıca inceleyecegiz. Fiyat, '
        'guclı yonler, zayıf yonler ve kim icin uygun olduğunu net olarak goreceksiniz.',
        'info'
    )

    # ══════════════════════════════════════════════════════════
    # BOLUM 2 BASLANGICI
    # ══════════════════════════════════════════════════════════
    doc.section_cover(
        2,
        '2026 da Hangi AI ile Ne Yapilir?',
        'Karsilastırmalı rehber ve kullanım senaryoları',
        'Bu bolumde 2026\'nın onde gelen AI aracllarını yan yana karsilastırıyor, her birinin '
        'guclü ve zayıf yanlarını, fiyatlandırmasını ve ideal kullanıcı profilini inceliyoruz.'
    )

    doc.new_page('Bolum 2: 2026 da Hangi AI ile Ne Yapilir?')
    doc.h1('2.1  Buyuk Dil Modelleri Karsilastırması')
    doc.sp(4)
    doc.text(
        '2026 itibarıyla piyasada onlarca rekabetci buyuk dil modeli bulunmaktadır. '
        'Hepsini denemek hem zaman alıcı hem de kafa karıstırıcıdır. Bu bolumde en '
        'onemli modelleri sistematik sekilde karsilastırarak karar vermenizi kolaylastıracagız.'
    )
    doc.h2('Claude (Anthropic)')
    doc.text(
        'Anthropic\'in gelistirdigi Claude, ozellikle uzun belgeler, kod yazma ve kompleks '
        'muhakeme gerektiren gorevlerde buyuk farklılık yaratır. 2025 sonunda piyasaya '
        'surulen Claude Sonnet 4.6 ve Opus 4.7 modelleri, yazılım gelistirme ve analitik '
        'dusunme konularında rakiplerine gore belirgin avantaj saglamaktadır.'
    )
    doc.table(
        ['Kriter', 'Detay'],
        [
            ['Model', 'Claude Sonnet 4.6 / Haiku 4.5 / Opus 4.7 (2026)'],
            ['Context Window', '200.000 token — yaklasık 150.000 kelime'],
            ['Guclu Yonleri', 'Uzun belge analizi, kod yazma, tutarlılık, guvenlik'],
            ['Zayıf Yonleri', 'Gorsel uretim yok, gercek zamanli web yok (bazi planlarda var)'],
            ['Fiyat (2026)', 'Ucretsiz / Pro $20/ay / Max $100/ay / API token bazlı'],
            ['Kim Icin', 'Yazılımcılar, arastırmacılar, hukuk/finans analistleri'],
            ['Ornek Kullanım', 'Claude Code ile tam proje gelistirme, 300 sayfalık belge ozetleme'],
        ],
        widths=[130, 341]
    )
    doc.sp(6)
    doc.box(
        'Claude\'un en buyuk avantajı "extended thinking" (uzatılmıs dusunme) ozelligi: '
        'Model zorlu problemlerde adım adım derinlemesine dusunebilir ve bu surecte '
        'hatalarını kendi kendine duzelter. Matematik, mantık ve kod problemlerinde '
        'bu ozellik buyuk performans artısı saglar.',
        'tip'
    )

    doc.h2('ChatGPT — OpenAI')
    doc.text(
        'OpenAI\'nın ChatGPT\'si, 2022\'den bu yana dunyanın en yaygın kullanılan AI aracı '
        'olma ozelligini korumaktadır. 2025 sonu itibarıyla GPT-5 ile yeni bir cag acılmıs, '
        'multimodal yetenekler (ses, goruntu, video) tek bir arayuzde birlestirilmistir.'
    )
    doc.table(
        ['Kriter', 'Detay'],
        [
            ['Model', 'GPT-5, GPT-4o, o3-mini, o3 (2026)'],
            ['Context Window', '128K token (GPT-4o), o3 modelleri daha az'],
            ['Guclu Yonleri', 'Genel amaclı, goruntu anlama, gorsel uretim (DALL-E 4), ses'],
            ['Zayıf Yonleri', 'Claude\'dan daha az tutarlı uzun bic gorevlerde'],
            ['Fiyat (2026)', 'Ucretsiz (sınırlı) / Plus $20/ay / Pro $200/ay'],
            ['Kim Icin', 'Her turlu kullanıcı, baslangıc duzeyi icin ideal'],
            ['Ornek Kullanım', 'Gunluk sohbet, goruntu analizi, DALL-E ile gorsel uretim'],
        ],
        widths=[130, 341]
    )


def main():
    doc = Doc()
    print("Icerik olusturuluyor — Ilk 20 sayfa...")

    kapak_sayfasi(doc)
    icindekiler(doc)
    bolum1_giris(doc)
    bolum1_ek_ve_bolum2_baslangic(doc)

    pages = doc.save('yapay_zeka_ogreniyorum_p1_20.pdf')
    print(f"\nTamamlandi! {pages} sayfa uretildi.")
    print("Dosya: yapay_zeka_ogreniyorum_p1_20.pdf")


if __name__ == '__main__':
    main()
