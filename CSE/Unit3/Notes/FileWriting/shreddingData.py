filename="TestData.cvs"
classes=["Advanced","Engineer","Collision","Automotive Service","Construction","CISCO","Software","Culinary","Diesel","Electrical","Graphic","Health","HVAC","Precision","Public","Radio","Vet","Welding"]
Advanced,Engineer,Collision,AutomotiveService,Construction,CISCO,Software,Culinary,Diesel,Electrical,Graphic,Health,HVAC,Precision,Public,Radio,Vet,Welding=[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]#with open(fileYouAreOpening,mode) as variable
with open(filename,"r") as file:
    #readlines returns a list
    listOflines= file.readlines()

for row in listOflines:
    #rstrip() removes the \n on the end of the row
    #split() splits the row based on a character
    if classes[0] in row:
        Advanced.append(row)
    #rowSplitter = row.rstrip().split("\t",7)
    #print(row)
#print(listOflines)

with open("adcanced.csv","w") as fileToWrite:
    for row in Advanced:
        print(row)