import functions.basic as basic, functions.files as files
import B01

def login(array):
    user = input("Masukan username: ")                                  # Input username
    pasw = input("Masukan password: ")                                  # Input password

    pasw = B01.encrypt(pasw)

    idx = cek_user(user, pasw)                                          # Login valid

    if idx == -1:                                                       # Jika username & password tidak ditemukan pada user.csv, login invalid
        print("Password atau username salah atau tidak ditemukan.")
        return

    id = array[idx][0]
    nama = array[idx][2]                                                # Mencari nama user
    role = array[idx][4]                                                # Mencari role user (semua role adalah user, kecuali jika diganti menjadi admin)
    print("Halo", nama + "! Selamat datang di “Binomo”.")               # Print login valid

    return [id, role]


def cek_user(user, pasw):                                               # Mengecek username & password sudah terdaftar pada user.csv atau belum
    array = files.csv_to_2d_array("files/user.csv")                     # Mengubah file user.csv menjadi array

    rows = basic.length(array)                                          # Menghitung jumlah baris pada user.csv
    for i in range(1, rows):                                            # Jika username & password terdaftar pada user.csv, login valid
        if user == array[i][1] and pasw == array[i][3]:
            return i

    return -1