#Kullanıcıdan bir karakter girişi alın. Eğer bu karakter bir harf ise, "Bu bir harftir." yazdırın; eğer sayı ise, "Bu bir sayıdır."; diğer durumlarda "Bu bir özel karakterdir." yazdırın.

karakter = input("Bir karakter giriniz: ")

if karakter.isalpha(): 
    print("Bu bir harftir.")
elif karakter.isdigit():  
    print("Bu bir sayıdır.")
else: 
    print("Bu bir özel karakterdir.")







#Kullanıcının girdiği bir sayının faktöriyelini hesaplayan bir program yazın. Örneğin, 5 için faktöriyel 5! = 5 × 4 × 3 × 2 × 1.

# sayi = int(input("Bir Sayı Giriniz:"))
# faktoriyel = 1
# for i in range(1, sayi + 1):
#     faktoriyel *= i

# print(f"{sayi}! = {faktoriyel}")