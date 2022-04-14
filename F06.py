# Program UbahStok
# Mengubah stok game pada files/game.csv
# Frankie Huang/16521266

import functions.files as files, functions.game as game


def ubah_stok():
    # Mengembalikan array berupa data stok pada files/game.csv yang sudah diubah

    # KAMUS LOKAL
    # array : array [0...N] of array[0...5] of string 
    # id_game, nama_game : string
    # row, stok, jumlah : integer

    # ALGORITMA
    array = files.csv_to_2d_array("files/game.csv")

    id_game = input("Masukkan ID game: ")
    
    if (not game.check_id_game(array, id_game)):                                         # Jika hasil cek mereturn 0, hentikan program
        return
    
    row = game.check_id_game(array, id_game)
    nama_game = array[row][1]
    stok = int(array[row][5])

    try:                                                                            # Cek apakah jumlah bisa diubah menjadi integer (dari string)
        jumlah = int(input("Masukkan jumlah: "))
    except:
        print("Jumlah tidak valid!")
        return

    if (stok+jumlah < 0):                                                           # Jika hasil perubahan bernilai negatif, hentikan program
        print("Stok game "+nama_game+" gagal dikurangi karena stok kurang. Stok sekarang: "+str(stok)+" (< "+str(abs(jumlah))+')')
        return

    array[row][5] = str(stok+jumlah)

    if (jumlah < 0):                                                                # Jika nilai jumlah negatif, print "berhasil dikurangi"
        print("Stok game "+nama_game+" berhasil dikurangi. Stok sekarang: "+str(stok+jumlah))
    else:                                                                           # Jika tidak, print "berhasil ditambahkan"
        print("Stok game "+nama_game+" berhasil ditambahkan. Stok sekarang: "+str(stok+jumlah))

    return array