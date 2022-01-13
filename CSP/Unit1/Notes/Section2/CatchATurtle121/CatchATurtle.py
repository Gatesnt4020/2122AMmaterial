#-----import statements------
import turtle as t
import random as r

#-----game configuration-----
wn = t.Screen()
SCREENW,SCREENH = 300,300
score=0
#tuple variable = ("fony style",fontsize,"font(B,I,U)")
fontSetup=("Comic Sans MS",30,"normal")
timer=5
timesUp=False
counterInverval=1000

counter = t.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(100,200)
counter.pendown()
counter.speed(0)


#-----initialize turtle------
mo = t.Turtle()
mo.shape("turtle")
mo.shapesize(2)
mo.fillcolor("brown")
mo.speed(0)

scorekeeper = t.Turtle()
scorekeeper.speed(0)
scorekeeper.hideturtle()
scorekeeper.penup()
scorekeeper.goto(100,200)
scorekeeper.pendown()


#-----game functions---------
def countdown():
    global timer,timesUp
    counter.clear()
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
    mo.penup()
    mo.hideturtle()
    mo.goto(newX,newY)
    mo.showturtle()
    mo.pendown()
    

#no matter what, if it is a mouse click
#   pass in x and y
def moClicked(x,y):
    #x and y are the cursor's coordinates
    print(x,y)
    print("mo was clicked")
    changePosition()
    updateScore()

#-----events-----------------
#obj.method(command or function name)
mo.onclick(moClicked)
wn.ontimer(countdown,counterInverval)    #clock widget from ______
wn.mainloop()