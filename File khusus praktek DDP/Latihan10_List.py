#Membuat list buah
ar_buah = ['Pepaya','Mangga','Pisang','Jambu','Belimbing']
#ganti buah pisang
ar_buah[2] = 'Apel'
#hapus buah belimbing      #hapus semua buah
del ar_buah[4]              #perintah dengan del ar_buah#
ar_buah.append('Salak')
ar_buah.append('Melon')
ar_buah.append('Jeruk')
ar_buah.append('Strawberry')
ar_buah.insert(1,'Naga')
#cetak satu2
print('Buah dgn index/key no.1 adalah buah',ar_buah[0])
print('Buah dgn index/key no.2 adalah buah',ar_buah[1])
print('Buah dgn index/key no.3 adalah buah',ar_buah[2])
print('Buah dgn index/key no.4 adalah buah',ar_buah[3])
print('Buah dgn index/key no.5 adalah buah',ar_buah[4])
print('Buah dgn index/key no.6 adalah buah',ar_buah[5])
print('-----------looping sebelum dipotong-------')
for buah in ar_buah:
    print('Buah',buah)
print('----------potong list----------')
print('Buah-buahan favoritku:',ar_buah[2:7])