# Program CariGamediToko
# Mencetak game di toko yang memenuhi kriteria input

import functions.basic as basic


def check_column(array, input, index):
    # Mengecek apakah nilai input sama dengan nilai di array per baris

    # KAMUS
    # row_length : integer

    # ALGORITMA
    row_length = basic.length(array)

    for i in range(row_length):
        if (array[i][index] != input):                          # Ubah baris id menjadi kosong jika tidak sesuai kriteria
            array[i][0] = ''
    
    return array


def find_game(array, id_input, nama_input, harga_input, kategori_input, tahun_input):
    # Mengecek apakah input diberi (bukan kosong)

    # ALGORITMA
    if (id_input != ''):                                        # Cek apakah input id kosong
        array = check_column(array, id_input, 0)
    if (nama_input != ''):                                      # Cek apakah input nama kosong
        array = check_column(array, nama_input, 1)
    if (kategori_input != ''):                                  # Cek apakah input kategori kosong
        array = check_column(array, kategori_input, 2)
    if (tahun_input != ''):                                     # Cek apakah input tahun kosong
        array = check_column(array, tahun_input, 3)
    if (harga_input != ''):                                     # Cek apakah input harga kosong
        array = check_column(array, harga_input, 4)
    
    return array


def search_game_at_store(game_array):
    # Mencetak game di toko yang memenuhi kriteria input

    # KAMUS
    # id_input : string
    # nama_input : string
    # harga_input : string
    # kategori_input : string
    # tahun_input : string
    # filtered_array : array of array of string
    # row_length : integer
    # num : integer

    # ALGORITMA
    id_input = input("Masukkan ID Game: ")
    nama_input = input("Masukkan Nama Game: ")
    harga_input = input("Masukkan Harga Game: ")
    kategori_input = input("Masukkan Kategori Game: ")
    tahun_input = input("Masukkan Tahun Rilis Game: ")

    filtered_array = find_game(game_array, id_input, nama_input, harga_input, kategori_input, tahun_input)
    row_length = basic.length(filtered_array)
    num = 1

    print("Daftar game pada toko yang memenuhi kriteria:")

    for i in range(row_length):
        if (filtered_array[i][0] != ''):                        # Cetak row yang bagian ID nya tidak kosong
            print(str(num) + ". " + filtered_array[i][0] + " | " + filtered_array[i][1] + " | " + filtered_array[i][4] + " | " + filtered_array[i][2] + " | " + filtered_array[i][3] + " | " + filtered_array[i][5])
            num += 1