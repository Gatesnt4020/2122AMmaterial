print("String Manipulation")
'''
    Data Types:
        Int, Float, Strings, List, Booleans
        Primitive: Int, Booleans, Float, Character
        Non-Primitive: Strings, List
'''
'''
#String Math
name="bobby"
age=17
print("Hello" + "bobby") #string addtion / conacatenation 
print("Hello" + name) #string addtion
print("Your age is " + str(age))     #concatenation

#convert a sting to an int
print(int("17"))

#convert an int or anything to a string 
print(str(age))

name=input("your name ")    #string addtion
age=input("grade level")    #string addtion
printJ("Wow, "+name+" you're in the "+str(grade)+",grade")

pet=input("what is your pets name? ")
age=input("How old is your pet? ")
size=input("How ig is your pet? ")
smell=input("Does your pet smell good? ")

#print("Your pet, "+pet+", sounds like a cool pet. I can't believe they are that "+age+"and "+size)
#print("I like "+smell+" smelling pets")

'''

"""
output=(f''' Your pet, {pet} , sounds like a cool pet.
 I can't believe they are that {age}  and {size}
I like {smell} smelling pets ''')
print(output)
"""
"""
'''
#convert your name to binary
print(bin(72))
#built in function: print, input, str, int, bin
#convert a character to an int
print(ord("B"))     #returns an int
print(bin(ord("B")))    #convert your name to binary
print(bin(ord("a")))
print(bin(ord("n")))
print(bin(ord("d")))
print(bin(ord("e")))
print(bin(ord("r")))

print(bin(-16))
print(bin(-16))
print(bin(0))
'''

'''
gasp=input("How much gas cost")
gasu=input("How many gallons did you purcahsed")
gasf=input("Total cost to fill up")
#convert string to a float
gasf=float(gasp)+int(gasu)
print(gasf)
'''
print("poop"+"poop") #add strings
print("poop"*20) #multiply strings
#print("pooppooppoop"/3) #divide strings doesn't work
#print("poopie"-"ie") #subtract string doesn't work
"""

first=input("what is your name? ")
last=input("What is our last name?")
first.first()
prefix=input("What is your title (Mr, Mrs, Dr, Sir").title()


#Hello, Mr. Bander
print(f"Hello, {prefix}. {fisrt} {last.title()}")
#swapcase
print("BillyBob".swapcase())

#name.title()=Bander
#name.upper()=BANDER
#name.lower()=bander