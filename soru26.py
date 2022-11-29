"""26-Rastgele Bir sayı üretilsin kullanıcı her seferinde sayıyı tahmin etmeye çalışsın ve  
bu işlem sayı bulununcaya kadar devam etsin
;Sayı bulunduğunda ekrana aynı satırda sayıyı ve kaçıncı denemede bulunduğu yazdırılsın.
"""

import random #random kütüphanesini importladık

#print(random.randint(1,10))

sayac = 0

r = random.randint(1,10) #1 ile 10 arasında bir sayı tahmin edildi





while True: #döngü tamamlanana kadar program bitmesin diye while True
    a = int(input('Random bir sayı tutuldu. Hangi sayı olduğunu tahmin edin: '))
    sayac +=1   #sayaca birer birer ekle ve yeni sayaç değeri bu olsun

    if a == r:#a r'ye eşitse (sayı bulunmuşsa)
        print('Sayıyı doğru tahmin ettiniz. Tutulan sayı: ',r)
        print(f'{sayac} denemede tahmin ettiniz.')
        break  #döngüyü kır


    


