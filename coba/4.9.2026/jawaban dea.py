#looping
import random
from coba import welcome_message

#welcome_message = " welcome to cuypy"
#cuypy_posision = random.randint(1,4)
#print("****************************")
#print(f"** {welcome_message} **")
#print("****************************")

welcome_message("welcome to cuypy")

nama_user = input("masukan nama kamu: ")
while nama_user == "":
   # print("Isi dulu namanya!")
   nama_user = input("isi nama kamu: ")

while True:
    cuypy_posision = random.randint(1,4)
    
    bentuk_goa = "|_|"
    goa_kosong = [bentuk_goa] * 4
    goa = goa_kosong.copy()

    #menambahkan join
    goa[cuypy_posision - 1] = "|i_t|"
    goa_kosong = " ".join(goa_kosong)
    goa = " ".join(goa)
    #print(goa)
    #print(f"posisi: {cuypy_posision}")

    while True:
        print(f'''
        halo {nama_user}! coba perhatikan goa di bawah ini
        {goa_kosong}
        ''')

    #tugas kali ini menambahkan while apa program
        while True:
            pilihan_user = input("Menurut kamu di goa nomor berapa cuypy berada? [1/2/3/4]:")
            if pilihan_user in ["1", "2", "3", "4"]:
                pilihan_user = int(pilihan_user)
                break
            else:
                print("silahkan dicoba kembali!")

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
        
        permainan_selsai = input("\n\napakah ingin melanjutkan? [y/n]:")
        if permainan_selsai == "n":
            break

    print("selsai thanks") 
    break   