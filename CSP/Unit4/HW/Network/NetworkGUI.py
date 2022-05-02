from tkinter import *
import os,time

root = Tk()
root.geometry("600x600")
root.title("Network GUI")

root.bind("<Escape>", lambda x: root.destroy())


def raiseBTN(name):
    #https://www.geeksforgeeks.org/how-to-check-which-button-was-clicked-in-tkinter/ to tell which button was pressed
    name.tkraise()
    
def back():
    mainFrame.tkraise()

    
#The ipconfig screen
#rome was here
ipFrame = Frame(root)
ipFrame.grid(row=0,column=0,sticky='news')
helpLBL= Label(ipFrame,text="IP information for all network adapters in use by Windows will be displayed",padx=5,pady=5)
helpLBL.grid(row=1,column=1)
backBTN = Button(ipFrame,text='Back',command=back)
backBTN.grid(row=0,column=0)
ipBTN = Button(ipFrame,text="IPconfig")
ipBTN.grid(row=2,column=1)
ipLBL = Label(ipFrame)

#The traceFrame screen
traceFrame = Frame(root)
traceFrame.grid(row=0,column=0,sticky='news')
helpLBL= Label(traceFrame,text="A utility designed for displaying the time it takes for a packet of information to travel between a local \ncomputer and a destination IP address or domain",padx=5,pady=5)
helpLBL.grid(row=1,column=1)
backBTN = Button(traceFrame,text='Back',command=back)
backBTN.grid(row=0,column=0)

#The pingFrame screen
pingFrame = Frame(root)
pingFrame.grid(row=0,column=0,sticky='news')
helpLBL= Label(pingFrame,text="Sends a request over the network to a specific device to see if it is reachable",padx=5,pady=5)
helpLBL.grid(row=1,column=1)
backBTN = Button(pingFrame,text='Back',command=back)
backBTN.grid(row=0,column=0)

#The nsFrame screen
nsFrame = Frame(root)
nsFrame.grid(row=0,column=0,sticky='news')
helpLBL= Label(nsFrame,text="Enter a host name (for example, 'whatis.com') and find out the corresponding IP address or \ndomain name system (DNS) record",padx=5,pady=5)
helpLBL.grid(row=1,column=1)
backBTN = Button(nsFrame,text='Back',command=back)
backBTN.grid(row=0,column=0)

#The main screen where the user will be able to access the commands
mainFrame = Frame(root)
mainFrame.grid(row=0,column=0,sticky='news')
mainLBL= Label(mainFrame,text="Welcome to my Network GUI if any of the button confuse you press them and they'll have an explanation",padx=5,pady=5)
mainLBL.grid(row=0,column=0,ipady=2,ipadx=2)
ipBTN = Button(mainFrame,text='ipconfig',bd=2,command=lambda i=ipFrame: raiseBTN(i))
ipBTN.grid(row=1,column=0,ipady=2,ipadx=2)
traceBTN = Button(mainFrame,text='tracert',bd=2,command=lambda i=traceFrame: raiseBTN(i))
traceBTN.grid(row=2,column=0,ipady=2,ipadx=2)
pingBTN = Button(mainFrame,text='ping',bd=2,command=lambda i=pingFrame: raiseBTN(i))
pingBTN.grid(row=3,column=0,ipady=2,ipadx=2)
nsBTN = Button(mainFrame,text='nslookup',bd=2,command=lambda i=nsFrame: raiseBTN(i))
nsBTN.grid(row=4,column=0,ipady=2,ipadx=2)

#The welcoming screen for the user
welcomeFrame = Frame(root)
welcomeLBL = Label(welcomeFrame,text="Welcome to my Network GUI")
startBTN = Button(welcomeFrame,text="Start",command=lambda i=mainFrame: raiseBTN(i))
welcomeFrame.grid(row=0,column=0,sticky='news')
#https://www.geeksforgeeks.org/python-place-method-in-tkinter/ making the buttons center themselves
welcomeLBL.place(anchor=NW)
startBTN.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()