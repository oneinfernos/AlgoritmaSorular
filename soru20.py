#20-Kullanıcın girdiği iki sayı arasındaki sayıların toplamını göster

bir = int(input('Birinci sayıyı giriniz: '))
iki = int(input('İkinci sayıyı giriniz: '))

t = 0

#program
for i in range(bir+1,iki):
    print(i)
    t += i

print(f'Girdiğiniz sayı arasındaki sayıları toplamı: {t}')




    
