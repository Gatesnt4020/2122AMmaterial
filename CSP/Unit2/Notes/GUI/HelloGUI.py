#python3 uses tkinter / python2 uses Tkinter
from tkinter import *

#in turtle: wn=Scren()
root = Tk()         #creates your screen
root.title("Hello") #set the window title
root.wm_geometry("200x100")  #size of the window

#object = Contructor(window,options)
myLabel = Label(root,text="Hello GUI")

myLabel.pack() #pack it into the screen THIS IS REQUEIED

root.mainloop()

#tutorialspoint
#geeksforgeeks