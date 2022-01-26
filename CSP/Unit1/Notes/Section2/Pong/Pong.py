#import statements
import turtle as t

#game config
COURT_HEIGHT=600
COURT_WIDTH = 1000
PADDLE_WIDTH = 40

#turtle generation
wn = t.Screen()
wn.setup(width=1.0,height=1.0)      #1.0 is fullscreen

border = t.Turtle(visible=False)    #same as hideturtle

#leftPlayer - redPlayer
leftPlayer = t.Turtle("square")
leftPlayer.color("red")
leftPlayer.penup()
leftPlayer.speed(0)
leftPlayer.setx(-COURT_WIDTH/2)     #set the padde on the left side of the court
leftPlayer.turtlesize(4,1)

#rightPlayer - bluePlayer
rightPlayer = t.Turtle("square")
rightPlayer.color("blue")
rightPlayer.penup()
rightPlayer.speed(0)
rightPlayer.setx(COURT_WIDTH/2)     #set the padde on the left side of the court
rightPlayer.turtlesize(4,1)

#functions
def drawField():
    '''#setup border
    border.speed(0)
    border.pensize(3)
    border.penup()
    #draw the top border
    # border.setposition(-COURT_WIDTH/2, COURT_HEIGHT/2)    #setposition(x,y)
    border.pendown()
    border.forward(COURT_width)
    border.penup()
    #draw the bottom border
    corder.sety(-COURT_HEIGHT/2)
    border.pendown()
    border.backward(COURT_WidTH)
    #draw the halfcourt line
    '''
    border.speed(0)
    border.pensize(3)
    border.penup()
    border.goto(-COURT_WIDTH/2,COURT_HEIGHT/2)
    border.pendown()
    border.forward(COURT_WIDTH)
    border.penup()
    border.goto(-COURT_WIDTH/2,-COURT_HEIGHT/2)
    border.pendown()
    border.forward(COURT_WIDTH)
    border.penup()
    border.goto(0,-COURT_HEIGHT/2)
    border.left(90)
    for i in range(COURT_HEIGHT//50):   #// returns int value for range
        border.pendown()
        border.forward(26)
        border.penup()
        border.forward(26)
        
def upLeft():
    y=leftPlayer.ycor()
    if y<(COURT_HEIGHT/2-PADDLE_WIDTH):
        leftPlayer.sety(y+10)
def downLeft():
    y=leftPlayer.ycor()
    if y>(-COURT_HEIGHT/2+PADDLE_WIDTH):
        leftPlayer.sety(y-10)
def upRight():
    y = rightPlayer.ycor()
    if y<(COURT_HEIGHT/2-PADDLE_WIDTH):
        rightPlayer.sety(y+10)
def downRight():
    y = rightPlayer.ycor()
    if y>(-COURT_HEIGHT/2+PADDLE_WIDTH):
        rightPlayer.sety(y-10)

#main game loop and events    
wn.onkeypress(upLeft,"w")
wn.onkeypress(downLeft,"s")
wn.onkeypress(upRight,"Up")
wn.onkeypress(downRight,"Down")

drawField()

wn.listen()

wn.mainloop()
