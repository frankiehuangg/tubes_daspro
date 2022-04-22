import B02, B03, F02, F03, F04, F05, F06, F07, F08, F09, F10, F11, F12, F13, F14, F15, F16, F17
import functions.files as files
import os

admin_function = ["register", "tambah_game", "ubah_game", "ubah_stok",  "topup"]
user_function = ["buy_game", "list_game", "search_my_game", "riwayat"]

def valid_role(function, role):
    if (role == "admin" and function in admin_function):
        for i in range(5):
            if (admin_function[i] == function):
                return True
    else:
        print("Maaf, anda tidak memiliki izin untuk menjalankan perintah berikut. Mintalah ke administrator untuk melakukan hal tersebut.")
    
    if (role == "user" and function in user_function):
        for i in range(4):
            if (user_function[i] == function):
                return True
    else:
        print("Maaf, anda harus menjadi user untuk melakukan hal tersebut.")
    
    return False
    
def main():
    folder = F15.load_data()

    if (folder == False):
        return

    game_array = files.csv_to_2d_array(folder+"/game.csv")
    kepemilikan_array = files.csv_to_2d_array(folder+"/kepemilikan.csv")
    riwayat_array = files.csv_to_2d_array(folder+"/riwayat.csv")
    user_array = files.csv_to_2d_array(folder+"/user.csv")

    user_data = F03.login(user_array)
    while (user_data == None):
        user_data = F03.login(user_array)

    user_id = user_data[0]
    role = user_data[1]

    is_running = True
    is_saved = True
    while (is_running):
        user_input = input("User input: ")
        os.system('cls')

        if (user_input == "register" and valid_role(user_input, role)):
            F02.register(user_array)
        elif (user_input == "tambah_game" and valid_role(user_input, role)):
            game_array = F04.tambah_game(game_array)
            is_saved = False
        elif (user_input == "ubah_game" and valid_role(user_input, role)):
            game_array = F05.ubah_game(game_array)
            is_saved = False
        elif (user_input == "ubah_stok" and valid_role(user_input, role)):
            game_array = F06.ubah_stok(game_array)
            is_saved = False
        elif (user_input == "list_game_toko"):
            F07.list_game_toko(game_array)
        elif (user_input == "buy_game" and valid_role(user_input, role)):
            riwayat_array, kepemilikan_array = F08.buy_game(riwayat_array, kepemilikan_array, user_id)
            is_saved = False
        elif (user_input == "list_game" and valid_role(user_input, role)):
            F09.list_game(user_id, kepemilikan_array, riwayat_array)
        elif (user_input == "search_my_game" and valid_role(user_input, role)):
            F10.search_my_game(kepemilikan_array)
        elif (user_input == "search_game_at_store"):
            F11.search_game_at_store(game_array)
            pass
        elif (user_input == "topup" and valid_role(user_input, role)):
            user_csv = F12.topup(user_csv)
            is_saved = False
        elif (user_input == "riwayat" and valid_role(user_input, role)):
            F13.riwayat(riwayat_array, user_id)
        elif (user_input == "help"):
            F14.help(role)
        elif (user_input == "save"):
            F16.save(game_array, kepemilikan_array, riwayat_array, user_array)
            is_saved = True
        elif (user_input == "exit"):
            F17.exit(game_array, kepemilikan_array, riwayat_array, user_array, is_saved)
            is_running = False
        elif (user_input == "kerangajaib"):
            B02.kerangajaib()
        elif (user_input == "tictactoe"):
            B03.tictactoe()
        else:
            print("Input tidak valid! Ketik 'help' untuk melihat daftar perintah.")

main()