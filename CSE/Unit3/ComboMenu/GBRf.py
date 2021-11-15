def menuOptions(question,sizes,prices):
     total=0
     option = input(question)
     if option == "y":
          chooseOption=True
          option = input(f"Which size? {sizes} ")
          if option == sizes[0]:
               total+=prices[0]
          elif option == sizes[1]:
               total+=prices[1]
          elif option == sizes[2]:
               total+=prices[2]
          elif option ==sizes[3]:
               total+=prices[3]
     print(option,total)      
         
q="wouldyoulike a drink? (y,n) "
s=["s","m","l","c"]
p=[1,1.75,2.25,2.25+.38]
menuOptions(q,s,p)

q="wouldyoulike a fries? (y,n) "
s=["s","m","l","m"]
p=[1,1.75,2.00,2.00]
menuOptions(q,s,p)