#kullanıcıdan 5 tane sayı isteyerek en büyük sayıyı listeye atayarak bulun
sayı=[]
sayı1=input("1.Sayıyı Giriniz:")
sayı2=input("2.Sayıyı Giriniz:")
sayı3=input("3.Sayıyı Giriniz:")
sayı4=input("4.Sayıyı Giriniz:")
sayı5=input("5.Sayıyı Giriniz:")
sayı.append(sayı1)
sayı.append(sayı2)
sayı.append(sayı3)
sayı.append(sayı4)
sayı.append(sayı5)
sayı.sort()
print("En Büyük Sayı:",sayı[4])

