import random
while True:
    seviye=input("Bir seviye(kolay/zor/orta) seçiniz:")
    if seviye=="kolay":
        uret=random.randint(1,10)
        break
    elif seviye=="orta":
        uret = random.randint(1, 50)
        break
    elif seviye=="zor":
        uret = random.randint(1, 100)
        break
    else:
        print("Lütfen doğru bir seçim yapınız!")
while True:
    tahmin=int(input("Bir tahminde bulununuz:"))

    if tahmin<uret:
        print("Sayınızı büyütün")
    elif tahmin>uret:
        print("Sayınızı küçültün")
    else:
        print("Tebrikler bildiniz")
        break