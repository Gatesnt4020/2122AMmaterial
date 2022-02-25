import random,time,os

class Connect4:

    def __init__(self):
        self.board = []
        self.rowsize = 6
        self.colsize = 7

    def makeBoard(self):            #makes the board for the user

        self.board=[]
        rows, cols = (self.rowsize,self.colsize)

        for r in range(rows):
            row = []
            for c in range(cols):
                row.append("  ")
            self.board.append(row)

    def printBoard(self):           #prints the board after it's made and after it needs to update a player move
        i = self.colsize*5-1
        for row in range(len(self.board)):
            print("_"*i)
            for col in range(len(self.board[row])):
                print(self.board[row][col], end=" | ")
            print()
        
        for i in range(len(self.board[0])):
            print(str(i), end=" "*4)
        print()

    def goodSpot(self,row,col):      #returns a T or F if the place is ok to place
        if row[col] == "  ":
            return True
        return False

    def playerSpot(self):           #user picks a col to place
        goodSpot = False
        while goodSpot is False:
            ui = input("Please choose a spot between 0-6 ")
            ui = ui.replace(" ", "")
            if ui == "":            #checks if user is inputing nothing
                continue
            if(not ui.isnumeric()): #checks if the user is inputing a number
                continue
            if int(ui) < 0 or int(ui) > self.rowsize:#checks if the user is inputing a valid number
                continue
            ui = int(ui)
            if self.board[0][ui] !="  ":        #check if the user is inputing a colum that is full
                print("This column is full please pick another spot between 0-6")
                continue
            goodSpot=True
        return ui

    def playerPiece(self):          #user picks the symbol that they'll use to play
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

    def play(self,pcol,sym):         #places the users symbol if the spot if good
        #https://www.geeksforgeeks.org/python-reversed-function/
        for row in reversed(self.board):
            if self.goodSpot(row,pcol):
                row[pcol] = " " + sym
                return True
        return False

    def checkForWinner(self,sym,board=None):#checks to see if anyone has won
        if board == None:
            board = self.board
        #check for horizontal wins
        for row in board:
            for i in range(0,len(row)):
                if i < len(row)-3:
                    if row[i] == row[i+1] == row[i+2] == row[i+3] == " "+sym:
                        return True
        #check for vertical wins
        for row in range(self.rowsize-3):
            for i in range(self.colsize):
                if board[row][i] == board[row+1][i] == board[row+2][i] == board[row+3][i] == " "+sym:
                    return True
        #check for ascending diagonals wins
        for row in range(self.rowsize):
            for col in range(self.colsize-3):
                if board[row][col] == board[abs(row-1)][abs(col+1)] == board[abs(row-2)][col+2] == board[abs(row-3)][col+3] == " "+sym:
                    return True
        #check for descending diagonal wins
        for row in range(self.rowsize):
            for col in range(self.colsize):
                if board[row][col] == board[abs(row-1)][abs(col-1)] == board[abs(row-2)][abs(col-2)] == board[abs(row-3)][abs(col-3)] == " "+sym:
                    return True
    
    def tie(self,board=None):
        if board == None:
            board = self.board
        for row in range(len(board)):
            for col in range(len(board)):
                if (board[row][col]) == "  ":
                    return False
        return True
        
c = Connect4()

print(f"""OBJECTIVE:
        To be the first player to connect 4 of the same colored discs(symbol) in a row (either vertically, horizontally, or diagonally
HOW TO PLAY:
        First, decide who goes first and what color each player will have. 
        Players must alternate turns, and only one disc can be dropped in each turn. 
        On your turn, drop one of your colored discs from the top into any of the seven slots. 
        The game ends when there is a 4-in-a-row or a stalemate.
        The starter of the previous game goes second on the next game.\nhttps://www.gamesver.com/the-rules-of-connect-4-according-to-m-bradley-hasbro/\n""")
game = True
while game:
    gameMode = input("what would you like to do PvP, PvC, or CvC ").lower()
    while gameMode != "pvp" and gameMode != "pvc" and gameMode != "cvc":
        gameMode = input("what would you like to do PvP, PvC, or CvC ").lower()
    c.makeBoard()
    players = c.playerPiece()
    i=0
    winner = False
    c.printBoard()
    if gameMode == "pvp":
        while not winner:
            time.sleep(1)
            if i%2 ==0:
                sym = players[0]
                currentPlayer = sym
            else:
                sym = players[1]
                currentPlayer = sym
            print(f"It is currently {currentPlayer} turn")
            spot = c.playerSpot()
            if not c.play(spot, sym):
                print(f"colum {spot} is full")
            if c.checkForWinner(sym):
                winner = True
                c.printBoard()
                print(f"Winner is {currentPlayer}")
            if c.tie():
                winner = True
                c.printBoard()
                print("No more moves lets so its a tie")
            i+=1
            os.system('cls' if os.name=='nt' else 'clear')
            c.printBoard()
    elif gameMode == "pvc":
        while not winner:
            time.sleep(2)
            if i%2 ==0:
                sym = players[0]
                currentPlayer = sym
                spot = c.playerSpot()
            else:
                sym = players[1]
                currentPlayer = sym
                spot = random.randint(0,6)
            if not c.play(spot, sym):
                print(f"colum {spot} is full")
                while c.play(spot, sym) != True:
                    spot = random.randint(0,6)
                    continue
            if c.checkForWinner(sym):
                winner = True
                c.printBoard()
                print(f"Winner is {currentPlayer}")
            if c.tie():
                winner = True
                c.printBoard()
                print("No more moves lets so its a tie")
            i+=1
            os.system('cls' if os.name=='nt' else 'clear')
            c.printBoard()
    else:
        print("There might be an issue with the bots skipping but it's fixed in pvp and pvc")
        while not winner:
            time.sleep(2)
            if i%2 ==0:
                sym = players[0]
                currentPlayer = sym
                spot = random.randint(0,6)
            else:
                sym = players[1]
                currentPlayer = sym
                spot = random.randint(0,6)
            if not c.play(spot, sym):
                print(f"colum {spot} is full")
                while c.play(spot, sym) != True:
                    spot = random.randint(0,6)
                    continue
            if c.checkForWinner(sym):
                winner = True
                c.printBoard()
                print(f"Winner is {currentPlayer}")
            if c.tie():
                winner = True
                c.printBoard()
                print("No more moves lets so its a tie")
            i+=1
            os.system('cls' if os.name=='nt' else 'clear')
            c.printBoard()
    playAgain = input("Do  you want to play again (y/n) ").lower()
    while playAgain != "y" and playAgain != "n":
        playAgain = input("Do  you want to play again (y/n) ").lower()
    if playAgain == "y":
        c = Connect4()
    else:
        game = False