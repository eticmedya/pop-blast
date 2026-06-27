#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Claude Code ile Mobil Uygulama Rehberi — Part 1
Kapak + Icindekiler + Giris + Google Play hesabi + Apple Developer hesabi
"""
from mobile_pdf_engine import Doc, PW, PH, ML, MR, MT, MB, CW, HDR_H
from mobile_pdf_engine import NAVY, ORANGE, WHITE, BLACK, GRAY_BG, GRAY_DARK, NAVY_LIGHT


def kapak_sayfasi(doc):
    """Kapak sayfasi"""
    doc.new_page('Claude Code ile Mobil Uygulama Gelistirme Rehberi')

    doc._fill(*NAVY)
    doc._rect(0, 0, PW, PH, 'f')

    doc._fill(*ORANGE)
    doc._rect(0, PH-6, PW, 6, 'f')

    doc._fill(*WHITE)
    doc._rect(ML-10, PH*0.36, CW+20, PH*0.50, 'f')

    doc._fill(*ORANGE)
    doc._rect(ML-10, PH*0.36, 6, PH*0.50, 'f')

    baslik1 = "CLAUDE CODE ILE"
    baslik2 = "MOBIL UYGULAMA"
    baslik3 = "GELISTIRME REHBERI"
    doc._fill(*NAVY)
    b1w = doc.f['bold'].measure(baslik1, 30)
    doc._txy(baslik1, 'bold', 30, (PW - b1w)/2, PH*0.80)
    b2w = doc.f['bold'].measure(baslik2, 30)
    doc._fill(*ORANGE)
    doc._txy(baslik2, 'bold', 30, (PW - b2w)/2, PH*0.80 - 38)
    b3w = doc.f['bold'].measure(baslik3, 30)
    doc._fill(*NAVY)
    doc._txy(baslik3, 'bold', 30, (PW - b3w)/2, PH*0.80 - 76)

    alt = "Sifirdan App Store'a: Android + iOS + Backend + Tasarim + Para Kazanma"
    doc._fill(*NAVY_LIGHT)
    aw = doc.f['reg'].measure(alt, 11.5)
    doc._txy(alt, 'reg', 11.5, (PW-aw)/2, PH*0.80 - 100)

    doc._stroke(*ORANGE)
    doc._lw(1.5)
    doc._line(ML+20, PH*0.80-114, PW-MR-20, PH*0.80-114)

    doc._fill(*NAVY)
    doc._rect(ML, PH*0.36+14, CW, 78, 'f')
    doc._fill(*ORANGE)
    doc._rect(ML, PH*0.36+14, 5, 78, 'f')
    doc._fill(*WHITE)
    doc._txy("Hazirlayan:", 'bold', 10, ML+14, PH*0.36+74)
    doc._fill(0.9, 0.9, 0.9)
    doc._txy("Aykut Uces  |  @aykutuces  |  EticMedya  |  vibecodingex.com",
             'bold', 11, ML+14, PH*0.36+56)
    doc._fill(0.75, 0.75, 0.8)
    doc._txy("React Native, Expo, Google Play, App Store, AdMob, Adapty,",
             'reg', 9, ML+14, PH*0.36+38)
    doc._txy("RevenueCat ve backend tasarimini iceren tam kapsamli rehber.",
             'reg', 9, ML+14, PH*0.36+26)

    doc._fill(*ORANGE)
    doc._rect(PW-MR-60, MB+30, 55, 24, 'f')
    doc._fill(*WHITE)
    yilw = doc.f['bold'].measure('2026', 14)
    doc._txy('2026', 'bold', 14, PW-MR-60+(55-yilw)/2, MB+40)

    doc._fill(*ORANGE)
    doc._rect(0, MB+8, PW, 4, 'f')


def icindekiler(doc):
    """Icindekiler"""
    doc.new_page('Icindekiler')

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
        ('Bolum 1', 'Giris: Claude Code ile Mobil Gelistirme',     '4'),
        ('Bolum 2', 'Google Play Console Hesabi Acma (TR 2026)',  '8'),
        ('Bolum 3', 'Apple Developer Program Hesabi Acma (TR 2026)','14'),
        ('Bolum 4', 'Windows\'ta Mobil Gelistirme Ortami Kurulumu','20'),
        ('Bolum 5', 'Mac\'te Mobil Gelistirme Ortami Kurulumu',    '26'),
        ('Bolum 6', 'React Native ve Expo Derinlemesine',          '32'),
        ('Bolum 7', 'Claude Code ile Sifirdan Mobil Uygulama',     '40'),
        ('Bolum 8', 'Backend Tasarimi',                            '54'),
        ('Bolum 9', 'UI/UX Tasarim Surec',                         '62'),
        ('Bolum 10','Fikir Bulma ve Pazar Arastirmasi (TrustMRR)','70'),
        ('Bolum 11','AdMob ile Reklam Geliri',                     '76'),
        ('Bolum 12','Adapty ile Abonelik Sistemi',                 '84'),
        ('Bolum 13','RevenueCat ile Abonelik Sistemi',              '90'),
        ('',        'Kapanis ve Kaynaklar',                        '96'),
    ]

    for bno, ad, sayfa in bolumler:
        is_main = bno != ''
        fk = 'bold' if is_main else 'reg'
        sz = 11 if is_main else 10
        color = NAVY if is_main else GRAY_DARK
        lh = 22 if is_main else 14

        doc._need(lh + 2)

        if is_main:
            doc._fill(*ORANGE)
            doc._rect(ML, doc._y - lh + 8, CW, 1, 'f')
            doc._y -= 6

        doc._fill(*color)
        doc._txy(f'{bno}  {ad}' if bno else ad, fk, sz, ML + (0 if is_main else 10), doc._y)

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
        "Bu rehber, hic kod yazmamis birinin Claude Code yardimiyla App Store ve "
        "Google Play'de yayinlanabilir bir mobil uygulama yapmasini hedefler. "
        "Adimlari sirayla takip edin.",
        'info'
    )


def bolum1_giris(doc):
    """Bolum 1: Giris"""

    doc.section_cover(
        1,
        'Giris: Claude Code ile Mobil Gelistirme',
        'Kod bilmeden mobil uygulama yapmak artik gercek',
        'Bu bolumde Claude Code\'un mobil gelistirmede nasil kullanildigini, '
        'bu rehberin nasil ilerleyecegini ve ihtiyaciniz olan zihniyeti aciklıyoruz.',
    )

    doc.new_page('Bolum 1: Giris')
    doc.h1('1.1  Bu Rehber Kime Hitap Ediyor?')
    doc.sp(4)
    doc.text(
        'Bu rehber, daha once hic kod yazmamis ama bir mobil uygulama fikri olan '
        'herkese; ayrica temel programlama bilgisi olup hizla App Store ve Google '
        'Play\'e gercek bir urun cikarmak isteyen gelistiricilere yoneliktir. '
        'Claude Code, terminal uzerinden calisan yapay zeka destekli bir kodlama '
        'asistanidir ve dogal dilde verdiginiz talimatlari gercek, calisan koda '
        'cevirir.'
    )
    doc.box(
        'Onceki bilgi seviyeniz onemli degil. Bu rehberi adim adim takip ederseniz '
        'sonunda gercek bir React Native uygulamaniz, calisan bir backend\'iniz ve '
        'gelir modeliniz (reklam veya abonelik) olacak.',
        'tip'
    )

    doc.h2('Neden Mobil Uygulama Icin Claude Code?')
    doc.bullets([
        'Claude Code, dosya yapisi olusturma, paket kurulumu, kod yazma ve hata '
        'duzeltmenin hepsini sizin yerinize otomatik yapar',
        'Terminal komutu bilmiyor olsaniz da Claude\'a Turkce talimat vererek '
        'her seyi yapabilirsiniz',
        'Hatalari kendisi analiz eder ve duzeltir — "Bu hatayi coz" demeniz yeterli',
        'Bir defada tum bir ekrani, bir API\'yi veya bir entegrasyonu yazabilir',
        'Kod kalitesi insan gelistiricisi seviyesinde veya daha tutarli olabilir',
    ])

    doc.new_page('Bolum 1: Giris')
    doc.h1('1.2  Bu Rehberin Yol Haritasi')
    doc.sp(4)
    doc.text(
        'Bu rehber, gercek bir uygulamayi yayinlama surecini takip eden mantikli '
        'bir sirada ilerler. Once magaza hesaplarinizi acacaksiniz (suresi uzun '
        'surebilir, bu yuzden en basta), ardindan gelistirme ortaminizi kuracak, '
        'sonra Claude Code ile uygulamanizi yazacak, son olarak para kazanma '
        'sistemlerini entegre edeceksiniz.'
    )

    doc.h2('Adim Adim Yol Haritasi')
    doc.table(
        ['Adim',  'Ne Yapilacak?',                          'Tahmini Sure'],
        [
            ['1',     'Google Play + Apple Developer hesabi acma', '1-3 gun (onay icin)'],
            ['2',     'Gelistirme ortami kurulumu (Node, Expo)',    '1-2 saat'],
            ['3',     'React Native + Expo proje olusturma',        '30 dakika'],
            ['4',     'Claude Code ile uygulama gelistirme',        '1-3 hafta (urune gore)'],
            ['5',     'Backend kurulumu (Supabase)',                '1-2 gun'],
            ['6',     'Tasarim ve UI cilalama',                     '2-5 gun'],
            ['7',     'Reklam/abonelik entegrasyonu',                '1-2 gun'],
            ['8',     'Magaza yayinlama ve inceleme',                '1-7 gun (Apple icin daha uzun)'],
        ],
        widths=[40, 260, 171]
    )
    doc.sp(6)
    doc.box(
        'Google Play ve Apple Developer hesap basvurularini EN BASTA yapin. '
        'Apple incelemesi bazen 24-48 saat surer, kimlik dogrulama gerekirse '
        'gunler alabilir. Bu sureyi bekleme suresi olarak kodlama sirasinda '
        'kullanabilirsiniz.',
        'warning'
    )

    doc.new_page('Bolum 1: Giris')
    doc.h1('1.3  Claude Code Kurulumu (Hizli Hatirlatma)')
    doc.sp(4)
    doc.text(
        'Claude Code\'u zaten kurmadıysanız asagidaki adimlari takip edin. '
        'Detaylı kurulum rehberi icin ana "Yapay Zeka Ogreniyorum" kitabinin '
        '4. bolumune bakabilirsiniz; burada hizli bir ozet veriyoruz.'
    )
    doc.code(
        '# 1. Node.js LTS surumunu kurun (nodejs.org)\n'
        '# 2. Terminal/PowerShell acin ve dogrulayin:\n'
        'node --version\n'
        'npm --version\n\n'
        '# 3. Claude Code\'u global kurun:\n'
        'npm install -g @anthropic-ai/claude-code\n\n'
        '# 4. Dogrulayin:\n'
        'claude --version\n\n'
        '# 5. Proje klasorunuzde Claude Code\'u baslatin:\n'
        'cd benim-mobil-uygulamam\n'
        'claude',
        'Terminal'
    )
    doc.box(
        'Claude Code\'u her zaman proje klasorunuzun icinde baslatin. '
        'Boyle calistirdiginizda Claude, o klasordeki dosyalari okuyup '
        'duzenleyebilir.',
        'info'
    )


def bolum2_google_play_hesabi(doc):
    """Bolum 2: Google Play Console Hesabi Acma (TR 2026)"""

    doc.section_cover(
        2,
        'Google Play Console Hesabi Acma (TR 2026)',
        'Android uygulamanizi yayinlamak icin ilk adim',
        'Bu bolumde Turkiye\'den 2026 itibariyle Google Play Console geliştirici '
        'hesabi nasil acilir, hangi belgeler gerekir ve vergi durumunuz ne olur '
        'detayli olarak inceliyoruz.',
    )

    # ── 2.1 Hesap Turu Secimi ──────────────────────────────────
    doc.new_page('Bolum 2: Google Play Console Hesabi Acma')
    doc.h1('2.1  Bireysel mi Kurumsal mi?')
    doc.sp(4)
    doc.text(
        'Google Play Console\'da hesap acarken iki secenekle karsilasirsiniz: '
        'Kisisel (Personal) hesap veya Kurumsal (Organization) hesap. '
        'Bu secim SONRADAN DEGISTIRILEMEZ, dikkatli secin.'
    )

    doc.h2('Kisisel vs Kurumsal Karsilastirmasi')
    doc.table(
        ['Kriter',          'Kisisel Hesap',                  'Kurumsal Hesap'],
        [
            ['Kimler icin',     'Bireysel gelistirici, hobi',     'Sirket, marka, ekip'],
            ['Gereken belge',   'TC kimlik / pasaport',           'D-U-N-S numarasi + sirket belgeleri'],
            ['Gelistirici adi', 'Google odeme profilinizdeki ad', 'Sirket adi'],
            ['Hesap degisimi',  'Sonradan kurumsala gecemez',     'Sonradan bireysele gecemez'],
            ['Onerilen',        'Ilk uygulamaniz icin',           'Sirketiniz varsa veya buyuyecekse'],
        ],
        widths=[100, 180, 191]
    )
    doc.sp(6)
    doc.box(
        'Ilk uygulamanizi yayinliyorsaniz ve henuz bir sirketiniz yoksa Kisisel '
        'hesapla baslayin. Ileride sirket kurarsaniz yeni bir Kurumsal hesap '
        'acabilirsiniz; eski hesabinizi kapatmaniza gerek yok.',
        'tip'
    )

    # ── 2.2 Kayit Adimlari ─────────────────────────────────────
    doc.new_page('Bolum 2: Google Play Console Hesabi Acma')
    doc.h1('2.2  Adim Adim Kayit Sureci')
    doc.sp(4)
    doc.bullets([
        '1. play.google.com/console adresine gidin',
        '2. Mevcut bir Google hesabiyla giris yapin (veya yeni olusturun)',
        '3. "Hesap olustur" butonuna tiklayin',
        '4. Hesap turunu secin: Kisisel veya Kurumsal',
        '5. Gelistirici adinizi girin (kullanicilarin magazada gorecegi isim)',
        '6. Iletisim bilgilerinizi (email, telefon) girin',
        '7. Google Play Geliştirici Dagitim Sozlesmesi\'ni okuyup onaylayin',
        '8. Tek seferlik 25 USD kayit ucretini odeyin (kredi/banka karti)',
        '9. Kimlik dogrulama surecini tamamlayin (Turkiye icin asagida detay var)',
        '10. Odeme profilinizi olusturun (gelir almak icin banka hesabi gerekir)',
    ])
    doc.box(
        'Kayit ucreti tek seferliktir, abonelik degildir. Onceden yuklemeli '
        'kartlar (prepaid) kabul edilmez; gercek bir kredi veya banka karti '
        'kullanmaniz gerekir.',
        'warning'
    )

    doc.h2('Gerekli Belgeler (Turkiye)')
    doc.bullets([
        'Kisisel hesap icin: T.C. kimlik karti veya pasaport (kimlik dogrulama '
        'istenirse)',
        'Kurumsal hesap icin: D-U-N-S numarasi, ticaret sicil gazetesi, '
        'vergi levhasi',
        'Gecerli bir kredi/banka karti (kayit ucreti icin)',
        'Banka hesabi (IBAN) — kazanc odemeleri icin gerekli',
    ])

    # ── 2.3 Kimlik Dogrulama ───────────────────────────────────
    doc.new_page('Bolum 2: Google Play Console Hesabi Acma')
    doc.h1('2.3  Google Play Geliştirici Kimlik Dogrulamasi')
    doc.sp(4)
    doc.text(
        'Google, sahte hesaplari ve dolandiriciligi engellemek icin tum '
        'gelistiricilerden kimlik dogrulamasi istemektedir. Bu surec hesap '
        'turunuza gore degisir.'
    )
    doc.bullets([
        'Kisisel hesap: Kimlik belgesi fotografi + selfie dogrulamasi '
        'istenebilir',
        'Kurumsal hesap: D-U-N-S numarasi + yetkili kisi dogrulamasi '
        'istenir',
        'Dogrulama suresi: Genellikle 1-3 is gunu, bazen daha uzun surebilir',
        'Play Console Yardim sayfasinda Turkiye icin gerekli belgeler '
        'ayrintili listelenmistir',
    ])
    doc.box(
        'D-U-N-S numarasi almak ucretsizdir ama 5 is gunune kadar surebilir. '
        'Kurumsal hesap acacaksaniz bu numarayi en basta, hesap acmadan once '
        'talep edin ki sureci uzatmayin.',
        'info'
    )

    # ── 2.4 Vergi ve Odeme Profili ─────────────────────────────
    doc.new_page('Bolum 2: Google Play Console Hesabi Acma')
    doc.h1('2.4  Turkiye\'de Vergi Durumu (2026)')
    doc.sp(4)
    doc.text(
        'Türkiye\'de mobil uygulama gelistiricileri icin 2026 yili itibariyle '
        'avantajli bir vergi rejimi bulunmaktadir. Bu konuda kesin karar icin '
        'bir mali musavire danismaniz onerilir, ancak genel cati su sekildedir:'
    )

    doc.h2('Ozel Banka Hesabi Yontemi')
    doc.bullets([
        '2026 yilinda yillik tahmini 7 milyon TL\'ye kadar olan App Store / '
        'Google Play gelirlerinde vergi avantaji mevcuttur',
        'Banka, hesabiniza giren paradan otomatik kesinti yapar ve devlete '
        'aktarir',
        'Bu sistemde ayrica KDV beyannamesi vermeniz gerekmez',
        'Sistemden yararlanmak icin bankanizla "genc girisimci" veya "mobil '
        'uygulama gelistirici" istisnasi hakkinda gorusun',
    ])

    doc.h2('Sosyal Guvenlik (Bağ-Kur)')
    doc.bullets([
        'Baska bir isyerinde SSK\'li (4A) calismiyorsaniz, mobil uygulama '
        'geliriniz nedeniyle Bağ-Kur\'a (4B) kayit zorunlulugu dogabilir',
        '2026 yilinda en dusuk Bağ-Kur primi aylik yaklasik 9.000-10.000 TL '
        'bandinda olmasi beklenmektedir',
        'Bu konuda guncel rakamlar icin SGK veya bir mali musavire basvurun',
    ])
    doc.box(
        'Vergi mevzuati her yil degisebilir. Bu bolumdeki bilgiler genel '
        'bilgilendirme amaclidir ve hukuki/mali tavsiye niteligi tasimaz. '
        'Gercek gelir elde etmeye basladiginizda bir mali musavirle calismaniz '
        'siddetle onerilir.',
        'warning'
    )

    doc.h2('Odeme Profili Kurulumu')
    doc.code(
        '# Play Console\'da odeme profili olusturma:\n'
        '# 1. Play Console > Ayarlar > Odeme profilleri\n'
        '# 2. "Profil ekle" tiklayin\n'
        '# 3. Hesap turunuza uygun bilgileri girin\n'
        '#    (Kisisel: TC kimlik bilgileri / Kurumsal: sirket bilgileri)\n'
        '# 4. Banka hesap bilgilerinizi (IBAN) ekleyin\n'
        '# 5. Vergi formu doldurun (W-8BEN benzeri uluslararasi form)\n'
        '# 6. Onay icin 1-2 is gunu bekleyin',
        'Terminal'
    )

    # ── 2.5 Magaza Listesi Hazirligi ───────────────────────────
    doc.new_page('Bolum 2: Google Play Console Hesabi Acma')
    doc.h1('2.5  Uygulama Olusturma ve Ilk Ayarlar')
    doc.sp(4)
    doc.bullets([
        'Play Console ana ekraninda "Uygulama olustur" tiklayin',
        'Uygulama adini girin (sonradan degistirilebilir)',
        'Varsayilan dil ve uygulama/oyun secimini yapin',
        'Ucretsiz mi ucretli mi oldugunu secin (ucretli secim sonradan '
        'ucretsize cevrilemez, ama ucretsiz her zaman ucretliye cevrilebilir)',
        'Gelistirici Dagitim Sozlesmesi onayini verin',
    ])

    doc.h2('Ilk Surum Yayinlamadan Once Gerekenler')
    doc.bullets([
        'Gizlilik politikasi URL\'si (zorunlu — basit bir sayfa yeterli)',
        'Uygulama simgesi (512x512 px PNG)',
        'Ekran goruntuleri (en az 2, telefon icin)',
        'Ozellik grafigi (1024x500 px banner)',
        'Kisa aciklama (80 karakter) ve tam aciklama (4000 karaktere kadar)',
        'Icerik derecelendirmesi anketi (IARC)',
        'Hedef kitle ve icerik beyani',
        'Veri guvenligi formu (hangi verileri topluyorsunuz?)',
    ])
    doc.box(
        'Claude Code\'a "Bu uygulama icin Google Play gizlilik politikasi '
        'sayfasi yaz ve basit bir HTML sayfasi olarak kaydet" diyebilirsiniz. '
        'Claude, uygulamanizin topladigi verilere uygun bir taslak hazirlar.',
        'tip'
    )


def bolum3_apple_developer_hesabi(doc):
    """Bolum 3: Apple Developer Program Hesabi Acma (TR 2026)"""

    doc.section_cover(
        3,
        'Apple Developer Program Hesabi Acma (TR 2026)',
        'iOS uygulamanizi App Store\'a cikarmak icin sart',
        'Bu bolumde Turkiye\'den Apple Developer Program\'a nasil kayit '
        'olunacagini, odeme zorluklarini nasil cozeceğinizi ve 2026 itibariyle '
        'gecerli sureci detaylı olarak inceliyoruz.',
    )

    # ── 3.1 Genel Bilgi ────────────────────────────────────────
    doc.new_page('Bolum 3: Apple Developer Program Hesabi Acma')
    doc.h1('3.1  Apple Developer Program Nedir?')
    doc.sp(4)
    doc.text(
        'Apple Developer Program, App Store\'da uygulama yayinlamak, TestFlight '
        'ile beta test yapmak ve gercek cihazda test etmek icin gereken yillik '
        'uyeliktir. 2026 itibariyle ucreti yillik 99 USD\'dir (bolgeye gore yerel '
        'para birimiyle tahsil edilebilir).'
    )

    doc.h2('Bireysel vs Kurum Hesabi')
    doc.table(
        ['Kriter',          'Bireysel (Individual)',          'Kurum (Organization)'],
        [
            ['Kimler icin',     'Tek kisi gelistirici',           'Sirket, resmi tuzel kisilik'],
            ['Gereken belge',   'TC kimlik numarasi',             'D-U-N-S numarasi + ticari belgeler'],
            ['Gorunen isim',    'Sizin adiniz',                    'Sirket adi'],
            ['Takim uyesi',     'Sinirli yetki paylasimi',         'Roller ile tam takim yonetimi'],
            ['Onerilen',        'Ilk uygulamaniz icin',            'Sirketiniz varsa'],
        ],
        widths=[100, 195, 176]
    )

    # ── 3.2 Odeme Zorluklari ve Cozumleri ──────────────────────
    doc.new_page('Bolum 3: Apple Developer Program Hesabi Acma')
    doc.h1('3.2  Turkiye\'den Odeme Yapma (En Sik Sorun)')
    doc.sp(4)
    doc.text(
        'Turkiye\'den Apple Developer kaydi yaparken en cok karsilasilan sorun '
        'odeme asamasidir. Apple bazi Turk banka kartlarini kabul etmeyebilir '
        've uluslararasi gecerlilige sahip bir kart istenir.'
    )

    doc.h2('Onerilen Odeme Yontemleri')
    doc.bullets([
        'Wise (eski TransferWise) sanal karti — coğu Avrupa/ABD sitesinde '
        'sorunsuz calisir',
        'Revolut sanal karti — anlik olusturulabilir, USD/EUR bakiye '
        'tutabilirsiniz',
        'Payoneer kartı — özellikle serbest calisanlar arasinda yaygin',
        'Turk bankalarinin bazi "sanal kart" urunleri (bankaya gore degisir, '
        'once test edin)',
    ])
    doc.box(
        'Odeme yaparken kullandiginiz kart, Apple Developer hesabindaki isimle '
        'AYNI kisiye ait olmalidir. Farkli bir kart kullanirsaniz Apple '
        'kayitinizi gecikmeye ugratip kimlik fotografi talep edebilir.',
        'warning'
    )

    # ── 3.3 Bireysel Kayit Adimlari ─────────────────────────────
    doc.new_page('Bolum 3: Apple Developer Program Hesabi Acma')
    doc.h1('3.3  Bireysel Hesap — Adim Adim')
    doc.sp(4)
    doc.bullets([
        '1. developer.apple.com/programs/enroll adresine gidin',
        '2. Mevcut bir Apple ID ile giris yapin (yoksa appleid.apple.com\'da '
        'olusturun)',
        '3. Iki faktorlu dogrulamayi (2FA) aktif edin — zorunludur',
        '4. "Enroll" / "Kaydol" butonuna tiklayin',
        '5. Hesap turu olarak "Individual" (Bireysel) secin',
        '6. Vergi mukimi ulke olarak Turkiye\'yi secin',
        '7. T.C. kimlik numaranizi girin (vergi kesintisi dogru yapilsin '
        'diye)',
        '8. Yasal adinizi ve adresinizi kimlikteki gibi tam girin',
        '9. Sozlesmeleri okuyup onaylayin',
        '10. 99 USD odemeyi uluslararasi gecerli kartla yapin',
        '11. Onay emaili bekleyin (genellikle 24 saat icinde gelir, bazen '
        'kimlik fotografi istenebilir)',
    ])

    # ── 3.4 Kurum Kaydi ─────────────────────────────────────────
    doc.new_page('Bolum 3: Apple Developer Program Hesabi Acma')
    doc.h1('3.4  Kurum Hesabi — D-U-N-S Numarasi Sureci')
    doc.sp(4)
    doc.text(
        'Eger sirketiniz adina kayit yapacaksaniz, Apple sizden bir D-U-N-S '
        'numarasi ister. Bu, Dun & Bradstreet tarafindan verilen, sirketinizin '
        'kimligini dogrulayan 9 haneli benzersiz bir numaradir.'
    )
    doc.bullets([
        '1. apps.dnb.com/duns sayfasindan D-U-N-S numarasi basvurusu yapin',
        '2. Sirketinizin ticaret sicil belgelerini, vergi levhasini hazirlayin',
        '3. Basvuru ucretsizdir; onay 5 is gunune kadar surebilir',
        '4. D-U-N-S numarasini aldiktan sonra Apple Developer kaydina baslayin',
        '5. Sirketinizin Apple ile sozlesme imzalama yetkisi olan tuzel kisilik '
        'olmasi sarttir (sahis sirketi degil, gercek anlamda tuzel kisilik)',
        '6. Apple, DBA (farkli ticari isim), marka adi veya sube basvurularini '
        'kabul etmez — resmi sirket adi kullanilmalidir',
    ])
    doc.box(
        'D-U-N-S numarasi almak zaman aldigi icin, eger sirketiniz varsa bu '
        'sureci EN BASTA, uygulama gelistirmeye baslamadan once tamamlayin.',
        'tip'
    )

    # ── 3.5 Onay Sonrasi ────────────────────────────────────────
    doc.new_page('Bolum 3: Apple Developer Program Hesabi Acma')
    doc.h1('3.5  Onay Sonrasi: Xcode ve App Store Connect')
    doc.sp(4)
    doc.text(
        'Apple Developer Program uyeliginiz onaylandiktan sonra Xcode\'da '
        'gercek cihazda test edebilir, App Store Connect\'te uygulama kaydi '
        'olusturabilir ve TestFlight ile beta test dagitabilirsiniz.'
    )
    doc.bullets([
        'App Store Connect (appstoreconnect.apple.com) adresinden yeni '
        'uygulama olusturun',
        'Bundle ID belirleyin (orn: com.sirketiniz.uygulamaadi)',
        'SKU (stok kodu, sadece sizin gorebileceginiz) girin',
        'Uygulama adi, kategori, fiyatlandirma bilgisi girin',
        'Xcode\'da "Signing & Capabilities" altinda Apple Developer '
        'hesabinizi baglayin',
    ])
    doc.box(
        'Yillik uyelik suresi dolmadan en az birkac hafta once Apple size '
        'hatirlatma emaili gonderir. Yenilemezseniz uygulamaniz App Store\'dan '
        'kaldirilir (silinmez, sadece gorunmez olur); yeniledikten sonra '
        'geri gelir.',
        'info'
    )
