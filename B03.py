# Program TicTacToe
# Menjalankan permainan TicTacToe

def print_board(board):
    # Mencetak papan permainan pada layar

    # ALGORITMA
    print("Status Papan")
    for i in range(3):
        for j in range(3):
            print(board[i][j],end='')
        print()

def is_valid_input(X, Y, board):
    # Mengecek apakah input pengguna valid

    # ALGORITMA
    if (X < 1 or X > 3):                                                                                    # Cek apakah X antara 1 dan 3
        print("Kotak tidak valid.")
        return False 
        
    if (Y < 1 or Y > 3):                                                                                    # Cek apakah Y antara 1 dan 3
        print("Kotak tidak valid.")
        return False 

    if (board[Y-1][X-1] != '#'):                                                                            # Cek apakah kotak sudah terisi
        print("Kotak sudah terisi. Silakan pilih kotak lain.")
        return False 
    
    return True

def check_cond(board):
    # Mengecek kondisi apakah ada pemenang atau seri atau tidak keduanya

    # KAMUS LOKAL
    # all_filled : boolean

    # ALGORITMA
    for i in range(3):
        if (board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != '#'):              # Cek secara vertikal
            print("Pemain “"+board[i][0]+"” menang.")
            return False
            
    for i in range(3):
        if (board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != '#'):              # Cek secara horizontal
            print("Pemain “"+board[i][0]+"” menang.")
            return False

    if (board[0][0] == board[1][1] and board[0][0] == board[2][2] and board[0][0] != '#'):                  # Cek secara diagonal \
        print("Pemain “"+board[0][0]+"” menang.")
        return False
    
    if (board[0][2] == board[1][1] and board[0][0] == board[2][0] and board[0][2] != '#'):                  # Cek secara diagonal /
        print("Pemain “"+board[0][2]+"” menang.")
        return False

    all_filled = True
    for i in range(3):
        for j in range(3):
            if (board[i][j] == '#'):                                                                        # Cek apakah semua kotak sudah terisi
                all_filled = False
                break
    
    if (all_filled):
        print("Permainan seri, tidak ada pemenang.")
        return False

    return True

def tictactoe():
    # Menjalankan permainan TicTacToe

    # KAMUS LOKAL
    # move : integer
    # board : array[0...2] of array[0...2] of integer
    # X, Y : integer

    # ALGORITMA
    move = 0
    board = [['#' for i in range(3)] for j in range(3)]
    
    while (check_cond(board)):
        print("Legenda:\n# Kosong\nX Pemain 1\nO Pemain 2\n")

        print_board(board)

        print(move)
        if (move % 2 == 0):
            print("Giliran pemain “X”:")
        else:
            print("Giliran pemain “O”:")
        X = int(input("X: "))
        Y = int(input("Y: "))
        while (not is_valid_input(X, Y, board)):
            if (move % 2 == 0):
                print("Giliran pemain “X”:")
            else:
                print("Giliran pemain “O”:")
            X = int(input("X: "))
            Y = int(input("Y: "))

        if (move % 2 == 0):
            board[Y-1][X-1] = "X"
        else:
            board[Y-1][X-1] = "O"
        
        move += 1