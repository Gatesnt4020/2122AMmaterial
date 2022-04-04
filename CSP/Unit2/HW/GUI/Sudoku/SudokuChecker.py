import os,time,math
#       i know i forgot to comment,comment,comment -5

class Checker:
    #Opens the files to add the content into a list while removing unnecessary elements
    
    @staticmethod
    def openFile(self,puzzle):
        with open(puzzle,"r+") as p:
            puzzleFromFile=p.readlines()
            index=0
            for i in puzzleFromFile:
                puzzleFromFile[index]=i.replace("\n","")
                if len(puzzleFromFile[index]) != 9:
                    print(index+1," was the line that had the wrong amount of characters")
                    os.sys.exit("Error in Sudoku File please have the puzzle as a 9 by 9 ")
                index+=1
            index=0
            for i in puzzleFromFile:
                puzzleFromFile[index] = []
                for j in i:
                    if not(j.isnumeric) and i != " ":
                        print(index+1," was the line that had the wrong character")
                        os.sys.exit("Error in Sudoku File please have puzzle with only nums and spaces")
                    puzzleFromFile[index].append(j)
                index+=1
            p.close
        return puzzleFromFile 

    #checking to see if there is a issue with the horizontal part
    def horizontalChecker(self,puzzleFromFile):
        for row in puzzleFromFile:
            nums=[]
            for i in row:
                if i != " ":
                    if i in nums:
                        i = "*"
                        return puzzleFromFile
                    else:  
                        nums.append(i)

    def verticalChecker(self,puzzleFromFile):
        for col in range(len(puzzleFromFile)):
            nums=[]
            for i in range(len(puzzleFromFile)):
                if puzzleFromFile[i][col] != " ":    
                    if puzzleFromFile[i][col] in nums:
                        puzzleFromFile[i][col] = "*"
                        return puzzleFromFile
                    else:  
                        nums.append(puzzleFromFile[i][col])

    def sectionChecker(self,puzzleFromFile):
        cols=0
        rows=0
        for sec in range(len(puzzleFromFile)):
            nums = []
            for i in range(math.floor(len(puzzleFromFile)/3)): 
                for j in range(math.floor(len(puzzleFromFile)/3)):
                    if puzzleFromFile[i+cols][j+rows] != " ":
                        if puzzleFromFile[i+cols][j+rows] in nums:
                            puzzleFromFile[i+cols][j+rows] = "*"
                            return puzzleFromFile
                        else:
                            nums.append(puzzleFromFile[i+cols][j+rows])
            rows+=3
            if (sec+1)%3==0:
                cols+=3
                rows=0
