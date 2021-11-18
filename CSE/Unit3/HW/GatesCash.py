#implement a program that calculates the change required to gice a user. 
#Use the least amount of coins possible
#divide the number first and get the whole value and then the do the modulo
#use // instead of math.floor()
q,d,n,p=0,0,0,0
change=[q,d,n,p]
def isFloat(ui):
    try:
        float(ui)
        return True
    except ValueError:
        return False

def printChange():
    if q == 1:
        print(f'''Quater: {q}''')
    elif q == 0:
        print()
    elif q>1:
        print(f'''Quaters: {q}''')
    if d == 1:
        print(f'''Dime: {d}''')
    elif d == 0:
        print()
    elif d>1:
        print(f'''Dimes: {d}''')
    if n == 1:
        print(f'''Nickel: {n}''')
    elif n == 0:
        print()
    elif n>1:
        print(f'''Nickels: {n}''')
    if p == 1:
        print(f'''Penny: {p}''')
    elif p == 0:
        print()
    elif p>1:
        print(f'''Pennies: {p}''')
    

def done(ui):
    #print(ui)
    #print(q,d,n,p)
    printChange()

ui = input("Change owed: ")
while isFloat(ui) is False: 
    ui = input("Change owed: ")
ui=float(ui)
if ui >= .25:
    q=ui//.25 
    ui=ui%.25
    #print(ui)
if ui >= .10:
    d=ui//.10
    ui=ui%.10
    #print(ui)
if ui >= .05:
    n=ui//.05
    ui=ui%.05
    if ui >= .009:
        ui+=.001
    #print(ui)
if ui >= .01:
    p=ui//.01
    ui=ui%.01
    #print(ui)
    if ui >= .009:
        p+=1
        ui=0
    #print(p)
    #print(ui)
done(ui)

'''
    sources:
     https://docs.python.org/3/library/math.html
     https://stackoverflow.com/questions/736043/checking-if-a-string-can-be-converted-to-float-in-python
    '''