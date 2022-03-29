import os,time,math
#       i know i forgot to comment,comment,comment -5
    
#Opens the files to add the content into a list while removing unnecessary elements
class justGetPoints:

    def iHateLife(self,puzzleFromFile):
        listy=[[],[],[],[],[],[],[],[],[]]
        temp=0
        for i in range(len(puzzleFromFile)):
            listy[temp].append(puzzleFromFile[i])
            if (i+1)%9==0:
                temp+=1
        print(listy)
        justGetPoints.horizontalChecker(None,listy)
        justGetPoints.verticalChecker(None,listy)
        justGetPoints.sectionChecker(None,listy)

    def openFile(self,puzzle):
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
    def horizontalChecker(self,puzzleFromFile):
        rowspot=1
        problems=[]
        problemType=["horizontal",'row','column']
        for row in puzzleFromFile:
            nums=[]
            col=1
            for i in row:
                if i in nums and i != "#":
                    problems.append(str(col))
                    problems.append(str(rowspot))
                    #os.system.exit("There was a horizontal error ")    would stop the program
                else:  
                    nums.append(i)
                col+=1
            rowspot+=1
        justGetPoints.listToString(None,problems,problemType)

    def verticalChecker(self,puzzleFromFile):
        
        problems=[]
        problemType=["vertical",'column','row']
        for col in range(len(puzzleFromFile)):
            nums=[]
            for i in range(len(puzzleFromFile)):
                if puzzleFromFile[i][col] in nums and puzzleFromFile[i][col] != "#":
                    problems.append(str(i+1))
                    problems.append(str(col+1))
                else:  
                    nums.append(puzzleFromFile[i][col])
        justGetPoints.listToString(None,problems,problemType)

    def sectionChecker(self,puzzleFromFile):
        problems=[]
        problemType=["section",'row','column']
        cols=0
        rows=0
        for sec in range(len(puzzleFromFile)):
            nums = []
            for i in range(math.floor(len(puzzleFromFile)/3)): 
                for j in range(math.floor(len(puzzleFromFile)/3)):
                    if puzzleFromFile[i+cols][j+rows] in nums and puzzleFromFile[i+cols][j+rows] != "#":
                        problems.append(str(sec+1))
                        problems.append(str(j+rows+1))
                        problems.append(str(i+cols+1))
                    else:
                        nums.append(puzzleFromFile[i+cols][j+rows])
            rows+=3
            if (sec+1)%3==0:
                cols+=3
                rows=0
        justGetPoints.listToString(None,problems,problemType)


    #used to change the list from the checkers to print out a string in the problem row
    def listToString(self,problems,problemType):
        if len(problems) > 0: 
            word=""
            for i in problems:
                word+=i
                if len(word)-1>=0:
                    word+=","
            word = word[:-1]
            
            if problemType[0]!="section":
                problem=str(len(problems)/2)
                print(f"The puzzle has {problem[0]} {problemType[0]} problem(s) in {problemType[1]}/{problemType[2]} {word}")
                print(f"First number is the {problemType[1]} and second is the {problemType[2]}")
                print()
            else: 
                problem=str(len(problems)/3)
                print(f"The puzzle has {problem[0]} {problemType[0]} problem(s) in {problemType[0]}/{problemType[1]}/{problemType[2]} {word}")
                print(f"First number is the {problemType[0]}, second is the {problemType[1]}, and the third  is the {problemType[2]}")
                print()
        else:
            print(f"The puzzle's {problemType[0]} has no problems")
            print()
