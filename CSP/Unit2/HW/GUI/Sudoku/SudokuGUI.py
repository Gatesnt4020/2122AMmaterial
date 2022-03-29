"""
Ok so after working a couple of puzzles and building out an algorithm to check if the user has solved the puzzle, now it is time to create a puzzle in a GUI.  This GUI needs to not only generate a puzzle, but check to see if the puzzle is correct.  

Below are the general requirements for the GUI:
Be able to run 3 different puzzles
Input for each missing number
A method to check if the puzzle is correct and to notify the user how the puzzle failed.  The more details the better.  You could output to a label or highlight the broken cell.

Things to remember:
Comment comment comment
DRY code
Reuse the code you already developed.
Utilize a class

Bonus opportunity:  Add to the GUI the ability for the user to create a puzzle or enter a puzzle and the GUI to solve the puzzle.  The simpler, drier, and last amount of lines the more points.  
If you solve using random number generation, will work, but more strategy the better.  You will need to output the finished puzzle to user."""

from tkinter import *
import SudokuChecker as Checker
import OldSudokuChecker as C
import os,time,random

root = Tk()
root.title("Sudoku")
root.wm_geometry("1360x800")
puzzlesName=["Puzzle1.txt","Puzzle2.txt","Puzzle3.txt"]
puzzle=random.choice(puzzlesName)
board=[]


#https://www.tutorialspoint.com/how-to-bind-the-escape-key-to-close-a-window-in-tkinter     makes esc close the window
def closeWindow(e):
        root.destroy()
root.bind('<Escape>', lambda e: closeWindow(e))

def startBoard():
    puzzleEntry = Checker.Checker.openFile(None,puzzle)
    rows=0
    for i in puzzleEntry:
        cols=0
        for j in i:
            if j == " ":
                puzzleEntry = Entry(root,bg='gray')
                puzzleEntry.grid(row=rows,column=cols,pady=25,padx=9)
                board.append(puzzleEntry)      #appends <tkinter.Entry object .!entry>
            else:
                puzzleLabel = Label(root,text=j)
                puzzleLabel.grid(row=rows,column=cols,pady=25,padx=9)
                board.append(puzzleLabel)
            cols+=1
        rows+=1

def check():
    curBoard=[]
    temp=0
    for i in board:
        try:
            spot = i.get()
            if spot =="":
                spot = "#"
            curBoard.insert(temp,spot)
        except (AttributeError,TypeError):
            #https://stackoverflow.com/questions/6112482/how-to-get-the-tkinter-label-text      grabs text of label
            spot= i.cget("text")
            curBoard.insert(temp,spot)
        except:
            print("Very Bad")
        temp+=1
    print(curBoard)
    C.justGetPoints.iHateLife(None,curBoard)

checkBTN = Button(root,text="click me",command=check)
checkBTN.grid(column=10,row=10)

startBoard()
root.mainloop()