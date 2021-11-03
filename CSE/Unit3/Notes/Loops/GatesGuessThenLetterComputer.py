import random
low=65
high=90
correctAnswer=False
ui=input("enter a letter for the computer ").upper()
while(not ui.isalpha()):
  ui=input("enter a letter for the computer ").upper()
while(not correctAnswer):
  guess=chr(random.randint(65,90))
  if ord(guess)==ord(ui):
    print("i got it")
    correctAnswer=True
  elif ord(guess)<ord(ui):
    print("to low")
    low=guess
  elif ord(guess)>ord(ui):
    print("to high")
    high=guess