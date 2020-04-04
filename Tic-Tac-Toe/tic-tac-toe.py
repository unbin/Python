from macros import BOARDW
from macros import BOARDH

# FUNCTIONS

def drawBoard(board):
    for row in board:
        print("\n" + '-' * 13 + "\n| ", end = "")
        for char in row:
            print(char + " | ", end = "")
    print("\n" + '-' * 13, end = '\n\n')

def gameover():
    return 0


def checkGameover():
    return 0

# VARIABLES

class player:
    turn = False
    char = 'X'

board = [[' ', ' ', ' '],
         [' ', ' ' ,' '],
         [' ', ' ', ' ']]


# MAIN

print(" Welcome to Tic-Tac-Toe!\n" + "-" * 25)

while (True):
    print("Select the your character (X/o):", end = ' ')
    usr = input()
    if (usr != 'x' and usr != 'X' and usr != 'o' and usr != 'O'):
        print("Please input X or O")
    else:
        player.char = usr.upper()
        if usr == 'o' or usr == 'O':
            player.turn = False
        break

while (not checkGameover):
    drawBoard(board)
