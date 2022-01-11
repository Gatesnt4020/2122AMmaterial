'''
    Sequences:
        Strings - "concatenated date"
        List - "list of data that can be different types"
        Tuple - immutable or they can change
        Array - immtable or they can change
        *Dictionaries

    #i = iterator   (n)
    for i in range(5)
    print("hi")

    i=0     #i = iterator
    while(i<5):
        print("hi")
        i+=1
    '''
import turtle as t

shapes=["arrow","turtle","circle","square","triangle","classic"]
colors=["red","blue","green","orange","pale goldenrod","medium violet red"]
myturds = []

for s in range(len(shapes)):
    #                      keyword parameter shape is a characteristic of your turtle
    bob = t.Turtle(shape=shapes[s])
    bob.fillcolor(colors[s])        #color of the turtle
    myturds.append(bob)

x,y=0,0
for turt in myturds:
    turt.pencolor(colors.pop())        #change the color of the pen
    turt.goto(x,y)
    x+=50
    y+=50


wn = t.Screen()
wn.mainloop()