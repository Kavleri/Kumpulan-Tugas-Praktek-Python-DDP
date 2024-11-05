tup1 = ('PK 1','PK 2', 1948, 1965)
tup2 = (1,2,3,4,5)
tup3 = ("Kucing", "Ikan Cupang", "kelinci", "Burung")

print('Index 3 pada tup1 adalah',tup1[3])
print('Bilangan index antara 1 dan 5 adalah',tup2[1:5])
print('Binatang peliharaanku adalah',tup3[1])

#Menggunakan fungsi len untuk menjumlahkan data tuple
Hewan = ("Kucing", "Ikan Cupang", "Kelinci", "Burung")
print('Jumlah hewanku ada', len(Hewan))

#Nested Tuple
gorengan = ('bakwan','risol','tempe goreng','piscok')
sop = ('sop ayam','sop iga','sop buntut','sop bakso')
nasi = ('nasi uduk', 'nasi kebuli','nasi goreng','nasi padang')

makanan = (gorengan,sop,nasi)
print('Data tuple gorengan')
print(makanan[0])
print(makanan[0][1])#untuk memanggi data gorengan satu2
print('Data tuple sop')
print(makanan[1])
print(makanan[1][1:4])#untuk memanggil data sop iga sampai sop bakso
print('Data tuple nasi')
print(makanan[2])

#Tuple and list
nama = str(input('masukkan nama mahasiswa : ')) #jika langsung ada namanya langsung dengan kode : nama ='Hisyam'
matkul = 'DDP'
nilai = int(input('masukkan nilai : '))

ket = ('gagal','lulus')[nilai >= 75]

print()
print('nama mahasiswa :',nama,
      '\nMatkul :',matkul,
      '\nNilai Mahasiswa :',nilai,
      '\nKeterangan :',ket)

# Tugas : Buatlah data list dengan 3 variabel, variabel pertama nama teman kalian,variabel kedua makanan favorit teman kalian, variabel ketiga domisili teman kalian
# masukkan kedalam satu variabel ini_teman
# panggil variabel nama teman dan panggil index 3
# tampilkan index 1-4 pada variabel nama
# panggil variabel makanan favorit dan panggi index 0
# tampilkan index 2-4 pada variabel makanan 
# panggil variabel domisili dan panggil index terakhir
#  tampilkan index 3-4 pada variabel domisili