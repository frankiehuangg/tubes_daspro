import functions.basic as basic,  functions.files as files

def cek_daftarGame(user_id, kepemilikan_array):
    tidak_punya = True
    kepemilikan = kepemilikan_array
    for row in kepemilikan :
        user_ID = row[1]
        if user_ID == user_id :
            tidak_punya = False
            break
    return tidak_punya
            
def list_user_game(user_id, riwayat_array):
    global jumlah_game
    jumlah_game = 0
    count = -1
    # urutan : no, ID game, nama game, kategori, tahun rilis, tahun beli, harga
    Riwayat = riwayat_array
    Game = files.csv_to_2d_array("files/game.csv")
    for row in Riwayat :
        user_ID = row[3]
        if user_ID == user_id :
            jumlah_game += 1
    daftar_game_user = [["" for i in range(7)] for i in range(jumlah_game)]
    for row in Riwayat :
        user_ID = row[3]
        riwayat_game_id = row[0]
        game_tahun_beli = row[4]
        if user_ID == user_id :
            count += 1
            for line in Game :
                game_id = line[0]
                game_nama = line[1]
                game_kategori = line[2]
                game_tahun_rilis = line[3]
                game_harga = line[4]
                if game_id == riwayat_game_id :
                    daftar_game_user[count][0] = str(count+1) + "."
                    daftar_game_user[count][1] = game_id
                    daftar_game_user[count][2] = game_nama
                    daftar_game_user[count][3] = game_kategori
                    daftar_game_user[count][4] = game_tahun_rilis
                    daftar_game_user[count][5] = game_tahun_beli
                    daftar_game_user[count][6] = game_harga
                    break
    return daftar_game_user

def list_game(user_id, kepemilikan_array, riwayat_array):
    print("-"*113)
    print(" "*52 +"GAME KAMU"+ " "*52)
    # cek apakah user sudah memiliki game
    if cek_daftarGame(user_id, kepemilikan_array):
        print("-"*113)
        print("\nMaaf, kamu tidak memiliki game! yuk beli game dulu dengan ketik perintah 'buy_game'")
    else :
        daftar_game_user = list_user_game(user_id, riwayat_array)
        print("-"*113)
        print("| NO ", end="")
        print("| ID GAME |", end="")
        print(" "*16 +" NAMA"+ " "*16, end="")
        print("|"+" "*4 +" KATEGORI"+ " "*4, end="")
        print("| TAHUN RILIS ", end="")
        print("| TAHUN PEMBELIAN ", end="")
        print("| HARGA  |")
        print("-"*113)
        for i in range(jumlah_game):
            for j in range(7):
                if j == 0 :
                    n = 3
                    print("|", end="")
                elif j==1:
                    n = 8
                elif j==2 :
                    n = 36
                elif j==3:
                    n = 16
                elif j==4 :
                    n = 12
                elif j ==5 :
                    n = 16
                else :
                    n = 7
                elemen = daftar_game_user[i][j]
                print(" "+ elemen +" "*(n-basic.length(elemen))+ "|", end="")
            print("")
        print("-"*113)