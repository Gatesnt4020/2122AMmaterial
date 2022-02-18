from tkinter import *

root = Tk()
root.geometry("200x100")

def selection():
    out = str(var.get())
    label.config(text=out)     #you reset a configuration

var= IntVar()

#at least 1 radiobutton is always turned on
#if you want option for no button choosen, make sure to use checkboxes
r1 = Radiobutton(root,text="option 1",value=10,variable=var,command=selection)
r1.pack()
r2 = Radiobutton(root,text="option 2",value=20,variable=var,command=selection)
r2.pack()

#outBTN = Button(root,text="click me",command=selection).pack()


label = Label(root)
label.pack()

root.mainloop()