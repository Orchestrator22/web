import random    #liberary

#nama = "dea hesti"
#usia = 20
welcome_message = " welcome to university"
universitas_prodi = "it"

print("****************************")
print(f"** {welcome_message} **")
print("****************************")

#print(f'''   
#nama saya adalah {nama}
#dan usia saya {usia}        

#nomor_saya = 20

#if nomor_saya == 4:
    #print("yes bener")
#else:
    #print("no tidak")
    
nama_user = input("masukan nama kamu: ")
print(f'''
halo selamat datang {nama_user}! di universitas
|_| |_| |_| |_|

''')

    
pilihan_user = input("prodi mana yang kamu pilih? [akuntan/it/managemen/si]: ")

if pilihan_user == universitas_prodi:
    print(f"selamat bergabung {nama_user} kamu terpilih di prodi {universitas_prodi} dari semua prodi {pilihan_user}")
        
else:
    print(f"pilihan salah kamu berhasil lolos di prodi {universitas_prodi} bukan di {pilihan_user}")
        
    