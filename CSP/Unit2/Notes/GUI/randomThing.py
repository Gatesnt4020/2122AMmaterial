from tkinter import *
from tkinter import ttk
from tkinter import filedialog

root = Tk()

def openfile():
    return filedialog.askopenfilename()

button = ttk.Button(root, text="Click me!", command=openfile)
button.grid(column=1, row=1)

root.mainloop()