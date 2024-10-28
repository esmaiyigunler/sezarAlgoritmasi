print("Sezar Şifreleme/Çözme Programı")
print("1.şifrele")
print("2.Çöz")
print("3.Çıkış")
while True:
    secim=input("Lütfen bir seçenek giriniz(1/2/3):")
    if secim=="1":
        metin=input("Şifrelenecek olan metni girin")
        kaydirma=int(input("Kaydırma miktarını girin"))
        sifreliMetin=[]
        for karakter in metin:
            if karakter.isalpha():
                kaydirmaEgik=kaydirma%26
                base=ord("a") if karakter.islower() else ord("A")
                sifreliKarakter=chr((ord(karakter)-base+kaydirmaEgik)%26+base)
                sifreliMetin.append(sifreliKarakter)
            else:
                sifreliMetin.append(sifreliKarakter)
                
        print(f"Şifreli Metin: {sifreliMetin}")
    elif secim=="2":
        metin=input("Şifrelenecek olan metni girin")
        kaydirma=int(input("Kaydırma miktarını girin"))
        sifreliMetin=[]
        for karakter in metin:
            if karakter.isalpha():
                kaydirmaEgik=-kaydirma%26
                base=ord("a") if karakter.islower() else ord("A")
                sifreliKarakter=chr((ord(karakter)-base+kaydirmaEgik)%26+base)
                sifreliMetin.append(sifreliKarakter)
            else:
                sifreliMetin.append(sifreliKarakter)
                
        print(f"Şifreli Metin: {sifreliMetin}")
    elif secim=="3":
        break
