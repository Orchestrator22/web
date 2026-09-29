#looping
import random

def start():
    while True:
        bentuk_goa = "|_|"
        goa_kosong = [bentuk_goa] * 4
        goa = goa_kosong.copy()

        cuypy_posision = random.randint(1,4)

        #menambahkan join
        goa[cuypy_posision - 1] = "|i_t|"
        goa_kosong = " ".join(goa_kosong)
        goa = " ".join(goa)
        

        print(f'coba perhatikan goa di bawah ini!\n\n{goa_kosong}\n')

        #tugas kali ini menambahkan while apa program
            
        pilihan_user = input("Menurut kamu di goa nomor berapa cuypy berada? [1/2/3/4] ")
        
        if pilihan_user == cuypy_posision:
            print(f"{goa} \nSelamat kamu menang!")
        else:
            print(f"{goa} \nKAMU KALAH!")
            
        permainan_selsai = input("\n\napakah ingin melanjutkan? [y/n]:")
        if permainan_selsai == "n":
            break

    print("selsai thanks")


if __name__ == '__main__':
    start()