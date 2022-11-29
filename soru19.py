#19-Girilen metnin harflerini alt alta yazdır

a = input('Bir metin giriniz: ')
sayac = 0

while sayac < len(a): #len: uzunluk komutu (sayaç a'ya atanan değerden küçük olduğu sürece)
    print(a[sayac])   #a listesinin sayac'ıncı harfini yazdır. (örneğin sayaç 7'de ise a'ya yazılan değerin 7.karakterini yazdır.)    
    sayac+= 1         #sayac'ı birer birer arttır.   

