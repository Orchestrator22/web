saldo_awal = 5000
deposit = input("berapa mau deposit: ") #25000
hutang = 50_000

saldo_total = int(saldo_awal) + int(deposit)
print(saldo_total)

if saldo_total == hutang:
    print("lunas")
elif saldo_total >= hutang:
    print("lunas dan lebih uangnya")
elif saldo_total <= hutang:
    print("belum lunas")
    
else:
    print("nabunglagi")
    