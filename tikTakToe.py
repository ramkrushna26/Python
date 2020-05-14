
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
        return ("Player %s won!!" % key)
    elif board['top-l'] == key and board['top-m'] == key and board['top-r'] == key:
        return ("Player %s won!!" % key)
    elif board['mid-l'] == key and board['mid-m'] == key and board['mid-r'] == key:
        return ("Player %s won!!" % key)
    elif board['low-l'] == key and board['low-m'] == key and board['low-r'] == key:
        return ("Player %s won!!" % key)
    elif board['low-l'] == key and board['mid-m'] == key and board['top-r'] == key:
        return ("Player %s won!!" % key)
    elif board['top-l'] == key and board['mid-l'] == key and board['low-l'] == key:
        return ("Player %s won!!" % key)
    elif board['top-m'] == key and board['mid-m'] == key and board['low-m'] == key:
        return ("Player %s won!!" % key)
    elif board['top-r'] == key and board['mid-r'] == key and board['low-r'] == key:
        return ("Player %s won!!" % key)
    else:
        return "play again"

def getInput(boardPlaces, key):
    if !board['top-l']:
        print("1 for 'top-l'", end=" ")
    if !board['top-m']:
        print("2 for 'top-m'", end=" ")
    if !board['top-r']:
        print("3 for 'top-r'", end=" ")
    if !board['top-l']:
        print("4 for 'mid-l'", end=" ")
    if !board['top-l']:
        print("5 for 'mid-m'", end=" ")
    if !board['top-l']:
        print("6 for 'mid-r'", end=" ")
    if !board['top-l']:
        print("7 for 'low-l'", end=" ")
    if !board['top-l']:
        print("8 for 'low-m'", end=" ")
    if !board['top-l']:
        print("9 for 'low-r'", end=" ")

board = {'top-l': 'o',
    'top-m': ' ',
    'top-r': 'x',
    'mid-l': ' ',
    'mid-m': 'o',
    'mid-r': ' ',
    'low-l': 'x',
    'low-m': ' ',
    'low-r': 'o'}

player1 = input("Who you want to be? x or o? : ").strip().lower()
if player1 == "x":
    player2 = "o"
else:
    player2 = "x"

boardPlaces = board.keys()

if board['top-m']:
    print("Empty")

printBoard(board)
result = checkBoard(board, key='o')
print(result)
