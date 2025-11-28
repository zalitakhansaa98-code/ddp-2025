import bangunruang as br 
import bangundatar as bd

print("~~~BANGUN RUANG~~~")
print(f"Volum kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"Volum balok adalah {br.balok(4,5,2)}")
print(f"Volum prisma segitiga adalah {br.prisma(5,4,5)}")
print(f"Volum tabung adalah {br.tabung(6,15)}")
print(f"Volum kerucut adalah {br.kerucut(4,14)}")

print("~~~BANGUN DATAR~~~")
print(f"Luas persegi adalah {bd.persegi(9)}")
print(f"Luas persegi panjang adalah {bd.persegi_panjang(5,5)}")
print(f"Luas segitiga adalah {bd.segitiga(16,5)}")
print(f"Luas lingkaran adalah {bd.lingkaran(6)}")
print(f"Luas jajargenjang adalah {bd.jajargenjang(6,5)}")