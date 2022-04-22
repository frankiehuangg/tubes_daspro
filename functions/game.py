# Program CheckIDGame
# Mengecek apakah ID yang dimasukkan valid dan terdapat pada file
# Frankie Huang/16521266

import functions.basic as basic

def check_id_game(array, id_game):
    # Mengecek apakah ID yang dimasukkan valid dan terdapat pada file

    # KAMUS LOKAL
    # lead_string : string
    # row_length : integer

    # ALGORITMA
    lead_string = basic.string_split(id_game, 0, 3)

    if (lead_string != "GAME"):                                                     # Jika awalan id_game tidak berformat "GAME", masukan tidak valid
        print("ID game tidak valid!")
        return 0
    
    for i in range(4, 7):
        try:                                                                        # Cek apakah akhiran id_game berformat integer
            int(id_game[i])
        except:
            print("ID game tidak valid!")
            return 0

    row_length = basic.length(array)

    for row in range(row_length):
        if (id_game == array[row][0]):                                              # Jika ID game didapat, return baris keberapa ditemukan
            return row
    
    print("Tidak ada game dengan ID tersebut!")
    return 0