#29-Bir string(önceden tanımlanmış) içerisinde kullanıcının girdiği bir stringin olup olmadığını kontrol et

#string listesi oluşturma
string = ['kalem', 'emir', 'kitap', 'ağaç', 'yastık', 'telefon', 'göz', 'şarj', 'hırka', 'halı', 'forma']

kelime = str(input('Bir kelime yazın: '))


if kelime in string:   #girilen kelime stringin içerisinde var mı?
    print('Listenin içinde olan bir kelime girdiniz.')