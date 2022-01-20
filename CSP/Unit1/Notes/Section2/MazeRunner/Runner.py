from turtle import *

wn=Screen()
runner=Turtle()

#functions or commands
def lookUp():
    runner.setheading(90)
def lookDown():
    runner.setheading(270)
def lookRight():
    runner.setheading(0)
def lookLeft():
    runner.setheading(180)
def go():
    runner.fd(20)

#events and bindings
wn.onkeypress(lookUp,"Up")
wn.onkeypress(lookDown,"Down")
wn.onkeypress(lookLeft,"Left")
wn.onkeypress(lookRight,"Right")
wn.onkeypress(go,"g")

#always make sure you have this
wn.listen()

wn.mainloop()