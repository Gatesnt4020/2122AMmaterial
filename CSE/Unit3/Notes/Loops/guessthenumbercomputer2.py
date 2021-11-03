import random
correctAnswer=False
low, high = 0, 100
while (not correctAnswer):
    computerGuess=random.randint(0,100)     #computer guesses a number
    ui=input(f"the cpu guessed: {computerGuess} - (h,l,c) ")

    if ui=="c":
        print("The cpu got it")
        correctAnswer=True                                                            
    elif ui=="h":
        print("cpu to high",computerGuess)
        high=computerGuess-1
    elif ui=="l":
        print("cpu to low",computerGuess)
        low=computerGuess+1