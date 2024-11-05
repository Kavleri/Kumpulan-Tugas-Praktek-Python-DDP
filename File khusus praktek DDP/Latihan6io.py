'''
diketahui sebuah toko elektronik:
TV=2jt, AC=3jt, Mesin Cuci=4jt
promo2:
Jika beli MC & min 3, diskon 30%
jika beli AC & min 2, diskon 20%
selain itu diskon 10%
'''
Pelanggan = input("Nama Pelanggan: ")
produk = input("NAma Produk: ")
jml_beli = int(input("Jumlah Beli"))
#set harga
if(produk== 'TV'): harga = 2000000
elif(produk == 'AC'): harga = 3000000
elif(produk == 'Mesin Cuci'): harga = 4000000
else: harga = 0
#set total harga
tohar = harga * jml_beli
#set diskon 
if(produk == 'Mesin Cuci' and jml_beli >= 3):
    diskon = 0.3 * tohar
elif(produk == 'AC' and jml_beli >= 2):
    diskon = 0.2 * tohar
else: diskon = 0.1 * tohar
haber = tohar - diskon
print("Nama Pelanggan: %s"
      "Produk pilihan: %s"
      "Jumlah Beli: %i"
      "Total Harga: %i"
      "Diskon: %.2f"
      "Harga Bersih: %.2f"
      %(Pelanggan,produk,jml_beli,tohar,diskon,haber))