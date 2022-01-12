import turtle as t       #t => alias

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

#moving the turtles    
iterations = 0
while iterations < 75 and len(horiz)>0: #check for the length here
    
    #move the turtle
    for h in horiz:
        h.forward(5)
    for v in vert:
        v.forward(5)
        
    #check for collision
    #if h and v overlap, then collsision
    if (abs(h.xcor() - v.xcor()) < 20): #check for the length here
        if (abs(h.ycor() - v.ycor()) < 20):
            h.fillcolor("white")
            v.fillcolor("white")
            horiz.remove(h)
            vert.remove(v)
    
    
    iterations+=1




wn=t.Screen()
wn.mainloop()