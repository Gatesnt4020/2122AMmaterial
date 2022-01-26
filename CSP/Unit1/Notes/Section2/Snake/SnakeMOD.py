#import
import turtle as t
import time
import random
#game configuration
delay = 0.1
color=0
bodyParts=[]
speed=15
#create turtle objects
wn = t.Screen()
wn.bgcolor("orange")
wn.setup(width=600,height=600)          #gice a default screen size


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
    if head.direction != "down":
        head.direction="up"
    
def down():
    if head.direction != "up":
        head.direction="down"
    
def left():
    if head.direction != "right":
        head.direction="left"
    
def right():
    if head.direction != "left":
        head.direction="right"
        
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
    global bodyParts,color,speed
    
    time.sleep(1)           #wait a second
    #move the head to 0,0
    head.goto(0,0)
    #make the head stop
    head.direction="stop"
    #hide the parts
    for parts in bodyParts:
        parts.goto(1000,1000)
    bodyParts=[]
    color=0
    speed=15
    
def eatingFood():
    global color,speed
    
    #Food Collision?
    #if head or food's distance <20
    if head.distance(food) < 20:
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
        bodyParts.append(part)
        color+=1
        color=color%2
        speed+=3
        
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

#events or running code
wn.listen()
wn.onkeypress(up,"w")
wn.onkeypress(right,"d")
wn.onkeypress(left,"a")
wn.onkeypress(down,"s")


#main game loop
while True:
    wn.update()     #updates or refreshes the screen
    
    #Border Collision?
    if head.xcor()>=290 or head.xcor()<=-290 or head.ycor()>=290 or head.ycor()<=-290:
        hideTheBodyParts()
        
    #Food Collision?
    eatingFood()
    
    #move the snake body
    bodyFollow()
    
    move()  #Move the head
    
    #Did we hit ourselves?
    bodyCollison()
    
    
    time.sleep(delay)
