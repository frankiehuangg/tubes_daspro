# Program ListGameToko
# Mencetak semua game di files/game.csv berdasarkan skema sorting

import functions.files as files, functions.basic as basic


def print_array(array):
    # Mencetak array 2 dimensi

    # KAMUS LOKAL
    # row_length, col_length, num = 1

    # ALGORITMA
    row_length = basic.length(array)
    col_length = basic.length(array[0])
    num = 1

    for i in range(1,row_length):
        print(str(num) + ". ", end='')
        for j in range(1,col_length):
            if (j == col_length-1):
                print(array[i][j])
                continue
            print(array[i][j], end="\t|")
        num += 1

    
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

    print_array(array)