# Program Files (Multifungsi)
# Frankie Huang/16521266

import functions.basic as basic


def csv_to_2d_array(dir):
    # Mengembalikan array 2 dimensi berupa isi dari file csv

    # KAMUS LOKAL
    # lines : array [0...N] of string
    # lines_length, line_length : integer
    # col : integer
    # array : array [0...lines_length] of array [0...col] of char

    # ALGORITMA
    csv = open(dir, 'r')

    lines = csv.readlines()

    lines_length = basic.length(lines)
    line_length = basic.length(lines[0])
    col = 0
    for i in range(line_length):
        if (lines[0][i] == ';'):
            col += 1
    
    array = [['' for i in range(col)] for j in range(lines_length)]

    for i in range(lines_length):
        for j in range(col):
            array[i][j] = read_cell(lines[i], j)
    
    return array


def append(dir, string):
    # Menambahkan baris pada akhir file

    # ALGORITMA
    csv = open(dir, 'a')

    csv.write('\n')
    csv.write(string)

    csv.close()


def write(dir, array):
    # Membuat file baru

    # KAMUS LOKAL
    # row_length, col_length : integer
    # string : string

    # ALGORITMA
    row_length = basic.length(array)
    col_length = basic.length(array[0])
    string = ""

    for i in range(row_length):
        for j in range(col_length):
            string += array[i][j]+';'
        string += '\n'
    
    csv = open(dir, 'w')

    csv.write(string)

    csv.close()


def read_cell(string, col):
    # Mengembalikan cell pada kolom ke-n pada baris

    # KAMUS LOKAL
    # string_length : integer
    # st : string

    # ALGORITMA
    string_length = basic.length(string)
    st = ""

    for i in range(string_length):
        if (col == 0):
            if (string[i] == ';' or string[i] == '\n'):
                break
            st += string[i]
    
        if (string[i] == ';'):
            col -= 1
        
    return st