# Program Basic (Multifungsi)


def string_to_array(string):
    # Mengubah string menjadi array of char

    # KAMUS LOKAL
    # col : integer
    # array : array [0...col-1] of char

    # ALGORITMA
    col = length(string)
    array = ['']*col

    for i in range(col):
        array[i] = string[i]
    
    return array


def length(array):
    # Mengembalikan panjang array/string

    # KAMUS LOKAL
    # i : integer

    # ALGORITMA
    i = 0
    while(1):
        try:
            array[i]
            i += 1
        except:
            return i


def array_split(array, start, finish):
    # Mengembalikan array dari start hingga finish (array slicing)

    # KAMUS LOKAL
    # n : integer
    # a : array [start...finish] of string

    # ALGORITMA
    n = finish-start+1
    a = [0]*n

    for i in range(n):
        a[i] = array[start]
        start += 1

    return a


def string_split(string, start, finish):
    # Mengembalikan string dari start hingga finish (string slicing)

    # KAMUS LOKAL
    # a : array [start...finish] of char

    # ALGORITMA
    a = array_split(string, start, finish)
    
    return array_to_string(a)


def array_to_string(array):
    # Mengubah array of char menjadi string

    # KAMUS LOKAL
    # string_length : integer
    # string : string

    # ALGORITMA
    string_length = length(array)
    string = ''

    for i in range(string_length):
        string += array[i]
    
    return string


def add_row(array_2d, array):
    # Menambahkan array pada akhir array 2 dimensi

    # KAMUS LOKAL
    # row_length, col_length : integer
    # new_array = array[0...col_length-1] of array[0...row_length-1] of string

    # ALGORITMA
    row_length = length(array_2d)
    col_length = length(array_2d[0])

    new_array = [['' for i in range(col_length)] for j in range(row_length+1)]

    for i in range(row_length):
        for j in range(col_length):
            new_array[i][j] = array_2d[i][j]

    new_array[-1] = array

    return new_array