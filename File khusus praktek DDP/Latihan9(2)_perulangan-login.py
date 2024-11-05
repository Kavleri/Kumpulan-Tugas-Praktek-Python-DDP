user_benar = "admin"
pass_benar  = "admin123"

login_succes = False

while not login_succes :
    username  = str(input("Masukkan username : "))
    password = str(input("Masukkan password : "))
    
    if username == user_benar and password == pass_benar:
        print("Login Berhasil")
        login_succes = True
    else:
        print("Login Gagal. silahkan coba lagi")
        break


