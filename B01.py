# Program Cipher
# Mengubah karakter pada file agar tidak mudah dibaca menggunakan Vigenere cipher

import functions.basic as basic, functions.files as files

key = ['t','U','B','3','5','_','d','A','S','p','R','0']                             # Kunci yang digunakan untuk cipher

def encrypt(string):
    # Mengenkripsi sebuah string

    # KAMUS LOKAL
    # string_length : integer
    # array : array[1...string_length] of char
    # char, char_key : integer
    # string : string

    # ALGORITMA
    string_length = basic.length(string)
    array = basic.string_to_array(string)

    for i in range(string_length):
        char = ord(array[i])-32
        char_key = ord(key[i%12])-32

        array[i] = chr(((char + char_key) % 96) + 32)
    
    string = basic.array_to_string(array)

    return string