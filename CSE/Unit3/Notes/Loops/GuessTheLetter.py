#just like guess the number, have the user, guess the letter
#gice them 3 strikes and they're out
#DO NOT create a sequence with all of the alphabet....
import random
letter=chr(random.randint(65,90))
strikes=0
correctAnswer=False
while(strikes !=3 and not correctAnswer):
    ui=input("Guess the letter ").upper()
    while(not ui.isalpha()):
        ui=input("Guess the letter ").upper()
    if ord(letter)==ord(ui):
        print("congrats")
        correctAnswer=True
    elif ord(letter)>ord(ui):
        print("your to low")
    elif ord(letter)<ord(ui):
        print("your to high")
    strikes+=1