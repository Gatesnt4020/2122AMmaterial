'''
    Procedures - Purple Blocks
    Functions - Block of code that completes an algoritm
    Methods - Methods are used with objects and Classes

    Two main types of functions:
    void (to do) - it doesn't return anything
    return (the results) - it gives the computer data back

'''

#define a function called howdy
def howdy():
    #print out howdy
    print("howdy")

#call the print function
print("the message to print")
#call the howdy function
#howdy()

#define a function that adds 2 numbers together
def adding():
    a=int(input("give me a number "))
    b=int(input("give me a number "))
    print(a+b)

#adding()

# define a function ymxb
#def ymxb():
#    #solve for y in the y=mx+b formula
#    m = int(input("enter the m "))
#    x = int(input("enter the x "))
#    b = int(input("enter the b "))
#    y = (m*x)+b
#    print(y)

#pass in variables
def ymxb(m,x,b):
    #solve for y in the y=mx+b formula
    print(m*x+b)

#return somthing
def returnYMBX(m,x,b):
    return (m*x+b)

print("x | y")
print("-----")
for i in range(101):
    #place in the 3 arguments
    #print(returnYMBX(3,i,-2)) #i is the x value for this equation
    print(f"{i} | {returnYMBX(3,i,-2)}")
