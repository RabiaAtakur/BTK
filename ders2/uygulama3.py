#Kullanıcıdan harf girilmesini isteyiniz e girerse erkek k girerse kadın denilsin
cinsiyet=input("Harf Giriniz:")
if cinsiyet=="k" or cinsiyet=="K":
    print("Kadın")#2. vaya daha fazla şart olursa elif kullanılır
elif cinsiyet=="e" or cinsiyet=="E":
    print("Erkek")
else:
    print("Lütfen E veya K giriniz!")

