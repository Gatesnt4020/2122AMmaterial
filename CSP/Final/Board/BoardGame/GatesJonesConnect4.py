import random,time
import Connect4
c=Connect4

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
                currentPlayer = "Player 1"
                sym = players[0]
            else:
                currentPlayer = "Player 2"
                sym = players[1]
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
            c.printBoard()
    elif gameMode == "pvc":
        while not winner:
            time.sleep(2)
            if i%2 ==0:
                currentPlayer = "Player 1"
                sym = players[0]
                spot = c.playerSpot()
            else:
                currentPlayer = "Player 2"
                sym = players[1]
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
            c.printBoard()
    else:
        print("There might be an issue with the bots skipping but it's fixed in pvp and pvc")
        while not winner:
            time.sleep(2)
            if i%2 ==0:
                currentPlayer = "Player 1"
                sym = players[0]
                spot = random.randint(0,6)
            else:
                currentPlayer = "Player 2"
                sym = players[1]
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
            c.printBoard()
    playAgain = input("Do  you want to play again (y/n) ").lower()
    while playAgain != "y" and playAgain != "n":
        playAgain = input("Do  you want to play again (y/n) ").lower()
    if playAgain == "y":
        c = Connect4()
    else:
        game = False