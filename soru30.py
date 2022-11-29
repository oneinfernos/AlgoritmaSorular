#30- Kullanıcının girdiği 2 sayı arasındaki çift sayıların ortalamasını bul

b = int(input('Birinci sayıyı giriniz: '))
s = int(input('İkinci sayıyı giriniz: '))

toplam = 0  #sayıların toplamını alacağımız için şimdilik değeri 0 olan bir toplam değişkeni oluşturduk
for i in range(b,s+1): # birinci sayıdan ikinci sayıyan kadar
    toplam += i        # toplama birinci sayıdan ikinci sayıya kadar olan değerleri ekle ve yeni toplam değeri bu olsun
    if i % 2 == 0:     #birinci sayıdan ikinci sayıya kadar olan sayıların 2 ile bölümünden kalan 0 ise
       print(i)        #bunları yazdır

ortalama = toplam / (s-b + 1)   #ortalamayı bulma
print('Çift sayıların ortalama değeri: ', ortalama)