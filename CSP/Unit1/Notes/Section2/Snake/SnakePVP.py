#import
import turtle as t
import time
import random
#game configuration
delay = 0.1
color=0
player1Bodyparts=[]
player2Bodyparts=[]
#create turtle objects
wn = t.Screen()
wn.bgcolor("orange")
wn.setup(width=600,height=600)          #give a default screen size


player1 = t.Turtle(shape="square")
player1.speed(0)
player1.penup()
player1.setx(15)
player1.direction="stop"

player2 = t.Turtle(shape="square")
player2.speed(0)
player2.penup()
player1.setx(-15)
player2.direction="stop"

#create the food
food = t.Turtle()
food.speed(0)
food.shape("circle")
food.shapesize(.5,.5)       #scaling the food down by 50%
food.color("green")
food.penup()
food.goto(100,100)

#functions
#player1 fun

def player1Up():
    if player1.direction != "s":
        player1.direction="w"
    
def player1Down():
    if player1.direction != "w":
        player1.direction="s"
    
def player1Left():
    if player1.direction != "d":
        player1.direction="a"
    
def player1Right():
    if player1.direction != "a":
        player1.direction="d"
        
def player2Up():
    if player2.direction != "down":
        player2.direction="up"

def player1Move():
    #depending on the direction, the coordinates change
    if player1.direction == "up":
        y = player1.ycor()     #get the y coor
        player1.sety(y+20)     #set the new y coordinate
      
    elif player1.direction == "down":
        y = player1.ycor()     #get the y coor
        player1.sety(y-20)     #set the new y coordinate
        
    elif player1.direction == "right":
        x = player1.xcor()     #get the x coor
        player1.setx(x+20)     #set the new x coordinate
    
    elif player1.direction == "left":
        x = player1.xcor()     #get the x coor
        player1.setx(x-20)     #set the new x coordinate

def player1EatingFood():
    global color
    
    #Food Collision?
    #if player1 or food's distance <20
    if player1.distance(food) < 20:
        #move the food
        #randint(-SCREENWIDTH-SNAKESIZE)
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #add a body part
        part = t.Turtle()
        part.speed(0)
        part.shape("square")
        if color ==0:
            part.color("yellow")
        else:
            part.color("black")
        part.penup()
        player1Bodyparts.apend(part)
        color+=1
        color=color%2

#player2 fun

def player2Down():
    if player2.direction != "up":
        player2.direction="down"
    
def player2Left():
    if player2.direction != "right":
        player2.direction="left"
    
def player2Right():
    if player2.direction != "left":
        player2.direction="right"
def player2Move():
    #depending on the direction, the coordinates change
    if player2.direction == "up":
        y = player2.ycor()     #get the y coor
        player2.sety(y+20)     #set the new y coordinate
      
    elif player2.direction == "down":
        y = player2.ycor()     #get the y coor
        player2.sety(y-20)     #set the new y coordinate
        
    elif player2.direction == "right":
        x = player2.xcor()     #get the x coor
        player2.setx(x+20)     #set the new x coordinate
    
    elif player2.direction == "left":
        x = player2.xcor()     #get the x coor
        player2.setx(x-20)     #set the new x coordinate
        
def hideTheBodyparts():     #gameover    #Border Collision?
    global player1Bodyparts,color
    
    time.sleep(1)           #wait a second
    #move the player1 to 0,0
    player1.goto(0,0)
    #make the player1 stop
    player1.direction="stop"
    #hide the parts
    for parts in player1Bodyparts:
        parts.goto(1000,1000)
    player1Bodyparts=[]
    color=0
    
def player2EatingFood():
    global color
    
    #Food Collision?
    #if player1 or food's distance <20
    if player1.distance(food) < 20:
        #move the food
        #randint(-SCREENWIDTH-SNAKESIZE)
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        food.goto(x,y)
        #add a body part
        part = t.Turtle()
        part.speed(0)
        part.shape("square")
        if color ==0:
            part.color("yellow")
        else:
            part.color("black")
        part.penup()
        bodyparts.apend(part)
        color+=1
        color=color%2
        
def bodyFollow():
    #move the snake
    #Move the butt to the neck
    for i in range(len(player1Bodyparts)-1, 0,-1):     #last index to the first index
        x=player1Bodyparts[i-1].xcor()    #get the x of the next bodypart
        y=player1Bodyparts[i-1].ycor()    #get the y of the next bodypart
        player1Bodyparts[i].goto(x,y)     #reset the current bodypart x,y
    
    #Move the neck to the player1
    if len(player1Bodyparts)>0:
        x=player1.xcor()
        y=player1.ycor()
        player1Bodyparts[0].goto(x,y)

def bodyCollison():
    for part in player1Bodyparts:
        if part.distance(player1) < 10:
            hideTheBodyparts()

#events or running code
wn.listen()
wn.onkeypress(player1Up,"w")
wn.onkeypress(player1Right,"d")
wn.onkeypress(player1Left,"a")
wn.onkeypress(player1Down,"s")
wn.onkeypress(player2Up,"Up")
wn.onkeypress(player2Right,"Right")
wn.onkeypress(player2Left,"Left")
wn.onkeypress(player2Down,"Down")


#main game loop
while True:
    wn.update()     #updates or refreshes the screen
    
    #Border Collision?
    if player1.xcor()>=290 or player1.xcor()<=-290 or player1.ycor()>=290 or player1.ycor()<=-290:
        hideTheBodyparts()
        
    #Food Collision?
    player1EatingFood()
    player2EatingFood()
    
    #move the snake body
    bodyFollow()
    
    player1Move()  #Move the player1
    player2Move()
    
    #Did we hit ourselves?
    bodyCollison()
    
    
    time.sleep(delay)
