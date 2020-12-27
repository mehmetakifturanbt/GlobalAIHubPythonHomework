"""
Simple Student Management System v1.0
Basit Öğrenci Yönetim Sistemi v1.0
Global AI Hub Bitirme Ödevi
Mehmet Akif TURAN
"""
# ÖRNEK KULLANICI: Akif Turan
import time

def kullaniciSorgu():
    durum = "başarısız"
    kullanicilar = {"kullanici0": { "name"   : "AKIF",
                                    "surname": "TURAN"},
                    "kullanici1": { "name"   : "ALI",
                                    "surname": "SEZGIN"},
                    "kullanici2": { "name"   : "IRMAK",
                                    "surname": "ŞEKER"},
                    "kullanici3": { "name"   : "KAĞAN",
                                    "surname": "NISA"}}
    for harf in ("Öğrenci Yönetim Sistemine Giriş İçin; \n"):
        print(harf,end="")
        time.sleep(0.03)
    for hataSay in range(3):
        name = input("Adınız: ")
        surname = input("Soyadınız: ")
        for ogrenci in range(len(kullanicilar)):
            if name.upper() == kullanicilar["kullanici"+str(ogrenci)]["name"] and surname.upper() == kullanicilar["kullanici"+str(ogrenci)]["surname"]:
                durum = "başarılı"
                print("\nHoşgeldiniz")
        if durum == "başarılı":
            break        
        print(f"Adınız ya da soyadınız YANLIŞ! {2-hataSay} hakkınız kaldı.")
        
    if durum == "başarısız":
        for harf in ("3 defa YANLIŞ giriş yaptınız. Lütfen daha sonra tekrar deneyiniz!\n"):
            print(harf,end="")
            time.sleep(0.02)
        kapat()
        
def kapat():
    for sayac in range(6):
        print(f"Program KAPATILIYOR!({5-sayac})")
        if sayac == 5:
            exit()
        time.sleep(1)
           
def dersTanimla():
    dersler = []
    devam = "E"
    sayac = 1
    print("""
DERS TANIMLAMA MODÜLÜ:
Almak istediğiniz dersleri kendiniz yazacaksınız.
En az 3 ders almalısınız.
En fazla 5 ders alabilirsiniz.
""")
    for harf in ("Ders Tanımlamak İçin; \n"):
        print(harf,end="")
        time.sleep(0.03)
    while devam.upper() == "E":
        ders = input(f"{sayac}. dersinizi giriniz: ")
        dersler.append(ders)
        sayac +=1
        if sayac == 6:
            print("Maximum ders sayısına ulaştınız!")
            break
        while True:
            devam = input("Başka ders eklemek istiyor musunuz? [E/H]")
            if devam.upper() == "E" or devam.upper() == "H":
                break
    print(f"{sayac-1} adet ders seçtiniz.\nSeçtiğiniz dersler: ")
    for akif in dersler:
        print(akif.upper())
    if len(dersler)<3:
        return("Sınıfta kaldınız.")
    return(dersler)

def notHesap(exam):
    secim = "mehmet akif turan"
    print("""
SINAV HESAPLAMA MODÜLÜ:
Sınavını almak istediğiniz dersi seçiniz.
""")
    sinavlar = ["VİZE","FİNAL","PROJE"]
    notlar = {}
    for sayac in range(len(exam)):
        print(f"{exam[sayac].upper()}\t ---> {sayac+1}")
        time.sleep(1)
    while not secim.isdigit() or int(secim) > len(exam) or int(secim)==0:
        secim = input("Kaç numaralı ders: ")
    ders = exam[int(secim)-1]
    for irmak in range(3):
        notunuz = "mehmet akif turan"
        while not notunuz.isdigit() or int(notunuz) > 100 or int(notunuz)<0:
            notunuz = input(f"Aldığınız {ders.upper()} dersinin {sinavlar[irmak]} notunu giriniz: ")
        notlar[sinavlar[irmak]]=notunuz

    puan = int(int(notlar["VİZE"])*0.3 + int(notlar["FİNAL"])*0.5 + int(notlar["PROJE"])*0.2)
    print("Ortalamanız:",puan)
    if puan>90:
        harfNotu="AA"
    elif puan>70:
        harfNotu="BB"
    elif puan>50:
        harfNotu="CC"
    elif puan>=30:
        harfNotu="DD"
    else:
        harfNotu="FF"
    if harfNotu == "FF":
        print("Dersten KALDINIZ!")
    else:
        print(f"Dersten {harfNotu} ile geçtiniz.")
    kapat()
    
def main():                            
    kullaniciSorgu()
    exam = dersTanimla()
    if isinstance(exam,str):
        print(exam)
        kapat()
    notHesap(exam)
    
if __name__ == "__main__":
    main()

