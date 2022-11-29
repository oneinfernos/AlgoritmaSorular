#22-Girilen Sayının Asal Sayı mı Değil mi olduğunu bul

a = int(input('Bir sayı giriniz: '))

if a < 2:
    print('Girilen sayı asal değil.')
if a == 2:
    print('Girilen sayı asal.')

for i in range(2,a):
    
