import turtle as t

COURT_HEIGHT=600
COURT_WIDTH = 1000

wn = t.Screen()

border = t.Turtle(visible=False)    #same as hideturtle
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
        
    
drawField()

wn.mainloop()
