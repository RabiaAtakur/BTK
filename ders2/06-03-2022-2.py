liste=[]#boş bir liste tanımlar
liste=["Elma","Armut",28]#artık listenin elemanları değisti
gunler=["pazartesi","Salı","Çarşamba"]
sayilar=[15,19,2,3,8,25,6]
isimler=["Ali","Veli","Ahmet","Zehra","Hatice"]
print(gunler)
print("0.indeksdeki eleman:",gunler[0])#ctrl+d çoğaltır,ctrl+y satırı siler
print(gunler[1])
print(gunler[2])
gunler.append("Perşembe")#append:yeni eleman ekler
print(gunler)
print("Eleman sayısı:",len(gunler))#len:listenin elemam sayısını verir
gunler.pop()#hiçbirşey yazılmadığında listenin son elemanını çıkarır
print(gunler)
gunler.pop(0)#0.indeksdeki elemanı siler
print(gunler)
print(sayilar)
sayilar.sort()#varsayılan(default)olarak küçükten büyüğe sıralar
print(sayilar)
sayilar.sort(reverse=True)#büyükten küçüğe doğru sıralar
print(sayilar)
isimler.sort()
print(isimler)
isimler.sort(reverse=True)
print(isimler)