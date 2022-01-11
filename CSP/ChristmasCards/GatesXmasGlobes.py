from turtle import *
from shapes import *
import random

myPen = Turtle()
myPen.shape("turtle")
myPen.speed(10)

window = turtle.Screen()
window.bgcolor("#69D9FF")
#bottom left starting point
#8 circles at the bottom
count = 8
x = 0
y = 0
tsize = random.randint(150,200)
csize = random.randint(20,25)
draw_triangle(myPen,"red",x,y,tsize)
draw_circle(myPen,"white",x+(tsize/2),y+(tsize*.85),csize+5)

while count!=0:
  draw_circle(myPen,"white",x,y-20,csize)
  x+=tsize*.15
  count-=1

'''
def draw_triangle(turtle, color, x, y, size):
def draw_circle(turtle, color, x, y, radius):
from turtle import *
from shapes import *
from random import randint

myPen = Turtle()
myPen.shape("turtle")
myPen.speed(10)

window = turtle.Screen()
window.bgcolor("#69D9FF")

y = -100
width = 240

#let's draw the trunk of the tree
draw_rectangle(myPen, "brown", -15, y-40, 30, 40)

#Now the tree itself
while width>20:
  width = width - randint(20,30)
  height = randint(15,35)
  x = 0 - width/2
  draw_rectangle(myPen, "green", x, y, width, height)
  y = y + height

#And finally let's add a star at the top of our tree.
draw_star(myPen, "yellow", 4, y, 20)

myPen.penup()
myPen.color("red")
myPen.goto(-100, -180)
myPen.write("Merry Christmas", None, None, "24pt bold")
myPen.hideturtle()  
'''
