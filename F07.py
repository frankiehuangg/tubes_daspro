# Program ListGameToko
# Mencetak semua game di files/game.csv berdasarkan skema sorting

import functions.files as files, functions.basic as basic, functions.game as game

def print_array(array):
    # Mencetak array 2 dimensi

    # KAMUS LOKAL
    # row_length, col_length, num = 1

    # ALGORITMA
    row_length = basic.length(array)

    max_name_len = 20
    max_cat_len = 10
    max_prc_len = 6

    for i in range(1, row_length):
        name_tab_amt = max_name_len - basic.length(array[i][1])
        if (name_tab_amt >= 0):
            print(array[i][1] + ' ' * name_tab_amt, end=" | ")
        else:
            game.print_long_string(array[i][1], max_name_len)

        cat_tab_amt = max_cat_len - basic.length(array[i][2])
        if (cat_tab_amt >= 0):
            print(array[i][2] + ' ' * cat_tab_amt, end=" | ")
        else:
            game.print_long_string(array[i][2], max_cat_len)

        print(array[i][3], end=" | ")

        prc_tab_amt = max_prc_len - basic.length(array[i][4])
        if (prc_tab_amt >= 0):
            print(array[i][4] + ' ' * prc_tab_amt, end=" | ")
        else:
            game.print_long_string(array[i][4], max_prc_len)

        print(array[i][5])
    
def sort(array, col, ascending):
    # Mengurutkan array berdasarkan kondisi sorting

    # KAMUS LOKAL
    # row : integer

    # ALGORITMA
    row = basic.length(array)

    if (ascending):
        for i in range(1,row):
            for j in range(i+1,row):
                if (array[i][col] > array[j][col]):     # Jika elemen kolom i > kolom j, ubah posisi
                    temp = array[j]
                    array[j] = array[i]
                    array[i] = temp
    else:
        for i in range(1,row):
            for j in range(i+1,row):
                if (array[i][col] < array[j][col]):     # Jika elemen kolom i < kolom j, ubah posisi
                    temp = array[j]
                    array[j] = array[i]
                    array[i] = temp


def list_game_toko(array):
    # Mencetak array 2 dimensi berdasarkan skema sorting

    # KAMUS LOKAL
    # array : array [0...N] of array[0...5] of string
    # sorting : string

    # ALGORITMA
    sorting = input("Skema sorting: ").lower()

    if (sorting == "harga+"):                           # Urutkan harga ascending
        sort(array, 4, True)
    elif (sorting == "harga-"):                         # Urutkan harga descending  
        sort(array, 4, False)
    elif (sorting == "tahun+"):                         # Urutkan tahun ascending
        sort(array, 3, True)
    elif (sorting == "tahun-"):                         # Urutkan tahun descending
        sort(array, 3, False)
    else:
        print("Skema input tidak valid!")
        return

    print_array(array)