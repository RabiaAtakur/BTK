"""
kullanıcı adı ve şifre alınız.kullanıcı adı olarak "admin" şifre olarak 123456 girilince
"sisteme başarılı bir şekilde giriş yaptınız" yanlış girildikçe
"kullanıcı veya şifre hatalı" yazıp tekrar kullanıcı adı ve şifre sorsun!
"""
kadi="admin"
sifre="123456"

while True:
    kadi = input("Kullanıcı Adını Giriniz:")
    sifre = input("Şifrenizi Giriniz:")
    if kadi=="admin" and sifre=="123456":
        print("sisteme başarılı bir şekilde giriş yaptınız")
        break
    else:
        print("kullanıcı veya şifre hatalı")