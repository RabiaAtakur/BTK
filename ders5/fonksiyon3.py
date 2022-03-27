#kendisine gönderilen kullanıcı adı ve şifreyi kontrol ederek sonucunda true ya da false gönderen fonksiyonun
#python kodu kullanıcıadı=admin,şifre=123456 olmalı
def kontrol(kadi,şifre):
    if kadi=='admin' and şifre=='123456':
        return True
    else:
        return  False
kadi=input("Kullanıcı adını giriniz:")
şifre=input("Şifrenizi giriniz:")
sonuc=kontrol(kadi,şifre)
if sonuc==True:
    print("Giriş Başarılı")
else :
    print("Giriş Başarısız")
