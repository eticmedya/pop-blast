#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Icerik Part 7 — Sayfa 134-190
Bolum 13: Prompt Muhendisligi
Bolum 14: ChatGPT, Codex ve OpenAI Ekosistemi
Bolum 15: AI ile Marketing
Bolum 16: Kritik Konular ve Gelecege Hazirlik
Kapanis ve Kaynaklar
"""
from pdf_engine import Doc
from pdf_engine import NAVY, ORANGE, WHITE, BLACK, GRAY_BG, GRAY_DARK

from content_part1 import kapak_sayfasi, icindekiler, bolum1_giris, bolum1_ek_ve_bolum2_baslangic
from content_part2 import bolum2_devami, bolum3_claude_ekosistemi
from content_part3 import bolum4_claude_code, bolum5_projeler_baslangic
from content_part4 import bolum5_mobil_windows, bolum5_mobil_mac, bolum5_desktop, bolum6_store
from content_part5 import bolum7_admob, bolum8_saas, bolum9_github
from content_part6 import bolum10_skills, bolum11_saas_proje, bolum12_falai


def bolum13_prompt(doc):
    """Bolum 13: Prompt Muhendisligi"""

    doc.section_cover(
        13,
        'Prompt Muhendisligi',
        'AI\'den daha iyi sonuclar alin',
        'Bu bolumde AI modellerinden en iyi sonuclari nasil alacaginizi, '
        'etkili prompt yazma tekniklerini ve Claude\'a ozel ipuclarini inceliyoruz.',
    )

    # ── 13.1 Prompt Muhendisligi Nedir? ───────────────────────
    doc.new_page('Bolum 13: Prompt Muhendisligi')
    doc.h1('13.1  Prompt Muhendisligi Nedir?')
    doc.sp(4)
    doc.text(
        'Prompt muhendisligi, AI modellerinden istediginiz sonuclari almanizi saglayan '
        'yonerge yazma sanatıdir. Ayni soruyu farkli bicimde sormak cok farkli '
        'sonuclar uretebilir. Iyi bir prompt, modele yeterli baglam, net hedef '
        've cikti formati verir.'
    )

    doc.h2('Temel Prensipler')
    doc.bullets([
        'Netlik: Ne istediginizi acikca ifade edin',
        'Baglam: Neden, kim icin, hangi kosullarda?',
        'Format: Cevabi nasil istiyorsunuz? (liste, tablo, kod, paragraf)',
        'Ornekler: Ornekler vererek beklentinizi somutlastirin',
        'Kisitlamalar: Ne yapmamasini istiyorsunuz?',
        'Persona: Claude\'u bir uzman olarak tanimlayin',
    ])

    doc.h2('Zayif vs Guclu Prompt')
    doc.code(
        '# ZAYIF:\n'
        '> "Bir marketing emaili yaz"\n\n'
        '# GUCLU:\n'
        '> "Sen deneyimli bir B2B SaaS copywriter\'sin.\n'
        '>  Hedef kitle: 10-50 calisanli KOBIler, karar verici CEO/CTO.\n'
        '>  Urun: proje yonetim araci, ayda $49.\n'
        '>  Amac: ucretsiz denemeye kayit.\n'
        '>  Ton: profesyonel ama samimi, jargondan kacin.\n'
        '>  Format:\n'
        '>    - Konu satiri (max 50 karakter, emoji yok)\n'
        '>    - On izleme metni (max 90 karakter)\n'
        '>    - Email govde (max 150 kelime)\n'
        '>    - CTA butonu metni\n'
        '>  Once 3 farkli konu satiri onerisini sun, sonra en iyisi\n'
        '>  icin tam emaili yaz."',
        'Terminal'
    )

    # ── 13.2 Chain of Thought ─────────────────────────────────
    doc.new_page('Bolum 13: Prompt Muhendisligi')
    doc.h1('13.2  Chain of Thought ve Reasoning')
    doc.sp(4)
    doc.text(
        'Chain of Thought (CoT), modelin adim adim dusunmesini istemenizi saglar. '
        'Bu yontem, ozellikle karmasik problem cozme, analiz ve karar alma '
        'gorevlerinde buyuk fark yaratir. Claude, extended thinking modunda '
        'cok daha derin bir CoT uygular.'
    )
    doc.code(
        '# Adim adim dusunmesini isteyin:\n'
        '> "Asagidaki problemi adim adim coz. Her adimda dusunce\n'
        '>  surecini goster:\n'
        '>  Bir e-ticaret sitesinde sepet terk orani %75.\n'
        '>  Bunu azaltmak icin en etkili 5 stratejiyi onerdir.\n'
        '>  Her strateji icin:\n'
        '>    - Uygulama karmasikligi (1-5)\n'
        '>    - Beklenen etki (1-5)\n'
        '>    - Oncelik siralama gerekcesl"\n\n'
        '# Veya Claude 3.7+ extended thinking:\n'
        '> "Bu mimari kararı derin analiz et. Tum tradeoff\'ları\n'
        '>  dusun: mikroservis mi yoksa monolit mi?"',
        'Terminal'
    )

    doc.h2('Few-Shot Prompting')
    doc.text(
        'Modele ornekler vererek beklenti kalibinizi olusturabilirsiniz. '
        'Bu "few-shot" yaklasimi ozellikle belirli bir format veya ton '
        'tutturmak icin cok etkilidir.'
    )
    doc.code(
        '> "Asagidaki ornekte oldugu gibi teknik kavramlari\n'
        '>  basit Turkce ile acikla:\n\n'
        '>  Ornek 1:\n'
        '>  KAVRAM: API\n'
        '>  ACIKLAMA: Iki uygulama arasindaki tercüman. Lokantanin\n'
        '>  garsonu gibi — siparisini aliyor, mutfaga iletıyor,\n'
        '>  yemeği sana getiriyor.\n\n'
        '>  Ornek 2:\n'
        '>  KAVRAM: Cache\n'
        '>  ACIKLAMA: Sik kullanilan bilgilerin akilci tutulan kopyas.\n'
        '>  Soforu her gun gidecegi adresi ezbere bilmesi gibi.\n\n'
        '>  Simdi acikla:\n'
        '>  KAVRAM: Veritabani Index"',
        'Terminal'
    )

    # ── 13.3 Role Prompting ───────────────────────────────────
    doc.new_page('Bolum 13: Prompt Muhendisligi')
    doc.h1('13.3  Rol Tanimlama ve Sistem Mesajlari')
    doc.sp(4)

    doc.h2('Etkili Rol Tanimlama')
    doc.code(
        '# Uzman persona:\n'
        '> "Sen 15 yillik deneyime sahip bir iOS gelistiricisin.\n'
        '>  Swift ve SwiftUI\'de uzmansin. App Store politikalarini\n'
        '>  ezber biliyorsun. Bana asagidaki kodu incele ve...\n\n'
        '# Elestirici persona:\n'
        '> "Sen bir girisim yatirimcisisn. Benim iş planımı oku\n'
        '>  ve en sert 10 itirazini sun. Yalinmaci olma."\n\n'
        '# Hedef kitle persona:\n'
        '> "Sen 55 yasinda, bilgisayar kullanimi sinirli bir emeklı\n'
        '>  kullanicisın. Bu uygulama talimatini okuyunca ne\n'
        '>  anlarsın, nerede kafan karisir?"',
        'Terminal'
    )

    doc.h2('Sistem Promptu Sablonu (API kullanimi)')
    doc.code(
        'const systemPrompt = `\n'
        'Sen EticBot\'sun — EticPanel.com\'un musteri destek asistani.\n\n'
        'GOREV: Kullanicilarin gorsel AI uretimi ile ilgili sorularini\n'
        'cevapla, sorunlarini coz.\n\n'
        'KURAL:\n'
        '- Sadece EticPanel ozelliklerinden bahset\n'
        '- Rakip urunler hakkinda yorum yapma\n'
        '- Teknik detaylari basit dille anlat\n'
        '- Her cevabin sonuna ilgili dok linki ver\n'
        '- Bilmiyorsan "Bu konuda destek ekibimize aktarayim" de\n\n'
        'TON: Yardımsever, sabırlı, profesyonel\n'
        '`;\n\n'
        'const response = await anthropic.messages.create({\n'
        '  model: "claude-sonnet-4-6",\n'
        '  system: systemPrompt,\n'
        '  messages: [{ role: "user", content: userMessage }],\n'
        '});',
        'TypeScript'
    )

    # ── 13.4 Prompt Kaliplari ─────────────────────────────────
    doc.new_page('Bolum 13: Prompt Muhendisligi')
    doc.h1('13.4  Hazir Prompt Kaliplari')
    doc.sp(4)

    doc.h2('Kod Inceleme')
    doc.code(
        '> "Asagidaki [DILI] kodunu incele:\n'
        '>  [KOD]\n\n'
        '>  Kontrol et:\n'
        '>  1. Guvenlik aciklarI (OWASP Top 10)\n'
        '>  2. Performans sorunları\n'
        '>  3. Okunabilirlik ve bakım kolayligi\n'
        '>  4. Hata yonetimi eksiklikleri\n'
        '>  5. Test edilebilirlik\n\n'
        '>  Her bulgu icin: Sorun, Neden Sorun, Cozum onerisI"',
        'Terminal'
    )

    doc.h2('Dokuman Yazma')
    doc.code(
        '> "Asagidaki fonksiyon icin dokumantasyon yaz:\n'
        '>  [KOD]\n\n'
        '>  Formatı:\n'
        '>  - Ne yapar (1 cumle)\n'
        '>  - Parametreler (tur + aciklama)\n'
        '>  - Donüs degeri\n'
        '>  - Olasi hatalar\n'
        '>  - Kullanim ornegi (gercekci bir senaryo ile)"',
        'Terminal'
    )

    doc.h2('Hata Ayiklama')
    doc.code(
        '> "Asagidaki hatayi alıyorum:\n'
        '>  HATA: [hata mesajı]\n\n'
        '>  ORTAM: [OS, dil versiyonu, kutuphane versiyonlari]\n\n'
        '>  KOD:\n'
        '>  [ilgili kod bolumu]\n\n'
        '>  Denediklerim: [ne denedim]\n\n'
        '>  Nedeni ne olabilir? En olasiliktan az olasiliga dogru\n'
        '>  sırala, her biri icin test adımı yaz."',
        'Terminal'
    )
    doc.box(
        'Hatayı Claude\'a verirken mutlaka: hata mesajı, ortam bilgisi, '
        'ilgili kod ve denediklerinizi ekleyin. Bu 4 bilgi olmadan '
        'Claude tahmin yurütmek zorunda kalır ve cevaplar yuzeysel olur.',
        'tip'
    )


def bolum14_openai(doc):
    """Bolum 14: ChatGPT, Codex ve OpenAI Ekosistemi"""

    doc.section_cover(
        14,
        'ChatGPT, Codex ve OpenAI Ekosistemi',
        'Diger guclu AI araclari',
        'Bu bolumde OpenAI\'nin sunduğu ChatGPT, API ve Codex gibi araclari, '
        'Claude ile kiyaslayarak ne zaman hangisini tercih etmeniz gerektigini inceliyoruz.',
    )

    # ── 14.1 OpenAI Ekosistemi ────────────────────────────────
    doc.new_page('Bolum 14: ChatGPT, Codex ve OpenAI Ekosistemi')
    doc.h1('14.1  OpenAI Ekosistemi Genel Bakis')
    doc.sp(4)
    doc.text(
        'OpenAI, yapay zeka alaninin en taninmis firmalarından biridir. '
        'ChatGPT\'yi, GPT-4o modelini, DALL-E gorsel uretimini, Whisper ses '
        'tanima sistemini ve Codex kod asistanini gelistirmistir. '
        'Tum bu urunler API araciligiyla entegre edilebilir.'
    )

    doc.h2('OpenAI Urunleri')
    doc.table(
        ['Urun',          'Ne Yapar?',                        'Fiyat'],
        [
            ['GPT-4o',        'Guclu genel amacli model',          'API: ~$5/1M token'],
            ['GPT-4o mini',   'Hizli ve ucuz model',               'API: ~$0.15/1M token'],
            ['o3 / o4-mini',  'Derin reasoning, matematik',        'API: degisken'],
            ['DALL-E 3',      'Metin-den-gorsel uretimi',          '$0.04-0.12/gorsel'],
            ['Whisper',       'Ses-den-metin donusumu',             '$0.006/dakika'],
            ['Embeddings',    'Metin vektorlestirme (RAG)',         '$0.02/1M token'],
            ['ChatGPT Plus',  'ChatGPT premium abonelik',          '$20/ay'],
        ],
        widths=[110, 220, 141]
    )

    # ── 14.2 ChatGPT vs Claude ────────────────────────────────
    doc.new_page('Bolum 14: ChatGPT, Codex ve OpenAI Ekosistemi')
    doc.h1('14.2  ChatGPT vs Claude: Ne Zaman Hangisi?')
    doc.sp(4)

    doc.table(
        ['Gorev',                   'Tercih',      'Neden?'],
        [
            ['Uzun dok. analizi',       'Claude',       'Daha uzun context, hassas okuma'],
            ['Matematik/mantik',        'o3/o4-mini',   'Reasoning modelleri ustelustun'],
            ['Gorsel uretim',           'DALL-E 3',     'OpenAI kendi entegrasyonu'],
            ['Ses tanima',              'Whisper',       'Sektorde standart, ucuz'],
            ['Kod yazma',               'Her ikisi',    'Benzer kalite; deneyin'],
            ['Guclu sistem promptu',    'Claude',       'Talimat takibi daha guvenilir'],
            ['Plugin/GPT ekosistemi',   'ChatGPT',      'GPT Store, action\'lar'],
            ['API maliyet',             'Duruma gore',  'GPT-4o mini genelde daha ucuz'],
            ['Turkce dil kalitesi',     'Claude',       'Daha dogal Turkce cevap'],
        ],
        widths=[150, 100, 221]
    )
    doc.sp(6)
    doc.box(
        'Bu kitap Claude uzerine yogunlasmiştır ancak her aracin guclü ve zayif '
        'oldugu alanlar vardir. Profesyonel bir AI kullanicisi tek bir araca '
        'bagimli kalmaz, goreve gore dogru araci secer.',
        'info'
    )

    # ── 14.3 OpenAI API Entegrasyonu ─────────────────────────
    doc.new_page('Bolum 14: ChatGPT, Codex ve OpenAI Ekosistemi')
    doc.h1('14.3  OpenAI API Entegrasyonu')
    doc.sp(4)
    doc.code(
        'npm install openai\n\n'
        'import OpenAI from "openai";\n\n'
        'const client = new OpenAI({\n'
        '  apiKey: process.env.OPENAI_API_KEY,\n'
        '});\n\n'
        '// Temel sohbet:\n'
        'const chat = await client.chat.completions.create({\n'
        '  model: "gpt-4o-mini",\n'
        '  messages: [\n'
        '    { role: "system", content: "Sen yardimci bir asistansin." },\n'
        '    { role: "user", content: "Turkiye\'nin baskenti neredir?" },\n'
        '  ],\n'
        '});\n'
        'console.log(chat.choices[0].message.content);\n\n'
        '// Streaming:\n'
        'const stream = await client.chat.completions.create({\n'
        '  model: "gpt-4o",\n'
        '  stream: true,\n'
        '  messages: [{ role: "user", content: prompt }],\n'
        '});\n'
        'for await (const chunk of stream) {\n'
        '  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");\n'
        '}',
        'TypeScript'
    )

    # ── 14.4 Whisper Ses Tanima ───────────────────────────────
    doc.new_page('Bolum 14: ChatGPT, Codex ve OpenAI Ekosistemi')
    doc.h1('14.4  Whisper ile Ses Tanima')
    doc.sp(4)
    doc.text(
        'OpenAI Whisper, 99 dili destekleyen guclu bir ses-den-metin modelidir. '
        'Toplanti kaydi cozumleme, podcast transkripsiyonu veya sesli komut '
        'gibi kullanim alanlari icin idealdir. Dakikada $0.006 ile oldukca uygun fiyatlidir.'
    )
    doc.code(
        'import fs from "fs";\n'
        'import OpenAI from "openai";\n\n'
        'const client = new OpenAI();\n\n'
        '// Ses dosyasini transkribe et:\n'
        'async function transkribe(dosyaYolu: string) {\n'
        '  const transkript = await client.audio.transcriptions.create({\n'
        '    file: fs.createReadStream(dosyaYolu),\n'
        '    model: "whisper-1",\n'
        '    language: "tr",  // Turkce icin\n'
        '    response_format: "verbose_json",\n'
        '    timestamp_granularities: ["segment"],\n'
        '  });\n'
        '  return transkript;\n'
        '}\n\n'
        '// Sonuc: { text, segments: [{start, end, text}] }',
        'TypeScript'
    )
    doc.box(
        'Claude Code\'a "Bu ses dosyasini transkribe et, toplanti notlari cikart '
        've eylem maddelerini listele" diyebilirsiniz. Claude, Whisper API ile '
        'transkript alip ardından kendi analizi ile ozet ve eylem maddeleri cikarir.',
        'tip'
    )

    # ── 14.5 DALL-E Gorsel ────────────────────────────────────
    doc.new_page('Bolum 14: ChatGPT, Codex ve OpenAI Ekosistemi')
    doc.h1('14.5  DALL-E 3 ile Gorsel Uretimi')
    doc.sp(4)
    doc.code(
        'const gorsel = await client.images.generate({\n'
        '  model: "dall-e-3",\n'
        '  prompt: "Futuristik bir Istanbul manzarasi, 2075 yili,\n'
        '           ucaklar ve Bogaz koprusu, dijital art tarzinda",\n'
        '  n: 1,\n'
        '  size: "1792x1024",\n'
        '  quality: "hd",      // standard veya hd\n'
        '  style: "vivid",     // vivid veya natural\n'
        '});\n'
        'console.log("Gorsel URL:", gorsel.data[0].url);',
        'TypeScript'
    )

    doc.h2('DALL-E 3 vs Flux Karsilastirmasi')
    doc.table(
        ['Kriter',         'DALL-E 3',                    'Flux Pro'],
        [
            ['Kalite',         'Yuksek, tutarli',              'Cok yuksek, fotorealist'],
            ['Prompt takibi',  'Cok iyi',                      'Iyi'],
            ['Hiz',            '10-15 saniye',                 '5-10 saniye'],
            ['Fiyat',          '$0.04-0.12/gorsel',            '~$0.005/gorsel'],
            ['API kolayligi',  'OpenAI SDK ile kolay',         'fal.ai SDK ile kolay'],
            ['Icerik kısıtı',  'Sıkı (OpenAI politikasi)',    'Orta'],
        ],
        widths=[110, 190, 171]
    )


def bolum15_marketing(doc):
    """Bolum 15: AI ile Marketing"""

    doc.section_cover(
        15,
        'AI ile Marketing',
        'Pazarlama sureclerinizi AI ile hizlandirin',
        'Bu bolumde icerik uretimi, sosyal medya yonetimi, SEO ve reklam '
        'metni yazimi gibi marketing gorevlerinde AI araclari nasil kullanilir inceliyoruz.',
    )

    # ── 15.1 Icerik Uretimi ───────────────────────────────────
    doc.new_page('Bolum 15: AI ile Marketing')
    doc.h1('15.1  AI ile Icerik Uretimi')
    doc.sp(4)
    doc.text(
        'Icerik uretimi AI\'nin en guclu oldugu alanlarin basinda gelir. '
        'Blog yazisi, sosyal medya gonderisi, email kampanyasi, urun aciklamasi '
        've reklam metni gibi icerikleri Claude ile cok daha hizli uretebilirsiniz. '
        'Onemli olan: AI\'yi baslangic noktasi olarak kullanmak, '
        'markanizin sesini ve gorusum eklemek.'
    )

    doc.h2('Blog Yazisi Kalıbı')
    doc.code(
        '> "Sen deneyimli bir [SEKTORUNUZ] uzmanısın.\n'
        '>  Hedef kitle: [HEDEF KITLE]\n'
        '>  Konu: [KONU]\n'
        '>  Anahtar kelime: [KELIME]\n\n'
        '>  1500-2000 kelimelik bir blog yazisi yaz:\n'
        '>  - SEO dostu baslik (H1)\n'
        '>  - Meta aciklama (155 karakter)\n'
        '>  - Giris: okuyucunun problemini ele al\n'
        '>  - 4-5 alt baslik (H2) ile yapilandirilmis govde\n'
        '>  - Gercek veriler ve ornekler kullan\n'
        '>  - Eylem cagirisi (CTA)\n'
        '>  - Istatistikler icin yer tutucu ekle, sonra ben dolduracagim"',
        'Terminal'
    )

    # ── 15.2 Sosyal Medya ─────────────────────────────────────
    doc.new_page('Bolum 15: AI ile Marketing')
    doc.h1('15.2  Sosyal Medya Icerik Uretimi')
    doc.sp(4)

    doc.h2('Platform Bazli Icerik')
    doc.code(
        '> "Asagidaki blog yazisindan 5 platform icin icerik uret:\n\n'
        '>  [BLOG METNI]\n\n'
        '>  1. Twitter/X: 5 tweet (280 karakter, ilk tweet en guclü)\n'
        '>  2. LinkedIn: Uzun format (600-900 karakter, profesyonel ton)\n'
        '>  3. Instagram: Caption (150-200 karakter + hashtag listesi)\n'
        '>  4. TikTok/Reels script: 30-60 saniye konusma metni\n'
        '>  5. WhatsApp broadcast: 3-4 cumle, sıcak ton\n\n'
        '>  Her platform icin orijinal sesi koru, kopyala-yapistir yapma."',
        'Terminal'
    )

    doc.h2('30 Gunluk Icerik Plani')
    doc.code(
        '> "Bir [SEKTÖR] SaaS sirketinin Twitter icin\n'
        '>  30 gunluk icerik plani olustur.\n\n'
        '>  Icerik kategorileri:\n'
        '>  - Egitici: %40 (ipuclari, "nasil yapilir")\n'
        '>  - Sosyal kanit: %20 (musteri hikayeleri, rakamlar)\n'
        '>  - Arkasi sahne: %20 (takım, gelistirme sureci)\n'
        '>  - Etklesim: %20 (soru, anket, tartisma)\n\n'
        '>  Her gun icin: Konu + Temel mesaj + Gorunum oneris"',
        'Terminal'
    )

    # ── 15.3 SEO ──────────────────────────────────────────────
    doc.new_page('Bolum 15: AI ile Marketing')
    doc.h1('15.3  AI ile SEO Optimizasyonu')
    doc.sp(4)
    doc.text(
        'SEO (Arama Motoru Optimizasyonu), organik trafik cekmenin en surdurulebilir '
        'yoludur. AI, anahtar kelime analizi, icerik planlama ve on-page optimizasyon '
        'konularinda ciddi hizlanma saglar.'
    )

    doc.h2('Anahtar Kelime Arastirmasi')
    doc.code(
        '> "[ANA KONU] hakkinda bir SaaS sitesi icin\n'
        '>  anahtar kelime stratejisi olustur:\n\n'
        '>  1. Head terms (yüksek hacim, rekabetci)\n'
        '>  2. Long-tail keywords (dusük hacim, dusük rekabet)\n'
        '>  3. LSI keywords (anlamsal iliskili)\n'
        '>  4. Question-based keywords ("nasıl", "nedir", "neden")\n'
        '>  5. Buyer intent keywords (satın alma niyetli)\n\n'
        '>  Her kategori icin 10 ornek sun.\n'
        '>  Hangi arama niyetini (informational/commercial/transactional)\n'
        '>  hedeflediklerini belirt."',
        'Terminal'
    )

    doc.h2('On-Page SEO Denetimi')
    doc.code(
        '> "Asagidaki sayfanin on-page SEO denetimini yap:\n'
        '>  URL: [URL]\n'
        '>  Hedef kelime: [KELIME]\n\n'
        '>  Kontrol et:\n'
        '>  - Title tag (50-60 karakter, kelime iceriyor mu?)\n'
        '>  - Meta description (150-160 karakter)\n'
        '>  - H1, H2, H3 hiyerarsisi\n'
        '>  - Kelime yogunlugu ve dogal kullanim\n'
        '>  - Ic ve dis link yapisi\n'
        '>  - Gorsel alt text\'leri\n'
        '>  - Sayfa hizi onerileri\n'
        '>  - Schema markup onerileri"',
        'Terminal'
    )

    # ── 15.4 Reklam Metinleri ─────────────────────────────────
    doc.new_page('Bolum 15: AI ile Marketing')
    doc.h1('15.4  Reklam Metni ve Dönüsüm Optimizasyonu')
    doc.sp(4)

    doc.h2('Google Ads Metni')
    doc.code(
        '> "Google Ads icin [URUN/HIZMET] reklamlari yaz:\n\n'
        '>  Hedef kitle: [KITLE]\n'
        '>  USP (benzersiz deger onerisi): [USP]\n'
        '>  Anahtar kelime: [KELIME]\n\n'
        '>  Her varyant icin:\n'
        '>  - 3 farkli Baslik (max 30 karakter)\n'
        '>  - 2 farkli Aciklama (max 90 karakter)\n'
        '>  - CTA onerisI\n\n'
        '>  5 farkli yaklasim dene:\n'
        '>  fayda odakli, soru formati, rakam/istatistik,\n'
        '>  aciliyet/kıtlık, sosyal kanit"',
        'Terminal'
    )

    doc.h2('A/B Test Hipotezleri')
    doc.code(
        '> "Mevcut landing page\'im icin A/B test hipotezleri olustur:\n\n'
        '>  Mevcut baslik: [BASLIK]\n'
        '>  Mevcut CTA: [CTA]\n'
        '>  Donusum orani: %2.1\n\n'
        '>  Onerilen testler:\n'
        '>  1. Baslik varyantlari (3 farkli)\n'
        '>  2. CTA metni varyantlari (3 farkli)\n'
        '>  3. Hero gorsel alternatifleri (tanimlama)\n'
        '>  4. Sosyal kanit pozisyonu\n\n'
        '>  Her test icin: hipotez, beklenen etki, olcum metrigi"',
        'Terminal'
    )

    # ── 15.5 Email Marketing ──────────────────────────────────
    doc.new_page('Bolum 15: AI ile Marketing')
    doc.h1('15.5  Email Marketing Otomasyonu')
    doc.sp(4)

    doc.h2('Onboarding Email Serisi')
    doc.code(
        '> "SaaS urun icin 7 gunluk onboarding email serisi yaz:\n\n'
        '>  Urun: [URUN ADI - 1 cumle aciklama]\n'
        '>  Hedef: Kullanici kor ozelligi kullansin ve 1. hafta churn etmesin\n\n'
        '>  Email 1 (hemen): Hosgeldin + ilk adim\n'
        '>  Email 2 (gun 1): Kor ozellik kesfetme\n'
        '>  Email 3 (gun 3): Gelismis ipucu\n'
        '>  Email 4 (gun 5): Kullanici basarı hikayesi\n'
        '>  Email 5 (gun 7): Nerede takildiniz? (mini anket)\n\n'
        '>  Her email:\n'
        '>  - Konu satiri (3 varyant)\n'
        '>  - On izleme metni\n'
        '>  - Govde (max 200 kelime)\n'
        '>  - Tek CTA butonu"',
        'Terminal'
    )
    doc.box(
        'AI ile yazilan emailler insan sesini yitirirse etkisiz kalır. '
        'Claude\'un yazdigini bir baslangic noktasi olarak kullanin; '
        'kendi hikayenizi, spesifik rakamlarınızı ve samimi sesinizi ekleyin. '
        'Robotik hissettiren emailler spam klasorune duser.',
        'warning'
    )


def bolum16_gelecek(doc):
    """Bolum 16: Kritik Konular ve Gelecege Hazirlik"""

    doc.section_cover(
        16,
        'Kritik Konular ve Gelecege Hazirlik',
        'AI\'yi guvenli ve etik kullanin',
        'Bu bolumde AI halusinasyonlari, telif hakki, veri gizliligi, '
        'is hayatindaki degisimler ve gelecege hazirlanma konularini tartisiyoruz.',
    )

    # ── 16.1 Halusinasyon ─────────────────────────────────────
    doc.new_page('Bolum 16: Kritik Konular ve Gelecege Hazirlik')
    doc.h1('16.1  AI Halusnasyonlari ve Guven Sorunu')
    doc.sp(4)
    doc.text(
        'Halusinasyon, AI modelinin yanlis veya tamamen uydurmasi bilgiyi '
        'gercekmiş gibi sunmasidir. Bu, AI\'nin en kritik risklerinden biridir. '
        'Ozellikle hukuki, tibbi, finansal bilgilerde AI cevaplarina korkusuzca '
        'guvenilmemelidir.'
    )

    doc.h2('Halusinasyon Riski Yuksek Alanlar')
    doc.bullets([
        'Spesifik istatistikler ve rakamlar (kaynak kontrolu sart)',
        'Son dakika haberleri (bilgi kesim tarihi nedeniyle)',
        'Hukuki yorumlar (bir avukattan teyit alin)',
        'Tibbi tavsiyeler (doktor onayı sart)',
        'Kisi biyografileri ve alıntılar (dogrulayin)',
        'Kod: sentaks dogru olsa da mantık hatası olabilir (test edin)',
    ])

    doc.h2('Halusinasyonu Onlemek icin')
    doc.code(
        '# AI\'ye gercek zamanlı kaynak aramasi yaptirin:\n'
        '> "Bu bilgiyi web aramasıyla dogrula ve kaynak ver"\n\n'
        '# Belirsizligi acikca isteyin:\n'
        '> "Emin olmadigin konularda acikca belirt"\n\n'
        '# Cross-check:\n'
        '> "Bu yanitini baska bir yontemle dogrular misin?"\n\n'
        '# Ozguven kalib:\n'
        '> "Bu yanita ne kadar guveniyorsun? 1-10 arasi puan ver.\n'
        '>  Guven puanin 7\'nin altındaysa kaynak sun veya belirt."',
        'Terminal'
    )

    # ── 16.2 Telif Hakki ──────────────────────────────────────
    doc.new_page('Bolum 16: Kritik Konular ve Gelecege Hazirlik')
    doc.h1('16.2  Telif Hakki ve Fikri Mulkiyet')
    doc.sp(4)
    doc.text(
        'AI ile uretilen iceriklerin telif hakki durumu hala hukuki olarak netlesme '
        'asamasindadir. Farkli ulkelerde farkli kararlar cikiyor. '
        'Pratik olarak dikkat etmeniz gereken 3 ana alan vardir.'
    )

    doc.h2('Dikkat Edilmesi Gerekenler')
    doc.bullets([
        'AI egitim verileri: Kullanilanlar AI telif davalarına konu oluyor (Adobe, Getty)',
        'Uretilen gorsel: Belirli sanatcilarin tarzi istenmemeli, fark edilebilir tur sart',
        'Kod: Github Copilot telif davasi devam ediyor; kritik uretim kodunu gozden gecirin',
        'Metin: AI ile yazılan icerik ticari telif gerektirmez (cogu ulkede) ama kaynagi belirtin',
        'Muzik: AI muzik aracları (Suno, Udio) lisanslama modelleri hala gelisiyor',
    ])
    doc.box(
        'En guvenli yaklasim: AI\'yi arastırma ve taslak icin kullanin, '
        'kritik urun kararlari icin bir hukuk danismanindan görüs alin. '
        'Teknoloji hızla ilerliyor, yasalar gecikmeyle takip ediyor.',
        'warning'
    )

    # ── 16.3 Veri Gizliligi ───────────────────────────────────
    doc.new_page('Bolum 16: Kritik Konular ve Gelecege Hazirlik')
    doc.h1('16.3  Veri Gizliligi ve GDPR/KVKK')
    doc.sp(4)
    doc.text(
        'AI araclarina gonderdiginiz veriler servis saglayicinin politikasina gore '
        'islenir. Ozellikle kurumsal kullanim, musteri verileri veya kisisel bilgiler '
        'iceren promptlar konusunda dikkatli olunmalıdir.'
    )

    doc.h2('Riskli Durumlar')
    doc.bullets([
        'Musteri verilerini (isim, email, TC) AI\'a kopyalayip yapistirmak',
        'Sirket ici gizli bilgileri (finansal raporlar, strateji) prompt\'a eklemek',
        'Kaynak kodu - ozellikle kapali kaynak projeler API üzerinden gondermek',
        'Saglik verileri (hasta bilgisi, teshis) AI\'ya isletmek',
    ])

    doc.h2('Guvenli Kullanim Onerileri')
    doc.bullets([
        'Anthropic API: Varsayilan olarak egitimde kullanilmaz (kurumsal endpoint)',
        'Veri anonimizasyonu: Gercek isimleri ve ID\'leri degistirerek gonderin',
        'On-premise: Gizli veri icin lokal LLM (Ollama + Llama/Mistral) kullanin',
        'Privacy mode: ChatGPT ve Claude Web icin "gizmiod" veya sohbet gecmisini kapatin',
        'GDPR uyumlulugu: Musteri verisi iceren AI ciktilarının ne kadar sure saklanacagini belgeleyin',
    ])

    # ── 16.4 Is Hayatindaki Degisimler ────────────────────────
    doc.new_page('Bolum 16: Kritik Konular ve Gelecege Hazirlik')
    doc.h1('16.4  Is Hayatindaki Degisimler')
    doc.sp(4)
    doc.text(
        'AI, bazi meslekleri dogrudan etkilerken yeni meslekler ve roller de '
        'ortaya cikmaktadir. En onemli beceri ise AI araclariyla verimli calisma '
        've AI\'nin yapamadigi insani becerileri gelistirme olacak.'
    )

    doc.h2('Etkilenen ve Donen Meslekler')
    doc.table(
        ['Meslek',              'Etki',     'Aciklama'],
        [
            ['Junior gelistirici',  'Yüksek',   'Rutin kod uretimi AI\'ye gecebilir'],
            ['Icerik yazari',       'Orta',     'AI taslak + insan ozgünlugu'],
            ['Grafik tasarimci',    'Orta',     'AI gorsel + insan marka yonü'],
            ['Veri girişi',         'Cok yüksek','Rutin veri isleme otomatiklesecek'],
            ['Musteri hizmetleri',  'Yüksek',  'Temel sorular AI chatbot ile'],
            ['Prompt mühendisi',    'Yeni rol', 'AI sistemlerini yonlendirme uzmani'],
            ['AI eğitmeni',         'Yeni rol', 'Sirketlere AI kullanim egitimi'],
            ['AI denetcisi',        'Yeni rol', 'AI sistemlerinin etik/guvenlik denetimi'],
        ],
        widths=[130, 80, 261]
    )

    doc.h2('Hayatta Kalma Stratejisi')
    doc.bullets([
        'AI ile calismayi ogren: AI rakibiniz degil aracınız olsun',
        'Uzmanlasi: Derinlik AI\'nin yuzeyselligini aser',
        'Insan becerileri: Empati, liderlik, musteri iliskisi AI\'nin zayif oldugu alanlar',
        'Surekli ogrenme: Bu alan ayda degisiyor, guncel kalin',
        'Yazi kabiliyeti: Iyi prompt yazmak = iyi dusunmek',
    ])

    # ── 16.5 Gelecege Bakis ───────────────────────────────────
    doc.new_page('Bolum 16: Kritik Konular ve Gelecege Hazirlik')
    doc.h1('16.5  Gelecege Bakis: 2026-2030')
    doc.sp(4)

    doc.h2('Yakin Vadede Beklenenler')
    doc.bullets([
        'Agent sistemleri: AI\'nin bagimsiz uzun vadeli gorevleri tamamlamasi yaygınlasacak',
        'Multimodal modeller: Ses, gorsel, video, kod anlayan tek modeller norm olacak',
        'Fiziksel AI: Robot sistemleri ve akinli cihazlar AI ile entegre olacak',
        'Kisisel AI: Her kullanicinin kisisellestirilmis, hafizali AI asistani',
        'AI kodlama: Buyük kod tabanlarını bagimsiz gelistirebilen AI sistemleri',
    ])

    doc.h2('Uzun Vadede')
    doc.text(
        'AGI (Artificial General Intelligence — Genel Yapay Zeka) tartişmaları '
        'devam etmektedir. Sam Altman ve Dario Amodei gibi isimler yaklastigini '
        'soylüyor; pek cok bilim insani cok daha uzak bir hedef oldugunu savunuyor. '
        'Hangi senaryo gerceklesirse gerceklessin, AI araclariyla erken tanisan ve '
        'kullanan kisiler rekabet avantajini koruyacak.'
    )
    doc.box(
        'Bu kitapta ogrendiginiz en onemli sey bir arac degil bir yaklasimdir: '
        'AI\'yi anlamak, dogru sormak ve ciktıyi elestirerek degerlendirmek. '
        'Araçlar degisecek, bu beceri kalici.',
        'tip'
    )


def kapanis(doc):
    """Kapanis ve Kaynaklar"""

    # ── Kapanis ───────────────────────────────────────────────
    doc.new_page('Kapanis')

    doc._fill(*NAVY)
    doc._rect(0, 0, 595.28, 841.89, 'f')

    doc._fill(*ORANGE)
    doc._rect(62, 740, 471.28, 4, 'f')

    doc._fill(*WHITE)
    baslik = 'Burada Yolculuk Bitiyor'
    from pdf_engine import PW
    bw = doc.f['bold'].measure(baslik, 28)
    doc._txy(baslik, 'bold', 28, (PW - bw) / 2, 680)

    alt = 'Gercek yolculuk ise simdi basliyor.'
    aw = doc.f['reg'].measure(alt, 15)
    doc._txy(alt, 'reg', 15, (PW - aw) / 2, 645)

    lines = [
        'Bu kitabi okudunuz. Simdi yapmaniz gereken tek sey:',
        'claude.ai\'yi acin, bir fikrinizi yazin, enter\'a basin.',
        '',
        'Ilk proje mükemmel olmayacak. Olmasina gerek yok.',
        'Her prompt ile daha iyi olacaksiniz.',
        'Her proje ile daha hızlı yapacaksiniz.',
        '',
        'Yapay zeka bir gün bir insanin yapabilecegi her seyi yapabilir',
        'mi? Belki. Ama bu gün degil.',
        '',
        'Bugun yapay zekayı kullananlar, kullanmayanlarin',
        'onunde olacak. Siz artik kullanacaksiniz.',
    ]

    y = 600
    for line in lines:
        if line:
            lw = doc.f['reg'].measure(line, 11)
            doc._fill(*WHITE)
            doc._txy(line, 'reg', 11, (PW - lw) / 2, y)
        y -= 18

    doc._fill(*ORANGE)
    imza = 'Aykut Uces | x.com/aykutuces'
    iw = doc.f['bold'].measure(imza, 13)
    doc._txy(imza, 'bold', 13, (PW - iw) / 2, 390)

    # ── Kaynaklar ─────────────────────────────────────────────
    doc.new_page('Kaynaklar ve Faydali Linkler')
    doc.h1('Kaynaklar ve Faydali Linkler')
    doc.sp(4)

    doc.h2('Resmi Dokumanlar')
    doc.bullets([
        'Claude dokumanlar: docs.anthropic.com',
        'Claude Code: docs.anthropic.com/claude-code',
        'OpenAI API: platform.openai.com/docs',
        'fal.ai dokumanlar: fal.ai/docs',
        'RevenueCat: docs.revenuecat.com',
        'Stripe dokumanlar: stripe.com/docs',
        'Supabase dokumanlar: supabase.com/docs',
        'Expo/React Native: docs.expo.dev',
    ])

    doc.h2('Tavsiye Edilen Kaynaklar')
    doc.bullets([
        'Hacker News (news.ycombinator.com) — AI/tech haberleri',
        'Latent Space Podcast — AI arastirma derinlemesi',
        'Lenny\'s Newsletter — SaaS ve product gelistirme',
        'IndieHackers.com — Bagimsiz gelistiricilerin toplulugu',
        'ProductHunt.com — Yeni AI araclari kesfetme',
        'GitHub Trending — Gunluk populer repolar',
        'x.com/aykutuces — Bu kitabin yazarinin AI guncellemeleri',
    ])

    doc.h2('Bu Kitabin Yazari')
    doc.text(
        'Aykut Uces, girisimci ve yazılım gelistiricidir. fal.ai uzerine insa edilmis '
        'EticPanel.com\'un kurucusudur. Yapay zeka araclari, SaaS gelistirme '
        've bağımsız urun gelistirme konularinda icerik uretmektedir.'
    )
    doc.bullets([
        'Twitter/X: @aykutuces',
        'Web: eticpanel.com',
    ])
    doc.sp(8)

    doc._fill(*NAVY)
    doc._rect(62, doc._y - 10, 471.28, 1.5, 'f')
    doc._y -= 20

    son = 'Yapay Zeka Ogreniyorum — v1.0 | Mayis 2026'
    from pdf_engine import PW
    sw = doc.f['reg'].measure(son, 10)
    doc._fill(*GRAY_DARK)
    doc._txy(son, 'reg', 10, (PW - sw) / 2, doc._y)


def main():
    doc = Doc()
    print("Icerik olusturuluyor — Sayfa 134-190...")

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
    bolum13_prompt(doc)
    bolum14_openai(doc)
    bolum15_marketing(doc)
    bolum16_gelecek(doc)
    kapanis(doc)

    pages = doc.save('yapay_zeka_ogreniyorum_tam.pdf')
    print(f"\nTamamlandi! Toplam {pages} sayfa uretildi.")
    print("Dosya: yapay_zeka_ogreniyorum_tam.pdf")


if __name__ == '__main__':
    main()
