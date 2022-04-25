from tkinter import *
from tkinter.tix import COLUMN

root = Tk()
root.geometry("960x960")
root.title("ATM")
    
root.bind("<Escape>", lambda x: root.destroy())

#making the main two frames that i'll use for the frontend
userGraphic = Frame(root,width=720,height=720,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
buttonGraphic = Frame(root,width=180,height=180,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
userGraphic.pack(side=TOP)
buttonGraphic.pack(side=BOTTOM)

#making the top part of the atm separating it into 3 different parts
leftBTN = Frame(userGraphic)
middleLBL = Frame(userGraphic)
rightBTN = Frame(userGraphic)
leftBTN.pack(side=LEFT)
middleLBL.pack()
rightBTN.pack(side=RIGHT)

#making the bottom part of the atm separating it into 2 different parts
numPad = Frame(buttonGraphic)
commandBTN = Frame(buttonGraphic)
numPad.pack(side=LEFT)
commandBTN.pack(side=RIGHT)

#top part of the atm frame
leftBTNs=[]
for i in range(4):
    btn = Button(leftBTN,text=f"B{i+1}")
    btn.grid(row=i)
    leftBTNs.append(btn)

LBL = LabelFrame(middleLBL,text="",width=500,height=500,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
LBL.grid(column=1)


rightBTNs=[]
for i in range(4):
    btn = Button(rightBTN,text=f"B{i+5}")
    btn.grid(row=i,column=2)
    rightBTNs.append(btn)

#bottom part of the atm frame
numBTNs=[]
for i in range(4):
    for j in range(3):
        btn = Button(numPad)
        btn.grid(row=i,column=j)
        numBTNs.append(btn)
listy=["7","8","9","4","5","6","1","2","3","","0",""]
for i in range(len(numBTNs)):
    numBTNs[i]['text'] = listy[i]

clearBTN = Button(commandBTN,text='Clear',background='yellow')
cancelBTN = Button(commandBTN,text='Cancel',background='red')
enterBTN = Button(commandBTN,text='Enter',background='green')
fillerBTN = Button(commandBTN)
clearBTN.grid(row=0)
cancelBTN.grid(row=1)
enterBTN.grid(row=2)
fillerBTN.grid(row=3)


root.mainloop()