# Program TambahGame
# Menambahkan game pada files/game.csv
# Frankie Huang/16521266

import functions.files as files, functions.basic as basic


def is_input_valid(nama_game, kategori, tahun_rilis, harga, stok_awal):
    # Mengecek apakah nama game, kategori, tahun rilis, harga, dan stok awal adalah input yang valid

    # ALGORITMA
    if (basic.length(nama_game) == 0):              # Cek apakah panjang nama 0 (tidak ada input)
        return False 
    
    if (basic.length(kategori) == 0):               # Cek apakah panjang kategori 0 (tidak ada input)
        return False 
    
    if (int(tahun_rilis) < 2000):                   # Cek apakah tahun rilis < 2000
        return False

    try:                                            
        int(tahun_rilis)                            # Cek apakah tahun rilis bisa diubah menjadi integer (dari string)
        if (int(tahun_rilis) < 0):
            return False

        int(harga)                                  # Cek apakah harga bisa diubah menjadi integer (dari string)
        if (int(harga) < 0):
            return False 
        
        int(stok_awal)                              # Cek apakah stok awal bisa diubah menjadi integer (dari string)
        if (int(stok_awal) < 0):    
            return False
    except:
        return False
    
    return True


def next_id(string):
    # Menjumlahkan angka dalam bentuk string

    # KAMUS LOKAL
    # array : array [0...string_length-1] of char
    # string : string
    # string_length : integer
    # i : integer

    # ALGORITMA
    if (string == 'id'):                            # Jika string bernilai 'id' (baris pertama), return "GAME001"
        return "GAME001"

    string_length = basic.length(string)
    array = basic.string_to_array(string)           # Ubah string ke bentuk array of char
    i = string_length-1

    while (i >= 0):
        if (array[i] != '9'):                       # Jika nilai bukan 9, jumlahkan 1
            array[i] = str(int(array[i])+1)
            break

        array[i] = 0                                # Jika bernilai 9, ubah jadi nol lalu traversal ke elemen i-1
        i -= 1
    
    string = basic.array_to_string(array)           # Ubah kembali array of char ke bentuk string

    return string


def tambah_game():
    # Menambahkan game yang diinput pada files/game.csv

    # KAMUS LOKAL
    # array = array [0...N-1] of string
    # id_game, nama_game, kategori, tahun_rilis, harga, stok_awal : string
    # string = string

    # ALGORITMA
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")
    stok_awal = input("Masukkan stok awal: ")

    while (not is_input_valid(nama_game, kategori, tahun_rilis, harga, stok_awal)):             # Validasi hingga nilai input bernilai true
        nama_game = input("Masukkan nama game: ")
        kategori = input("Masukkan kategori: ")
        tahun_rilis = input("Masukkan tahun rilis: ")
        harga = input("Masukkan harga: ")
        stok_awal = input("Masukkan stok awal: ")

    array = files.csv_to_2d_array("files/game.csv")                                             # Ubah bentuk .csv ke bentuk array 2 dimensi
    id_game = next_id(array[-1][0])

    append_array = [id_game,nama_game,kategori,tahun_rilis,harga,stok_awal]                     # Satukan semua nilai dalam bentuk array

    array = basic.add_row(array, append_array)                                                  # Append array ke array 2 dimensi

    return array