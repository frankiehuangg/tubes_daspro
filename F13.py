import functions.basic as basic, functions.files as files

def riwayat(array, user_id):
    rows = basic.length(array)                                                                          # Menghitung jumlah baris yang ada
    
    if rows == 1:                                                                                       # Jika baris hanya 1, user tidak punya riwayat pembelian game
        print("Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.")
        return
    
    print("Daftar game:")
    num = 1                                                                                             # List dimulai dengan angka 1
    
    for i in range(rows):
        if array[i][3] == user_id:
            print(str(num)+".", array[i][0],"|", array[i][1],"|", array[i][2],"|", array [i][4],"|")
            num += 1