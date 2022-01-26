board = [[]]
rowsize = 6
colsize = 7

def makeBoard():
    global board,rowsize,colsize

    board=[]
    rows, cols = (rowsize,colsize)

    for r in range(rows):
        row = []
        for c in range(cols):
            row.append("#")
        board.append(row)

def printBoard():
    global board

    for row in range(len(board)):
        for col in range(len(board[row])):
            print(board[row][col], end=" ")
        print()
    
    for i in range(len(board[0])):
        print(str(i), end=" ")

makeBoard()
printBoard()