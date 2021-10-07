total=0
sandwich = input("chicken $5.25, beef $6.25, tofu $5.75 ")
print(sandwich,total)
if sandwich == "c":
    total+=5.25
elif sandwich == "b":
    total+=6.25
elif sandwich == "t":     #needs o be an elif because if I spell it wrong, it will charge 5.75
    total+=5.75

print(f"Your sandwich order: {sandwich}")

#iteration 2

drink = input("Would you like a drink (y,n) ")
if drink == "y":
    drink = input("small $1.00, medium $1.75, large $2.25(s,m,l) ")
    if drink == "s":
         total+=1.00
    elif drink == "m":
        total+=1.75
    elif drink == "l":
        #ask if they want a child drink for $0.38
        drink = input("would you like a child drink for $0.38 more (y,n) ")
        if drink == "y":
            total+=(2.25+.38)
        else:
            total+=2.25
else:
    print(f"your order is sandwich:{sandwich}, drink: {drink}, subtotal: {total}")