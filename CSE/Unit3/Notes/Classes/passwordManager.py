import random
nono=[chr(34),chr(39),chr(45),chr(47),chr(60),chr(62),chr(92)]
ui=input("hm ")

def passwordGen():
    global ui
    if ui == "Generate Password":
        ui = input("How long do you want your password? ")
        while(not ui.isdigit()): ui=input("How long do you want your password ")
        length=0
        while length != int(ui):
            genPass=chr(random.randint(33,122))
            while  not (genPass in nono):
                print(genPass)
        length+=1

passwordGen()

open

'''
Outside Sources:

'''