#15- 1-100 Arası 3′ e ve 5′ e tam bölünen sayıları bul

for i in range(1,101):
    if(i % 3 == 0 and i % 5 == 0): #i nin 3 ile ve 5 ile bölümü 0 ise
        print(i)