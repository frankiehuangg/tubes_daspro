# Program Binomo
# Program multifungsi yang bisa digunakan seperti aplikasi penyedia layanan software

import B02, B03, F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12, F13, F14, F15, F16, F17
import functions.files as files
import os

admin_function = ["register", "tambah_game", "ubah_game", "ubah_stok",  "topup"]
user_function = ["buy_game", "list_game", "search_my_game", "riwayat"]

def valid_role(function, role):
    # Cek apakah pengguna dengan role input bisa menggunakan fungsi

    # ALGORITMA
    if (role == "admin"):
        for i in range(5):
            if (admin_function[i] == function):
                return True
        
        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
    
    if (role == "user"):
        for i in range(4):
            if (user_function[i] == function):
                return True
        
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
        
    return False
    
def main():
    # Program utama yang akan jalan saat program berjalan

    # KAMUS LOKAL
    # game_array, kepemilikan_array, riwayat_array, user_array = array of array of string
    # user_data = array of string
    # user_id, role = string
    # is_running, is_saved = boolean
    # user_input = string

    # ALGORITMA
    folder = F15.load_data()

    # Cek apakah folder terdapat di direktori
    if (folder == False):
        return

    # Buka semua file csv sebagai array 2d
    game_array = files.csv_to_2d_array(folder+"/game.csv")
    kepemilikan_array = files.csv_to_2d_array(folder+"/kepemilikan.csv")
    riwayat_array = files.csv_to_2d_array(folder+"/riwayat.csv")
    user_array = files.csv_to_2d_array(folder+"/user.csv")

    # Lakukan proses login (validasi) dan ambil data user id dan role
    user_data = F03.login(user_array)
    while (user_data == None):
        user_data = F03.login(user_array)

    user_id = user_data[0]
    role = user_data[1]

    # Cek apakah program masih berjalan (belum exit) dan apakah ada data yang diubah (pada beberapa fungsi tertentu)
    is_running = True
    is_saved = True
    while (is_running):
        # Ambil input pengguna dan hapus konsol
        user_input = input("\nUser input: ")
        os.system('cls')

        if (user_input == "register"):                                                                          # Lakukan register
            if (valid_role(user_input, role)):
                F02.register(user_array)
        elif (user_input == "login"):                                                                           # Jalankan fungsi login dan ubah data user jika berhasil
            user_data = F03.relog(user_array)
            if (user_data != None):
                user_id = user_data[0]
                role = user_data[1]
        elif (user_input == "tambah_game"):                                                                     # Tambahkan game pada game_array
            if (valid_role(user_input, role)):
                game_array = F04.tambah_game(game_array)
                is_saved = False
        elif (user_input == "ubah_game"):                                                                       # Ubah data game pada game_array
            if (valid_role(user_input, role)):
                game_array = F05.ubah_game(game_array)
                is_saved = False
        elif (user_input == "ubah_stok"):                                                                       # Ubah stok game pada game_array
            if (valid_role(user_input, role)):
                game_array = F06.ubah_stok(game_array)
                is_saved = False
        elif (user_input == "list_game_toko"):                                                                  # Cetak semua data pada game_array
            F07.list_game_toko(game_array)
        elif (user_input == "buy_game"):                                                                        # Membeli game di toko
            if (valid_role(user_input, role)):
                game_array, kepemilikan_array, riwayat_array, user_array = F08.buy_game(game_array, kepemilikan_array, riwayat_array, user_array, user_id)
                is_saved = False
        elif (user_input == "list_game"):                                                                       # Mencetak semua game yang dimiliki pengguna
            if (valid_role(user_input, role)):
                F09.list_game(user_id, kepemilikan_array, riwayat_array)
        elif (user_input == "search_my_game"):                                                                  # Cari game yang dimiliki pengguna
            if (valid_role(user_input, role)):
                F10.search_my_game(user_id, riwayat_array, game_array)
        elif (user_input == "search_game_at_store"):                                                            # Cari game yang ada di toko
            F11.search_game_at_store(game_array)
            pass
        elif (user_input == "topup"):                                                                           # Topup (ubah saldo pengguna) dan simpan data user_array
            if (valid_role(user_input, role)):
                user_array = F12.topup(user_array)
                is_saved = False
        elif (user_input == "riwayat"):  # NOT
            if (valid_role(user_input, role)):
                F13.riwayat(riwayat_array, user_id)
        elif (user_input == "help"):                                                                            # Cetak semua fungsi yang bisa diakses user
            F14.help(role)
        elif (user_input == "save"):                                                                            # Write ke-4 array pada folder yang diinput
            F16.save(game_array, kepemilikan_array, riwayat_array, user_array)
            is_saved = True
        elif (user_input == "exit"):                                                                            # Keluar dari program
            F17.exit(game_array, kepemilikan_array, riwayat_array, user_array, is_saved)
            is_running = False
        elif (user_input == "kerangajaib"):                                                                     # Bermain kerang ajaib
            B02.kerangajaib()
        elif (user_input == "tictactoe"):                                                                       # Bermain tic tac toe
            B03.tictactoe()
        else:                                                                                                   # Cetak jika input tidak valid
            print("Input tidak valid! Ketik 'help' untuk melihat daftar perintah.")

main()