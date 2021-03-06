import random,string

upperCase = string.ascii_uppercase
lowerCase = string.ascii_lowercase
numbers = string.digits
symbols = string.punctuation

def generate(numberUpper, numberLower, num, sym):
    password = ""
    for i in range(numberUpper):
        password+=upperCase[random.randint(0, len(upperCase)-1)]
    for i in range(numberLower):
        password+=lowerCase[random.randint(0, len(lowerCase)-1)]
    for i in range(num):
        password+=numbers[random.randint(0, len(numbers)-1)]
    for i in range(sym):
        password+=symbols[random.randint(0, len(symbols)-1)]
    password = list(password)
    random.shuffle(password)
    return "".join(password)

ui = input("Do you want to generate a password: ")
print("Enter quit to stop the program")
while ui != "quit":
    numberUpper = int(input("How many upper:"))
    numberLower = int(input("How many lower: "))
    num = int(input("How many numbers: "))
    sym = int(input("How many symbols: "))
    print(generate(numberUpper, numberLower, num, sym))
    ui = input("Do you want to generate a password: ")