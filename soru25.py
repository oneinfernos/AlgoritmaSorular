#25-Fonksiyon kullanarak yarıçapı girilen dairenin alanını hesapla
#yarıçapın karesi * pi sayısı


def daire():  #fonksiyon tanımlama
    a = int(input('Yarıçapı giriniz: '))
    alan = a*a * 3.14
    print('Dairenin alanı: ',alan)
    

daire() #tanımladığımız fonskiyonun içinde istenilen programın tamamı olduğu için fonksiyonu direkt çağırdık.
