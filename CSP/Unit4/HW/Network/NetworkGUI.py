from tkinter import *
import os,time

root = Tk()
root.geometry("500x500")
root.title("Network GUI")

root.bind("<Escape>", lambda x: root.destroy())

#The welcoming screen for the user
welcomeFrame = Frame(root,width=500,height=500,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
LBL = Label(welcomeFrame,text="Welcome to my Network GUI",width=500,height=500,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
time.sleep(4)

#The main screen where the user will be able to access the commands
mainFrame = Frame(root,width=500,height=500,bd=0,highlightbackground="black",highlightcolor="black",highlightthickness=1)
mainFrame.tkraise()
lbl = Label(mainFrame,text="hello")