from tkinter import *    #import everything from Tkinter
#from Tkinter import *   #this is for Python 2
root = Tk()              #creating the window
n=0
#              whichWindow, and the options
canvas = Canvas(root,height=600,width=600)
canvas.grid()            #places it in the window

for i in range(3):#tiers
    canvas.create_polygon(300,300-50-n-n,325+n,325-50-n,275-n,325-25-25-n)
    n+=25
#stump
canvas.create_rectangle(275+25/2,275,325-25/2,300)
#ornaments
canvas.create_oval(305,190,315,200,fill="green")
canvas.create_oval(290,210,300,220,fill="blue")
canvas.create_oval(290,225,300,235,fill="red")
canvas.create_oval(305,225,315,235,fill="red")
canvas.create_oval(275,225,285,235,fill="red")
canvas.create_oval(280,190,290,200,fill="green")
#present
canvas.create_rectangle(360,290,400,330,fill="green")
canvas.create_rectangle(360,315,400,310,fill="red")
canvas.create_rectangle(385,290,380,330,fill="red")

#star
canvas.create_polygon(290,140+10,305,145+10,300,150+10,285,150+10,280,145+10)
#canvas.create_oval(290,140,310,150,fill="yellow")#top of the tree

#snowman
canvas.create_oval(130,400,230,500)#bot
canvas.create_oval(130,400,230,300)#mid
canvas.create_oval(130,300,230,200)#top
canvas.create_oval(150,220,160,230,fill="black")#leye
canvas.create_oval(170,220,180,230,fill="black")#reye
canvas.create_oval((130+230)/2-5,305,(130+230)/2+5,315,fill="black")#top btn
canvas.create_oval((130+230)/2-5,385,(130+230)/2+5,395,fill="black")#mid btn
canvas.create_oval((130+230)/2-5,(400+500)/2+5,(130+230)/2+5,(400+500)/2-5,fill="black")#bot btn
canvas.create_polygon((130+230)/2,(300+200)/2+10,(130+230)/2,(300+200)/2-10,(130+230)/2+10,(300+200)/2,fill="orange")

#snow
canvas.create_oval(0,0,5,5)
canvas.create_oval(400,400,405,405)
canvas.create_oval(200,500,205,505)

#text
canvas.create_text(300,100,text="A circle is techincally a star",fill="black",font=("Helvetica 15 bold"))

#image
canvas.pack(expand=YES,fill=BOTH)
pic = PhotoImage(file="MinecraftSkin.png")
canvas.create_image(100,500,image=pic)
#https://stackoverflow.com/questions/43009527/how-to-insert-an-image-in-a-canvas-item

root.mainloop()          #running the window

#Need to have a 3 tiered tree with ornaments        done
#Need at least 1 wrapped present        done
#Need a star        done
#Need a snowman     done
#Need some snow     done
#Need some text     done

#Need an image
