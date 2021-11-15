'''
orderInformation=[]
Menu=["Krabby Patty","Doubles Krabby Patty","Triple Krabby Patty","Coral Bits","Kelp Rings","Krabby Meal","Doubles Krabby Meal","Triple Krabby Meal",
"Salty Sea Dog","FootLong","Sailors Surprise","Golden Loaf","Kelp Shake","Seafoam Soda"]
class Menu:
     def __init__(self, question, options):
          self.question = q
          self.options = o


Order1=Menu("would you like to look at the menu? (y/n) ","what would you like ")
'''
'''
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
'''
'''
q="would you like a drink? (y,n) "
o=["s","m","l","c"]
p=[1,1.75,2.25,2.25+.38]
menuOptions(q,o,p)

q="would you like a fries? (y,n) "
o=["s","m","l","m"]
p=[1,1.75,2.00,2.00]
menuOptions(q,o,p)
'''

'''
https://www.geeksforgeeks.org/python-classes-and-objects/
'''