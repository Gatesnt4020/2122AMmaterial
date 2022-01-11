#x,y is now in the middle
from turtle import *
from shapes import *


myPen = Turtle()
window = Screen()

for i in range(4):
    myPen.forward(145)
    #myPen.forward(184)
    myPen.right(90)

myPen.penup()
myPen.goto(-200,-200)
myPen.pendown()

for i in range(4):
    myPen.forward(145)
    #myPen.forward(184)
    myPen.right(90)

myPen.circle(60)
myPen.forward(100)
myPen.left(135)
myPen.forward(100/1.41)
myPen.left(90)
myPen.forward(100/1.41)

draw_circle(myPen,"blue",100,100,50)
draw_circle(myPen,"green",-100,-100,-50)
draw_sqaure(myPen, "magenta",-100,100,50)
draw_rectangle(myPen,"#0F2B68",-300,300,50,25)

mainloop()