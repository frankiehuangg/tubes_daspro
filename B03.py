
def print_board(board):
    print("Status Papan")
    for i in range(3):
        for j in range(3):
            print(board[i][j],end='')
        print()

def tictactoe():
    print("Legenda:\n# Kosong\nX Pemain 1\nO Pemain 2\n")

    board = [['#' for i in range(3)] for j in range(3)]

    print_board(board)

tictactoe()