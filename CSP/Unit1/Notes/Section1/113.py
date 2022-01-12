import turtle as t 

#object = module.Constructir()
bob = t.Turtle()
bob.shape("turtle")
bob.forward(100)
bob.left(90)
bob.forward(100)
bob.speed(0)
#bob.circle(100,180)
#bob.circle(100,180,3)

#use a while loop to draw a square
count = 8
while count != 0:
    bob.forward(100)
    bob.left(22.5)
    count-=1

window = t.Screen()
window.mainloop()