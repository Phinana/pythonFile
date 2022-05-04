altsinir = 9
ustsinir = 7129
liste = []

def asalKontrol(sayi):
    sayac = 0
    for i in range(2, int(sayi)):
        if (int(sayi) % i == 0):
            sayac += 1
            break
    if (sayac != 0):
        return 0
    else:
        return sayi

while altsinir < ustsinir:
    if asalKontrol(altsinir) != 0:
        liste.append(altsinir)
    altsinir += 1

print(liste)
