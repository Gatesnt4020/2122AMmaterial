#iteration 1
total=0
orderInformation = []
chooseSandwich,chooseFries,chooseDrink = False,False,False

sandwich = input("Would you like a sandwich (y/n) ")
if sandwich == "y":
  sandwich = input("Which sandwich would you like:  chicken $5.25, beef $6.25, tofu $5.75 ")
  if sandwich=="c" or sandwich=="b" or sandwich=="t":
      orderInformation.append("sandwich: "+sandwich)
      chooseSandwich=True
  if sandwich == "c":
      total+=5.25
  elif sandwich == "b":
      total+=6.25
  elif sandwich == "t":    #needs to be an elif because if I spell it wrong, it will charge 5.75
      total+=5.75
'''
sandwich = input("Which sandwich would you like:  chicken $5.25, beef $6.25, tofu $5.75 ")
if sandwich=="c" or sandwich=="b" or sandwich=="t":
     orderInformation+=(f"\tSandwich:\t{sandwich}\n")
     chooseSandwich=True
if sandwich == "c":
     total+=5.25
elif sandwich == "b":
     total+=6.25
elif sandwich == "t":    #needs to be an elif because if I spell it wrong, it will charge 5.75
     total+=5.75
'''

#iteration 2
global drink
drink = input("Would you like a drink? (y,n) ")
if drink == "y":
  chooseDrink=True
  drink = input("Which size? s,m,l ")
  if drink == "s":
      total+=1
  elif drink == "m":
      total+=1.75
  elif drink == "l":
      #ask if they want a child size for $0.38 more
      drink = input("Would you like a child size for $.38 more? (y,n) ")
      if drink=="y":
            total+=(2.25+.38)
            drink = "c"
      else:
            total+=2.25
  orderInformation.append("drink: " +drink)


#iteration 3
global fries
fries = input("Would you like fries with that? (y,n) ")
if fries == "y":
     chooseFries=True
     fries = input("Which size? s,m,l ")
     if fries == "s":
          fries = input("Would you like to Mega-Size? (y,n) ")
          if fries=="y":
               fries="l"
               total+=2.00
          else:
               fries="s"
               total+=1.00
     elif fries == "m":
          total+=1.75
     elif fries == "l":
          total+=2.00
     orderInformation.append("fries: "+fries)

#iteration 4
ketchup = int(input("How many ketchup packets do you want? ($.25 ea) "))
orderInformation.append("ketchup: "+str(ketchup))
total+= (ketchup*.25)

if chooseDrink and chooseFries and chooseSandwich:
     total-=1

finaltotal = (total*1.07)
orderInformation.append(f"Subtotal: ${round(total,2)}")
orderInformation.append(f"final total: ${round(finaltotal,2)}")
for i in orderInformation:
  print(i)


"""
print(f'''
Your order:
     Sandwich:  {sandwich}
     Drink:     {drink}
     Fries:     {fries}
     Ketchup:   {ketchup}
     Subtotal: ${total}

''')
"""