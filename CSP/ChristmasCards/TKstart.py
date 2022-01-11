from tkinter import *    #import everything from Tkinter
#from Tkinter import *   #this is for Python 2
root = Tk()              #creating the window

#              whichWindow, and the options
canvas = Canvas(root,height=600,width=600)
canvas.grid()            #places it in the window



#starting to draw
#rectangle
#create_rectange(x1,y1,x2,y2,*options)
canvas.create_rectangle(0,400,600,600,fill="green")

canvas.create_rectangle(300,400,350,350,fill="brown")


#oval => circle
#create_oval(x1,y1,x2,y2,*options)
#canvas.create_oval(275,275,325,325)
#line
#create_line(x1,y1,x2,y2,*options)
#canvas.create_line(100+16,120,275+16,325)

#any shape
#create_polygon(x1,y1,x2,y2,x3,y3,etc,*options)
#canvas.create_polygon(300,300-50,325,325-50,275,325-25-25)

root.mainloop()          #running the window

#Need a 3 tiered Tree with ornaments
#Need at least 1 wrapped present
#Need a star
#Need a snowman
