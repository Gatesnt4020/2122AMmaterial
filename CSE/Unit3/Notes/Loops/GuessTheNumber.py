import random
#Build out a program that asks the user to guess a number.
#   (Just like out app....)
#after 3 chances, the program stops
#while the ui has not given us a number:
#random.choice(something)
secretNumber=random.randint(0,100)
strike=0
correctAnswer=False
while (strike != 3 and not correctAnswer):
    ui=input("Guess a number btw 0-100 ")
    while(not ui.isdigit()):
        #   keep asking for a number
            ui=input("Guess a number btw 0-100 ")

    if secretNumber==int(ui):
        print("congrats")
        correctAnswer=True                                                            
    elif secretNumber<int(ui):
        print("your to high")
    elif secretNumber>int(ui):
        print("your to low")
    strike+=1