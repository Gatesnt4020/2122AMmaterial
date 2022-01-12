#sampleBoard = [["1", "2", "3"],["4", "5", "6"],["7", "8", "9"]]

'''
for row in range(len(sampleBoard)):
    for columns in range(len(sampleBoard[row])):
        print(sampleBoard[row][columns])
'''

def printBoard(board):
    for r in range(len(board)):
        print(board[r][0]+"|"+board[r][1]+"|"+board[r][2])
        if r<len(board)-1:
            print("-"*5)

def catGame(board):
    #check every spot to see if there is somthing
    for row in range(len(board)):    #range(len(sampleBoard))->[0,1]
        for colums in range(len(board[row])):
            if (board[row][colums]) == " ":
                return False
    print("CAT GAME!")
    return True     #return stop the function and give a vaule back

def checkForWinner(board):
    #check horizontallly
    for r in range(len(board)):
        if (board[r][0] == board[r][1] and board[r][1] == board[r][2] and board[r][0]  != " "):
            print("Winner winner turkey dinner!")
            printBoard(board)
            return True
    #check vertically
        for c in range(len(board)):
            if (board[c][0] == board[c][1] and board[c][1] == board[c][2] and board[c][0]  != " "):
                print("Winner winner turkey dinner!")
                printBoard(board)
                return True
    #switching our symbols

def chooseSpot(r,c,symbol,board):
    if board[r][c] == " ":
        board[r][c]=symbol
        return True
    return False

board=[[" ", " ", " "],[" ", " ", " "],[" ", " ", " "]]

symbol="X"
while symbol!="Q":
    printBoard(board)
    goodSpot=False
    while not goodSpot:
        r= int(input("row: "))-1
        c = int(input("col: "))-1
        if ((0<=r<=2) and (0<=c<=2)):
            if (not chooseSpot(r,c,symbol,board)):
                print("Spots Taken")
            else:
                goodSpot = True
    
    #check for a winner or CAT
    if catGame(board) or checkForWinner(board):
        symbol="Q"
    #switching our symbols
    if symbol=="X":
        symbol="O"
    else:
        symbol="X"