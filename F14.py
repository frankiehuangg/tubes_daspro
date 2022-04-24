def helpadmin(): #Mengeluarkan menu help untuk admin
    print ('==========================Menu Bantuan Bagi Admin==========================')
    print ('1. register             - Untuk melakukan registrasi user baru')
    print ('2. login                - Untuk melakukan login ke dalam sistem')
    print ('3. tambah_game          - Untuk menambah game yang dijual pada toko')
    print ('4. ubah_game            - Untuk mengubah informasi pada game')
    print ('5. ubah_stock           - Untuk mengubah stok persediaan game pada toko')
    print ('6. list_game_toko       - Untuk melihat list game yang dijual pada toko')
    print ('7. search_game_at_store - Untuk Mencari Game yang ada di Toko')
    print ('8. topup                - Untuk menambahkan saldo kepada user ')
    print ('9. kerangajaib          - Untuk bertanya kepada kerang ajaib')
    print ('10. tictactoe           - Untuk bermain tic tac toe')
    print ('11. help                - Untuk memberikan panduan penggunaan sistem')
    print ('12. save                - untuk menyimpan data setelah dilakukan perubahan')
    print ('13. exit                - Untuk menghentikan program')
    return

def helpuser() : #Mengeluarkan menu help untuk user
    print ('==========================Menu Bantuan Bagi User==========================')
    print ('1. login                - Untuk melakukan login ke dalam sistem')
    print ('2. list_game_toko       - Untuk melihat list game yang dijual pada toko')
    print ('3. buy_game             - Untuk membeli game yang diinginkan')
    print ('4. list_game            - Untuk melihat daftar game yang dimiliki pengguna')
    print ('4. search_my_game       - Untuk mencari game yang dimiliki oleh pengguna')
    print ('5. search_game_at_store - Untuk Mencari Game yang ada di Toko')
    print ('6. riwayat              - Untuk melihat riwayat pembelian game pengguna')
    print ('7. kerangajaib          - Untuk bertanya kepada kerang ajaib')
    print ('8. tictactoe            - Untuk bermain tic tac toe')
    print ('9. help                 - Untuk memberikan panduan penggunaan sistem')
    print ('10. save                - untuk menyimpan data setelah dilakukan perubahan ')
    print ('11. exit                - Untuk menghentikan program')
    return
    
def help(role) : 
    #Program utama yang memanggil prosedur lain sesuai dengan status pengguna (admin/user)
    if (role == 'user') :
        helpuser()
    else:
        helpadmin()
    return
