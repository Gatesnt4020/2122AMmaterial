import turtle as t

shapes=["arrow","turtle","circle","square","triangle","classic"]*2
colors=["red","blue","green","orange","pale goldenrod","medium violet red"]*2
myturds = []

for i in range(len(shapes)):
    #                      keyword parameter shape is a characteristic of your turtle
    c = colors.pop()
    bob = t.Turtle(shape=shapes[i])
    bob.fillcolor(c)        #color of the turtle
    bob.pencolor(c)                 #change the color of the pen
    bob.penup()
    myturds.append(bob)

x,y=0,0
direction=90
distance=50
for turt in myturds:
    turt.goto(x,y)
    turt.setheading(direction)          #setheading sets the angle or direction
    turt.pendown()
    turt.right(45)
    turt.forward(distance)
    x,y=turt.xcor(),turt.ycor()       #getting the x,y for the next turt
    direction = turt.heading()
    distance+=10
    



wn = t.Screen()
wn.mainloop()