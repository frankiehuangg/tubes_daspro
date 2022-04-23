import functions.basic as basic,  functions.files as files

def list_user_game(user_id, riwayat_array, game_array):
    # urutan : no, ID game, nama game, kategori, tahun rilis, tahun beli, harga
    jumlah_game = 0
    count = 0
    Riwayat = riwayat_array
    Game = game_array

    for row in Riwayat :
        user_ID = row[3]
        if user_ID == user_id :
            jumlah_game += 1
    daftar_game_user = [["" for i in range(7)] for j in range(jumlah_game)]

    for row in Riwayat :
        user_ID = row[3]
        riwayat_game_id = row[0]
        game_tahun_beli = row[4]
        if user_ID == user_id :
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
            count += 1

    return daftar_game_user

def remove_row(array_2d, row_number):
    row_length = basic.length(array_2d)
    col_length = basic.length(array_2d[0])
    new_array_2d = [["" for i in range(col_length)] for i in range(row_length-1)]
    for i in range(row_length):
        if i < row_number :
            for j in range(col_length):
                new_array_2d[i][j] = array_2d[i][j]
        elif i> row_number :
            for j in range(col_length):
                new_array_2d[i-1][j] = array_2d[i][j]
    return new_array_2d

def search_my_game(user_id, riwayat_array, game_array):
    id_game = input("Masukkan ID Game : ")
    release_year = input("Masukkan Tahun Rilis Game : ")

    if id_game == '' and release_year == '':
        print("Input tidak valid!")
        return

    daftar_game_user = list_user_game(user_id, riwayat_array, game_array)

    jumlah_game = basic.length(daftar_game_user)

    new_daftar_game_user = []
    for i in range(basic.length(daftar_game_user)) :
        game_ID = daftar_game_user[i][1]
        game_tahun_rilis = daftar_game_user[i][4]

        # mengisi keduanya 
        if id_game != '' and game_tahun_rilis != '' and id_game == game_ID and game_tahun_rilis == release_year:
            new_row = daftar_game_user[i]
            new_daftar_game_user = basic.add_row(new_daftar_game_user, new_row)
            continue

        # hanya mengisi id game
        elif id_game != '' and game_tahun_rilis == '' and id_game == game_ID :
            new_row = daftar_game_user[i]
            new_daftar_game_user = basic.add_row(new_daftar_game_user, new_row)
            continue
        
        # hanya mengisi tahun rilis
        elif id_game == '' and  release_year != '' and game_tahun_rilis == release_year :
            new_row = daftar_game_user[i]
            new_daftar_game_user = basic.add_row(new_daftar_game_user, new_row)
            continue

    print("-"*113)
    print(" "*52 +"GAME KAMU"+ " "*52)
    print(" "*93 + "ID GAME : "+ id_game + " "*3)
    print(" "*89 + "TAHUN RILIS : "+ release_year + " "*6)
    if basic.length(new_daftar_game_user)==0 :
        print("-"*113)
        # cek apakah user sudah memiliki game
        if jumlah_game == 0 : 
            print("\nMaaf, kamu tidak memiliki game! Yuk beli game dulu dengan ketik perintah 'buy_game'!")
        else :
            print("\nTidak ada Game di inventory-mu yang memenuhi kriteria!")
    # print tabel daftar game
    else :
        print("-"*113)
        print("| NO ", end="")
        print("| ID GAME |", end="")
        print(" "*16 +" NAMA"+ " "*16, end="")
        print("|"+" "*4 +" KATEGORI"+ " "*4, end="")
        print("| TAHUN RILIS ", end="")
        print("| TAHUN PEMBELIAN ", end="")
        print("| HARGA  |")
        print("-"*113)
        row_length = basic.length(new_daftar_game_user)
        for i in range(row_length):
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
                elemen = new_daftar_game_user[i][j]
                print(" "+ elemen +" "*(n-basic.length(elemen))+ "|", end="")
            print("")
        print("-"*113)