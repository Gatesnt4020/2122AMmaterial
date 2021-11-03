import random
low=0
high=10000**10000
correctAnswer=False
ui=input("enter a number for the computer 0-100,000,000 ")
while(not ui.isdigit()):
        ui=input("enter a number for the computer 0-100,000,000 ")
        #keeps asking for a # if a # wasn't entered
while(not correctAnswer):
    guess=random.randint(low, high)
    if guess==int(ui):
        print("i got it")
        correctAnswer=True
    elif guess<int(ui):
        print("to low")
        low=guess
    elif guess>int(ui):
        print("to high")
        high=guess