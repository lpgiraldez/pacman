"""
PACMAN
Python 2.7.5
Windws 7
"""

from random import randint

# board variable and dimensions
board = []
dim_rows = 30
dim_cols = 80

def createBoard():

    # creates a board 30x80 (30 rows and 80 cols) with '#' everywhere
    for x in range(0,dim_rows):
        board.append(["#"]*dim_cols)
    
    for row in range(0,dim_rows):
        for col in range(0,dim_cols):
            # generate a random board. First and last row and col stays "X"
            if row != 0 and row != dim_rows-1 and col != 0 and col != dim_cols-1:
                board[row][col] = getRandomChar()

def getRandomChar():

    rand = randint(1,20)    
    if rand < 2:    # rand = 1
        return "$"  # 5% money
    
    elif rand < 17: # 1 < rand < 17
        return "."  # 75% food
    
    else:           # 17 < rand < 20
        return "#"  # 20% wall
    

def printBoard():

    for row in board:
        print "".join(row)
        

createBoard()
printBoard()
