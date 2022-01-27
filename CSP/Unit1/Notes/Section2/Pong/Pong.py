#import statements
from lib2to3.pgen2.token import RIGHTSHIFT
from tkinter import font
import turtle as t
import random as rand

#game config
COURT_HEIGHT = 600
COURT_WIDTH = 1000
PADDLE_WIDTH = 40
BALL_SIZE=15
speed=10
leftScore=0
rightScore=0
fontSettings = ("Arial",100,"normal")
darkMode=True

#turtle generation
wn = t.Screen()
wn.setup(width=1.0,height=1.0)     #1.0 is fullscreen 
ball = t.Turtle()
ball.shape("circle")
ball.color("black")
ball.penup()
ball.speed(0)


border = t.Turtle(visible=False)   #same as hideturtle

#leftPlayer - redPlayer
leftPlayer = t.Turtle("square")
leftPlayer.color("red")
leftPlayer.penup()
leftPlayer.speed(0)
leftPlayer.setx(-COURT_WIDTH/2)         #set the paddle on the left side of the court
leftPlayer.turtlesize(4,1)              #turns a square into a rectangle

lScore=t.Turtle(visible=False)
lScore.speed(0)
lScore.penup()
lScore.setposition(-COURT_WIDTH/4,COURT_HEIGHT/4)
lScore.write(leftScore,font=fontSettings)

#rightPlayer - bluePlayer
rightPlayer = t.Turtle("square")
rightPlayer.color("blue")
rightPlayer.penup()
rightPlayer.speed(0)
rightPlayer.setx(COURT_WIDTH/2)         #set the paddle on the left side of the court
rightPlayer.turtlesize(4,1)              #turns a square into a rectangle

rScore=t.Turtle(visible=False)
rScore.speed(0)
rScore.penup()
rScore.setposition(COURT_WIDTH/4,COURT_HEIGHT/4)
rScore.write(rightScore,font=fontSettings)

#Functions
def drawField():
    #setup border
    border.speed(0)
    border.pensize(3)
    border.penup()
    #draw the top border
    border.setposition(-COURT_WIDTH/2, COURT_HEIGHT/2)  #setposition(x,y)
    border.pendown()
    border.forward(COURT_WIDTH)
    border.penup()
    #draw the bottom border
    border.sety(-COURT_HEIGHT/2)
    border.pendown()
    border.backward(COURT_WIDTH)   #in the bottom left corner
    #draw the halfcourt line
    border.penup()
    border.setposition(0,-COURT_HEIGHT/2)
    border.pendown()
    border.setheading(90)
    border.pensize(1)
    #dashes.....
    for i in range(COURT_HEIGHT//50):       #// returns int value for range
        border.forward(26)
        border.penup()
        border.forward(26)
        border.pendown()
def upLeft():
    y=leftPlayer.ycor()
    if y<(COURT_HEIGHT/2-PADDLE_WIDTH):
        leftPlayer.sety(y+10)
     
def downLeft():
    y=leftPlayer.ycor()
    if y>(-COURT_HEIGHT/2+PADDLE_WIDTH):
        leftPlayer.sety(y-10)
     
def upRight():
    y=rightPlayer.ycor()
    if y<(COURT_HEIGHT/2-PADDLE_WIDTH):
        rightPlayer.sety(y+10)
     
def downRight():
    y=rightPlayer.ycor()
    if y>(-COURT_HEIGHT/2+PADDLE_WIDTH):
        rightPlayer.sety(y-10)
          
def resetBall():        #debugging/gameover
    ball.setposition(0,0)
    if rand.randint(0,1) == 0:      #choose who serves
        ball.setheading(rand.randint(135,225))         #setheading for direction
    else:
        ball.setheading(rand.randint(-45,45))

def collideWithPaddle(paddle,b):    #passing the paddle and ball turtle
    #this f(x) will check if the gien paddle and ball collide
    if paddle.distance(b) <PADDLE_WIDTH:
        b.setheading(180-b.heading())
        if b.xcor()>0:      #on the right side of the court
            b.setx(b.xcor()-10)   #cheat to keep the ball out of the paddle
    else:
        b.setx(b.xcor()+5)  #cheat tot keep the ball out of the paddle
    b.forward(speed)

def move():    #reseting the ball's x,y 
    global leftScore, rightScore
    ball.forward(speed)
    x,y = ball.position()
    #did hit the top or bottom?
    if y>(COURT_HEIGHT/2-BALL_SIZE):
        ball.setheading(-ball.heading()-20)
    elif y<(-COURT_HEIGHT/2+BALL_SIZE):
        ball.setheading(-ball.heading()+20)
    #did it hit the edge?
    elif x>(COURT_WIDTH/2) or x<(-COURT_WIDTH/2):
        if x>COURT_WIDTH/2:
            leftScore+=1
            lScore.clear()
            lScore.write(leftScore,font=fontSettings)
        else:
            rightScore+=1
            rScore.clear()
            rScore.write(rightScore,font=fontSettings)
        resetBall()
    #did it hit a paddle?
    else:
        collideWithPaddle(leftPlayer,ball)
        collideWithPaddle(rightPlayer,ball)
    wn.ontimer(move,15)

if darkMode==True:
    wn.bgcolor("black")
    ball.colir("white")
    border.color("white")

#main game loop and events
wn.onkeypress(upLeft,"w")
wn.onkeypress(downLeft,"s")
wn.onkeypress(upRight,"Up")
wn.onkeypress(downRight,"Down")
wn.onkeypress(resetBall,"r")
wn.listen()

drawField()
move()

wn.mainloop()