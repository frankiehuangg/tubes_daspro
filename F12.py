import functions.basic as basic, functions.files as files

def topup(array):
    user = input("Masukan username: ")                                              # Input username
    saldo_input = int(input("Masukan saldo: "))                                     # Input jumlah saldo (positif berarti tambah saldo, negatif berarti kurang/ambil saldo.)
    
    idx = cek_user(user)                                                            # Login valid

    if idx == -1:                                                                   # Jika username & password tidak ditemukan pada user.csv, login invalid
        print("Username", user, "tidak ditemukan.")
        return
    
    nama = array[idx][2]                                                            # Mencari nama user
    saldo = int(array[idx][5])                                                      # Mencari saldo user (semua role adalah user, kecuali jika diganti menjadi admin)
    
    if saldo_valid(saldo, saldo_input) == False:                                    # Saldo akhir invalid
        print("Masukan tidak valid.")                                               # Print apabila topup tidak berhasil
        return
    
    array[idx][5] = str(saldo + saldo_valid(saldo, saldo_input))                    # Jumlah saldo akhir
    print("Top up berhasil. Saldo", nama, "bertambah menjadi", array[idx][5]+".")   # Print apabila topup berhasil
    
    return array

def cek_user(user):                                                                 # Mengecek username & password sudah terdaftar pada user.csv atau belum
    array = files.csv_to_2d_array("files/user.csv")                                 # Mengubah file user.csv menjadi array
    rows = basic.length(array)                                                      # Menghitung jumlah baris pada user.csv
    
    for i in range(1, rows):                                                        # Jika username & password terdaftar pada user.csv, login valid
        if user == array[i][1]:
            return i
    
    return -1

def saldo_valid(saldo, saldo_input):                                                # Mengecek apakah saldo akhir valid
    if saldo + saldo_input < 0:                                                     # Jika saldo akhir bernilai negatif, saldo akhir invalid
        return -1
    return saldo + saldo_input