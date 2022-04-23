# Program UbahGame
# Mengganti keterangan game pada files/game.csv

import functions.files as files, functions.game as game


def is_input_valid(array, id_game, tahun_rilis, harga):
    # Mengecek apakah id game, tahun rilis, dan harga valid

    # KAMUS LOKAL
    # row : integer

    # ALGORITMA
    if (not game.check_id_game(array, id_game)):                    # Cek apakah id_game terdapat pada file
        return 0
    
    try:
        (tahun_rilis == "" or int(tahun_rilis) < 2000)              # Cek apakah tahun_rilis dapat diubah menjadi integer (jika input tidak kosong)
    except:
        print("Tahun rilis tidak valid!")
        return 0

    try:
        (harga == "" or int(harga) < 0)                             # Cek apakah harga dapat diubah menjadi integer (jika input tidak kosong)
    except:
        print("Harga tidak valid!")
        return 0
    
    row = game.check_id_game(array, id_game)

    return row


def ubah_game(array):
    # Mengembalikan array berupa data pada files/game.csv yang sudah diubah

    # KAMUS LOKAL
    # array : array [0...N] of array[0...5] of string 
    # id_game, nama_game, kategori, tahun_rilis, harga : string
    # row : integer

    # ALGORITMA
    id_game = input("Masukkan ID game: ")
    nama_game = input("Masukkan nama game: ")
    kategori = input("Masukkan kategori: ")
    tahun_rilis = input("Masukkan tahun rilis: ")
    harga = input("Masukkan harga: ")

    if (not is_input_valid(array, id_game, tahun_rilis, harga)):    # Jika input tidak valid, terminasi program 
        return array
    
    row = is_input_valid(array, id_game, tahun_rilis, harga)

    if (nama_game != ""):                                           # Jika input nama game tidak kosong, ubah nilai pada array
        array[row][1] = nama_game
    if (kategori != ""):                                            # Jika input kategori tidak kosong, ubah nilai pada array
        array[row][2] = kategori
    if (tahun_rilis != ""):                                         # Jika input tahun rilis tidak kosong, ubah nilai pada array
        array[row][3] = tahun_rilis
    if (harga != ""):                                               # Jika input harga tidak kosong, ubah nilai pada array
        array[row][4] = harga
    
    return array