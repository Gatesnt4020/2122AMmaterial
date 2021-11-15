filename="TestData.cvs"
classes=["Advanced","Engineer","Collision","Automotive Service","Construction","CISCO","Software","Culinary","Diesel","Electrical","Graphic","Health","HVAC","Precision","Public","Radio","Vet","Welding"]
#Advanced,Engineer,Collision,AutomotiveService,Construction,CISCO,Software,Culinary,Diesel,Electrical,Graphic,Health,HVAC,Precision,Public,Radio,Vet,Welding=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]#with open(fileYouAreOpening,mode) as variable
listOfList=[]

for i in classes:
    listOfList.append([])

with open(filename,"r") as file:
    #readlines returns a list
    listOflines= file.readlines()

#Shreds the data to its appropiate list

for row in listOflines:
    for i in range(len(classes)):
        if classes[i] in row:
            listOfList[i].append(row)



#write to the text files
for i in range(len(classes)):
    with open(f"{classes[i]}.csv","w") as fileToWrite:
        for row in listOfList[i]:
            fileToWrite.write(row)