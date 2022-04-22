def helpadmin():
    print ('==========================Menu Bantuan Bagi Admin==========================')
    print ('>>>')
    print ('1. register             - Untuk melakukan registrasi user baru')
    print ('2. login                - Untuk melakukan login ke dalam sistem')
    print ('3. tambah_game          - Untuk menambah game yang dijual pada toko')
    print ('4. ubah_game            - Untuk mengubah informasi pada game')
    print ('5. ubah_stock           - Untuk mengubah stok persediaan game pada toko')
    print ('6. list_game_toko       - Untuk melihat list game yang dijual pada toko')
    print ('7. search_game_at_store - Untuk Mencari Game yang ada di Toko')
    print ('8. topup                - Untuk menambahkan saldo kepada user ')
    print ('9. help                 - Untuk memberikan panduan penggunaan sistem')
    print ('10. save                - untuk menyimpan data setelah dilakukan perubahan')
    print ('11. exit                - Untuk menghentikan program')
    print ('12. kerangajaib         - Untuk bertanya kepada kerang ajaib')
    print ('13. tictactoe           - Untuk bermain tic tac toe')
    return

def helpuser() :
    print ('==========================Menu Bantuan Bagi User==========================')
    print ('>>>')
    print ('1. login                - Untuk melakukan login ke dalam sistem')
    print ('2. list_game_toko       - Untuk melihat list game yang dijual pada toko')
    print ('3. buy_game             - Untuk membeli game yang diinginkan')
    print ('4. list_game            - Untuk melihat daftar game yang dimiliki pengguna')
    print ('4. search_my_game       - Untuk mencari game yang dimiliki oleh pengguna')
    print ('5. search_game_at_store - Untuk Mencari Game yang ada di Toko')
    print ('6. riwayat              - Untuk melihat riwayat pembelian game pengguna')
    print ('7. help                 - Untuk memberikan panduan penggunaan sistem')
    print ('8. save                 - untuk menyimpan data setelah dilakukan perubahan ')
    print ('9. exit                - Untuk menghentikan program')
    print ('10. kerangajaib         - Untuk bertanya kepada kerang ajaib')
    print ('11. tictactoe           - Untuk bermain tic tac toe')
    return
    
def help(user_id) :
    if (user_id == 'user') :
        helpuser()
    else:
        helpadmin()
    return