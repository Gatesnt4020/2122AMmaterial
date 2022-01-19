#-----import statements-----
import turtle as t
import random as r
import leaderboard as lb
#-----Leaderboard-----------
FILENAME = "leaderboard.txt"
#read, write, or append
#write - will overwrite material
#append - add the data to the bottom of the file
with open(FILENAME,"r") as f:
     file = f.readlines()     #file is a list of the data
     f.close()
     
#-----game configuration----
name = input("Please enter your name ")
wn = t.Screen()
SCREENW,SCREENH = 300,300
score=0
#tuple variable = ("fontstyle",fontsize,"font (B,I,U)")
fontSetup=("Comic Sans MS", 30, "normal")
timer=3
timesUp=False
counterInverval = 1000
#-----initialize turtle-----
mo = t.Turtle()
mo.shape("turtle")
mo.shapesize(2)
mo.fillcolor("brown")
mo.speed(0)
scorekeeper = t.Turtle()
scorekeeper.hideturtle()
scorekeeper.penup()
scorekeeper.goto(100,200)
scorekeeper.pendown()
scorekeeper.speed(0)
counter = t.Turtle()
counter.hideturtle()
counter.penup()
counter.goto(100,165)
counter.speed(0)
#-----game functions--------
def updateHS():
     global FILENAME
     with open(FILENAME,"a") as f:
          f.write("AAA,10")
          f.close()
def countdown():
     global timer, timesUp
     counter.clear()
     if timer<=0:
          counter.write("Time's up",font=fontSetup)
          timesUp=True
          #updateHS()
          manageLeaderboard()
     else:
          counter.write(f"Time: {timer}",font=fontSetup)
          timer-=1
          #recursively run this function again to create a loop
          counter.getscreen().ontimer(countdown,counterInverval)
def updateScore():
     global score
     #it will see the var score in other parts of the program
     score+=1
     scorekeeper.clear()      #clear what it already wrote
     #write the score
     scorekeeper.write(f"Score: {score}",font=fontSetup) 
def changePosition():
     #move the turtle to a random location on the screen
     newX = r.randint(-SCREENW/2,SCREENW/2)
     newY = r.randint(-SCREENH/2,SCREENH/2)
     mo.color("white")
     mo.pencolor("red")
     mo.stamp()
     mo.pencolor("black")
     mo.color("blue")
     mo.penup()         #doesn't leave a trail
     mo.hideturtle()    #don't see where it is going
     mo.goto(newX,newY)
     mo.showturtle()
     mo.pendown()
#read in the top 5 scores and draw it on the screen
def manageLeaderboard():
     global score
     global scorekeeper
     global mo
     global name
     
     mo.goto(1000,1000)
     
     #parallel list ->same length and corresponding data based on the index
     namesList = lb.get_names(FILENAME)   #accessor method to get the names
     scoresList = lb.get_scores(FILENAME)
     
     print("namesList",namesList)
     print("scoresList",scoresList)
     
     #show the lb w/ or w/o the current player
     if(len(scoresList)<5 or score >= int(scoresList[4])):
          lb.update_leaderboard(FILENAME, namesList, scoresList, name, score)
          lb.draw_leaderboard(True, namesList, scoresList, scorekeeper, score)
     else:
          lb.draw_leaderboard(False, namesList, scoresList, scorekeeper, score)
     
#no matter what, if it is a mouse click
#    pass in x and y
def moClicked(x,y): 
     #x and y are the cuursor's coordinates
     print(x,y)
     print("mo was clicked")
     changePosition()
     updateScore()
#-----events----------------
#obj.method(command or function name)
mo.onclick(moClicked)
wn.ontimer(countdown,counterInverval)
wn.mainloop()