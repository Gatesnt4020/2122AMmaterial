import random
damage = 4
maxHp = 12
hp = 12
block = 3
evade = 5
exp = 0
levelreq = 50
deaths = 0
monster = 0
mondam = 5
monhp = 7
monb = 1
hardness = 1
ui = ""
get = ""
level = 0
invt = ['clothes', 'potion']


def inventory():
    global invt
    global ui
    if ui == "i":
        print("you opened your inventory")#print the invt list
        for i in invt:
            print(i)
#    tutorial = 0
#    if tutorial == 0:
#     print("welcome to your inventory to select an item use numbers and your list starts at zero")
#      tutorial = tutorial + 1
        ui = input("what would you like to do use or remove (u/r) ")
        while ui != "u" and ui != "r":
            ui = input("what would you like to do use or remove (u/r) ")
        if ui == "u":
            ui = input("what would you like to select ")
            while  not (ui in invt):    ui = input("what would you like to select ")#checks if what the user put is in the invt list and if it is then continues
            print("you have selected " + ui)
        elif ui == "r":
            ui = input("what would you like to remove ")
            while not (ui in invt): ui = input("what would you like to remove ")#checks if what the user put is in the invt list and if it is then continues and removes it
            invt.remove(ui)
            print("you have removed " + ui)

def hpPotion():
    global hp
    global maxHp
    global ui
    recover = maxHp / 2     #sets the amount of how much the user could recover
    if ui == "potion":
        ui = True       #if the user says potion in the invt in the use part sets the ui to True (side note gonna need to fix this for later things (maybe))
        if ui == True:
            if hp + recover >= maxHp:#checks to see if the added health will be over the maxhp and if it is itll set it to the maxhp
                hp = maxHp
            else:#if the added health isnt equal or over the max health then itll just add it to the health
                hp += recover
            ui = False

def gameover():
    global deaths
    global damage
    global hp
    global block
    global evade
    global exp
    global invt
    global monster
    global mondam
    global monhp
    global monb
    global hardness
    global ui
    global level
    deaths = deaths + 1
    ui = input(f'''game over 
would you like to try again (y/n)
''')
    while ui != "y" and ui != "n":
        ui = input(f'''game over 
would you like to try again (y/n)
''')
    if ui == "y":       #resets all the variables to there default when the player wants to play again
        damage = 4
        hp = 12
        block = 3
        evade = 5
        exp = 0
        mondam = 5
        monhp = 7
        monb = 1
        hardness = 1
        ui = ""
        level = 0
        invt.clear()
        invt = ['clothes']
        start()
    elif ui == "n":
        print("thank you for playing come again. total deaths:" + deaths)


def monattack():
    global block
    global mondam
    global hp
    crit = (random.randint(1, 30))#user has a chance to land a crit with a random number
    if crit > 5:#if the user doesnt crit then attack does the base damage
        mondamgive = mondam - block
        hp = hp - mondamgive
    elif crit <= 5:#if the user does crit then atack does more damage 
        mondamgive = mondam * 1.5 - block
        hp = hp - mondamgive
    if hp <= 0:#if the attack makes the players health go to 0 or lower it does the gameover funtion
        gameover()


def dodge():
    global evade
    global mondam
    if evade > mondam:#if the user evadion is higher than the monsters damage they have a chance to do damage to monster and not get hit
        counter()
    elif evade <= mondam:#if the user evadion is equal or lower than the monster damage the will take damage
        print("you have failed your dodge")
        monattack()
        battle()


def counter():#same as the userattak just without the monattack if the monster is still alive
    global damage
    global monb
    global monhp
    crit = (random.randint(1, 30))
    if crit > 5:
        mondamdealt = damage - monb
        monhp = monhp - mondamdealt
    elif crit <= 5:
        mondamdealt = damage * 1.5 - monb
        monhp = monhp - mondamdealt
    if monhp > 0:
        battle()
    elif monhp <= 0:
        monhp = 7
        encounter()


def userattack():#pretty much the same as monattack just the users attack
    global damage
    global monb
    global monhp
    crit = (random.randint(1, 30))
    if crit > 5:
        mondamdealt = damage - monb
        monhp = monhp - mondamdealt
    elif crit <= 5:
        mondamdealt = damage * 1.5 - monb
        monhp = monhp - mondamdealt
    if monhp > 0:
        monattack()
        battle()
    elif monhp <= 0:
        monhp = 7
        encounter()


def flee():#user has a 1/3 chance to fail a run if they do fail they are put in combat
    flee = (random.randint(1, 3))
    if flee == 1:
        print(f'''you have failed to flee
you have engaged in combat''')
        battle()
    elif flee > 1:
        print("you have successfully fled")
        encounter()
def run():#like the flee function but it'll do damage if the user fails it and the user cant spam run
    run = (random.randint(1, 3))
    if run == 1:
        print("you failed to run")
        monattack()
        battle()
    elif run > 1:
        print("you have successfully fled")
        battle()

def battle():
    global invt
    global monster
    global monhp
    global ui
    global hp
    ui = input(f'''{nm}: health {round(hp,2)} 
{monster}: health {round(monhp,2)} 
what would you like to do dodge, attack, inventory, run (d/a/i/r) 
''')        #print the user and mon health so the user knows what there at and the mon at
    while ui != "d" and ui != "r" and ui != "i" and ui != "a" and ui != "s" and ui != "g":
        ui = input(f'''{nm}: health {round(hp,2)} 
{monster}: health {round(monhp,2)} 
what would you like to do dodge, attack, inventory, run (d/a/i/r) 
''')
    if ui == "a":#lets the user attack sends user to the userattack()
        print("you use attack on " + monster)
        userattack()
    elif ui == "r":#lets the user try and run sends user to the run()
        print("you have used run")
        run()
    elif ui == "d":#lets the user try and dodge sends user to the dodge()
        print("you used dodge")
        dodge()
    elif ui == "i":#allows the user to look inside there inventory and equip, remove, or consume items
        inventory()
        battle()

def encounter():
    global monster
    monster = (random.randint(1, 3))# picks a random number and what ever the number is itll send that monster out 
    if monster == 1:
        monster = "spider"
        print("you have encountered a " + monster)
        ui = input("do you want to battle or flee (b/f) ")#allows the user to fight the monster or attempt to flee
        while ui != "f" and ui != "b":
            ui = input("do you want to battle or flee (b/f) ")
        if ui == "b":
            print("you have engaged in combat")
            battle()
        elif ui == "f":
            flee()
    elif monster == 2:
        monster = "slime"
        print("you have encountered a " + monster)
        ui = input("do you want to battle or flee (b/f) ")#allows the user to fight the monster or attempt to flee
        while ui != "f" and ui != "b":
            ui = input("do you want to battle or flee (b/f) ")
        if ui == "b":
            print("you have engaged in combat")
            battle()
        elif ui == "f":
            flee()
    elif monster == 3:
        monster = "troll"
        print("you have encountered a " + monster)
        ui = input("do you want to battle or flee (b/f) ")#allows the user to fight the monster or attempt to flee
        while ui != "f" and ui != "b":
            ui = input("do you want to battle or flee (b/f) ")
        if ui == "b":
            print("you have engaged in combat")
            battle()
        elif ui == "f":
            flee()

def start():
    global deaths
    global nm
    global ui
    if deaths > 0:# if the user has died then it welcomes back the user 
        print(f'''welcome back {nm} to the text base adventure
death count: {deaths}''')
    ui = input("where do you want to go outside, cellar, attic, (o,c,a) ")#ask the user were to go but only option is the cellar since leaving is your end goal
    while ui != "o" and ui != "c" and ui != "a":
        ui = input(
            "where do you want to go outside, cellar, attic, (o,c,a,) ")
    if ui == "o":
        print("as you try and open the door, you cant seem to open it ")
        ui = input("where do you want to go cellar or attic (c/a) ")
        while ui != "c" and ui != "a":
            ui = input("where do you want to go cellar or attic (c/a) ")
        if ui == "c":
            print("you went to the cellar")
            print("as you head down the ladder you hear something faintly from the distance")#lets the user know there about to encounter something
       #lets the player wait for something to occur by delaying the text
            encounter()
        elif ui == "a":
            print(
                f'''as you head toward the stairs to the attic you see that it is pitch black so youll have to wait 
until theres light''')
            ui = input("where do you want to go cellar (c) ")
            while ui != "c":
                ui = input("where do you want to go cellar (c) ")
            if ui == "c":
                print("you went to the cellar")
                print("as you head down the ladder you hear something faintly from the distance")
                encounter()
    elif ui == "c":
        print("you went to the cellar")  
        print("as you head down the ladder you hear something faintly from the distance")
        encounter()
    elif ui == "a":
        print(f'''as you head toward the stairs to the attic you see that it is pitch black so youll have to wait 
until theres light''')
        ui = input("where do you want to go cellar or outside (c/o) ")
        while ui != "c" and ui != "o":
            ui = input("where do you want to go cellar or outside (c/o) ")
        if ui == "c":
            print("you went to the cellar")
            print("as you head down the ladder you hear something faintly from the distance")
            encounter()
        elif ui == "o":
            print(
                "as you try and open the door, you cant seem to open it ")
            ui = input("where do you want to go cellar (c) ")
            while ui != "c":
                ui = input("where do you want to go cellar (c) ")
            if ui == "c":
                print("you went to the cellar")
                print("as you head down the ladder you hear something faintly from the distance")
                encounter()

ui = input("would you to play? (y/n) ")#sees if the user wants to play or not
while ui != "y" and ui != "n":
    ui = input("would you to play? (y/n) ")
if ui == "y":
    nm = input("what is your name? ")
    start()
elif ui == "n":
    print("goodbye")