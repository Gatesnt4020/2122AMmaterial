from cmath import nan
from operator import index
import pandas as pd

def txt_to_csv(FILENAME):
    with open(FILENAME,'r+') as file:
        f=file.readlines()
        for i in range(len(f)):
            temp=""
            lastChr=""
            for j in range(len(f[i])):
                if lastChr != " " or f[i][j] != " ":
                    if f[i][j] == " ":
                        if lastChr.isnumeric() or lastChr == "S":
                            temp+=","
                        else:
                            if i!=0:
                                temp+=" "
                            else:
                                temp+=","
                    else:
                        temp+=f[i][j]
                lastChr=f[i][j]
            temp=temp[:-2]
            temp+="\n"
            f[i] = temp
            f[i] = f[i]
            f[i] = f[i].replace('-9999',"")
        file.close()
    with open("new EVV Weather Obs.csv","w+") as file:
        for line in f:
            file.write(line)
        file.close()

def cleanUp(FILENAME,removable):
    df = pd.read_csv(FILENAME,header=0)
    try:
        removable=int(removable)
        temp=removable
        for i in range(removable):
            ui=input("which header would you like to remove ")
            try:
                del df[ui]
            except:
                print("you typed the header wrong try again")
                removable+=1
                break
    except:
        print("please enter a number")
        cleanUp("new EVV Weather Obs.csv",input("how many headers do you want to remove "))
    if temp == removable:
        df.to_csv('out.csv',index=False)
        df['DATE']=df['DATE'].str.replace(".0","")
        

txt_to_csv('EVV Weather Obs.txt')

cleanUp("new EVV Weather Obs.csv",input("how many headers do you want to remove "))