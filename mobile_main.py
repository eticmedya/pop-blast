#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Claude Code ile Mobil Uygulama Rehberi — Ana Birlestirme Scripti
Tum bolumleri sirayla render eder ve tek bir PDF olarak kaydeder.
"""
from mobile_pdf_engine import Doc
from mobile_part1 import (
    kapak_sayfasi, icindekiler, bolum1_giris,
    bolum2_google_play_hesabi, bolum3_apple_developer_hesabi,
)
from mobile_part2 import bolum4_windows_ortam, bolum5_mac_ortam
from mobile_part3 import bolum6_react_native_expo
from mobile_part4 import bolum7_claude_code_tutorial
from mobile_part5 import bolum8_backend_tasarimi, bolum9_uiux_tasarim
from mobile_part6 import (
    bolum10_fikir_bulma, bolum11_admob, bolum12_adapty,
    bolum13_revenuecat, kapanis,
)


def main():
    doc = Doc()

    kapak_sayfasi(doc)
    icindekiler(doc)
    bolum1_giris(doc)
    bolum2_google_play_hesabi(doc)
    bolum3_apple_developer_hesabi(doc)
    bolum4_windows_ortam(doc)
    bolum5_mac_ortam(doc)
    bolum6_react_native_expo(doc)
    bolum7_claude_code_tutorial(doc)
    bolum8_backend_tasarimi(doc)
    bolum9_uiux_tasarim(doc)
    bolum10_fikir_bulma(doc)
    bolum11_admob(doc)
    bolum12_adapty(doc)
    bolum13_revenuecat(doc)
    kapanis(doc)

    pages = doc.save('claude_code_mobil_rehberi.pdf')
    print('TOPLAM SAYFA:', pages)


if __name__ == '__main__':
    main()
