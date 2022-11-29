#7-Kullanıcıdan vize ve final notlarınını al geçip kaldığını yazdır (Baün Şartları geçerlidir)
#45

v = int(input('Vize notunuzu giriniz: '))
f = int(input('Final notunuzu giriniz: '))
print(v)
print(f)

if(v>=45 and f>= 45): #and operatörü ile iki koşul da true döndüğünde döngü devam edecek
    print('Geçtiniz.')
else:
    print('Kaldınız.')