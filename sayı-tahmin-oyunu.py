tuttugumsayi=3
while True:
    sayı = int(input("Bir sayı tahmin et:"))
    if sayı < tuttugumsayi:
        print("Sayıyı Büyült")
    elif sayı > tuttugumsayi:
        print("Sayıyı Küçült")
    else:
        print("Tebrikler bildiniz")
        break
