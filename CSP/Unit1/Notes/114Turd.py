import turtle as t

donny = t.Turtle()
donny.shape("circle")

#draw 1 row of red dots
x= -250
while(x<250):
    y=200
    while (y > 0 ):
        if (x==-250):
            donny.color("purple")
        donny.goto(x,y)
        donny. stamp()
        donny.color("orange")
        y-=20
    x+=50
    


wn = t.Screen()
wn.mainloop()
