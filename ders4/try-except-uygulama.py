liste=[2,4,"a",87,"5b","51"]
#yukarıdaki listenin sadece int olanlarını try except ile ekrana yazınız
for i in liste:
    try:
        print(int(i))
    except:
       pass