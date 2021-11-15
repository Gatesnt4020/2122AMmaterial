import random
secretNumber=int(input("guess a number btwn 0-100 ")) #user sets a guess
correctAnswer=False
guesses=0
numbaguesses=[]
while (not correctAnswer):
    computerGuess=random.randint(0,100)     #computer guesses a number
    numbaguesses.append(computerGuess)
    if secretNumber==computerGuess:
        print("The cpu got it")
        correctAnswer=True                                                            
    elif secretNumber<computerGuess:
        print("cpu to high",computerGuess)
    elif secretNumber>computerGuess:
        print("cpu to low",computerGuess)
    else:
        print("sorry,cpu was wrong",computerGuess)
    guesses+=1
print("it took this many guesses: ",guesses)
print("the numbers the computer guesses ", numbaguesses)