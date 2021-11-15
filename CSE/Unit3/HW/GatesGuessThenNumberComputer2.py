import random
correctAnswer=False
low, high = 0, 100
guesses=0
numbaguesses=[]
ui=input("enter a number for the computer 0-100,000,000 ")
while(not ui.isdigit()):
        ui=input("enter a number for the computer 0-100,000,000 ")
        #keeps asking for a # if a # wasn't entered
while (not correctAnswer):
    computerGuess=random.randint(0,100)     #computer guesses a number
    numbaguesses.append(computerGuess)
    if computerGuess==ui:
        print("The cpu got it")
        correctAnswer=True                                                            
    elif computerGuess>ui:
        print("cpu to high",computerGuess)
        high=computerGuess-1
    elif computerGuess<ui:
        print("cpu to low",computerGuess)
        low=computerGuess+1
print("it took this many guesses: ",guesses)
print("the numbers the computer guesses ", numbaguesses)