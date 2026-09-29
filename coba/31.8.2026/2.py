nama_saya = "dea hesti"

print(nama_saya.find("h")) #mencari
print(len(nama_saya)) #panjang data
print("d" in nama_saya) #mencari keberadaan bnr ada atau tdk sama seperti bolean

print(nama_saya.upper())
print(nama_saya.capitalize())
print(nama_saya.count("d"))


#== sama dengan
#> lebih dari
#< kurang dari
# != tidak sama dengan
# >= lebih dari sama dengan
# <=kurang dari sama dengan
#AND OR


usia = 50
if usia == 20:
    print("usia remaja")
else:
    print("tidak sama")

usia = 20
if usia > 20:
    print("usia remaja")
else:
    print("tidak sama")

usia = 20
if usia >= 20:
    print("usia remaja")
else:
    print("tidak sama")

usia = 10
if usia >= 5 and usia <= 10:
    print("masih muda")
else:
    print("tidak sesuai")

usia = 50
if usia >= 5 and usia <= 10:
    print("usia remaja")
elif usia > 10 and usia <= 20:
    print("hai hai hai")
else:
    print("tidak sama")
    