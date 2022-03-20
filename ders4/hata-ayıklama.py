#print(a)#NameError hatası verir
#print("Btk"deneme)#syntax error
#print(10/0)#zeroDivisionError hatası verir
#int("5a")#valueError hatası verir
try:
    sayi=int(input("Bir Sayı Giriniz:"))
    sayi2=int(input("Bir Sayı Giriniz:"))
    print("Bölüm:",sayı/sayı2)
except ValueError:
    print("Lütfen sayı gir! Harf Girme!")
except ZeroDivisionError:
    print("0'a bölme yapılamaz")
except SyntaxError:
    print("Yazım hatan var")
except NameError:
    print("Böyle bi değişken yok")
except:
    print("Genel hatan oluştu")
print("Program buradan çalışmaya devam eder...")