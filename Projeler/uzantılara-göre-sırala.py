import os


def duzenle():
    klasor = input("Düzenlenecek Klasör:")
    dosyalar = [] #dosyalar depolanıcak
    uzantilar = [] # uzantılar depolanıcak
    def list_dir():
        for dosya in os.listdir(klasor):
            if os.path.isdir(os.path.join(klasor,dosya)): #dosyamız klasör mü?
                continue
            if dosya.startswith("."): #dosyamız gizli bir dosya mı ?
                continue
            else:
                dosyalar.append(dosya)
    list_dir()
    #uzantıları alma
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]
        if uzanti in uzantilar: #uzanti daha önce eklendi mi
            continue
        else:
            uzantilar.append(uzanti)
    for uzanti in uzantilar: #klasörler oluşturuluyor
        if os.path.isdir(os.path.join(klasor,uzanti)):
            continue
        else:
            os.mkdir(os.path.join(klasor,uzanti))
    for dosya in dosyalar:
        uzanti = dosya.split(".")[-1]
        os.rename(os.path.join(klasor,dosya),os.path.join(klasor,uzanti,dosya))

if __name__=="__main__":
    duzenle()
