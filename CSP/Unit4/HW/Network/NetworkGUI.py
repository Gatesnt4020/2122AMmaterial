from tkinter import *
import os,datetime

root = Tk()
root.geometry("600x700")
root.title("Network GUI")

root.bind("<Escape>", lambda x: root.destroy())

output = StringVar()

#makes a parent frame for the help and main frames
firstFrame=Frame(root)
firstFrame.grid(row=0,column=0,sticky='news')
secondFrame=Frame(root)
secondFrame.grid(row=0,column=0,sticky='news')

#used to continue after the help frame comes up 
def back():
    firstFrame.tkraise()

#will run the text through a powershell and grabs the information and puts it's input a the output variable
def doCommand(ui):
    global output
    try:
        output.set(os.popen(f"{ui} {ip.get()}").read())
    except:
        output.set(os.popen(ui).read())

#grabs the current datetime and write what was in the output into a txt file
def save():
    #landen gave me this idea so thank you landen
    open(datetime.datetime.ctime(datetime.datetime.now()).replace(":","_")+".txt","w").write(output.get())

helpInfo=("IPconfig - IP information for all network adapters in use by Windows will be displayed","Tracert - A utility designed for displaying the time it takes for a packet of information to travel between a local \ncomputer and a destination IP address or domain","Ping - Sends a request over the network to a specific device to see if it is reachable","NSLookUp - Enter a host name (for example, 'whatis.com') and find out the corresponding IP address or \ndomain name system (DNS) record")

helpFrame = Frame(secondFrame)
helpFrame.grid(row=0,column=0)

backBTN = Button(helpFrame,text='Continue',command=back)
backBTN.grid(row=0,column=0)

#prints the info of what things do incase the user doesn't know what they are
for i in range(len(helpInfo)):
    lbls = Label(helpFrame,text=helpInfo[i])
    lbls.grid(row=i+1,column=0)

mainFrame = Frame(firstFrame)
mainFrame.pack()

outputFrame = Frame(firstFrame)
outputFrame.pack()

#main buttons to run the commands for the gui
ipconfig = Button(mainFrame,text="ipconfig",justify=CENTER,command=lambda:doCommand("ipconfig"))
ipconfig.grid(row=0,column=0)
ping = Button(mainFrame,text="ping",justify=CENTER,command=lambda:doCommand("ping"))
ping.grid(row=0,column=1)
tracert = Button(mainFrame,text="trace route",justify=CENTER,command=lambda:doCommand("tracert"))
tracert.grid(row=0,column=2)
nslookup = Button(mainFrame,text="nslookup",justify=CENTER,command=lambda:doCommand("nslookup"))
nslookup.grid(row=0,column=3)

#is the entry were you would put your ipaddress or url to look up
ip = Entry(outputFrame,justify=CENTER)
ip.grid(row=2,column=0)

#puts the information giving to the output var and prints it out
outputLBL = Label(outputFrame,width=60,height=30,textvariable=output,background='black',foreground='white',justify=CENTER)
outputLBL.grid(row=3,column=0)

#the save button
saveBtn = Button(outputFrame,text="Save",justify=CENTER,command=save)
saveBtn.grid(row=4,column=0)

root.mainloop()
