pembeli = "Icy"
uang = 10000
if uang >= 10000:
    ket = "Lapar"
else:
    ket = "Gak bisa jajan"

if uang >= 5000 and uang <= 10000: pembelian = "Batagor"
elif uang >= 2000 and uang <= 4999: pembelian = "Telur Gulung"
elif uang >= 1000 and uang <= 1999: pembelian = "Gula-Gula"
elif uang >= 0 and uang <= 0 : pembelian = "Puasa"

print("pembeli\t\t:",pembeli,
      "\nUang\t\t:",uang,
      "\nReason\t\t:",ket,
      "\nMembeli\t\t:",pembelian )
