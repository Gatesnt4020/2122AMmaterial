import glob

def makeFiles(name):
    #relative file path => the path from your file to another file
    with open(f"data/{name}","r",encoding="utf-8") as f:
        file = f.readlines()
        
    #print(file)

    print("original length of file: ",len(file))

    reducedFile=[]
    for line in file:
        if line != "\n":
            reducedFile.append(line)

    #print(reducedFile)
    
    with open(f"out/{name}","w+",encoding="utf-8") as f:
        for line in reducedFile:
            f.write(line)
    print("reduced length of file: ",len(reducedFile))

#print which books are present in directory
books = (glob.glob("data/*.txt"))       #* stands for wildcard

bookList=[]
for b in books:
    bookList.append(b[5:])
print(bookList)

for i in range(len(bookList)):
    makeFiles(bookList[i])
    print()