#import
from re import L
import turtle as t
import time
import random
#game configuration
delay = 0.1
speed=20
bodyParts=[]
isPause=False
isHardMode=False
asked=0
#create turtle objects
wn = t.Screen()
t.title("Snake")
wn.bgcolor("orange")
wn.setup(width=600,height=600)          #gice a default screen size
t.colormode(255)



head = t.Turtle(shape="square")
head.speed(0)
head.penup()
head.direction="stop"

#create the food
food = t.Turtle()
food.speed(0)
food.shape("circle")
food.shapesize(.5,.5)       #scaling the food down by 50%
food.color("green")
food.penup()
food.goto(100,100)

#functions
def up():
    global isPause
    if isPause ==False:
        if head.direction != "down":
            head.direction="up"
    
def down():
    global isPause
    if isPause ==False:
        if head.direction != "up":
            head.direction="down"
    
def left():
    global isPause
    if isPause ==False:
        if head.direction != "right":
            head.direction="left"
    
def right():
    global isPause
    if isPause ==False:
        if head.direction != "left":
            head.direction="right"
        
def pause():
    global isPause
    if isPause == False:
        isPause=True
    else:
        isPause=False
        
def move():
    
    #depending on the direction, the coordinates change
    if head.direction == "up":
        y = head.ycor()     #get the y coor
        head.sety(y+speed)     #set the new y coordinate
    
    elif head.direction == "down":
        y = head.ycor()     #get the y coor
        head.sety(y-speed)     #set the new y coordinate
        
    elif head.direction == "right":
        x = head.xcor()     #get the x coor
        head.setx(x+speed)     #set the new x coordinate
    
    elif head.direction == "left":
        x = head.xcor()     #get the x coor
        head.setx(x-speed)     #set the new x coordinate
        
def hideTheBodyParts():     #gameover    #Border Collision?
    global bodyParts,delay,eaten,speed
    
    time.sleep(1)           #wait a second
    #move the head to 0,0
    head.goto(0,0)
    #make the head stop
    head.direction="stop"
    #hide the parts
    for parts in bodyParts:
        parts.goto(1000,1000)
    bodyParts=[]
    delay = 0.1
    eaten=0
    speed=20
    
def eatingFood():
    global speed
    
    #Food Collision?
    #if head or food's distance <20
    if head.distance(food) < speed:
        #move the food
        #randint(-SCREENWIDTH-SNAKESIZE)
        x=random.randint(-290+speed,290-speed)
        y=random.randint(-290+speed,290-speed)
        r,g,b=random.randint(1,255),random.randint(1,255),random.randint(1,255)
        food.goto(x,y)
        #add a body part
        part = t.Turtle()
        part.speed(0)
        part.shape("square")
        part.color((r,g,b))
        part.penup()
        bodyParts.append(part)
        speed+=2
        
def bodyFollow():
    #move the snake
    #Move the butt to the neck
    for i in range(len(bodyParts)-1, 0,-1):     #last index to the first index
        x=bodyParts[i-1].xcor()    #get the x of the next bodypart
        y=bodyParts[i-1].ycor()    #get the y of the next bodypart
        bodyParts[i].goto(x,y)     #reset the current bodypart x,y
    
    #Move the neck to the head
    if len(bodyParts)>0:
        x=head.xcor()
        y=head.ycor()
        bodyParts[0].goto(x,y)

def bodyCollison():
    for part in bodyParts:
        if part.distance(head) < 10:
            hideTheBodyParts()

def hardMode():
    global isHardMode,asked
    if asked == 0:
        ui=wn.textinput("Game difficulty","Hard mode(1) or normal(2)")
        while ui != "1" and ui != "2":
            ui=wn.textinput("Game difficulty","Hard mode(1) or normal(2)")
        if ui == "1":
            isHardMode=True
        asked+=1
    if isHardMode:
        time.sleep(2)
        x=random.randint(-290+speed,290-speed)
        y=random.randint(-290+speed,290-speed)
        food.goto(x,y)
        

wn.textinput("Your movement","your keys are wasd w is up a is left s is down d is right and p is to pause the game")
hardMode()



#events or running code
wn.listen()
wn.onkeypress(up,"w")
wn.onkeypress(right,"d")
wn.onkeypress(left,"a")
wn.onkeypress(down,"s")
wn.onkeypress(pause,"p")


#main game loop
while True:
    wn.update()     #updates or refreshes the screen
    if not isPause:
        #Border Collision?
        if head.xcor()>=290 or head.xcor()<=-290 or head.ycor()>=290 or head.ycor()<=-290:
            hideTheBodyParts()
            
        #Food Collision?
        eatingFood()
        hardMode()
        #move the snake body
        bodyFollow()
        
        move()  #Move the head
        
        #Did we hit ourselves?wawdawdawd;wpwaadwadawdwadwad
        bodyCollison()
    
    
    time.sleep(delay)