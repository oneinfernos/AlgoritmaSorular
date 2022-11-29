"""23- 1 den kullanıcının girmiş olduğu sayıya kadar olan tek ve çift sayıların toplamını ayrı ayrı bulan 
ve sonucu ekranda göster
"""

sayi = int(input('Bir sayı giriniz: '))
toplam = 0
while True:
    for i in range(1, sayi+1):
        if sayi % 2 == 0:
            toplam +=i
            print(toplam)
        

"""yapamadım"""