import turtle as t
import random as rand

COURT_HEIGHT = 600
COURT_WIDTH = 1000
BALL_SIZE=15

wn = t.Screen()

ball = t.Turtle()
ball.shape("circle")
ball.color("black")
ball.penup()
ball.speed(0)


border = t.Turtle(visible=False)   #same as hideturtle
def drawField():
    #setup border
    border.speed(0)
    border.pensize(3)
    border.penup()
    #draw the top border
    border.setposition(-COURT_WIDTH/2, COURT_HEIGHT/2)  #setposition(x,y)
    border.pendown()
    border.forward(COURT_WIDTH)
    #border.penup()
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
    border.goto(-COURT_WIDTH/2, COURT_HEIGHT/2)
    border.backward(COURT_HEIGHT)

def resetBall():        #debugging/gameover
    ball.setposition(0,0)
    if rand.randint(0,1) == 0:      #choose who serves
        ball.setheading(rand.randint(135,225))         #setheading for direction
    else:
        ball.setheading(rand.randint(-45,45))


def move():     #reseting the ball's x,y
    ball.forward(20)
    x,y = ball.position()
    #did hit the top or bottom?
    if y>=(COURT_HEIGHT/2-BALL_SIZE) or y<=(-COURT_HEIGHT/2-BALL_SIZE):
        ball.setheading(-ball.heading())
    elif x >=(COURT_WIDTH/2-BALL_SIZE) or x<=(-COURT_WIDTH/2-BALL_SIZE):
        resetBall()
    #did it hit the edge?
    #did it hit a paddle?
    wn.ontimer(move,20)


drawField()
move()

wn.listen()
wn.onkeypress(resetBall,"r")
wn.mainloop()