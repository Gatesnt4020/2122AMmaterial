import turtle as t       #t => alias
import random

horiz=[]
vert=[]

shapes=["arrow","turtle","circle","square","triangle","classic"]
hcolors=["red","blue","green","orange","purple","gold"]
vcolors=["magenta","black","darkred","silver","yellow","lime"]

#create all of your turtles
loc=50
for s in shapes:
    #horizontal moving turtles
    lenonardo = t.Turtle(shape=s)
    lenonardo.speed(0)
    horiz.append(lenonardo)
    lenonardo.penup()
    c = hcolors.pop()
    lenonardo.fillcolor(c)
    lenonardo.goto(-350,loc)
    lenonardo.setheading(0)
    
    #vertical moving turtles
    lenonardo = t.Turtle(shape=s)
    lenonardo.speed(0)
    vert.append(lenonardo)
    lenonardo.penup()
    c = vcolors.pop()
    lenonardo.fillcolor(c)
    lenonardo.goto(-loc,350)
    lenonardo.setheading(270)
    
    loc+=50
    

bob=t.Turtle()
bob.penup()
bob.goto(-350,350)
bob.pendown()
for i in range(4):
    bob.forward(350)
    bob.forward(90)
    
    
    

#moving the turtles    
iterations = 0
while True: #check for the length here
        
    #move the turtle
    for h in horiz:
        for v in vert:
            v.forward(random.randint(1-10))
            h.forward(random.randint(1-10))

        #check end of map
        #vertical moving the end of map is at what y value? y=0
        if v.ycor() < 0:
            v.goto(v.xcor(),350)
        #horizontal mobing the end of the map is at what x value? x=0
        if h.xcor() > 0:
            h.goto(h.ycor(),350)




wn=t.Screen()
wn.mainloop()