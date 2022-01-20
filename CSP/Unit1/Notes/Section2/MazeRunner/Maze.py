from turtle import *

wn=Screen()
mazeDrawer = Turtle()
mazeDrawer.speed(0)
mazeDrawer.pensize(5)
mazeDrawer.penup()

distance = 500
PATH_WIDTH = 20
NUMWALLS = 25

#move the turtle to the top right
mazeDrawer.goto(300,300)
mazeDrawer.right(90)
mazeDrawer.pendown()

#draw the right and bottom wall
mazeDrawer.fd(distance)
mazeDrawer.right(90)
mazeDrawer.fd(distance)
mazeDrawer.right(90)

#draw the remaining walls
for i in range(NUMWALLS-2):
    distance-=PATH_WIDTH
    mazeDrawer.fd(distance)
    mazeDrawer.right(90)
    
    
wn.mainloop()