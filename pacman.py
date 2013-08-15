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

# actual row and col positions 
pac_row = dim_rows/2 
pac_col = dim_cols/2

# points
points = 0


def createBoard():
    global board
    
    # creates a board 30x80 (30 rows and 80 cols) with '#' everywhere
    for x in range(0,dim_rows):
        board.append(["#"]*dim_cols)

    # generate a random board. First and last row and col stays "X"
    for row in range(0,dim_rows):
        for col in range(0,dim_cols):            
            if row != 0 and row != dim_rows-1 and col != 0 and col != dim_cols-1:
                board[row][col] = getRandomChar()

    # Pacman goes in de middle position
    board[dim_rows/2][dim_cols/2] = "C"


def getRandomChar():

    rand = randint(1,20)    
    if rand < 2:    # rand = 1
        return "$"  # 5% money
    
    elif rand < 17: # 1 < rand < 17
        return "."  # 75% food
    
    else:           # 17 < rand < 20
        return "#"  # 20% wall
  

def printBoard():
    global board

    print "Points -> "+str(points)
    for row in board:
        print "".join(row)

def nextMovement():    
    # 'a' = left
    # 'd' = right
    # 'w' = up
    # 's' = down
    global board
    global pac_row
    global pac_col
    global points
    
    while True:
        mov = raw_input("Input your movement (a,d,s,w) -> ")
        if mov == "a":
            next_row = pac_row
            next_col = pac_col - 1
            break
        elif mov == "d":
            next_row = pac_row
            next_col = pac_col + 1
            break
        elif mov == "w":
            next_row = pac_row - 1
            next_col = pac_col
            break
        elif mov == "s":
            next_row = pac_row + 1
            next_col = pac_col
            break
        else:
            print "Invalid input (a,d,s,w)"
            printBoard()

    if validMovement(next_row,next_col):
        # do something
        print "Valid movement"
        board[next_row][next_col] = "C"
        board[pac_row][pac_col] = " "
        pac_row = next_row
        pac_col = next_col
        printBoard()
        
    else:
        print "Invalid movement"
        printBoard()  
        
        
def validMovement(next_row,next_col):
    global points
       
    if board[next_row][next_col] != "#":
        if board[next_row][next_col] == ".":
            points += 1
            return True
        elif board[next_row][next_col]  == "$":
            points +=10
            return True
    else:
        return False


# main
createBoard()
printBoard()

while True:
    nextMovement()
    print "actual row::"+str(pac_row)
    print "actual_col: "+str(pac_col)
