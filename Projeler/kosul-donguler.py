# Kolay: Kullanıcıdan bir sayı alın ve bu sayının pozitif, negatif veya sıfır olduğunu belirten bir program.

# sayi = int(input("Bir Sayı Giriniz:"))

# if sayi > 0:
#     print("Sayı Pozitiftir")
# elif sayi < 0:
#     print("Sayi Negatiftir")
# else:
#     print("Sayı Sıfırdır")


# Kolay: 1'den 10'a kadar olan sayıları içeren bir liste oluşturun. Döngü kullanarak bu sayıları toplayın.

# liste = [1,2,3,4,5,6,7,8,9,10]
# toplam = 0
# for i in liste:
#     toplam += i

# print(toplam)


# Orta: Faktöriyel hesaplayan bir program yazın. (Kullanıcıdan bir sayı alarak o sayının faktöriyelini bulun.)
def faktoriyel_dongu(n):
    faktoriyel = 1
    for i in range(1, n + 1):
        faktoriyel *= i
    return faktoriyel

sayi =int(input("Bir Sayı Giriniz:")) 
print(f"{sayi} sayısının faktöriyeli:", faktoriyel_dongu(sayi))

