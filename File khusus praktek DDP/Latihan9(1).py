string = ""
bar = 1

jmlh_baris = int(input("Masukan  Jumlah Baris : "))
#Looping Baris
while bar <= jmlh_baris :
    kol = bar
    #Looping kolom
    while kol > 0:
        string += '*'
        kol = kol -1
    string += "\n"
    bar  = bar + 1
print(string)    
