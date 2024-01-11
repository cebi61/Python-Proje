# Dosya Okuma:
# Bir metin dosyası oluşturun ve içerisine metin ekleyin. Ardından bu dosyayı Python ile açıp içeriğini ekrana yazdırın.

# with open("Açılacak Dosya.txt","w") as d:
#     d.write("Bu örnek bir metindir.")

# with open("Açılacak Dosya.txt","r") as d:
#     icerik = d.read()
#     print(icerik)





# Dosya Yazma:
# Kullanıcının girdiği metni bir dosyaya yazan bir program yazın. Dosya daha önceden varsa üzerine yazsın, yoksa yeni bir dosya oluştursun.


# metin = input("Bir Metin Giriniz:")

# with open ("Yazılacak Metin.txt","w") as y:
#     y.write(metin)
    


# Dosya Kapama:
# Bir dosyayı açın, içeriğini okuyun ve sonra dosyayı kapatın. Daha sonra aynı dosyayı tekrar açıp içeriğini değiştirin.

# with open("Yazılacak Metin.txt") as r:
#     icerik = r.read()
#     print(icerik)
#     r.close()

# with open("Yazılacak Metin.txt","w") as d:
#     degisim = input("Bir Metin Giriniz:")
#     d.write(degisim)
#     d.close()
