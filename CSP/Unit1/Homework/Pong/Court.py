import turtle as t

COURT_HEIGHT = 600
COURT_WIDTH = 1000

wn = t.Screen()

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

drawField()

wn.mainloop()