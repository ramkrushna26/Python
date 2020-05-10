
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
        print("Player '" + key + "' won!!")

board={'top-l': 'o',
    'top-m': ' ',
    'top-r': 'x',
    'mid-l': ' ',
    'mid-m': 'o',
    'mid-r': ' ',
    'low-l': 'x',
    'low-m': ' ',
    'low-r': 'o'}

printBoard(board)
checkBoard(board, key='o')
