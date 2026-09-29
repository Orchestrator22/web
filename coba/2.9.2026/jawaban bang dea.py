import random

welcome_message = " welcome to cuypy"
cuypy_posision = random.randint(1,4)

print("****************************")
print(f"** {welcome_message} **")
print("****************************")

    
nama_user = input("masukan nama kamu: ")

bentuk_goa = "|_|"
goa_kosong = [bentuk_goa] * 4
goa = goa_kosong.copy()

#menambahkan join
goa[cuypy_posision- 1] = "|i_t|"
goa_kosong = " ".join(goa_kosong)
goa = " ".join(goa)
#print(goa)
#print(f"posisi: {cuypy_posision}")

print(f'''
halo {nama_user}! coba perhatikan goa di bawah ini
{goa_kosong}
''')
 
pilihan_user = int(input("Menurutkamu di goa nomor berapa cuypay berada? [1 / 2 / 3 / 4]: "))
confirm_answer = input(f"apakah kamu yakin jawabannya adalah {pilihan_user}? [y/n]: ")
 
if confirm_answer == "n":
    print("program selsai")
    exit()
elif confirm_answer == "y":       
    if pilihan_user == cuypy_posision:
        print(f"{goa} \nSelamat {nama_user} kamu menang!")
    else:
        print(f"{goa} \nKAMU KALAH!")
else:
    print("coba lagi")
    exit
    