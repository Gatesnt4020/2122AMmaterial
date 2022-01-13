#-----import statements------
import turtle as t
import random as r

#-----game configuration-----
wn = t.Screen()
SCREENW,SCREENH = 300,300
score=0
#tuple variable = ("fony style",fontsize,"font(B,I,U)")
fontSetup=("Comic Sans MS",15,"normal")
timer=10
timesUp=False
start=False
counterInverval=1000
totclick=0

counter = t.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(-300,200)
counter.pendown()
counter.speed(0)


#-----initialize turtle------
mo = t.Turtle()
mo.shape("turtle")
mosize=2
mo.shapesize(mosize)
mo.fillcolor("blue")
mo.speed(0)

scorekeeper = t.Turtle()
scorekeeper.speed(0)
scorekeeper.hideturtle()
scorekeeper.penup()
scorekeeper.goto(100,200)
scorekeeper.pendown()

aimbot = t.Turtle()
aimbot.speed(0)
aimbot.hideturtle()
aimbot.penup()
aimbot.goto(-50,200)
aimbot.pendown()



#-----game functions---------
def aim(x,y):
    global totclick,score,timesUp

    totclick+=1
    aimbot.clear()
    aimbot.write(f"Total clicks: {totclick}",font=fontSetup)
    if timesUp == True:
        aimbot.goto(0,0)
        acc = (score/totclick)*10
        aimbot.write(f"your accuracy is {round(acc),2}")
    

def countdown():
    global timer,timesUp
    counter.clear()
    if start !=False:
        if timer <= 0:
            counter.write("Times's up",font=fontSetup)
            timesUp=True
        else:
            counter.write(f"Time: {timer}",font=fontSetup)
            timer-=1
            #recursively run this function again to create a loop
            counter.getscreen().ontimer(countdown,counterInverval)

def updateScore():
    global score
    #it will see the var score in other parts of the program
    score+=1
    scorekeeper.clear()     #clear what it already wrote
    #write the score
    scorekeeper.write(f"Score: {score}",font=fontSetup)


def changePosition():
    global SCREENH,SCREENW
    #move the turtle to a random location on screen.
    newX = r.randint(-SCREENW/2,SCREENW/2)
    newY = r.randint(-SCREENH/2,SCREENH/2)
    mo.color("white")
    mo.pencolor("red")
    mo.stamp()
    mo.pencolor("black")
    mo.color("blue")
    mo.penup()         #doesn't leave a trail
    mo.hideturtle()    #don't see where it is going
    mo.goto(newX,newY)
    mo.showturtle()
    mo.pendown()
    

#no matter what, if it is a mouse click
#   pass in x and y
def moClicked(x,y):
    global timesUp,start,mosize
    if start !=True:
        start=True
        counter.getscreen().ontimer(countdown,counterInverval)
    if timesUp != True:
        #x and y are the cursor's coordinates
        print(x,y)
        print("mo was clicked")
        wn.bgcolor('red')
        changePosition()
        updateScore()
        wn.bgcolor('white')
        mosize=mosize/2
        mo.shapesize(mosize)
        if mosize<=(2/(2**3)):
            mosize=5
       
#-----events-----------------
#obj.method(command or function name)
mo.onclick(moClicked)
wn.onscreenclick(aim)
wn.ontimer(countdown,counterInverval)    #clock widget from ______
wn.mainloop()