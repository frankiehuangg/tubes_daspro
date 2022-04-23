import F16

def exit(game_array, kepemilikan_array, riwayat_array, user_array, is_saved):
    if (not is_saved):
        program = True
        while (program == True) :
            akhiri = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)").lower()
            while ((akhiri != 'y') and (akhiri != 'n')):
                akhiri = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)").lower()
            if (akhiri == 'y'):
                F16.save(game_array, kepemilikan_array, riwayat_array, user_array)    
                break 
            elif (akhiri == 'n'):
                break
    return