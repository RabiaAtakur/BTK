#dikdörtgenin alanını ve çevresini hesaplayan 2 ayrı fonksiyon yazınız.
#kullanıcıdan aldığınız değere göre alanı ve çevreyi ekrana yazınız
def çevre(uk,kk):
    return 2*(kk+uk)
uk=int(input("Uzun Kenarı Giriniz:"))
kk=int(input("Kısa Kenarı Giriniz:"))
print(alan(uk,kk))
def alan(uk,kk):
    print(uk*kk)
alan(uk,kk)
çevre(uk,kk)
"""
def cevre(kısa,uzun):
    return (kısa+uzun)*2
def alan(kısa,uzun):
    return kısa*uzun
kısa_kenar=int(input("Kısa Kenar:"))
uzun_kenar=int(input("Uzun Kenar:"))
print("Çevre:",cevre(kısa_kenar,uzun_kenar))
print("ÇeAlan:",alan(kısa_kenar,uzun_kenar))
"""