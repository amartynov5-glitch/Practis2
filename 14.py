a = int(input())
gal = a // (17*29)
sikl = (a % (17*29)) // 29
knat = (a % (17*29)) % 29

if gal > 0:
    print(gal, "галлеон")
if sikl > 0:
    print(sikl, "сиклей")
if knat > 0:
    print(knat, "кнатов")