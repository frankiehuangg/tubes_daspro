import functions.basic as basic, functions.game as game

def riwayat(array, user_id):
    rows = basic.length(array)                                                                          # Menghitung jumlah baris yang ada

    max_name_len = 20
    max_prc_len = 6

    num = 0

    for i in range(1, rows):
        if (array[i][3] == user_id):
            num += 1
    
    if num == 0:                                                                                       # Jika baris hanya 1, user tidak punya riwayat pembelian game
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
        return
    
    num = 1                                                                                             # List dimulai dengan angka 1
    print("Daftar game:")
    
    for i in range(1, rows):
        if (array[i][3] == user_id):
            print(num, end=". ")

            print(array[i][0], end=" | ")

            name_tab_amt = max_name_len - basic.length(array[i][1])
            if (name_tab_amt >= 0):
                print(array[i][1] + ' ' * name_tab_amt, end=" | ")
            else:
                game.print_long_string(array[i][1], max_name_len)

            prc_tab_amt = max_prc_len - basic.length(array[i][2])
            if (prc_tab_amt >= 0):
                print(array[i][2] + ' ' * prc_tab_amt, end=" | ")
            else:
                game.print_long_string(array[i][2], max_prc_len)

            print(array[i][4], end=" |\n")
