# Program CariGamediToko
# Mencetak game di toko yang memenuhi kriteria input

import functions.basic as basic, functions.files as files

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
    global toko_kosong
    toko_kosong = True
    # ALGORITMA
    if (id_input != ''):                                        # Cek apakah input id kosong
        array = check_column(array, id_input, 0)
        toko_kosng = False
    if (nama_input != ''):                                      # Cek apakah input nama kosong
        array = check_column(array, nama_input, 1)
        toko_kosong = False
    if (kategori_input != ''):                                  # Cek apakah input kategori kosong
        array = check_column(array, kategori_input, 2)
        toko_kosong = False
    if (tahun_input != ''):                                     # Cek apakah input tahun kosong
        array = check_column(array, tahun_input, 3)
        toko_kosong = False
    if (harga_input != ''):                                     # Cek apakah input harga kosong
        array = check_column(array, harga_input, 4)
        toko_kosong = False
    
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

    print("-"*103)
    print(" "*46 +"GAME STORE"+ " "*46)
    if basic.length(filtered_array)==0 :
        print("-"*103)
        # cek apakah di toko ada game
        if toko_kosong == False : 
            print(" "*38 + "\nMaaf, Game tidak tersedia!" + " "*38)
        else :
            print(" "*25+"\nTidak ada Game di GAME STORE yang memenuhi kriteria!" + " "*25)
    # print tabel daftar game
    else :
        # id;nama;kategori;tahun_rilis;harga;stok;
        print("-"*103)
        print("| NO  ", end="")
        print("| ID GAME |", end="")
        print(" "*16 +" NAMA"+ " "*16, end="")
        print("|"+" "*4 +" KATEGORI"+ " "*4, end="")
        print("| TAHUN RILIS ", end="")
        print("| HARGA ", end="")
        print("| STOK  |")
        print("-"*103)
        row_length = basic.length(filtered_array)
        for i in range(row_length):
            if (filtered_array[i][0] != ''):
                for j in range(6):
                    if j == 0 :
                        n = 8
                        print("| "+ str(num) +"."+" "*(3-basic.length(str(num))) + "|", end="")
                    elif j==1:
                        n = 36
                    elif j==2 :
                        n = 16
                    elif j==3:
                        n = 12
                    elif j==4 :
                        n = 6
                    else :
                        n = 6
                    elemen = filtered_array[i][j]
                    print(" "+ elemen +" "*(n-basic.length(elemen))+ "|", end="")
                num +=1
            print("")
        print("-"*103)

game_array = files.csv_to_2d_array("files/game.csv")
print(game_array)
search_game_at_store(game_array)