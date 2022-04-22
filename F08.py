import functions.files as files
import datetime as dt

def cek_gameUser(id_game, user_id, kepemilikan_array):
    punya = False
    kepemilikan = kepemilikan_array
    for row in kepemilikan :
        ID_game = row[0]
        user_ID = row[1]
        if ID_game==id_game and user_ID == user_id :
            punya = True
            break
    return punya

def cek_saldo(user_id, harga):
    User = files.csv_to_2d_array("user.csv")
    for row in User :
        saldo = row[5]
        user_ID = row[0]
        if user_ID==user_id:
            if int(saldo) >= int(harga) :
                tidak_cukup = False
            else :
                tidak_cukup = True
            return tidak_cukup
    
def cek_stok(id_game):
    habis = True
    Game = files.csv_to_2d_array("game.csv")
    for row in Game:
        game_ID = row[0]
        game_stok = row[5]
        if game_ID == id_game :
            if game_stok > 0 :
                habis = False
            break
    return habis

def buy_game(user_id, kepemilikan_array, riwayat_array) :
    id_game = input("Masukkan ID Game: ")
    Game = files.csv_to_2d_array("game.csv")
    for row in Game :
        game_harga = row[4]
        game_ID = row[0]
        if game_ID==id_game:
            harga = game_harga
            break
    for row in Game :
        game_ID = row[0]
        game_nama = row[1]
        if game_ID==id_game:
            nama_game = game_nama
            break
    # cek apakah game sudah dimiliki
    if cek_gameUser(id_game, user_id, kepemilikan_array) :
        print("Anda sudah memiliki Game tersebut!")

    # cek apakah game masih tersedia di toko
    elif cek_stok(id_game):
        print("Stok Game tersebut sedang habis!")

    # cek apakah saldo cukup
    elif cek_saldo(user_id, harga):
        print("Saldo anda tidak cukup untuk membeli Game tersebut!")
    
    # masukkan ke kepemilikan dan riwayat
    else :
        print("Yeay! Game", nama_game, "berhasil dibeli!")
        year_now = str(dt.date.today().year)
        
        new_row_riwayat = [id_game, nama_game, harga, user_id, year_now]
        new_row_kepemilikan = [id_game, user_id]

        Riwayat_new = files.add_row(riwayat_array, new_row_riwayat)
        Kepemilikan_new = files.add_row(kepemilikan_array, new_row_kepemilikan)
        return (Riwayat_new, Kepemilikan_new)
