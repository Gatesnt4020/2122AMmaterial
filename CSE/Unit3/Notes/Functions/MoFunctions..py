import random

#void function - no return
#pass in information
def giveMeSomeNumbers(amountOfNumbers,smallest,biggest):
    listy=[]
    # create a list of random numbers 
    for i in range(amountOfNumbers):
        listy.append(random.randint(smallest,biggest))
        print(listy)
        return listy

randomListOfNumbres=giveMeSomeNumbers(10,82,495)
#randomListOfNumbres=giveMeSomeNumbers(10)

print(min(randomListOfNumbres))
print(max(randomListOfNumbres))
print(sum(randomListOfNumbres))

#define the function ave that takes in a list of numbers and returns the average
def ave(listy):
    return sum(randomListOfNumbres)/len(randomListOfNumbres)
print(ave(randomListOfNumbres))

def range(listy):
    return sum(listy)-min(listy)
print(ave(randomListOfNumbres))
#print(range(ranodmListOfNumbers))

#range-> max value to the min calue (max-min)
def range(listy):
    return max(listy)-min(listy)

print(range(randomListOfNumbres))

#print -> / ont 1 or itself

#range-> max value to the min value (max-min)
#A BIG NO NO NO -> do NOT reuse or call your functioins the same name
#   as
#if i tis divisible by itself or 1
def isPrime(numberToCheck):
    #check if numberToCheck is divisible by the users btwn itself and1
    for i in range(2,numberToCheck):
        #check to see if numberToCheck is divisbles by i
        if(numberToCheck%i==0):
            return False

    #if all of the calcualtions are not prime 
    return True

for i in randomListOfNumbres:
    if isPrime(i):
        print(True,i,randomListOfNumbres)


# 
# print(isPrime(5))
# print(isPrime(20))
# print(isPrime(2))
# print(isPrime(1))
# 
#[7,6,1,4,8,2,5]
#6/5-dec
#6/4->dec
#6/3->whole
#6/2->whole
#4/3->dec
#4/2->whole
#5/4->dec
#d/3->dec
#5/2->dec
#remainder %
