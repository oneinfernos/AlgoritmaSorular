#10-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini hesapla
#Vücut Kitle İndeksi (VKİ) = Vücut Ağırlığı (kg) / Boy Uzunluğunun Karesi (m2)

boy = float(input('Metre cinsinden boyunuzu giriniz: ')) #metre cinsinden olduğu için float olarak girilmesini istiyoruz (örn: 1.80)
kilo = int(input('Kilonuzu giriniz: '))

vki = kilo / (boy*boy)
print(vki)