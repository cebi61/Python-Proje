# 1 - Kullanıcının girdiği iki sayının bölümünü ve kalanını döndüren bir fonksiyon yazın.


# def bol_kalan(sayi1, sayi2):
#     bölüm = sayi1 / sayi2
#     kalan = sayi1 % sayi2
#     print(f"{sayi1} ve {sayi2}'nin bölümü= {bölüm}")
#     print(f"{sayi1} ve {sayi2}'nin kalanı= {kalan}")

# sayi1 = int(input("Bir Sayı Giriniz:"))
# sayi2 = int(input("Bir Sayı Giriniz:"))

# bol_kalan(sayi1, sayi2)

#_______________________________________________________________________________________________________


# 2 - Kullanıcının girdiği bir sayının karesini alan ve sonucu ekrana yazdıran bir fonksiyon yazın.

# def kare_alan(sayi1):
#     kare = sayi ** 2 
#     print(f"{sayi}'nın karesi: {kare}")
#     return kare

# sayi = float(input("Bir Sayı Giriniz:"))
# kare_alan(sayi)

#_______________________________________________________________________________________________________

# 3 - Kullanıcının girdiği iki sayının en büyük ortak bölenini (EBOB) bulan bir fonksiyon yazın.

# def ebob_bul(sayi1, sayi2):
#     while sayi2 != 0:
#         sayi1, sayi2 = sayi2, sayi1 % sayi2
#     return sayi1

# sayi1 = int(input("Birinci sayıyı giriniz: "))
# sayi2 = int(input("İkinci sayıyı giriniz: "))

# ebob = ebob_bul(sayi1, sayi2)

# print(f"{sayi1} ve {sayi2} sayılarının EBOB'u: {ebob}")
