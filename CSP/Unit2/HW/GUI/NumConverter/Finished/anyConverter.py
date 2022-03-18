class Convert:

    def converter(ui,base,change):
        try:
            letters="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            highExp = len(ui)-1
            decimal=0
            for i in ui:
                numba= letters.index(i)
                decimal+=(numba*int(base)**highExp)
                highExp-=1
            digitList=[]
            exp=0
            while decimal>=int(change)**exp:      #to change base 2 into a different one change the 2 into another number
                digitList.insert(0,int(change)**exp)  #insert instead of add to the end
                exp+=1
        
            #2nd we iterated through the digitList to find how many of each bit is in our number
            for i in range(len(digitList)):
                temp=digitList[i]
                digitList[i]=decimal//digitList[i]
                decimal-=(digitList[i]*temp)
                digitList[i]=letters[digitList[i]]
        
            #3rd convert out 10-15 to A-F
            #4th concate the digitList together
            out=""
            for b in digitList:
                out+=b

            return out
        except:
            return("ERROR")
        
        
'''ui = input("number please ")
base = int(input("base please "))
change = int(input("change please "))
Convert(ui,base,change).converter()'''
