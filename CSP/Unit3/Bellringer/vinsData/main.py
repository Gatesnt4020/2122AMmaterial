with open("vins.csv","r+") as f:
    vin = f.readlines()
    index=0
    for i in vin:
        index+=1
        if (len(i)-1) !=17:
            print(i,index)
        if "I" in i or "O" in i or "Q" in i:
            print(i,index)