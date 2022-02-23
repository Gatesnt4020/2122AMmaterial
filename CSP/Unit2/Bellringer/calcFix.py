#import
from tkinter import *


#create root
root = Tk()
root.geometry("312x324")
root.title("Calculator")

#thanks landen
def checkExpress():
    #https://www.geeksforgeeks.org/python-arithemtic-operators/
    operators="/*-+"
    for i in range(len(expression)):
        #loops through expression.
        #checks if expression behind currently checked is in arithmetics as wll
        #runs true when two operators is detected next to each other
        if expression[i] in operators and expression[i-1] in operators:
            return True
    #returns false when no issue was detected
    return False

#functions
def buttonClick(item):
    global expression
    expression+=str(item)
    outputText.set(expression)
    
def clearButton():
    global expression
    expression=""
    outputText.set(expression)

    
def equalButton():
    global expression
    try:
        if not(checkExpress()):
            result=str(eval(expression))
            if len(result)>8:
                outputText.set("OVERFLOW")
            else:
                outputText.set(result)
        else:
            outputText.set("ERROR")
    except:
        outputText.set("ERROR")
    expression=""
    
#global variables
expression=""
outputText= StringVar() #StringVar is a var that is  used in widgets
#                       if your're wanting to pass values to a widget, you need a StringVar()

#add your widgets
inputFrame = Frame(root,width=312,height=50,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
inputFrame.pack(side=TOP)     #this will make sure it stays on the top

inputField = Entry(inputFrame, bd=0, justify=RIGHT, width=312, textvariable=outputText, font=("Arial",18,'bold'))
inputField.grid(row=0,column=0)
inputField.pack(ipady = 10) #ipady is internal padding

buttonFrame = Frame(root,width=312,height=272.5,bg="grey")
buttonFrame.pack()

clear = Button(buttonFrame,text="C",fg="black",width=32,height=3,bd=0,bg="#eee",command=clearButton)
clear.grid(row=0,column=0,columnspan=3,padx=1,pady=1)
divide = Button(buttonFrame,text="/",fg="black",width=10,height=3,bd=0,bg="#eee",command=lambda:buttonClick("/"))
divide.grid(row=0,column=3,padx=1,pady=1)
seven = Button(buttonFrame,text="7",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(7)).grid(row=1,column=0,padx=1,pady=1)
eight = Button(buttonFrame,text="8",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(8)).grid(row=1,column=1,padx=1,pady=1)
nine = Button(buttonFrame,text="9",fg="black",width=10,height=3,bd=0,bg="#fff",command=lambda:buttonClick(9)).grid(row=1,column=2,padx=1,pady=1)
multiply = Button(buttonFrame,text="*",fg="black",width=10,height=3,bd=0,bg="#eee",command=lambda:buttonClick("*")).grid(row=1,column=3,padx=1,pady=1)

# third row
four = Button(buttonFrame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",command=lambda:buttonClick(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
five = Button(buttonFrame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",command=lambda:buttonClick(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
six = Button(buttonFrame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",command=lambda:buttonClick(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
minus = Button(buttonFrame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",command=lambda:buttonClick("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

# fourth row
one = Button(buttonFrame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",command=lambda:buttonClick(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
two = Button(buttonFrame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",command=lambda:buttonClick(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
three = Button(buttonFrame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff",command=lambda:buttonClick(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
plus = Button(buttonFrame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",command=lambda:buttonClick("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

# fourth row
zero = Button(buttonFrame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "#fff",command=lambda:buttonClick(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
point = Button(buttonFrame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",command=lambda:buttonClick(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
equals = Button(buttonFrame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee",command=equalButton).grid(row = 4, column = 3, padx = 1, pady = 1)

root.mainloop()