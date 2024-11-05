pilihan = int(input("Pilih bidang (1=Segitiga, 2=Persegi Panjang): "))

if pilihan == 1:
    bidang = "Segitiga"
    alas = float(input("Masukkan Alas: "))
    tinggi = float(input("Masukkan Tinggi: "))
    luas = 0.5 * alas * tinggi
    print("Bidang %s dengan alas %.2f dan tinggi %.2f luasnya = %.2f" % (bidang, alas, tinggi, luas))
elif(pilihan == 2):
     bidang = "Segitiga"
     alas = float(input("Masukkan Alas:"))
     tinggi = float(input("Masukkan Tinggi:"))
     luas = 0.5 * alas * tinggi
     print("Bidang %s dengan alas %.2f dan tinggi %.2f luasnya = %.2f"
     %(bidang, alas, tinggi, luas))

elif(pilihan == 3):
     bidang = "Persegi Panjang"
     p = float(input("Masukkan Panjang:"))
     l = float(input("Masukkan Lebar:"))
     luas = p * l
     print("Bidang %s dengan panjang %.2f dan lebar %.2f luasnya = %.2f" %(bidang, p, l, luas))
else: print("No. Bidang yang Anda pilih tidak ada")