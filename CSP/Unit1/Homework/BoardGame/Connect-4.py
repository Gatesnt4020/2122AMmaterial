board = [[]]
rowsize = 6
colsize = 7
gameOver=False
turn = 0

def makeBoard():            #makes the board for the user
    global board,rowsize,colsize

    board=[]
    rows, cols = (rowsize,colsize)

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append("#")
        board.append(row)

def printBoard():           #prints the board after it's made and after it needs to update a player move
    global board

    for row in range(len(board)):
        print("_"*colsize*4)
        for col in range(len(board[row])):
            print(board[row][col], end=" | ")
        print()
    
    for i in range(len(board[0])):
        print(str(i), end=" "*3)

def goodSpot(row,col):      #returns a T or F if the place is ok to place
    if row[col] == "#":
        return True
    return False

def playerSpot():           #user picks a col to place
    ui = input("Please choose a spot between 0-6 ")
    while(not ui.isnumeric()):
        ui = input("Please choose a spot between 0-6 ")
    ui=int(ui)
    while ui < 0 or ui > rowsize:
        ui = input("Please choose a spot between 0-6 ")
    while board[0][ui] !="#":
        print("This column is full please pick another spot between 0-6")
        playerSpot()
    return ui

def playerPiece():          #user picks the symbol that they'll use to play
    p1 = input("Choose a symbol 'X' or 'O' ")
    while True:
        if p1.upper() == "X":
            p2="O"
            print("You are X and player 2 is O")
            return p1.upper(),p2
        elif p1.upper() == "O":
            p2="X"
            print("You are O and player 2 is X")
            return p1.upper(),p2
        else:
            p1 = input("Choose a symbol 'X' or 'O' ")

def play(pcol,sym):         #places the users symbol
    #https://www.geeksforgeeks.org/python-reversed-function/
    for i in reversed(board):
        if goodSpot(i,pcol):
            i[pcol] = "" + sym
            return True
        return False

def checkForWinner(sym,board):#checks to see if anyone has won
    #check for the line wins
    for row in board:
        for i in range(0,len(row)):
            if i < len(row)-3:
                if row[i] == row[i+1] == row[i+2] == row[i+3] == ""+sym:
                    return True
    #check for the diagonals win 