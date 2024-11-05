'''
PT. Krai memiliki sistem penggajian dengan data sbb (input):
nama pengawal, divisi, agama, jabatan
gaji pokok: jika staff = 4jt, kabag = 7jt, manager = 10jt
tunjab = 20% dari gapok
zakat 2,5 % dari total gaji(ternary) =
jika muslim dan total gaji 7jt
gaji bersih = (gapok+tunjab)- zakat
'''

pegawai = input("Nama Pegawai: ")
divisi = input ("Nama Divisi: ")
agama = input ("Agama Pegawai: ")
jabatan = input ("Jabatan Pegawai: ")
#set gaji
if jabatan == "staff":
    gaji = 4000000
elif jabatan == "kabag":
    gaji = 7000000
elif jabatan == "manager":
    gaji = 10000000
#Menghitung Tunjangan Jabatan
tunjab = 0.2 * gaji
#Menghitung Total Gaji
total_gaji = gaji + tunjab
#Menghitung Gaji Kotor
gaji_kotor =  gaji + tunjab
#Menghitung Zakat
if agama == "muslim" and total_gaji >= 7000000:
    zakat = 0.025 * total_gaji
else:
   zakat = 0
#Menghitun Gaji Bersih
gaji_bersih = (gaji + tunjab) - zakat
print("Gaji Bersih Pegawai: ", gaji_bersih)
#Output
print(f"Nama Pegawai: {pegawai}")
print(f"Nama Divisi: {divisi}")
print(f"Agama Pegawai: {agama}")
print(f"Jabatan Pegawai: {jabatan}")
print(f"Gaji Pokok: {gaji}")
print(f"Tunjangan Jabatan: {tunjab}")
print(f"Total Gaji: {total_gaji}")
print(f"Gaji Kotor: {gaji_kotor}")
print(f"Gaji Bersih: {gaji_bersih}")

