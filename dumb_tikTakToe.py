
from random import randint

def printBoard(board):
    # This function prints the board
    print(board['top-l'] + " | " + board['top-m'] + " | " + board['top-r'])
    print("----------")
    print(board['mid-l'] + " | " + board['mid-m'] + " | " + board['mid-r'])
    print("----------")
    print(board['low-l'] + " | " + board['low-m'] + " | " + board['low-r'])


def checkBoard(board, key):
    # This functions checks for possible winning patterns
    if board['top-l'] == key and board['mid-m'] == key and board['low-r'] == key:
        return True
    elif board['top-l'] == key and board['top-m'] == key and board['top-r'] == key:
        return True
    elif board['mid-l'] == key and board['mid-m'] == key and board['mid-r'] == key:
        return True
    elif board['low-l'] == key and board['low-m'] == key and board['low-r'] == key:
        return True
    elif board['low-l'] == key and board['mid-m'] == key and board['top-r'] == key:
        return True
    elif board['top-l'] == key and board['mid-l'] == key and board['low-l'] == key:
        return True
    elif board['top-m'] == key and board['mid-m'] == key and board['low-m'] == key:
        return True
    elif board['top-r'] == key and board['mid-r'] == key and board['low-r'] == key:
        return True
    return False


def insertIntoBoard(board, player, position):
    if position == 1:
        board['top-l'] = player
    if position == 2:
        board['top-m'] = player
    if position == 3:
        board['top-r'] = player
    if position == 4:
        board['mid-l'] = player
    if position == 5:
        board['mid-m'] = player
    if position == 6:
        board['mid-r'] = player
    if position == 7:
        board['low-l'] = player
    if position == 8:
        board['low-m'] = player
    if position == 9:
        board['low-r'] = player


def getInput(board, key):
    if not board['top-l']:
        print("1 for 'top-left'")
    if not board['top-m']:
        print("2 for 'top-middle'")
    if not board['top-r']:
        print("3 for 'top-right'")
    if not board['mid-l']:
        print("4 for 'mid-lelf'")
    if not board['mid-m']:
        print("5 for 'mid-middle'")
    if not board['mid-r']:
        print("6 for 'mid-right'")
    if not board['low-l']:
        print("7 for 'low-left'")
    if not board['low-m']:
        print("8 for 'low-middle'")
    if not board['low-r']:
        print("9 for 'low-right'")
    return int(input("Enter " + key + " position: ").strip())

board = {'top-l': '',
    'top-m': '',
    'top-r': '',
    'mid-l': '',
    'mid-m': '',
    'mid-r': '',
    'low-l': '',
    'low-m': '',
    'low-r': ''}

player1 = input("Who you want to be? x or o? : ").strip().lower()
if player1 == "x":
    player2 = "o"
else:
    player2 = "x"

boxFilled = []
result = False

while result != True:
    player1Input = getInput(board, player1)
    insertIntoBoard(board, player1, player1Input)
    boxFilled.append(player1Input)
    printBoard(board)
    result = checkBoard(board, player1)
    if result == True:
        print("You won!")
        break
    player2Input = randint(1, 9)
    for i in range(0, 9):
        if player2Input in boxFilled:
            player2Input = randint(1, 9)
            continue
        else:
            break
    insertIntoBoard(board, player2, player2Input)
    boxFilled.append(player2Input)
    print("After Bot:")
    printBoard(board)
    result = checkBoard(board, player2)
    if result == True:
        print("Bot won!")
        break
