# Program Membeli Game
# menambahkan game yang berada di toko (game_array) menjadi kepunyaan user dengan menambahkan data di riwayat(riwayat_array) dan kepemilikan (kepemilikan_array)

import functions.files as files, functions.basic as basic
import datetime as dt

from functions.game import check_id_game

# fungsi untuk mengecek apakah user sudah memiliki game yang diinput
def cek_gameUser(id_game, user_id, kepemilikan_array):
    # KAMUS LOKAL
    # punya : bool
    # ID_game, user_ID : str
    
    # ALGORITMA
    punya = False
    for row in kepemilikan_array :
        ID_game = row[0]
        user_ID = row[1]
        if ID_game==id_game and user_ID == user_id :
            punya = True
            break
    return punya

# fungsi untuk mengecek apakah saldo user mencukupi untuk memebli game yang diinput
def cek_saldo(user_id, harga, user_array):
    # KAMUS LOKAL
    # saldo, user_ID : str
    # tidak_cukup : bool
    
    # ALGORITMA
    for row in user_array :
        saldo = row[5]
        user_ID = row[0]
        if user_ID==user_id:
            if int(saldo) >= int(harga) :
                tidak_cukup = False
            else :
                tidak_cukup = True
            row[5] = str(int(row[5]) - int(harga))
            return tidak_cukup
    
# fungsi untuk mengecek apakah game yang diinput tersedia di toko atau tidak
def cek_stok(id_game, game_array):
    # KAMUS LOKAL
    # habis : bool
    # array_length, game_stok : int
    # game_ID : str
    
    # ALGORITMA
    habis = True
    array_length = basic.length(game_array)

    for i in range(1, array_length):
        game_ID = game_array[i][0]
        game_stok = int(game_array[i][5])
        if game_ID == id_game :
            if game_stok > 0 :
                habis = False
                game_array[i][5] = str(int(game_array[i][5])-1)
            break

    return habis

# fungsi untuk menambahkan game yang diinput kedalam kepemilikan_array dan riwayat_array setelah semua pengecekan
def buy_game(game_array, kepemilikan_array, riwayat_array, user_array, user_id):
    # KAMUS LOKAL
    # id_game, idx_game, harga_game, nama_game : str
    # new_row_riwayat, new_row_kepemilikan : str
    
    # ALGORITMA
    id_game = input("Masukkan ID Game: ")

    idx_game = check_id_game(game_array, id_game)
    # Cek apakah game ada di toko
    if (not idx_game):
        return game_array, kepemilikan_array, riwayat_array, user_array 

    harga_game = game_array[idx_game][4]
    nama_game = game_array[idx_game][1]

    # Cek apakah game sudah dimiliki
    if cek_gameUser(id_game, user_id, kepemilikan_array):
        print("Anda sudah memiliki Game tersebut!")
        return game_array, kepemilikan_array, riwayat_array, user_array 

    # cek apakah game masih tersedia di toko
    elif cek_stok(id_game, game_array):
        print("Stok Game tersebut sedang habis!")
        return game_array, kepemilikan_array, riwayat_array, user_array 

    # cek apakah saldo cukup
    elif cek_saldo(user_id, harga_game, user_array):
        print("Saldo anda tidak cukup untuk membeli Game tersebut!")
        return game_array, kepemilikan_array, riwayat_array, user_array 
    
    # masukkan ke kepemilikan dan riwayat
    print("Yeay! Game", nama_game, "berhasil dibeli!")
    year_now = str(dt.date.today().year)
    
    new_row_riwayat = [id_game, nama_game, harga_game, user_id, year_now]
    new_row_kepemilikan = [id_game, user_id]

    riwayat_array = basic.add_row(riwayat_array, new_row_riwayat)
    kepemilikan_array = basic.add_row(kepemilikan_array, new_row_kepemilikan)

    return game_array, kepemilikan_array, riwayat_array, user_array 