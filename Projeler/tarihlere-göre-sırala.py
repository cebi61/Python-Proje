import os
from datetime import datetime

def duzenle():
    klasor = input("Düzenlenecek Klasör:")
    dosyalar = [] 
    tarihler = [] 

    def list_dir():
        for dosya in os.listdir(klasor):
            dosya_yolu = os.path.join(klasor, dosya)
            if os.path.isdir(dosya_yolu):
                continue
            if dosya.startswith("."):
                continue
            else:
                dosyalar.append(dosya)

    list_dir()

    for dosya in dosyalar:
        dosya_yolu = os.path.join(klasor, dosya)
        tarih_damgasi = os.stat(dosya_yolu).st_mtime  # Dosya değişiklik zamanı alınıyor.
        tarih = datetime.fromtimestamp(tarih_damgasi).strftime("%d-%m-%Y")
        if tarih not in tarihler:
            tarihler.append(tarih)

    for tarih in tarihler:
        klasor_yolu = os.path.join(klasor, tarih)
        if not os.path.isdir(klasor_yolu):
            os.mkdir(klasor_yolu)

    for dosya in dosyalar:
        dosya_yolu = os.path.join(klasor, dosya)
        tarih_damgasi = os.stat(dosya_yolu).st_mtime
        tarih = datetime.fromtimestamp(tarih_damgasi).strftime("%d-%m-%Y")
        yeni_yol = os.path.join(klasor, tarih, dosya)
        os.rename(dosya_yolu, yeni_yol)

if __name__ == "__main__":
    duzenle()
