import argparse, os

def load_data():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", nargs="?")
    args = parser.parse_args()
    if not args.folder : #Tidak ada nama folder yang diinputkan
        print ("Tidak ada nama folder yang diberikan!")
        return False
    else :
        if os.path.exists(args.folder): #Nama folder tersedia
            print ("Loading…")
            print ("Selamat datang di antarmuka “Binomo”")
            return args.folder            
        else : #Nama folder yang dimasukkan tidak tersedia
            print (f"Folder '{args.folder}' tidak ditemukan.")
            return False