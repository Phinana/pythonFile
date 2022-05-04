import random

u = int(input("Kac kupon istiyorsunuz? : "))
kuponlar = []

j=0
i=0
while i < u:
    while j < 6:
        kuponlar.append(random.randint(1, 90))
        j += 1
    i += 1

i=0
j=0

while i < 6:
    while j < 6:
        print(kuponlar)
        j += 1
    i += 1