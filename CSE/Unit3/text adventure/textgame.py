from playsound import playsound
import winsound, random, time
'''
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process
>>
py -3 -m venv .venv
>> .venv\scripts\activate
'''

def music():
    playsound(r'C:\\Users\axill\OneDrive\Documents\CSE\Music\MainTheme.wav')
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\Overworld.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\Dungeon.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\Ganon'sLair.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\ConfrontingGanon.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\ZeldaRescued.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\Ending.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\HyruleisRestored.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\ImportantItem.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\SmallItem.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\TriforceofWisdom.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\TriforceofPower.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\Discovery.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\SneakyTrap.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\ItemAppears.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\SecretNearby.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\Whistle.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\Defeated.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\TimedEvent.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\PowerUp!.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\PowerDown.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\SuperPower!.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\ObjectivesMenuOpen.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\ObjectivesMenuClose.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\TimerCount.wav")
    playsound(r"C:\\Users\axill\OneDrive\Documents\CSE\Music\GanonLaughs.wav")

#start date 10/6/21
#use ui as a global ONLY for thing that are used alot outside of combat etc... like inventory/stats/look around etc...

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
collectables=['loovar','neptoona','rusty swordfish','skippyjack','stowfish','toona','ancient fish','colossal catish','cuccofish','ferocious pirarucu','fragrant reekfish','lord chapu-chapu','mooranha',
'postal salmon','termina bass','termina loach','skullfish']
equipable = ['sword','clothes','torch','excalibur','bow','boomerang','magical boomerang','bomb','magical rod','book of magic','white sword',
'magical sword','wooden shield','magical shield','blue ring','red ring',]
ammo=['arrow','silver arrow']
consum = ['potion','food']
totalItems = ['clothes', 'potion', 'sword', 'key', 'torch','excaibur','bow','boomerang','magical boomerang','bomb','arrow','silver arrow','food','magical rod','fishing pole','book of magic','white sword',
'magical sword','wooden shield','magical shield','blue ring','red ring','magical key','drachma','clock',]


def grab():
    global invt
    global ui
    if 12 >= len(invt):
        if ui == "g":
            ui = input("what do you want to grab ")
            while not(ui in totalItems) : ui = input("try again with something grabable ")
            invt.append(ui)
            #will take what the player inputs then appends it to the invt list
            print("you have grabbed " + ui)
    elif 12<len(invt):
        print("your inventory is to full please remove something ")

def equip():
    print()


def stats():  #add level to the stats under exp
    global damage
    global hp
    global block
    global evade
    global exp
    global deaths
    global ui
    global level
    global levelreq
    nextLevel= levelreq-exp
    if ui == "s":#grabs all the variables related to the user and prints them out 
        print(f'''damage: {round(damage,2)} 
hp: {round(hp,2)} 
block: {round(block,2)} 
evade: {round(evade,2)}
exp: {round(exp,2)}
next level: {round(nextLevel,2)}
level: {level} 
deaths: {deaths}''')


def progress():  
    global damage
    global hp
    global block
    global evade
    global exp
    global mondam
    global monhp
    global monb
    global maxHp
    #  global hardness maybe do something with this for mobs level up
    global level
    global levelreq
    if exp >= levelreq:
        level += 1#when the exp is greater or equal to the required exp then it adds a level
        if level > 10:#if the user level is greater than 10 it multiples the user and mon stats by 1.6
            damage *= 1.6
            hp *= 1.6
            maxHp *= 1.6
            block *= 1.6
            evade *= 1.6
            mondam *= 1.5
            monhp *= 1.5
            monb *= 1.5
            levelreq *= 1.5
        elif level > 0:#if the user level is lower than 10 it multiples the user and mon stats by 1.6
            damage *= 1.5
            hp *= 1.5
            maxHp *= 1.6
            block *= 1.5
            evade *= 1.5
            mondam *= 1.25
            monhp *= 1.25
            monb *= 1.25
            levelreq*= 1.25

#so for level to add one make it were it multiples exp by 1.5 then make it add when the exp is equal to the number it was multiplied
#for level make a base of 50 and when exp hits that it adds one to the level then multiples the base number by 1.5


#tutorial on how invt works, ask what they want to do, something else maybe
#maybe you can like say look at 'said item' and itll  say a description
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
            if ui in equipable:
                equip()
            if ui in consum:        #consumables like potion and food can be used once before there removed
                hpPotion()
                invt.remove(ui)
        elif ui == "r":
            ui = input("what would you like to remove ")
            while not (ui in invt): ui = input("what would you like to remove ")#checks if what the user put is in the invt list and if it is then continues and removes it
            invt.remove(ui)
            print("you have removed " + ui)


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
        success()
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
        success()
        encounter()


def success():#after the player win a fight theyre sent to get exp
    global monster
    global exp
    global nm
    global hardness
    if hardness == 1:#if the difficult/hardness is at one they get a random # of exp and exp increases as hardness goes up 
        exp += (random.randint(10, 30))
    elif hardness == 2:
        exp += (random.randint(10, 30))
    elif hardness == 3:
        exp += (random.randint(30, 50))
    print(f'''you successfully killed {monster} 
{nm} exp: {exp}''')
    progress()


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
    elif ui == "s":#prints the user stats to them 
        stats()
        battle()
    elif ui == "g":#allows for the user to grab probably wont be in this function in later time
        grab()
        battle()


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
    #print("type help for instructions if confused")
    winsound.PlaySound(r'C:\\Users\axill\OneDrive\Documents\CSE\Music\MainTheme.wav', winsound.SND_ALIAS )
    ui = input("type s to continue ")       #makes the user learn that "s" is to show your stats when the user wants to see there stats later on in the game
    while ui != "s":
        ui = input("type s to continue ")
    if ui == "s":
        stats()
        print("these are your stats. enter s when you want to look at your stats again")
    ui = input("type l to continue (not 1/one its a L) ")       #makes the user learn that "l" is to show your surrounding so the user can look around later in the game
    while ui != "l":
        ui = input("type l to continue (not 1/one its a L) ")
    if ui == "l":
        print(
            f'''as you awake you see a door that looks worn down, an open cellar door that has a ladder connected to
it, and a set of stair that lead to an attic. press l when you want to look around again''')
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
            time.sleep(3)       #lets the player wait for something to occur by delaying the text
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
                time.sleep(3)
                encounter()
    elif ui == "c":
        print("you went to the cellar")  
        print("as you head down the ladder you hear something faintly from the distance")
        time.sleep(3)
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
            time.sleep(3)
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
                time.sleep(3)
                encounter()

ui = input("would you to play? (y/n) ")#sees if the user wants to play or not
while ui != "y" and ui != "n":
    ui = input("would you to play? (y/n) ")
if ui == "y":
    nm = input("what is your name? ")
    start()
elif ui == "n":
    print("goodbye")

'''
#https://www.geeksforgeeks.org/python-list/cc
https://docs.python.org/3/library/time.html#time.sleep
https://docs.python.org/3/library/os.html
https://www.geeksforgeeks.org/implementing-web-scraping-python-beautiful-soup/
https://www.geeksforgeeks.org/play-sound-in-python/
https://docs.python.org/3/library/winsound.html
https://downloads.khinsider.com/game-soundtracks/album/the-legend-of-zelda-nes
https://docs.python.org/3/library/shutil.html
https://zelda.fandom.com/wiki/Items_in_The_Legend_of_Zelda.
https://zelda.fandom.com/wiki/Fish
'''