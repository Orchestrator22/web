#typecasting re assignment
tanggal_lahir = 10
tanggal_lahir = 20

print(tanggal_lahir)

#typecasting 1
tanggal_lahir = "20"
konversi_tanggal_lahir = int(tanggal_lahir)

print(konversi_tanggal_lahir)

#typecasting 2
tanggal_lahir = "20"
tanggal_lahir = int(tanggal_lahir)

print(tanggal_lahir)

#data list
kardus = ["mangga", "apel", "jeruk"]
kardus.append("anggur")
kardus.append("semangka") #variable kardus diisi kembali dengan data baru append adalah penambahan.
print(len(kardus)) #len menghitung panjang data atau banyaknya data
print(kardus[0])   #array indeks nya dari 0 dari setiap data
print(kardus[4 - 3])
print(kardus[4])

#library
def grade(nilai):
    if nilai>= 90: 
        print(f"nilai{nilai} mendapatkan grade A")
    elif nilai >= 80 and nilai <= 89:
        print(f"nilai{nilai} mendapatkan grade B")   # susunan library
    elif nilai >= 70 and nilai <= 79:
        print("nilai {nilai} mendapatkan grade C")
    else:
        print("nilai {nilai} mendapatkan grade D")
        
nilai = 82
grade(nilai)

#jika sudah punya library hanya perlu panggil dengan seperti dibawah ini!

#from library_dea.grade import grade

#nilai = 82         
#grade(nilai) 

#ini adalah kode yg di pakai jika kita sudah mempunyai library contoh: 
#library_dea.grade 
#library ini dapat mempermudah sehingga kita hanya panggil 
#library yang sudah ada dengan import dan tarang output 
#yang ingin dihasilkan akan muncul hanya dengan kode singkat 
#dan pemanggilan dari sebuah library.



