#import
import turtle as t
import time
import random
#game configuration
delay = 0.1
bodyParts=[]
bodyParts1=[]
ispause=False
#create turtle objects
wn = t.Screen()
wn.bgcolor("orange")
wn.setup(width=600,height=600)          #gice a default screen size
t.colormode(255)

head = t.Turtle(shape="square")     #left player
head.speed(0)
head.penup()
head.goto(-40,0)
head.direction="stop"

head1 = t.Turtle(shape="square")        #right player
head1.speed(0)
head1.penup()
head1.goto(40,0)
head1.direction="stop"

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
    global ispause
    if ispause ==False:
        if head.direction != "down":
            head.direction="up"
    
def down():
    global ispause
    if ispause ==False:
        if head.direction != "up":
            head.direction="down"
    
def left():
    global ispause
    if ispause ==False:
        if head.direction != "right":
            head.direction="left"
    
def right():
    global ispause
    if ispause ==False:
        if head.direction != "left":
            head.direction="right"
        
def up1():
    global ispause
    if ispause ==False:    
        if head1.direction != "down":
            head1.direction="up"
    
def down1():
    global ispause
    if ispause ==False:    
        if head1.direction != "up":
            head1.direction="down"
    
def left1():
    global ispause
    if ispause ==False:
        if head1.direction != "right":
            head1.direction="left"
    
def right1():
    global ispause
    if ispause ==False:
        if head1.direction != "left":
            head1.direction="right"
        
def move():
    #depending on the direction, the coordinates change
    if head.direction == "up":
        y = head.ycor()     #get the y coor
        head.sety(y+20)     #set the new y coordinate
      
    elif head.direction == "down":
        y = head.ycor()     #get the y coor
        head.sety(y-20)     #set the new y coordinate
        
    elif head.direction == "right":
        x = head.xcor()     #get the x coor
        head.setx(x+20)     #set the new x coordinate
    
    elif head.direction == "left":
        x = head.xcor()     #get the x coor
        head.setx(x-20)     #set the new x coordinate
        
def move1():
    #depending on the direction, the coordinates change
    if head1.direction == "up":
        y = head1.ycor()     #get the y coor
        head1.sety(y+20)     #set the new y coordinate
      
    elif head1.direction == "down":
        y = head1.ycor()     #get the y coor
        head1.sety(y-20)     #set the new y coordinate
        
    elif head1.direction == "right":
        x = head1.xcor()     #get the x coor
        head1.setx(x+20)     #set the new x coordinate
    
    elif head1.direction == "left":
        x = head1.xcor()     #get the x coor
        head1.setx(x-20)     #set the new x coordinate
        
def hideTheBodyParts():     #gameover    #Border Collision?
    global bodyParts
    
    time.sleep(1)           #wait a second
    #move the head to 0,0
    head.goto(0,0)
    #make the head stop
    head.direction="stop"
    #hide the parts
    for parts in bodyParts:
        parts.goto(1000,1000)
    bodyParts=[]

def hideTheBodyParts1():     #gameover    #Border Collision?
    global bodyParts1
    
    time.sleep(1)           #wait a second
    #move the head to 0,0
    head1.goto(0,0)
    #make the head stop
    head1.direction="stop"
    #hide the parts
    for parts in bodyParts1:
        parts.goto(1000,1000)
    bodyParts1=[]
    
def eatingFood():
    
    #Food Collision?
    #if head or food's distance <20
    if head.distance(food) < 20:
        #move the food
        #randint(-SCREENWIDTH-SNAKESIZE)
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        r,g,b=random.randint(1,255),random.randint(1,255),random.randint(1,255)
        food.goto(x,y)
        #add a body part
        part = t.Turtle()
        part.speed(0)
        part.shape("square")
        part.color((r,g,b))
        part.penup()
        bodyParts.append(part)

def eatingFood1():
    
    #Food Collision?
    #if head or food's distance <20
    if head1.distance(food) < 20:
        #move the food
        #randint(-SCREENWIDTH-SNAKESIZE)
        x=random.randint(-290,290)
        y=random.randint(-290,290)
        r,g,b=random.randint(1,255),random.randint(1,255),random.randint(1,255)
        food.goto(x,y)
        #add a body part
        part1 = t.Turtle()
        part1.speed(0)
        part1.shape("square")
        part1.color((r,g,b))
        part1.penup()
        bodyParts1.append(part1)
        
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

def bodyFollow1():
    #move the snake
    #Move the butt to the neck
    for i in range(len(bodyParts1)-1, 0,-1):     #last index to the first index
        x=bodyParts1[i-1].xcor()    #get the x of the next bodypart
        y=bodyParts1[i-1].ycor()    #get the y of the next bodypart
        bodyParts1[i].goto(x,y)     #reset the current bodypart x,y
    
    #Move the neck to the head
    if len(bodyParts1)>0:
        x=head1.xcor()
        y=head1.ycor()
        bodyParts1[0].goto(x,y)

def bodyCollison():
    for part in bodyParts:
        if part.distance(head) < 10:
            hideTheBodyParts()

def bodyCollison1():
    for part in bodyParts1:
        if part.distance(head1) < 10:
            hideTheBodyParts1()
            
def pause():
    global ispause
    if ispause == False:
        ispause=True
    else:
        ispause=False

#events or running code
wn.listen()
wn.onkeypress(up,"w")
wn.onkeypress(right,"d")
wn.onkeypress(left,"a")
wn.onkeypress(down,"s")
wn.onkeypress(up1,"Up")
wn.onkeypress(right1,"Right")
wn.onkeypress(left1,"Left")
wn.onkeypress(down1,"Down")
wn.onkeypress(pause,"p")
#wn.textinput("your keys are wasd for the left player w is up a is left s is down d is right and for the right player the arrow keys plus p is to pause the game")


#main game loop
while True:
    wn.update()     #updates or refreshes the screen
    if not ispause:
        #Border Collision?
        if head.xcor()>=290 or head.xcor()<=-290 or head.ycor()>=290 or head.ycor()<=-290:
            hideTheBodyParts()
            
        if head1.xcor()>=290 or head1.xcor()<=-290 or head1.ycor()>=290 or head1.ycor()<=-290:
            hideTheBodyParts1()
        #Food Collision?
        eatingFood()
        eatingFood1()
        
        #move the snake body
        bodyFollow()
        bodyFollow1()
        
        move()  #Move the head
        move1()
        
        #Did we hit ourselves?
        bodyCollison()
        bodyCollison1()
        
        
        time.sleep(delay)
