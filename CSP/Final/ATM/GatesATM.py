#reminder future me to ethier put debug_mode to True or False (current_state=False)
#made by Christian N. Gates
from tkinter import *
import pandas as pd
import os,math,sys
import GatesCustomer as GC

root = Tk()
root.geometry("720x720")
root.title("ATM")
root.bind("<Escape>", lambda x: root.destroy())

expression=""
outputText = StringVar()

debug_mode=False
creditIndex=''
transferIndex=''
account=''
trys=2
loggingIn = True

'''
    this one keeped all the information that wasnt just the needed info
    def cleanUp():
        if not(os.path.exists("GatesDB.txt")):
            df = pd.read_csv('original/db.tsv',header=0)
            headers=("StreetNumber","Zip","DOB","Savings","Checkings","CreditCard","Pin")
            for i in df.columns:
                #removes the $ from the saving and checking column
                if i == "Savings" or i == "Checkings":
                    df[i] = df[i].str.replace("$","")
                #makes all the headers that should only be numbers into numbers else it becomes a nan
                if i in headers:
                    df[i] = pd.to_numeric(df[i],errors='coerce')
                #checks all the headers except st num and if there under 10 then it becomes a nan
                if i in headers[1:]:
                    for j in range(len(df[i])):
                        if df[i][j] < 10:
                            df[i][j] = math.nan
            #if any of the values in file are nan then it removes them
            for i in df.columns:
                df.dropna(subset=[i],inplace=True)
            df.to_csv('GatesDB.txt',index=False)'''

def cleanUp():
    #checks to see if my db has ben made if not will make it from the db given
    if not(os.path.exists("GatesDB.txt")):
        #reads the file in
        df = pd.read_csv('original/db.tsv',header=0)
        #these will be the only headers will keep so we put them into a sequence
        headers=("Savings","Checkings","CreditCard","Pin")
        for i in df.columns:
            #removes the $ from the saving and checking column
            if i == "Savings" or i == "Checkings":
                df[i] = df[i].str.replace("$","")
            #checks the headers and if it is in it we keep the data and check it else we will delete it
            if i in headers:
                df[i] = pd.to_numeric(df[i],errors='coerce')
                for j in range(len(df[i])):
                    if df[i][j] < 10:
                        df[i][j] = math.nan
            else:
                del df[i]
        #if any of the values in file are nan then it removes them
        for i in df.columns:
            df.dropna(subset=[i],inplace=True)
        #writes another fill with all the data we messed with
        df.to_csv('GatesDB.txt',index=False)

def buttonClick(item):
    global expression,debug_mode
    #when a button is click it would add it to a string unless it was in the main screen or the balacne screen
    if lbl.cget("text") != "B1->Deposit | B2->Withdrawal | B3->Balance Inquiry | B4->Transfer Balance | B5->Change Pin | B6->Log out" and lbl.cget("text") != "Your balance inquiry (hit enter)":
        expression += str(item)
        #if debug mode is on then during the login state it would show * instead of plain text
        if debug_mode:
            item=len(expression)*"*"
            outputText.set(item)
        else:
            outputText.set(expression)
    
def backButton():
    #resets the top label text to what it used to be making it look like the main screen
    if not(loggingIn):
        lbl.config(text="B1->Deposit | B2->Withdrawal | B3->Balance Inquiry | B4->Transfer Balance | B5->Change Pin | B6->Log out")

def clearButton():
    #clears what the user was putting in
    global expression
    expression=""
    outputText.set(expression)
   
def cancelButton():
    #stops the program
    root.destroy()

def login():
    global expression,loggingIn,trys,creditIndex
    #checks to see if the index of the customers card has been changed
    if creditIndex != '':
        #if the pin does not match the index of the customers card subtracts from tries
        if not(GC.Customer.checkPin(creditIndex,expression)):
            trys-=1
        else:
            #if the person got the pin correct says they've logged in and makes the login state false
            lbl.config(text="B1->Deposit | B2->Withdrawal | B3->Balance Inquiry | B4->Transfer Balance | B5->Change Pin | B6->Log out")
            loggingIn=False
            trys = 3
    #checks to see if the login state is still false
    if loggingIn:        
        #will grab the first part of the tuple that contains a true/card index or a false/false
        if GC.Customer.chcekCredit(expression)[0]:
            creditIndex = GC.Customer.chcekCredit(expression)[1]
            lbl.config(text="Please enter your pin number")
        else:
            #if card number does not exist then subtract from tries
            trys-=1

def subMain():
    global expression,creditIndex,account,trys,transferIndex
    #checks which label is up and depending on the label will continue with the process
    if lbl.cget("text") == "Enter the amount you would like to deposit":
        #if the it return a str then there was an error but if its a boolean then it succeeded
        if type(GC.Customer.deposit(creditIndex,expression,account)) != str:
            #subtracts from the trys if it happened
            trys-=1
            #if the account is 1 then its the savings else its the checking account
            if account == "1":
                lbl.config(text=f"Your balance inquiry > Savings ${str(GC.Customer.balance(creditIndex)[0])}")
            else:
                lbl.config(text=f"Your balance inquiry > Checkings ${str(GC.Customer.balance(creditIndex)[1])}")
        #if the error is over then tells the user that its to much
        elif GC.Customer.deposit(creditIndex,expression,account) =="Over $500":
            lbl.config(text="Transaction cannot exceed $500")
        #if the amount is an increments a 5 then tells the user
        elif GC.Customer.deposit(creditIndex,expression,account) =="Not an increments of 5":
            lbl.config(text="Must be increments of $5 bills")
        else:
            #if the amount makes the person go under 10 then tells the user
            lbl.config(text="Overdraft Issue")
    elif lbl.cget("text") == "Enter the amount you would like to withdraw":
        if type(GC.Customer.withdraw(creditIndex,expression,account)) != str:
            trys-=1
            if account == "1":
                lbl.config(text=f"Your balance inquiry > Savings ${str(GC.Customer.balance(creditIndex)[0])}")
            else:
                lbl.config(text=f"Your balance inquiry > Checkings ${str(GC.Customer.balance(creditIndex)[1])}")
        elif GC.Customer.withdraw(creditIndex,expression,account) =="Over $500":
            lbl.config(text="Transaction cannot exceed $500")
        elif GC.Customer.withdraw(creditIndex,expression,account) =="Not an increments of 5":
            lbl.config(text="Must be increments of $5 bills")
        else:
            lbl.config(text="Overdraft Issue")
    elif lbl.cget("text") == "Enter the account you would like to transfer from (1->Savings | 2->Checkings)":
        #checks the tuple and grabs the first index and if its true continue
        if GC.Customer.findAccount(expression)[0]:
            #sets the account to what the user would want and changes the lbl
            account = GC.Customer.findAccount(expression)[1]
            lbl.config(text="Enter the amount you would like to transfer")
    elif lbl.cget("text") == "Enter the amount you would like to transfer":
        if type(GC.Customer.transfer(creditIndex,expression,account,transferIndex)) != str:
            trys-=1
            if account == "1":
                lbl.config(text=f"Your balance inquiry > Savings ${str(GC.Customer.balance(creditIndex)[0])}")
            else:
                lbl.config(text=f"Your balance inquiry > Checkings ${str(GC.Customer.balance(creditIndex)[1])}")
        elif GC.Customer.transfer(creditIndex,expression,account,transferIndex) =="Over $500":
            lbl.config(text="Transaction cannot exceed $500")
        elif GC.Customer.transfer(creditIndex,expression,account,transferIndex) =="Not an increments of 5":
            lbl.config(text="Must be increments of $5 bills")
        else:
            lbl.config(text="Overdraft Issue")

def main():
    global expression,creditIndex,account,transferIndex
    subMain()
    #checks which label is up and depending on the label will continue with the process
    if lbl.cget("text") == "Enter the account you would like to deposit to (1->Savings | 2->Checkings)":
    #checks the tuple and grabs the first index and if its true continue
        if GC.Customer.findAccount(expression)[0]:
            #sets the account to what the user would want and changes the lbl
            account = GC.Customer.findAccount(expression)[1]
            lbl.config(text="Enter the amount you would like to deposit")
    elif lbl.cget("text") == "Enter the account you would like to withdrawl from (1->Savings | 2->Checkings)":
        if GC.Customer.findAccount(expression)[0]:
            account = GC.Customer.findAccount(expression)[1]
            lbl.config(text="Enter the amount you would like to withdraw")
    elif lbl.cget("text") == "Your balance inquiry (hit enter)":
        lbl.config(text=f"Your balance inquiry > Savings ${str(GC.Customer.balance(creditIndex)[0])} | Checkings ${str(GC.Customer.balance(creditIndex)[1])}")
    elif lbl.cget("text") == "Enter the credit card you would like to transfer to":
        #will grab the first part of the tuple that contains a true/card index or a false/false
        if GC.Customer.chcekCredit(expression)[0]:
            #if the card does exist sets it to a variable
            transferIndex = GC.Customer.chcekCredit(expression)[1]
            lbl.config(text="Enter the account you would like to transfer from (1->Savings | 2->Checkings)")
    elif lbl.cget("text") == "Enter the a new pin":
        #inputs a number and it becomes there pin
        GC.Customer.pin(creditIndex,expression)

def enterButton():
    global expression,account,loggingIn,trys
    #has a temp var of how many current trys there are
    temp=trys
    #sees if during the login part the trys have subtracted more than once if so adds one
    if temp-2 == trys:
        trys+=1
    #if all three trys have been used then it stops the program
    if trys <= 0:
        #if its not in the login process does a different exit
        if not(loggingIn):
            #removes the buttons that allow the user to use the program
            for i in range(3):
                leftBTNs[i].grid_forget()
                rightBTNs[i].grid_forget()
            #tells the user what there account looks like then closes the program
            if lbl.cget("text") == f"Your balance inquiry > Savings ${str(GC.Customer.balance(creditIndex)[0])} | Checkings ${str(GC.Customer.balance(creditIndex)[1])}, hit enter again to close program":
                sys.exit()
            else:
                lbl.config(text=f"Your balance inquiry > Savings ${str(GC.Customer.balance(creditIndex)[0])} | Checkings ${str(GC.Customer.balance(creditIndex)[1])}, hit enter again to close program")
        else:
            sys.exit()
    #checks if the users is in the login state and if they've put inputed anything
    if expression != "" or lbl.cget("text") == "Your balance inquiry (hit enter)":
        if loggingIn:
            login()
        else:
            main()

    expression=""
    outputText.set(expression)

def changeOption(title):
    #changes the label depending on what button was pressed
    if not(loggingIn):
        if title == "B1":
            lbl.config(text="Enter the account you would like to deposit to (1->Savings | 2->Checkings)")
        elif title == "B2":
            lbl.config(text="Enter the account you would like to withdrawl from (1->Savings | 2->Checkings)")
        elif title == "B3":
            lbl.config(text="Your balance inquiry (hit enter)")
        elif title == "B4":
            lbl.config(text="Enter the credit card you would like to transfer to")
        elif title == "B5":
            lbl.config(text="Enter the a new pin")
        else:
            root.destroy()

cleanUp()

#making the main two frames that i'll use for the frontend
userGraphic = Frame(root,width=200,height=200,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
buttonGraphic = Frame(root,width=50,height=50,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
userGraphic.pack()
buttonGraphic.pack()

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

#top left part of the atm frame
leftBTNs=[]
for i in range(3):
    btn = Button(leftBTN,text=f"B{i+1}",command=lambda s=f"B{i+1}": changeOption(s))
    btn.grid(row=i)
    leftBTNs.append(btn)

#the main screen of the atm
lbl = Label(middleLBL,text="Please enter your card number")
Lbl = Label(middleLBL,textvariable=outputText,width=80,height=30)
lbl.grid(row=0,column=0)
Lbl.grid(row=1,column=0)

#top right part of the atm frame
rightBTNs=[]
for i in range(3):
    btn = Button(rightBTN,text=f"B{i+4}",command=lambda s=f"B{i+4}": changeOption(s))
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
    numBTNs[i].configure(command=lambda s=listy[i]: buttonClick(s))

clearBTN = Button(commandBTN,text='Clear',background='yellow',width=4,height=1,command=clearButton)
cancelBTN = Button(commandBTN,text='Cancel',background='red',width=4,height=1,command=cancelButton)
enterBTN = Button(commandBTN,text='Enter',background='green',width=4,height=1,command=enterButton)
backBTN = Button(commandBTN,width=4,height=1,text='back',background='gray',command=backButton)
clearBTN.grid(row=0,ipadx=1,ipady=1)
cancelBTN.grid(row=1,ipadx=1,ipady=1)
enterBTN.grid(row=2,ipadx=1,ipady=1)
backBTN.grid(row=3,ipadx=1,ipady=1)

root.mainloop()