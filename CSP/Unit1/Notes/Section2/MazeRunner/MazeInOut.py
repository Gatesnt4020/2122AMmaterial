from turtle import *
import random

distance = 20
PATH_WIDTH = 20
NUMWALLS = 25

wn=Screen()
mazeDrawer = Turtle()
mazeDrawer.speed(0)
mazeDrawer.pensize(5)
mazeDrawer.setheading(90)
mazeDrawer.penup()
mazeDrawer.goto(100,-50)
mazeDrawer.pendown()

#gmae functions
def lookUp():
    mazeDrawer.setheading(90)
def lookDown():
    mazeDrawer.setheading(270)
def lookRight():
    mazeDrawer.setheading(0)
def lookLeft():
    mazeDrawer.setheading(180)
def go():
    mazeDrawer.fd(20)


def drawDoor():
    mazeDrawer.forward(10)
    mazeDrawer.penup()
    mazeDrawer.forward(PATH_WIDTH*2)
    mazeDrawer.pendown()

def drawBarrier():
    mazeDrawer.forward(PATH_WIDTH*3)
    mazeDrawer.left(90)
    mazeDrawer.forward(PATH_WIDTH*2)
    mazeDrawer.backward(PATH_WIDTH*2)
    mazeDrawer.right(90)

#events and mainloop running code
lengthOfTheWall = PATH_WIDTH
wn.onkeypress(lookUp,"Up")
wn.onkeypress(lookDown,"Down")
wn.onkeypress(lookLeft,"Left")
wn.onkeypress(lookRight,"Right")
wn.onkeypress(go,"g")
#draw the remaining walls
for i in range(NUMWALLS):
    lengthOfTheWall+=PATH_WIDTH
    #skip the first 4 walls
    if(i>3):
        #find when to draw a door
        door = random.randint(2*PATH_WIDTH, lengthOfTheWall-2*PATH_WIDTH)
        #find when to draw a barrier
        barrier=random.randint(2*PATH_WIDTH, lengthOfTheWall-2*PATH_WIDTH)
        
        #CHECK to see if hte door and barrier are within a range
        while abs(door-barrier) < PATH_WIDTH:
            door=random.randint(2*PATH_WIDTH, lengthOfTheWall-2*PATH_WIDTH)
        
        if(door<barrier):
            if i<23:
                drawDoor()
            drawBarrier()
        else:
            if i<23:
                drawDoor()
            drawBarrier()
        mazeDrawer.fd(lengthOfTheWall)
        mazeDrawer.left(90)
mazeDrawer.penup()
mazeDrawer.goto(-50,20)

wn.listen()
wn.mainloop()