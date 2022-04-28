from tkinter import *

root = Tk()
root.geometry("720x720")
root.title("ATM")
    
root.bind("<Escape>", lambda x: root.destroy())

#making the main two frames that i'll use for the frontend
userGraphic = Frame(root,width=500,height=500,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
buttonGraphic = Frame(root,width=180,height=180,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
userGraphic.pack(side=TOP)
buttonGraphic.pack(side=BOTTOM)

#making the top part of the atm separating it into 3 different parts
leftBTN = Frame(userGraphic)
middleLBL = Frame(userGraphic)
rightBTN = Frame(userGraphic)
leftBTN.pack(side=LEFT)
rightBTN.pack(side=RIGHT)
middleLBL.pack()

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
        btn = Button(numPad,width=1,height=1)
        btn.grid(row=i,column=j,ipady=1,ipadx=1)
        numBTNs.append(btn)
listy=["7","8","9","4","5","6","1","2","3","","0",""]
for i in range(len(numBTNs)):
    numBTNs[i]['text'] = listy[i]

clearBTN = Button(commandBTN,text='Clear',background='yellow',width=4,height=1)
cancelBTN = Button(commandBTN,text='Cancel',background='red',width=4,height=1)
enterBTN = Button(commandBTN,text='Enter',background='green',width=4,height=1)
fillerBTN = Button(commandBTN,width=4,height=1)
clearBTN.grid(row=0,ipadx=1,ipady=1)
cancelBTN.grid(row=1,ipadx=1,ipady=1)
enterBTN.grid(row=2,ipadx=1,ipady=1)
fillerBTN.grid(row=3,ipadx=1,ipady=1)


root.mainloop()