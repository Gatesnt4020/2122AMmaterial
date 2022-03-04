import os,time

'''
    Goal of this program is to check and see if the Sudoku puzzle the user enters is correct.
    This program should be ran in the same directory as a text file called Puzzle.txt
    The program will check if the Sudoku puzzle is correct then output to the console if it is correct or not.
    If you've never played Sudoku before, here's the rules:  https://sudoku.com/how-to-play/sudoku-rules-for-complete-beginners/
    I have listed out a couple ideas to create this program.  You do not need to do this my way, but I'm telling ya, it will help in the long run.


    #read in the text file into a 2D List so you can iterate through it like we did in Tic Tac Toe
    puzzleFromFile=[]
    #open the file
    #utilize a for loop to iterate through the file
        #each line should be converted into a list and appended to the board
        
    #utilize a function where you enter a list or row and check if the row has 1-9 exclusively
    def rowChecker(rowToCheck):
        #if the board isn't solved horizontally, then return False
        return True

    #create a function that takes in your 2D List above and checks if each horizontal row has 1-9 exclusively
    def horizontalCheck(boardToCheck):
        #loop through the boardToCheck (which should be the puzzleFromFile variable)
        #   each iteration you will have a list so check to see if that list has 1-9, if it doesn't return False
        #if the board isn't solved horizontally, then return False
        return True

    #create a function that takes in your 2D List above and checks if each vertical column has 1-9 exclusively
    def verticalCheck(boardToCheck):
        #You should already have a function to check a row if it has 1-9 exclusively.
        #   Rotate the boardToCheck and pass in the board to horizontalCheck
        #if the board isn't solved horizontally, then return False
        return True

    #create a function checks the different sections of board.  You could make the function dynamic by passing in which section to check.
    def sectionCheck(boardToCheck):
        #if the board isn't solved horizontally, then return False
        return True

    #working code
    if horizontalCheck(puzzleFromFile):
        print("passed horizontally")
    elif verticalCheck(puzzleFromFile):
        print("passed vertically")
    elif sectionCheck(puzzleFromFile):    
    
        need to be able to tell the user which section failed
        there are 9 sections 
        1   2   3
        4   5   6
        7   8   9
    
    failedSection=1
    print(f"Section {failedSection} Didn't Pass")
    
    

    - You can assume the data coming in is like the examples
    - Need to tell the user where it failed, the more specific the more points (which row, which col, which section)
        - Some Points: tell the user which method failed first
        - Average Points: tell which row or column the puzzle failed on
        - All Points: the exact cell that failed
    - Seriously, you will want this for later.
    - Take baby steps.  That's why I recommend functions so you can get more points faster and partial credit when you're stuck.
    '''
    
#Opens the files to add the content into a list while removing unnecessary elements
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

#checking to see if there is a issue with the horizontal part
def horizontalChecker():
    issue=1
    problems=[]
    for row in puzzleFromFile:
        nums=[]
        for i in row:
            if i in nums:
                '''print()
                print(f"There was a horizontal error in row {issue}")
                print()'''
                problems.append(str(issue))
                #os.system.exit("There was a horizontal error ")    would stop the program
            else:  
                nums.append(i)
        issue+=1
    return problems

def verticalChecker():
    issue=9
    problems=[]
    for col in range(len(puzzleFromFile)):
        nums=[]
        for i in range(len(puzzleFromFile)):
            if puzzleFromFile[col-i][col] in nums:
                problems.append(str(col+1))
            else:  
                nums.append(puzzleFromFile[col-i][col])
        issue-=1
    return problems

def sectionChecker():
    problems=[]
    for sec in range((len(puzzleFromFile))):
        nums = []
        issue=9
        for i in range(int(issue/3)):
            if puzzleFromFile[i-3][sec-3] in nums:
                problems.append(str(sec))
            else:  
                nums.append(puzzleFromFile[i-3][sec-3])
            issue-=3
        return problems


#used to change the list from the checkers to print out a string in the problem row
def listToString(problems):
    if len(problems) > 0: 
        word=""
        for i in problems:
            word+=i
            if len(word)-1>=0:
                word+=","
        word = word[:-1]
        print(f"The puzzle has {len(problems)} horizontal problem(s) in row(s) {word}")
        print()
    


ui = input("Would you like to 'solve' or 'check' a Sudoku Puzzle ").lower()
while ui != "solve" and ui != "check":
    ui = input("Would you like to 'solve' or 'check' a Sudoku Puzzle ").lower()
if ui == "check":    
    ui = input("Would you like to 'enter' your puzzle or 'import' your puzzle ").lower()
    while ui != "enter" and ui != "import":
        ui = input("Would you like to 'enter' your puzzle or 'import' your puzzle ").lower()
    while ui == "import":
#       https://stackoverflow.com/questions/11968976/list-files-only-in-the-current-directory      used to print the files in the directory for user friendlyness and for bad spelling
        print(os.listdir(os.curdir))
        print("Note please use txt files")
        puzzle = input("Which file would you like to import ")
        if not(os.path.exists(puzzle)):
            print("This file does not exist please see if you entered the name wrong or if the file is in the current directory")
            print("Note did you forget .txt")
            print()
            time.sleep(1)
            continue
        else:
            openFile(puzzle)
            os.system('cls')
            problems = horizontalChecker()
            listToString(problems)
            problems = verticalChecker()
            listToString(problems)
            problems = sectionChecker()
            listToString(problems)
            time.sleep(5)
    while ui == "enter":
        print("This is still currently being worked on")
else:
    print("This is still currently being worked on")