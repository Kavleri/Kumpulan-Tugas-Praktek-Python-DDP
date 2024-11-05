# List makanan dengan 2 dimensi
list_makanan = [
["Bakwan", "Combro", "Misro"],
["Sop Iga", "Sop Buntut", "Sop Kaki","Sop Ayam"],
["Nasi Uduk", "Nasi Goreng", "Nasi Rames"]
]
print('------cetak per satuan------')
print(list_makanan[0][0])#Bakwan
print(list_makanan[1][2])#Sop Kaki
print(list_makanan[2][2])#Nasi Rames
print('------cetak semuanya dengan nestedLoop------')
for menu in list_makanan:
   for makanan in menu:
     print(makanan)