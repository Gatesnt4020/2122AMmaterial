import turtle as t 

bob = t.Turtle()
#forward,right,left,left,right,left,left,right,left,left,right
bob.penup()
bob.goto(200,0)
bob.pendown()
bob.setheading(90)
bob.forward(100)
for i in range(4):
    bob.right(90)
    bob.forward(100)
    bob.left(90)
    if i !=4:
        bob.forward(100)
        bob.left(90)
        bob.forward(100)


wn = t.Screen()
wn.mainloop()