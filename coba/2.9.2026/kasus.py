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

goa[cuypy_posision- 1] = "|i_t|"
#print(goa)
#print(f"posisi: {cuypy_posision}")


#tugas menambahkan kode join variabel
print(f'''
halo {nama_user}! coba perhatikan goa di bawah ini
{" ".join(goa_kosong)}
''')
 
pilihan_user = int(input("Menurutkamu di goa nomor berapa cuypay berada? [1 / 2 / 3 / 4]: "))
confirm_answer = input(f"apakah kamu yakin jawabannya adalah {pilihan_user}? [y/n]: ")
 
if confirm_answer == "n":
    print("program selsai")
    exit()
elif confirm_answer == "y":       
    if pilihan_user == cuypy_posision:
        print(f"{" ".join(goa)} \nSelamat {nama_user} kamu menang!")
    else:
        print(f"{" ".join(goa)} \nKAMU KALAH!")
else:
    print("coba lagi")
    exit
    