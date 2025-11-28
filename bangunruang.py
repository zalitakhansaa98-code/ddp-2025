import math

def kubus (sisi):
    hasil = math.pow(sisi, 3)
    return hasil

def balok (p,l,t):
    hasil = p * l * t
    return hasil

def prisma(alas, tinggi_segitiga, tinggi_prisma):
    luas_alas = 0.5 * alas * tinggi_segitiga
    hasil = luas_alas * tinggi_prisma
    return hasil

def kerucut(jari_jari, tinggi):
    hasil = (1/3) * math.pi * jari_jari * jari_jari * tinggi
    return hasil

def tabung(jari_jari, tinggi):
    hasil = math.pi * jari_jari * jari_jari * tinggi
    return hasil

print(kubus(3))
print(balok(3,3,3))
print(prisma(3,3,3))
print(kerucut(4,14))
print(tabung(6,15))