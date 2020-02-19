#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 17:51:31 2020

@author: mturan
"""



accounts = ("I. Dönen Varlıklar",
            "A. Hazır Değerler",
            "1. Kasa",
            "2. Alınan Çekler",
"3. Bankalar",
"4. Verilen Çekler ve Ödeme Emirleri (-)",
"5. Diğer Hazır Değerler",
"B. Menkul Kıymetler",
"1. Hisse Senetleri",
"2. Özel Kesim Tahvil, Senet ve Bonoları",
"3. Kamu Kesimi Tahvil, Senet ve Bonoları",
"4. Diğer Menkul Kıymetler
"5. Menkul Kıymetler Değer Düşüklüğü Karşılığı (-)
"C. Ticari Alacaklar
"1. Alıcılar
"2. Alacak Senetleri
"3. Alacak Senetleri Reeskontu (-)
"4. Kazanılmamış Finansal Kiralama Faiz Gelirleri (-)
"5. Verilen Depozito ve Teminatlar
"6. Diğer Ticari Alacaklar
"7. Şüpheli Ticari Alacaklar
"8. Şüpheli Ticari Alacaklar Karşılığı (-)
"D. Diğer Alacaklar
"1. Ortaklardan Alacaklar
"2. İştiraklerden Alacaklar
"3. Bağlı Ortaklılardan Alacaklar
"4. Personelden Alacaklar
"5. Diğer Çeşitli Alacaklar
"6. Diğer Alacak Senetleri Reeskontu (-)
"7. Şüpheli Diğer Alacaklar
"8. Şüpheli Diğer Alacaklar Karşılığı (-)
"E. Stoklar
"1. İlk Madde ve Malzeme
"2. Yarı Mamuller - Üretim
"3. Mamuller
"4. Ticari Mallar
"5. Diğer Stoklar
"6. Stok Değer Düşüklüğü Karşılığı (-)
"7. Verilen Sipariş Avansları
"F. Yıllara Yaygın İnşaat ve Onarım Maliyetleri
"1. Yıllara Yaygın İnşaat ve Onarım Maliyetleri
"2. Yıllara Yaygın İnşaat Enflasyon Düzeltme Hesabı
"3. Taşeronlara Verilen Avanslar
"G. Gelecek Aylara Ait Giderler ve Gelir Tahakkukları
"1. Gelecek Aylara Ait Giderler
"2. Gelir Tahakkukları
"H. Diğer Dönen Varlıklar
"1. Devreden KDV
"2. İndirilecek KDV
"3. Diger KDV
"4. Peşin Ödenen Vergiler ve Fonlar
"5. İş Avansları
"6. Personel Avansları
"7. Sayım ve Tesellüm Noksanları
"8. Diğer Çeşitli Dönen Varlıklar
"9. Diğer Çeşitli Dönen Varlıklar Karşılığı (-)
"II. DURAN VARLIKLAR
"A. Ticari Alacaklar
"1. Alıcılar
"2. Alacak Senetleri
"3. Alacak Senetleri Reeskontu (-)
"4. Kazanılmamış Finansal Kiralama Faiz Gelirleri (-)
"5. Verilen Depozito ve Teminatlar
"6. Şüpheli Alacaklar Karşılığı (-)
"B. Diğer Alacaklar
"1. Ortaklardan Alacaklar
"2. İştiraklerden Alacaklar
"3. Bağlı Ortaklılardan Alacaklar
"4. Personelden Alacaklar
"5. Diğer Çeşitli Alacaklar
"6. Diğer Alacak Senetleri Reeskontu (-)
"7. Şüpheli Diğer Alacaklar Karşılığı (-)
"C. Mali Duran Varlıklar
"1. Bağlı Menkul Kıymetler
"2. Bağlı Menkul Kıymetler Değer Düşüklüğü Karşılığı
"3. İştirakler
"4. İştiraklere Sermaye Taahhütleri (-)
"5. İştirakler Sermaye Payları Değer Düşüklüğü
"6. Bağlı Ortaklıklar
"7. Bağlı Ortaklıklar Sermaye Taahütleri (-)
"8. Bağlı Ortaklıklar Sermaye Payları Değer
"9. Diğer Mali Duran Varlıklar
"10. Diğer Mali Duran Varlıklar Karşılığı (-)
"D. Maddi Duran Varlıklar
"1. Arazi ve Arsalar
"2. Yer Altı ve Yer Üstü Düzenleri
"3. Binalar
"4. Tesis, Makina ve Cihazlar
"5. Taşıtlar
"6. Demirbaşlar
"7. Diğer Maddi Duran Varlıklar
"8. Birikmiş Amortismanlar (-)
"9. Yapılmakta Olan Yatırımlar
"10. Verilen Avanslar
"E. Maddi Olmayan Duran Varlıklar
"1. Haklar
"2. Şerefiye
"3. Kuruluş ve Örgütlenme Giderleri
"4. Araştırma ve Geliştirme Giderleri
"5. Özel Maliyetler
"6. Diğer Maddi Olmayan Duran Varlıklar
"7. Birikmiş Amortismanlar (-)
"8. Verilen Avanslar
"F. Özel Tükenmeye Tabi Varlıklar
"1. Arama Giderleri
"2. Hazırlık ve Geliştirme Giderleri
"3. Diğer Özel Tükenmeye Tabi Varlıklar
"4. Birikmiş Tükenme Payları (-)
"5. Verilen Avanslar
"G. Gelecek Yıllara Ait Giderler ve Gelir Tahakkukları
"1. Gelecek Yıllara Ait Giderler
"2. Gelir Tahakkukları
"H. Diğer Duran Varlıklar
"1. Gelecek Yıllarda İndirilecek KDV
"2. Diğer KDV
"3. Gelecek Yıllar İhtiyacı Stoklar
"4. Elden Çıkarılacak Stoklar ve Maddi Duran Varlıklar
"5. Peşin Ödenen Vergiler ve Fonlar
"6. Geçici Hesap
"7. Diğer Çeşitli Duran Varlıklar
"8. Stok Değer Düşüklüğü Karşılığı (-)
"9. Birikmiş Amortismanlar (-) AKTİF TOPLAMI
"PASİF
"III. Kısa Vadeli Yabancı Kaynaklar
"A. Mali Borçlar
"1. Banka Kredileri
"2. Finansal Kiralama İşlemlerinden Borçlar
"3. Ertelenmiş Finansal Kiralama Borçlanma
"4. Uzun Vadeli Kredilerin Anapara Taksitleri ve
"5. Tahvil, Anapara, Borç, Taksit ve Faizleri
"6. Çıkarılmış Bonolar ve Senetler
"7. Çıkarılmış Diğer Menkul Kıymetler
"8. Menkul Kıymetler İhraç Farkı (-)
"9. Diğer Mali Borçlar
"B. Ticari Borçlar
"1. Satıcılar
"2. Borç Senetleri
"3. Borç Senetleri Reeskontu (-)
"4. Alınan Depozito ve Teminatlar
"5. Diğer Ticari Borçlar
"C. Diğer Borçlar
"1. Ortaklara Borçlar
"2. İştiraklere Borçlar
"3. Bağlı Ortaklıklara Borçlar
"4. Personele Borçlar
"5. Diğer Çeşitli Borçlar
"6. Diğer Borç Senetleri Reeskontu (-)
"D. Alınan Avanslar
"1. Alınan Sipariş Avansları
"2. Alınan Diğer Avanslar
"E.Yıllara Yaygın İnşaat ve Onarım Hakedişleri
"1. Yıllara Yaygın İnşaat ve Onarım Hakediş Bedelleri
"2. Yıllara Yaygın İnşaat Enflasyon Düzeltme Hesabı 
"F.Ödenecek Vergi ve Diğer Yükümlülükler
"1. Ödenecek Vergi ve Fonlar
"2. Ödenecek Sosyal Güvenlik Kesintileri
"3. Vadesi Geçmiş Ertelenmiş veya Taksitlendirilmiş 
"4. Ödenecek Diğer Yükümlülükler
"G. Borç ve Gider Karşılıkları
"1. Dönem Karı Vergi ve Diğer Yasal Yükümlülük 
"2. Dönem Karının Peşin Ödenen Vergi ve Diğer 
"3. Kıdem Tazmninatı Karşılığı
"4. Maliyet Giderleri Karşılığı
"5. Diğer Borç ve Gider Karşılıkları
"H. Gelecek Aylara Ait Gelirler ve Gider Tahakkukları 
"1. Gelecek Aylara Ait Gelirler
"2. Gider Tahakkukları
"I. Diğer Kısa Vadeli Yabancı Kaynaklar
"1. Hesaplanan KDV
"2. Diğer KDV
"3. Merkez ve Şubeler Cari Hesabı
"4. Sayım ve Tesellüm Fazlaları
"5. Diğer Çeşitli Yabancı Kaynaklar IV. Uzun Vadeli Yabancı Kaynaklar
"A. Mali Borçlar
"1. Banka Kredileri
"2. Finansal Kiralama İşlemlerinden Borçlar
"3. Ertelenmiş Finansal Kiralama Borçlanma
"4. Çıkarılmış Tahviller
"5. Çıkarılmış Diğer Menkul Kıymetler
"6. Menkul Kıymetler İhraç Farkı (-)
"7. Diğer Mali Borçlar
"B. Ticari Borçlar
"1. Satıcılar
"2. Borç Senetleri
"3. Borç Senetleri Reeskontu (-)
"4. Alınan Depozito ve Teminatlar
"5. Diğer Ticari Borçlar
"C. Diğer Borçlar
"1. Ortaklara Borçlar
"2. İştiraklere Borçlar
"3. Bağlı Ortaklıklara Borçlar
"4. Diğer Çeşitli Borçlar
"5. Diğer Borç Senetleri Reeskontu (-)
"6. Kamuya Olan Ertelenmiş veya Taksitlendirilmiş
"D. Alınan Avanslar
"1. Alınan Sipariş Avansları
"2. Alınan Diğer Avanslar
"E. Borç ve Gider Karşılıkları
"1. Kıdem Tazminatı Karşılıkları
"2. Diğer Borç ve Gider Karşılıkları
"F. Gelecek Yıllara Ait Gelirler ve Gider Tahakkukları
"1. Gelecek Yıllara Ait Gelirler
"2. Gider Tahakkukları
"G. Diğer Uzun Vadeli Yabancı Kaynaklar
"1. Gelecek Yıllara Ertlenen veya Terkin Edilen KDV 
"2. Tesise Katılma Payları
"3. Diğer Çeşitli Uzun Vadeli Yabancı Kaynaklar
"V. Öz Kaynaklar
"A. Ödenmiş Sermaye
"1. Sermaye
"2. Ödenmemiş Sermaye (-)
"3. Sermaye Düzeltmesi Olumlu Farkları
"4. Sermaye Düzeltmesi Olumsuz Farkları(-)
"B. Sermaye Yedekleri
"1. Hisse Senedi İhraç Primleri
"2. Hisse Senedi İptal Karları
"3. Maddi Duran Varlık Yeniden Değerleme Artışları 
"4. İştirakler Yeniden Değerleme Artışları
"5. Diğer Sermaye Yedekleri
"6. Kayda Alınan Emtia Özel Karşılık Hesabı
"7. Demirbaş Makine ve Teçhizat Özel Karşılık
"C. Kar Yedekleri
"1. Yasal Yedekler
"2. Statü Yedekleri
"3. Olağanüstü Yedekler 
"4. Diğer Kar Yedekleri 
"5. Özel Fonlar
"D. Geçmiş Yıl Karları 
"1. Geçmiş Yıl Karları
"E. Geçmiş Yıllar Zararları (-) 
"1. Geçmiş Yıllar Zararları (-)
"F. Dönem Net Karı (zararı) 
"1. Dönem Net Karı
"2. Dönem Net Zararı (-)
"PASİF TOPLAMI
"GELİR TABLOSU
"A. Brüt Satışlar
"1. Yurtiçi Satışlar
"2. Yurtdışı Satışlar
"3. Diğer Gelirler
"B. Satış İndirimleri (-)
"1. Satıştan İadeler (-)
"2. Satış İskontoları (-)
"3. Diğer İndirimler (-)
"C.Net Satışlar
"D. Satışların Maliyeti (-)
"1. Satılan Mamuller Maliyeti (-)
"2. Satılan Ticari Mallar Maliyeti (-) 
"3. Satılan Hizmet Maliyeti (-)
"4. Diğer Satışların Maliyeti (-)
"Brüt Satış Karı veya Zararı
"E. Faaliyet Giderleri (-)
"1. Araştırma ve Geliştirme Giderleri (-)
"2. Pazarlama, Satış ve Dağıtım Giderleri (-)
"3. Genel Yönetim Giderleri (-)
"Faaliyet Karı veya Zararı
"F. Diğer Faaliyetlerden Olağan Gelir ve Karlar
"1. İştiraklerden Temettü Gelirleri
"2. Bağlı Ortaklıklardan Temettü Gelirleri
"3. Faiz Gelirleri
"4. Komisyon Gelirleri
"5. Konusu Kalmayan Karşılıklar
"6. Menkul Kıymet Satış Karları
"7. Kambiyo Karları
"8. Reeskont Faiz Gelirleri
"9. Enflasyon Düzeltmesi Karları
"10. Diğer Olağan Gelir ve Karlar
"G. Diğer Faaliyetlerden Olağan Gider ve Zararlar (-)
"1. Komisyon Giderleri (-)
"2. Karşılık Giderleri (-)
"3. Menkul Kıymet Satış Zararları (-)
"4. Kambiyo Zararları (-)
"5. Reeskont Faiz Giderleri (-)
"6. Enflasyon Düzeltmesi Zararları (-)
"7. Diğer Olağan Gider ve Zararlar (-)
"H. Finansman Giderleri (-)
"1. Kısa Vadeli Borçlanma Giderleri (-)
"2. Uzun Vadeli Borçlanma Giderleri (-)
"Olağan Kar veya Zarar
"I. Olağan Dışı Gelir ve Karlar
"1. Önceki Dönem Gelir ve Karları
"2. Diğer Olağandışı Gelir ve Karlar
"J. Olağandışı Gider ve Zararlar (-)
"1. Çalışmayan Kısım Gider ve Zararları (-)
"2. Önceki Dönem Gider ve Zararları (-)
"3. Diğer Olağandışı Gider ve Zararlar (-)
"Dönem Karı veya Zararı




