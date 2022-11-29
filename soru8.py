#8-Girilen Sayının Tek mi Çift mi Olduğunu Bul

s = int(input('Bir sayı giriniz: '))
print(s)

if(s % 2 == 0): #girilen sayının 2 ile bölümünden kalan 0 ise sayı çifttir
    print('Çift.')
else:
    print('Tek.')
