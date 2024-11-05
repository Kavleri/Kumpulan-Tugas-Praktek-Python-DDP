#belajar nested loop
#contoh  1
for i in range(10):
    for j in range(i+1):
     print('@', end= '')
    print()  #mengakhiri baris dan pindah ke baris baru
    
#contoh 2
for i in range(10):
    for j in range(10-i):
        print('@', end=' ')
        print()  #mengakhiri baris dan pindah ke baris baru


#contoh 3
for i in range(10):
    for j in range(i):
        print('@', end=' ')
        print()  #mengakhiri baris dan pindah ke baris baru