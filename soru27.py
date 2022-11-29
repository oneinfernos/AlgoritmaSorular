#27-Fonksiyon kullanarak iki nokta arası uzaklığı bul . (Koordinatları kullanıcı girecek)

#fonksiyon tanımlama
def uzaklik():
    b = int(input('Birinci koordinatı giriniz: '))
    i = int(input('İkinci koordinatı giriniz: '))

    print('Uzaklık: ',abs(b) + i) #abs ile mutlak değer alınır.


#fonksiyon çağırma
uzaklik()