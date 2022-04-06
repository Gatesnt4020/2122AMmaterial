import pandas as pd

def makeFile():
    with open('EVV Weather Obs.txt','r+') as file:
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

#makeFile()

df = pd.read_csv("new EVV Weather Obs.csv",header=0)
un = df['TOBS'].unique()
print(un)