import glob
import matplotlib.pyplot as plt

def makeFiles(name):
    #relative file path => the path from your file to another file
    with open(f"data/{name}","r",encoding="utf-8") as f:
        file = f.readlines()
        
    #print(file)


    reducedFile=[]
    for line in file:
        if line != "\n":
            reducedFile.append(line)

    #print(reducedFile)
    
    with open(f"out/{name}","w+",encoding="utf-8") as f:
        for line in reducedFile:
            f.write(line)

#print which books are present in directory
books = (glob.glob("data/*.txt"))       #* stands for wildcard

bookList=[]
for b in books:
    bookList.append(b[5:])

for i in range(len(bookList)):
    makeFiles(bookList[i])
    
#Going to find the page count
cleanBookList=glob.glob("out/*.txt")
bookList=[]
for b in cleanBookList:
    bookList.append(b[4:])

def pageNumber(FILENAME):
    with open(f"out/{FILENAME}","r",encoding="utf-8") as f:
        file = f.readlines()
        lastLine=(file[-1])
        #find the numbers in the lastLine
        number=""
        for i in range(len(file)):
            for letter in lastLine:
                if letter.isdigit():
                    number+=letter
            if number !="":
                return int(number)
            lastLine=file[-i]
            
            
pageCount=[]
#Loop through the books, find the number of pages in each book,
#       and graph this in a graph
for i in range(len(bookList)):
    pageCount.append(pageNumber(bookList[i]))
titles=[1,2,3,4,5,6,7]
plt.bar(titles,pageCount)
plt.title("Num of Pages in each HP Book")
plt.xlabel("Book #")
plt.ylabel("Page Count")
plt.show()