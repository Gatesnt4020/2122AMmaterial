#USE ONLY IN VSC UNTIL I FIGURE OUT HOW TO PRINT UNICODE IN PS
#R,r,N,n,B,b,Q,q,K,k,P,p,_= "♖","♜","♗","♝","♘","♞","♕","♛","♔","♚","♙","♟"," " = "`u{265C}","`u{2656}","`u{265D}","`u{2657}","`u{265E}","`u{2658}","`u{2265B}","`u{2655}","`u{265A}","`u{2654}","`u{265F}","`u{2659}","`u{1F67E}" 
R,r,N,n,B,b,Q,q,K,k,P,p,_= "♖♜♗♝♘♞♕♛♔♚♙♟ "
board = [
[R,N,B,Q,K,B,N,R],
[P,P,P,P,P,P,P,P],
[_,_,_,_,_,_,_,_],
[_,_,_,_,_,_,_,_],
[_,_,_,_,_,_,_,_],
[_,_,_,_,_,_,_,_],
[p,p,p,p,p,p,p,p],
[r,n,b,q,k,b,n,r]]
letters = "ABCDEFGH"
color=True
gameOver=False

#TODO get done with printing the board(1/20)
def printBoard(board):
    for r in board:     #takes whats inside of the board list
        for c in r:     #takes whats inside of r
            print(c, end=' ')
        print()

def goodSpot():
    row,col,row1,col1=0,0,0,0
    badSpot=True
    while badSpot == True:
        start=input("Piece location ")
        start=start.lower()
        if len(start) <=0 or len(start) >2:
            print("Please enter only 2 characters.")
            continue
        #https://www.geeksforgeeks.org/python-continue-statement/
        row = start[0]
        col =start[1]
        if not row.isalpha() or not col.isdigit():
            print("Please input a letter then a number.")
            continue
        row = letters.find(row)
        if not(0<row<8):
            print("Please enter a letter on the board")
            continue
        col = int(col)
        if not (0<col<8):
            print("Please enter a number on the board")
            badSpot=False
    badSpot=True
    while badSpot== True:
        move=input("Piece location ")
        move=move.lower()
        if len(move) <=0 or len(move) >2:
            print("Please enter only 2 characters.")
            continue
        #https://www.geeksforgeeks.org/python-continue-statement/
        row1 = move[0]
        col1 =move[1]
        if not row1.isalpha() or not col1.isdigit():
            print("Please input a letter then a number.")
            continue
        row1 = letters.find(row1)
        if not(0<row1<8):
            print("Please enter a letter on the board")
            continue
        col1 = int(col1)
        if not (0<col1<8):
            print("Please enter a number on the board")
            badSpot=False
    return(row,col,row1,col1)
    

#https://stackoverflow.com/questions/47224560/print-2d-list-with-equal-character-spacing-python
#thought the pieces looked cool


#TODO get movement done(1/23-1/24) & get board to update placement
while True:
    print("Please input a letter then a number")
    if color == True:
        printBoard(board)
        print("Whites turn")
        goodSpot()
        #ui=input("")
        start="rol"+"col"
        move="rol1"+"col1"
        color = False
        print("\n"*50)
    else:
        printBoard(board)
        print("Blacks turn")
        goodSpot()
        color = True
        print("\n"*50)




#TODO get winning and losing done(1/25)



#TODO get the pawn switching done(1/26)



#TODO get the extra movenments done(1/27)