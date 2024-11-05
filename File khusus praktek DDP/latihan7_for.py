#belajar looping/literasi/perulangan dengan for
#menggunakan for dengan list
print('---------Cetak Angka 1 s/d 10 ---------')
angka = 20
for no in range(angka):
    no = no - 1 #incremental/aksi
    print('bilangan', no)
    
print('---------Cetak Bil Genap 1 s/d 20 ---------')
for bil in range(angka):
    bil += 1
    if bil  % 2 == 0:
        print('Bilangan genap', bil)

print('---------Cetak  Bil Ganjil 1 s/d 20 ---------')
for a in range(angka):
    a += 1
    if a % 2 == 1:
        print('Bilangan ganjil', a)
