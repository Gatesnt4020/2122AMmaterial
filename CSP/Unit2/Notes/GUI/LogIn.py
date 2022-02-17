#python3 uses tkinter / python2 uses Tkinter
from tkinter import *
masterUsername = "admin"
masterPassword = "admin"

def logOut():
    loginFrame.tkraise()

def pressMyButton():
    print("You pressed the button")
    #get the info from the GUI
    un = usernameEntry.get()
    pw = passwordEntry.get()        #get the info from the GUI
    
    #check against master log in
    if un == masterUsername and pw == masterPassword:
        print("You're logged in")
        authFrame.tkraise() #bring it to the top

#in turtle: wn=Scren()
root = Tk()         #creates your screen
root.title("LogIn") #set the window title
root.wm_geometry("300x300")  #size of the window

authFrame = Frame(root)
authFrame.grid(row=0,column=0,sticky='news')

#Frame for the login
#object = Constructor(window)
loginFrame = Frame(root)
loginFrame.grid(row=0,column=0,sticky='news')
#sticky is a nanchor parameter to north, east, west, south



#items into the frame
#hungarian naming convention
usernameLBL = Label(loginFrame,text="Username: ")
usernameLBL.pack(pady=5,padx=5)
usernameEntry = Entry(loginFrame,bd=3)
usernameEntry.pack(pady=5,padx=5)
passwordLBL = Label(loginFrame,text="Password: ")
passwordLBL.pack(pady=5,padx=5)
passwordEntry = Entry(loginFrame,bd=3,show="*")
passwordEntry.pack(pady=5,padx=5)

loginBTN = Button(loginFrame,text="Log In",bd="5",command=pressMyButton)
loginBTN.pack(pady=20,padx=175)

helloLBL = Label(authFrame,text="Oh hello there")
helloLBL.pack(padx=5)

logOutBTN = Button(authFrame,text="log out",command=logOut)
logOutBTN.pack(pady=20,padx=175)
root.mainloop()

