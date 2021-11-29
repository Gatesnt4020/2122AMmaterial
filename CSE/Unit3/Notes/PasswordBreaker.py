import datetime #do anything with timing, check out this module
def bruteForcer():
    passwordToCheck = 123456
    beginTime = datetime.datetime.now()
    #generate the password
    cpuGuess = 0
    haveNotGuessedThePassword = True
    while(haveNotGuessedThePassword):
        #print(cpuGuess) if we print, it will take longer
    #check to see if it is equal
        if cpuGuess == passwordToCheck:
            print(f"Got it!  {cpuGuess}")
            haveNotGuessedThePassword = False
        else:
            cpuGuess
    endTime = datetime.datetime.now()
    print(endTime-beginTime)
    #if not generate new`
