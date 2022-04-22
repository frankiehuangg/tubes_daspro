import functions.files as files
import os

def save (game_array, kepemilikan_array, riwayat_array, user_array):
    dir = input ("Masukkan nama folder penyimpanan: ")
    if not os.path.exists(dir):
        os.mkdir(dir)
    files.write(dir+"/game.csv",game_array)
    files.write(dir+"/kepemilikan.csv",kepemilikan_array)
    files.write(dir+"/riwayat.csv",riwayat_array)
    files.write(dir+"/user.csv",user_array)

    print ("Saving...")
    print ("Data telah disimpan pada folder", dir)
    return