print("Hesap Makinası")
print("Toplama için 1 Çıkarma için 2 Bölme için 3 Çarpma içinde 4 Üstünü almak için 5 Karesini almak için 6 yazınız")
c = input("Buraya Yukarıdaki Sayılardan Birini Yazın")


if c == str(1) :
        Birinci_sayı = input("Toplanılacak Olan Sayı: ")
        İkinci_sayı = input("Toplanan: ")
        print("Cevap: " ,int(Birinci_sayı) +  int(İkinci_sayı) )
elif c == str(2) :
            Birinci_sayı = input("Çıkartılacak Olan Sayı: ")
            İkinci_sayı = input("Çıkarılan: ")
            print("Cevap: " , int(Birinci_sayı) -  int(İkinci_sayı) )
elif c == str(3) :
            Birinci_sayı = input("Bölünecek Sayı: ")
            İkinci_sayı = input("Bölen: ")
            print("Cevap: " , int(Birinci_sayı) / int(İkinci_sayı) )

elif c == str(4) :
            Birinci_sayı = input("Çarpılacak Olan Sayı: ")
            İkinci_sayı = input("Çarpanı: ")
            print("Cevap: " , int(Birinci_sayı) *  int(İkinci_sayı) )

elif c == str(5) :
            Birinci_sayı = input("Üstünü Almak İstediğiniz Sayı : ")
            İkinci_sayı = input("Üstü: ")
            print("Cevap: " , int(Birinci_sayı) **  int(İkinci_sayı) )
elif c == str(6):
            Birinci_sayı = input("Karesini Almak İstediğiniz Sayı: ")
            print("Cevap: ", int(Birinci_sayı) * int(2) )
