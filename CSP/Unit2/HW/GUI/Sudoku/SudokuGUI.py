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
import os,time,random

root = Tk()
root.title("Sudoku")
root.wm_geometry("400x400")

frames=[]
curframe=0
def nextFrame(r):
    info = something.get()
    info2 = something2.get()
    if info != "" and info2 != "":
        if info != "something" and info2 != "something else":
            curframe+=1
            frames[curframe].tkraise()
        else:
            info.set("Please enter the correct information to move on")
    else:
        info.set("Please do not leave this field blank")
root.bind('<Return>', lambda r :nextFrame(r))

#https://www.tutorialspoint.com/how-to-bind-the-escape-key-to-close-a-window-in-tkinter     makes esc close the window
def closeWindow(e):
    root.destroy()
root.bind('<Escape>', lambda e: closeWindow(e))

def notFinished():
    print("This section is still being worked on please come back later when it is finished")
    return True

def downloadPuzzles():
    puzzlesName=["Puzzle1.txt","Puzzle2.txt","Puzzle3.txt"]
    puzzles=[[[' ', '5', ' ', '1', ' ', ' ', ' ', ' ', ' '], ['2', ' ', '4', ' ', ' ', ' ', ' ', '9', '3'], ['7', '2', '1', ' ', '3', '8', '6', '4', ' '], ['4', '3', ' ', ' ', '5', '7', '9', '8', '1'], [' ', ' ', ' ', ' ', '6', '1', ' ', ' ', '2'], [' ', ' ', ' ', ' ', ' ', '4', ' ', ' ', '9'], ['6', '4', ' ', '8', ' ', '2', ' ', ' ', ' ']],
    [[' ', ' ', '6', '5', '1', ' ', ' ', ' ', '8'], ['7', ' ', '3', '8', ' ', ' ', '6', '9', '1'], ['2', ' ', ' ', ' ', '3', ' ', '5', '4', '7'], [' ', ' ', '1', '7', ' ', ' ', ' ', '8', ' '], ['6', ' ', ' ', '3', ' ', '1', '7', '5', ' '], ['8', ' ', '7', '4', '5', ' ', '3', '1', ' '], [' ', '8', '5', '6', ' ', ' ', '9', ' ', ' '], ['9', ' ', ' ', ' ', ' ', '5', ' ', '7', ' '], [' ', '7', '4', ' ', ' ', ' ', ' ', ' ', ' ']],
    [[' ', '8', '9', ' ', '6', ' ', ' ', ' ', ' '], [' ', ' ', ' ', '5', ' ', ' ', ' ', ' ', '8'], ['6', '1', ' ', ' ', ' ', ' ', '9', '3', ' '], [' ', ' ', ' ', '4', '3', ' ', ' ', '7', '9'], ['1', ' ', ' ', ' ', '9', ' ', ' ', ' ', ' '], [' ', ' ', '4', '6', ' ', ' ', '8', '5', ' '], ['3', ' ', ' ', ' ', '5', '7', ' ', ' ', ' '], [' ', '9', '7', ' ', '4', '6', '5', '2', '3'], ['5', '4', '1', ' ', '2', '8', ' ', '9', '6']]]
    print(puzzles[0])
    print(puzzles[1])
    puzzle1=[puzzles[0]]
    puzzle2=[]
    puzzle3=[]
    for i in puzzlesName:
        puzzleNum=0
        with open(i,"w+") as p:
            for i in range(len(puzzles[puzzleNum])):
                p.writelines(puzzles[puzzleNum][i])
                p.write("\n")
        puzzleNum+=1
        print("is this working")
downloadPuzzles()
    
if  not(os.path.exists('Puzzle1.txt')):
    info.set("Would you like to 'download' the 3 demo Sudoku files, 'import' your own, or 'enter' one.")
    info = something.get()
    while info != "download" or info != "import" or info != "enter":
        info.set("Would you like to 'download' the 3 demo Sudoku files, 'import' your own, or 'enter' one.")
        info = something.get()
    if info == "download":
        if not(notFinished()):
                downloadPuzzles()
                nextFrame()
    elif info == "import":
        if not(notFinished()):
                puzzleEntry = Entry(curframe,bd=3,text="Which file would you like to import: ")
                nextFrame()
    else:
        if not(notFinished()):
            puzzleEntry = Entry(curframe,bd=3,text="Please enter your puzzle (for blanks please enter ., ,#): ")
            enterPuzzle()

puzzleFromFile=[]
def openFile(puzzle):
    global puzzleFromFile
    with open(puzzle,"r+") as p:
        puzzleFromFile=p.readlines()
        index=0
        for i in puzzleFromFile:
            puzzleFromFile[index]=i.replace("\n","")
            index+=1
        index=0
        for i in puzzleFromFile:
            puzzleFromFile[index] = []
            for j in i:
                puzzleFromFile[index].append(j)
            index+=1
        p.close

openFile(input())
print(puzzleFromFile)
root.mainloop()