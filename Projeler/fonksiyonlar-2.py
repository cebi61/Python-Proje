# Kolay: İki sayı alan ve bunları toplayan bir fonksiyon yazın.

# def toplam(sayi1,sayi2):
#     toplam_sayi = sayi1 + sayi2
#     return toplam_sayi

# sayi1 = int(input("Birinci Sayıyı Giriniz:"))
# sayi2 = int(input("İkinci Sayıyı Giriniz:"))
# sonuc = toplam(sayi1,sayi2)
# print(f"{sayi1}+{sayi2} = {sonuc}")


# Kolay: Bir kelimenin uzunluğunu hesaplayan bir fonksiyon yazın.

# def kelime_uzunlugu(kelime):
#     return len(kelime)

# ornek_kelime = "Merhaba"
# uzunluk = kelime_uzunlugu(ornek_kelime)

# print(f"{ornek_kelime} kelimesinin uzunluğu: {uzunluk}")





# Orta: İki sayı arasındaki asal sayıları bulan bir fonksiyon yazın.

# def arasindaki_asal_sayilar(baslangic, bitis):
#     """Verilen iki sayı arasındaki asal sayıları bulan fonksiyon."""
#     asal_sayilar = []

#     for sayi in range(max(2, baslangic), bitis + 1):
#         if asal_mi(sayi):
#             asal_sayilar.append(sayi)

#     return asal_sayilar

# def asal_mi(sayi):
#     """Verilen sayının asal olup olmadığını kontrol eden fonksiyon."""
#     if sayi < 2:
#         return False
#     for i in range(2, int(sayi**0.5) + 1):
#         if sayi % i == 0:
#             return False
#     return True

# baslangic = 10
# bitis = 50

# asal_sayilar_arasi = arasindaki_asal_sayilar(baslangic, bitis)
# print(f"{baslangic} ile {bitis} arasındaki asal sayılar: {asal_sayilar_arasi}")


