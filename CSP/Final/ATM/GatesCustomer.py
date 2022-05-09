import pandas as pd
class Customer:
    
    def __init__(self,cardnum,pin):
        self.cardnum = cardnum
        self.pin = pin

    def chcekCredit(cardnum):
        #checks if its a blank string
        if cardnum != "":
            df = pd.read_csv('GatesDB.txt',header=0)
            #checks if the card exist if so returns the true and the index of the card
            for i in range(len(df["CreditCard"])):
                if df["CreditCard"][i] == int(cardnum):
                    return True,i
        return False,False
    
    def checkPin(index,pin):
        #checks if its a blank string
        if pin != "":
            #checks if the input matches the card's pin
            df = pd.read_csv('GatesDB.txt',header=0)
            if df["Pin"][index] == int(pin):
                return True
        return False

    def findAccount(account):
        #tells whether the user wants to use there saving or checking account else they enter another number
        if account == "1" or account == "2":
            return True,account
        else:
            return False,False

    def checkingAmount(amount,total):
        #if the amount is over 500 throws an error
        if int(amount) > 500:
            return "Over $500"
        #if the amount isnt an increment of 5 throws an error
        if (int(amount)%5) != 0:
            return "Not an increments of 5"
        #if the amount +/- from the current balance in that account is over $10 then true else false
        if total >=10:
            return True
        else:
            return "Overdraft issue"

    def deposit(index,amount,account):
        #checks if the string is blank
        if amount != "":
            df = pd.read_csv('GatesDB.txt',header=0)
            #checks whether the user wanted savings or checkings
            if account == "1":
                #grabs the amount of the spot wanted
                depot = df["Savings"][index]
                #https://www.geeksforgeeks.org/how-to-fix-numpy-float64-object-cannot-be-interpreted-as-an-integer/ making the current amount not a npfloat64
                depot = depot.astype(int)
                #finds the total of what should be in that spot
                total=depot + int(amount)
                #if it passes the function sets the total as the new balance if not returns the error
                if type(Customer.checkingAmount(amount,total)) != str:
                    df.loc[index,"Savings"] = total
                    df.to_csv('GatesDB.txt',index=False)
                    return True
                else:
                    return Customer.checkingAmount(amount,total)
            else:
                #same as top
                depot = df["Checkings"][index]
                #https://www.geeksforgeeks.org/how-to-fix-numpy-float64-object-cannot-be-interpreted-as-an-integer/ making the current amount not a npfloat64
                depot = depot.astype(int)
                total=depot + int(amount)
                if type(Customer.checkingAmount(amount,total)) != str:
                    df.loc[index,"Checkings"] = total
                    df.to_csv('GatesDB.txt',index=False)
                    return True
                else:
                    return Customer.checkingAmount(amount,total)

    def withdraw(index,amount,account):
        #checks if the string is blank
        if amount != "":
            df = pd.read_csv('GatesDB.txt',header=0)
            #checks whether the user wanted savings or checkings
            if account == "1":
                #grabs the amount of the spot wanted
                depot = df["Savings"][index]
                #https://www.geeksforgeeks.org/how-to-fix-numpy-float64-object-cannot-be-interpreted-as-an-integer/ making the current amount not a npfloat64
                depot = depot.astype(int)
                total=depot - int(amount)
                #if it passes the function sets the total as the new balance if not returns the error
                if type(Customer.checkingAmount(amount,total)) != str:
                    df.loc[index,"Savings"] = total
                    df.to_csv('GatesDB.txt',index=False)
                    return True
                else:
                    return Customer.checkingAmount(amount,total)
            else:
                #same as top
                depot = df["Checkings"][index]
                #https://www.geeksforgeeks.org/how-to-fix-numpy-float64-object-cannot-be-interpreted-as-an-integer/ making the current amount not a npfloat64
                depot = depot.astype(int)
                total=depot - int(amount)
                if type(Customer.checkingAmount(amount,total)) != str:
                    df.loc[index,"Checkings"] = total
                    df.to_csv('GatesDB.txt',index=False)
                    return True
                else:
                    return Customer.checkingAmount(amount,total)

    def balance(index):
        #returns what the current balance is to the user
        df = pd.read_csv('GatesDB.txt',header=0)
        return df["Savings"][index], df["Checkings"][index]

    def transfer(index,amount,account,person):
        #uses two prior made functions to transfer money
        Customer.withdraw(index,amount,account)
        Customer.deposit(person,amount,"1")

    def pin(index,pin):
        #checks if string is blank if not then replaces the old pin with the new one
        if pin != "":
            df = pd.read_csv('GatesDB.txt',header=0)
            df.loc[index,"Pin"] = pin
            df.to_csv('GatesDB.txt',index=False)