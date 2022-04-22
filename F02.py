from B01 import encrypt
import functions.basic as basic, functions.files as files
import B01

def register(array):                                                                        # Registrasi user
    nama = input("Masukan nama: ")                                                          # Input nama
    user = input("Masukan username: ")                                                      # Input username
    pasw = input("Masukan password: ")                                                      # Input password

    pasw = B01.encrypt(pasw)

    if validasi(user) == False:                                                             # Jika username tidak dapat di validasi, username tidak valid
        print("Username", user, "tidak valid.")
        return

    array = files.csv_to_2d_array("files/user.csv")                                         # Mengubah user.csv jadi array

    if validasi_sudah(user, array) == False:                                                # Jika username sudah terpakai, username tidak valid
        print("Username", user, "sudah terpakai, silakan menggunakan username lain.")
        return
    
    id = str(int(array[-1][0]) + 1)                                                         # ID user
    arraycsv = [id, user, nama, pasw, "user", "0"]                                          # Data user untuk user.csv
    array = basic.add_row(array, arraycsv)                                                  # Menambah data baru untuk baris terakhir user.csv
    
    files.write("files/user.csv", array)                                                    # Menuliskan hasilnya pada user.csv

def validasi(user):                                                                         # Validasi apakah username sesuai dengan syarat
    user_len = basic.length(user)                                                           # Menghitung panjang username

    for i in range (user_len):                                                              # Jika username sesuai syarat, lanjutkan hingga keseluruhan benar
        if ord(user[i]) == 45 or ord(user[i]) == 95:
            continue
        if ord(user[i]) >= 48 and ord(user[i]) <= 57:
            continue
        if ord(user[i]) >= 65 and ord(user[i]) <= 90:
            continue
        if ord(user[i]) >= 97 and ord(user[i]) <= 122:
            continue
        return False
    
    return True

def validasi_sudah(user, array):                                                            # Validasi apakah username sudah dipakai atau belum
    rows = basic.length(array)                                                              # Menghitung jumlah baris yang ada

    for i in range(1, rows):
        if user == array[i][1]:                                                             # Jika username sudah ada, username tidak valid
            return False

    return True
