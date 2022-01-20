from turtle import *
from random import randint
walls = []
openings = []
def createMaze():
    maze = Turtle()
    maze.speed(0)
    maze.pensize(5)
    maze.up()
    maze.goto(350, 350)
    maze.right(90)
    maze.down()
    loops = 0
    wall = 0
    while 700-(loops*25) > 0:
        for i in range(2):
            lineLen = 700-(loops*25)
            while lineLen > 0:
                if (randint(0, 10) == 0 and loops > 1):
                    openings.append([wall, [maze.xcor(), maze.ycor()]])
                    maze.up()
                    maze.forward(25)
                    maze.down()
                elif(randint(0,25) == 0 and loops > 1):
                    walls.append([wall, [maze.xcor(), maze.ycor()]])
                    maze.right(90)
                    maze.forward(25)
                    maze.back(25)
                    maze.left(90)
                    maze.forward(25)
                else:
                    maze.forward(25)
                lineLen-=25
            wall+=1
            maze.right(90)
        loops+=1
    maze.goto(0,0)
    maze.color("red")
    maze.shape("circle")
    maze.stamp()
    maze.hideturtle()
    print(walls)
    print(openings)
def runRunner():
    runner = Turtle()
    runner.up()
    runner.speed(1)
    runner.goto(337.5, 325)
    runner.right(90)
    inner = 0
    type = "vert"
    while runner.ycor() >= -350 and runner.ycor() <= 350:
        wn.bgcolor("white")
        if (type == "vert"):
            if ([inner+4, [runner.xcor()-12.5, runner.ycor()]] in openings):
                wn.bgcolor("green")
                print(f"Opening {inner+4}, {[runner.xcor()-12.5, runner.ycor()]}.")
                if (runner.heading() == 270):
                    runner.right(90)
                    runner.forward(25)
                    runner.left(90)
                else:
                    runner.left(90)
                    runner.forward(25)
                    runner.right(90)
                inner+=4
            if ([inner, [runner.xcor()+12.5, runner.ycor()]] in walls):
                wn.bgcolor("yellow")
                print(f"Wall {inner}, {[runner.xcor()+12.5, runner.ycor()]}.")
                runner.right(180)
            if (runner.ycor() == 350 - round(inner / 4,0) * 25):
                wn.bgcolor("yellow")
                print(f"Wall {runner.ycor()} = {350 - round(inner / 4,0) * 25}.")
                runner.left(180)
                #runner.back(12.5)
                #runner.left(90)
                #runner.forward(12.5)
                #type="hoz"
            if (runner.ycor() == -350 + round(inner / 4,0) * 25):
                wn.bgcolor("yellow")
                print(f"Wall {runner.ycor()} = {-350 + round(inner / 4,0) * 25}.")
                runner.right(180)
        '''
        Broken Code.../Unfinished
                else:
            if ([inner+4, [runner.xcor(), runner.ycor()-12.5]] in openings):
                wn.bgcolor("green")
                print(f"Opening {inner+4}, {[runner.xcor(), runner.ycor()-12.5]}.")
                runner.right(90)
                runner.forward(25)
                runner.left(90)
                inner+=4
            if ([inner, [runner.xcor(), runner.ycor()+12.5]] in walls):
                wn.bgcolor("yellow")
                print(f"Wall {inner}, {[runner.xcor(), runner.ycor()+12.5]}.")
                runner.left(180)
            if (runner.xcor() == 350 - round(inner / 4,0) * 25):
                wn.bgcolor("yellow")
                print(f"Wall {runner.xcor()} = {350 - round(inner / 4,0) * 25}.")
                runner.right(180)
            if (runner.xcor() == -350 + round(inner / 4,0) * 25):
                wn.bgcolor("yellow")
                print(f"Wall {runner.xcor()} = {-350 + round(inner / 4,0) * 25}.")
                runner.right(180)
        '''
        runner.forward(25)
        print(runner.xcor(), runner.ycor())
        print(runner.heading())
    wn.bgcolor("red")
wn = Screen()
createMaze()
runRunner()
wn.mainloop()