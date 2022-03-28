import os,time,math
#       i know i forgot to comment,comment,comment -5

class Checker:
    #Opens the files to add the content into a list while removing unnecessary elements
    def openFile(self,puzzle):
        global puzzleFromFile
        with open(puzzle,"r+") as p:
            puzzleFromFile=p.readlines()
            index=0
            for i in puzzleFromFile:
                puzzleFromFile[index]=i.replace("\n","")
                if len(i) >= 9:
                    print("There is an error in your Sudoku File please fix it then try again")
                    return False
                index+=1
            index=0
            for i in puzzleFromFile:
                puzzleFromFile[index] = []
                for j in i:
                    if not(i.isnumeric) and i != "":
                        print("There is an error in your Sudoku File please fix it then try again")
                        return False
                    puzzleFromFile[index].append(j)
                index+=1
            p.close
            return True,puzzleFromFile

    #checking to see if there is a issue with the horizontal part
    def horizontalChecker(self):
        for row in puzzleFromFile:
            nums=[]
            for i in row:
                if i in nums:
                    print()
                    #os.system.exit("There was a horizontal error ")    would stop the program
                else:  
                    nums.append(i)

    def verticalChecker(self):
        for col in range(len(puzzleFromFile)):
            nums=[]
            for i in range(len(puzzleFromFile)):
                if puzzleFromFile[i][col] in nums:
                    print()
                else:  
                    nums.append(puzzleFromFile[i][col])

    def sectionChecker(self):
        cols=0
        rows=0
        for sec in range(len(puzzleFromFile)):
            nums = []
            for i in range(math.floor(len(puzzleFromFile)/3)): 
                for j in range(math.floor(len(puzzleFromFile)/3)):
                    if puzzleFromFile[i+cols][j+rows] in nums:
                        print
                    else:
                        nums.append(puzzleFromFile[i+cols][j+rows])
            rows+=3
            if (sec+1)%3==0:
                cols+=3
                rows=0