import os
while True:
    print("1-Klasör oluştur")
    print("2-Klasör sil")
    secim=input("Seçiminiz:")
    if secim=="1":
        ad=input("Oluşturmak istediğiniz klasör adı giriniz:")
        for i in range(1,11):
            os.mkdir("elma"+str(i))
    elif secim=="2":
        ad = input("Silinecek klasör adı giriniz:")
        for i in range(1, 11):
            os.rmdir("elma" + str(i))