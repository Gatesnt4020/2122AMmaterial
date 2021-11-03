#simple, are you ready for school?
#Checklist........
#readyList=[False,False,False,False]#False,False,False,False,False,False]
questionList=["Did you wake up? (y/n) ","Did you get dress with new clothes and not your pjs? (y/n) ","Did you pet Fido? (y/n) "]
i = 0
while(i<len(questionList)):
    readyList.append(False)
    i+=1
print(readyList)
#build a loop that inserts (appends) the appropriate amount of False values



#keep asking the same 3 questions, until readyList is full of True:
#   check to see if the sure entered y for the question
#       change the index of that question in the readylist to True
while(False in readyList):
    i=0
    while(i<len(questionList)):
        if (readyList[i]==False):
            ui=input(questionList[i])
            if ui =="y":
                readyList[i]=True
        i+=1
print("you're ready for school")