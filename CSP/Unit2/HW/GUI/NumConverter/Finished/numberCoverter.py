from distutils.cmd import Command
from tkinter import *
import anyConverter

root = Tk()
root.geometry("312x324")
root.title("Number Converter")
outputText=StringVar()

def printResult():      #grabs the string inside the entry boxes
    ui = entry0.get()
    base = entry1.get()
    change = entry2.get()
    changeNum = anyConverter.Convert.converter(ui,base,change)      #changes the numbers into what user wants
    outputText.set(changeNum)
    label3.config(text="Result is " +outputText.get())  #print the numbers out that the user wants

def clearButton():      # clears the users entry boxes from the begining of string to end
    entry0.delete(0,END)
    entry1.delete(0,END)
    entry2.delete(0,END)

label0 = Label(root)
label0.config(text="Please enter your number wanted to covert")
label0.grid(row=0,column=0,padx=3,pady=3)

entry0 = Entry(root,bd=3,justify=RIGHT)
entry0.grid(row=1,column=0,padx=3,pady=3)

label1 = Label(root)
label1.config(text="Please enter the base of the number")
label1.grid(row=2,column=0,padx=3,pady=3)

entry1 = Entry(root,bd=3,justify=RIGHT)
entry1.grid(row=3,column=0,padx=3,pady=3)

label2 = Label(root)
label2.config(text="Please enter the base of the number wanted")
label2.grid(row=4,column=0,padx=3,pady=3)

entry2 = Entry(root,bd=3,justify=RIGHT)
entry2.grid(row=5,column=0,padx=3,pady=3)

label3 = Label(root)
outputText.set('Result is ')
label3.config(text=outputText.get())
label3.grid(row=6,column=0,padx=3,pady=3)

result = Button(root,text="Calculate",command=printResult)
result.grid(row=7,column=0)
clear = Button(root,text="Clear",command=clearButton)
clear.grid(row=7,column=1)



root.mainloop()
'''numOfLabels=4
numOfEntrys=numOfLabels-1
items=[]
descriptions=["Please enter your number wanted to covert","Please enter the base of the number","Please enter the base of the number wanted","Result is "]

def clear():
    items[1]
    items[3]
    items[5]

def printResult():
    ui = items[1].get()
    base = items[3].get()
    change = items[5].get()
    changeNum= anyConverter.Convert(ui,base,change).converter()
    items[6].set(changeNum)


for i in range(numOfLabels):
    item = Label(root)      #items[0,2,4,6]
    item.config(text=descriptions[i])
    items.append(item)
    if numOfEntrys - i != numOfEntrys:
        item = Entry(root)  #items[1,3,5]
        item.grid(row=(i+len(items)),column=0,pady=10,padx=5)
        items.append(item)
    else:
        item = Button(root) #items[7,8]
        item.grid(row=(i+len(items)),column=0,pady=10,padx=5,text="Calculate",command=printResult,bd=10)
        items.append(item)
        item = Button(root)
        item.grid(row=(i+len(items)),column=0,pady=10,padx=5,text="Clear",command=clear,bd=10)
        items.append(item)
'''
