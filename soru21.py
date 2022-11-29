"""21-Kullanıcıya sinema ya da tiyatro tercihi sorulsun. Sinema izlemek için 49.50 TL, tiyatro için 29.8 TL 
ödenmesi gerekmedir. Öğrencilere %50 indirim yapıldığı düşünülerek öğrenci ise indirim yapılan; öğrenci değilse
indirimsiz tutarı hesaplayarak ekrana yazdır
"""

ogrenci_kelimeler = ['öğrenci', 'Öğrenci', 'ogrenci', 'Ogrenci']  #girilen değer öğrenci olduğunda kelimenin 
#türevleri
tam_kelimeler = ['Tam', 'tam']  #tam kelimesinin türevleri
sinema = 49.50
tiyatro = 29.80
secim = int(input('1-Sinema\n2-Tiyatro\nSinema mı tiyatro mu tercih edersiniz?(1 veya 2yi seçin): '))
ogrenci = str(input('Öğrenci mi tam mısınız?'))

if secim == 1:
    if ogrenci in ogrenci_kelimeler:
        print('Tutarınız: ', sinema/2)
    else:
        print('Tutarınız: ',sinema)
    

if secim == 2:
    if ogrenci in tam_kelimeler:
        print('Tutarınız: ', tiyatro)
    else: 
        print('Tutarınız: ',tiyatro/2)

