#24-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda göster

m = int(input('Maaşınızı giriniz: '))
z = int(input('Zam oranınızı giriniz: '))

zmo = m * z / 100 + m #maaş çarpı zam bölü 100 = maaşın zam oranı. + maaş = zamlı maaş

print(zmo)