'''
#mode = the one that recurrs the most
#min= smallest
#max = highest
#range = the lowest to the highest

range(10)   #generate a list of nmbers from 0 up to the number in the ()
print(range(10))
#range(start,stop,step)
print(range(0,10,2))
print(range(0,100))


#for i many times in range(number of times, I need it to run):
for i in range(0,11,2): #print out even nums from 0-9
    print(i)

#print out odd numbers from 37-83
for i in range(37,84,2):
    print(i)

#for someVariable in aList:
#   do something

for i in [0,1,2,3,4,5,6,7,8,9]:
    print(i)

name=["bob","ryan","will","wyatt","sydni","aidan","paige"]
for i in name:
    #every iteration -> i becomes hat item in the list
    print(i)


number=[7,60,5,24,9,20,12,22,21,10]
for i in range(len(number)):    #creates an index
    number[i]*=2
    print(number[i])            #gets the item in thde list @ the index
print(number)

for i in number:
    i*=2
    print(i)
print(number)

#algorithm that takes in user input
#   ask the user for 10 numbers
#   print out the total of those numbers
total=0
for i in the range(10):
    ui = float(input("give a num"))
    total+=ui
print(total)


for i in range(99999**99999):
    ui = input("Guess what")
    if (ui!="WHAT" and ui!="WAT" and ui!="WUT" and ui!="WATT"):
        print("Chicken butt")
        break
'''

name="jimbob"   #rember: string are sequences... just like lists...
print(name)
for i in name:
    print(i)    #i is each letter
for i in range(len(name)):
    print(name[i])  #i is the index for each letter

name="spongebob sqaurepants"
numberOfVowels=0
for i in name:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :
        numberOfVowels+=1
print(numberOfVowels)

numberOfVowels=0
vowels=["a","e","i","o","u"]
for i in name:
    if i in vowels:
        numberOfVowels
print(numberOfVowels)