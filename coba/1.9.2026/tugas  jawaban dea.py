import random

welcome_message = " welcome to university"
universitas_prodi = "it"

print("****************************")
print(f"** {welcome_message} **")
print("****************************")

    
nama_user = input("masukan nama kamu: ")
print(f'''
halo selamat datang {nama_user}! di universitas
|_| |_| |_| |_|

''')

while True:
    
    pilihan_user = input("prodi mana yang kamu pilih? [akuntan/it/managemen/si]: ")
    pilihan = input("apakah ingin melanjutkan? [y/n]: ")
    
    if pilihan == "n":
        print("program selsai")
        break
        
    if pilihan_user == universitas_prodi:
        print(f"selamat bergabung {nama_user} kamu terpilih di prodi {universitas_prodi} dari semua prodi {pilihan_user}")
    elif pilihan_user != universitas_prodi:
        print(f"pilihan salah kamu berhasil lolos di prodi {universitas_prodi} bukan di {pilihan_user}")
        break
    else:
        print("coba lagi")
        
    break 