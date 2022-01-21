from turtle import *
import random
import mazeleaders as lb
import os


FILENAME = "leaderboard.txt"
if os.path.exists(FILENAME) == False:
    f = open(FILENAME,"w")
    f.write("")
    f.close

with open(FILENAME,'r') as f:
    file = f.readlines()
    f.close()

name = input("Please enter your name ")
distance = 20
PATH_WIDTH = 20
NUMWALLS = 25
timer=0
counterInverval=1000
fontSetup=("Comic Sans MS",10,"normal")
gameover = False
dead = False
x=0
y=0
end =[-234,-234,132]
pstep=0
bstep=0
istep=0

wn=Screen()
ma = Turtle()
ma.speed(0)
ma.pensize(5)
ma.setheading(90)
ma.penup()
ma.goto(100,-50)
ma.pendown()

timekeeper=Turtle()
timekeeper.speed(0)
timekeeper.hideturtle()
timekeeper.penup()
timekeeper.goto(100,200)
timekeeper.pendown()

pinky = Turtle()
blinky = Turtle()
inky = Turtle()
pinky.penup()
blinky.penup()
inky.penup()

pinky.goto(241,330)
pp=pinky.ycor()
pinky.setheading(270)
blinky.goto(-292,330)
pb=blinky.ycor()
blinky.setheading(270)
inky.goto(-180,200)
pi=inky.xcor()



#game functions
def lookUp():
    ma.setheading(90)

def lookDown():
    ma.setheading(270)

def lookRight():
    ma.setheading(0)

def lookLeft():
    ma.setheading(180)

def go():
    global gameover
    ma.fd(20)
    x=ma.xcor()
    y=ma.ycor()
    if (20>x>0):
        if (60>y>40):
            gameover = True
            ma.hideturtle()

def gofast():
    global gameover
    ma.fd(40)
    x=ma.xcor()
    y=ma.ycor()
    if (20>x>0):
        if (60>y>40):
            gameover = True
            ma.hideturtle()

def updateHS():
    global FILENAME
    with open(FILENAME,"a") as f:
        f.write("AAA,10")
        f.close()
        
def manageLeaderboard():
     global timer
     global timekeeper
     global name
    
     
     #parallel list ->same length and corresponding data based on the index
     namesList = lb.get_names(FILENAME)   #accessor method to get the names
     timersList = lb.get_time(FILENAME)
     
     print("namesList",namesList)
     print("timersList",timersList)
     
     #show the lb w/ or w/o the current player
     if(len(timersList)<5 or timer >= int(timersList[4])):
          lb.update_leaderboard(FILENAME, namesList, timersList, name, timer)
          lb.draw_leaderboard(True, namesList, timersList, timekeeper, timer)
     else:
          lb.draw_leaderboard(False, namesList, timersList, timekeeper, timer)
          

def count():
    global timer, gameover, dead,pstep,bstep,istep
    if gameover == True:
        pinky.hideturtle()
        blinky.hideturtle()
        inky.hideturtle()
        ma.goto(0,0)
        ma.pendown()
        ma.clear()
        wn.onkeypress(None,"Up")
        wn.onkeypress(None,"Down")
        wn.onkeypress(None,"Left")
        wn.onkeypress(None,"Right")
        wn.onkeypress(None,"g")
        wn.onkeypress(None,"w")
        manageLeaderboard()
    else:
        timer+=1
        ma.getscreen().ontimer(count,counterInverval)
        p=pinky.ycor()
        b=blinky.ycor()
        i=inky.xcor()
        if (p>end[0]):
            pstep+=1
            pinky.fd(40)
        else:
            for ss in range(pstep):
                pinky.backward(40)
            pstep-=pstep
        if (b>end[1]):
            bstep+=1
            blinky.fd(40)
        else:
            for ss in range(bstep):
                blinky.backward(40)
            bstep-=bstep
        if (i<end[2]):
            istep+=1
            inky.fd(40)
        else:
            for ss in range(istep):
                inky.backward(40)
            istep-=istep
        if (abs(ma.xcor() - pinky.xcor()) < 40): #check for the length here
            if (abs(ma.ycor() - pinky.ycor()) < 40):
                dead=True
                gameover=True
                print("dead")
        if (abs(ma.xcor() - blinky.xcor()) < 30): #check for the length here
            if (abs(ma.ycor() - blinky.ycor()) < 30):
                dead=True
                gameover=True
                print("dead")
        if (abs(ma.xcor() - inky.xcor()) < 40): #check for the length here
            if (abs(ma.ycor() - inky.ycor()) < 40):
                dead=True
                gameover=True
                print("dead")


def drawDoor():
    ma.forward(10)
    ma.penup()
    ma.forward(PATH_WIDTH*2)
    ma.pendown()

def drawBarrier():
    ma.forward(PATH_WIDTH*3)
    ma.left(90)
    ma.forward(PATH_WIDTH*2)
    ma.backward(PATH_WIDTH*2)
    ma.right(90)


#events and mainloop running code
lengthOfTheWall = PATH_WIDTH
wn.onkeypress(lookUp,"Up")
wn.onkeypress(lookDown,"Down")
wn.onkeypress(lookLeft,"Left")
wn.onkeypress(lookRight,"Right")
wn.onkeypress(go,"g")
wn.onkeypress(gofast,"w")

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
            if i<21:
                drawDoor()
            else:
                ma.forward(PATH_WIDTH*2.5)
            if i<24:
                drawBarrier()
            else:
                ma.forward(PATH_WIDTH)
        else:
            if i<21:
                drawDoor()
            else:
                ma.forward(PATH_WIDTH*2.5)
            if i<24:
                drawBarrier()
            else:
                ma.forward(PATH_WIDTH)
        ma.fd(lengthOfTheWall)
        ma.left(90)
ma.penup()
ma.hideturtle()
ma.goto(10,50)
ma.shape("circle")
ma.fillcolor("green")
ma.stamp()
ma.fillcolor("black")
ma.goto(350,350)
ma.shape("turtle")
ma.showturtle()        

wn.listen()
wn.ontimer(count,counterInverval)
wn.mainloop()