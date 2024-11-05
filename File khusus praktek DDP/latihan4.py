Mahasiswa = "Muhammad Hisyam"
Nilai = 99.99
#dinyatakan lulus minimal 100

if Nilai >= 70:
    ket = "Lulus"
else:
    ket = "gagal"
#uji grade dengan multi level if
#if cuaca ='cerah' and badan = 'sehat' and ongkos = 'ada'
if Nilai >= 90 and Nilai <= 100: grade = 'A'
elif Nilai >= 80 and Nilai <= 90: grade = 'B'
elif Nilai >= 70 and Nilai <= 80: grade = 'C'
elif Nilai >= 60 and Nilai <= 70: grade = 'D'
#cetak
print("Nama mahasiswa\t:",Mahasiswa,
      "\nNilai\t\t:",Nilai,
      "\nDinyatakan\t:",ket,
      "\nGrade\t\t:",grade)