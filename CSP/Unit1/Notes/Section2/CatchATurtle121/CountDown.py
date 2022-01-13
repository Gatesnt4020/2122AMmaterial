import turtle as t

timer=5
timesUp=False
counterInverval=1000
fontSetup=("Comic Sans MS",30,"normal")


wn =t.Screen()
counter = t.Turtle()

def countdown():
    global timer,timesUp
    counter.clear()
    if timer <= 0:
        counter.write("Times's up",font=fontSetup)
        timesUp=True
    else:
        counter.write(f"Time: {timer}",font=fontSetup)
        timer-=1
        #recursively run this function again to create a loop
        counter.getscreen().ontimer(countdown,counterInverval)

#wn.onscreenclick()    Run a command when the screen is clicked....
#ontimer(command,interval)
wn.ontimer(countdown,counterInverval)    #clock widget from ______

wn.mainloop()