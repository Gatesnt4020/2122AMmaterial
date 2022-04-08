from ast import Pass
import glob
import matplotlib.pyplot as plt

lineRemoved=0
def makeFiles(name):
    global lineRemoved
    #relative file path => the path from your file to another file
    with open(f"data/{name}","r",encoding="utf-8") as f:
        file = f.readlines()
        
    #print(file)

    reducedFile=[]
    for line in file:
        if line != "\n":
            reducedFile.append(line)
        else:
            lineRemoved+=1

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
            
def makeGraphs(items):
    titles=[1,2,3,4,5,6,7]
    plt.bar(titles,items)
    plt.title("Num of Pages in each HP Book")
    plt.xlabel("Book #")
    plt.ylabel("Page Count")
    plt.show()
    plt.pie(pageCount,labels=titles,autopct='%1.1f%%',)
    plt.show()

pageCount=[]
#Loop through the books, find the number of pages in each book,
#       and graph this in a graph
for i in range(len(bookList)):
    pageCount.append(pageNumber(bookList[i]))
makeGraphs(pageCount)

def charNumbers(FILENAME):
    with open(f"out/{FILENAME}","r",encoding="utf-8") as f:
        file = f.readlines()
        chrAmount=0
        for line in file:
            if "Page | " in line:
                Pass
            else:
                line = line.replace("\n","")
                for i in line:
                    chrAmount+=1
        return chrAmount                    

chrCount=[]
for i in range(len(bookList)):
    chrCount.append(charNumbers(bookList[i]))
#makeGraphs(chrCount)


def wordNumbers(FILENAME):
    with open(f"out/{FILENAME}","r",encoding="utf-8") as f:
        file = f.readlines()
        wordAmount=0
        for line in file:
            if "Page | " in line:
                Pass
            else:
                line = line.replace("\n","")
                if len(line) == 3 or len(line) == 5 or len(line) == 9 or len(line) >= 11:
                    wordAmount+=1
        return wordAmount                    

wordCount=[]
for i in range(len(bookList)):
    wordCount.append(wordNumbers(bookList[i]))
print(wordCount)
#makeGraphs(wordCount)

harry = ['Harry Potter','Harry']
ron = ['Ron','Ron Weasley']
al = ['Albus','Dumbledore']
hag = ['Hagrid']
her = ['Hermione','Hermione Granger']
dra = ['Draco Malfoy','Draco']
val=['Lord Voldemort']
characters=[harry,0,ron,0,al,0,hag,0,her,0,dra,0,val,0]

def charactersCounter(FILENAME):
    with open(f"out/{FILENAME}","r",encoding="utf-8") as f:
        file = f.readlines()
        for i in range(len(characters)):
            for line in file:
                try:
                    for j in range(len(characters[i])):
                        if characters[i][j] in line:
                            characters[i+1]= characters[i+1] + 1 
                            break
                except:
                    Pass

for i in range(len(bookList)):
    charactersCounter(bookList[i])

#book1 org = 496 kb book1 clean = 486 kb
#book2 org = 555 kb book2 clean = 544 kb
#book3 org = 708 kb book3 clean = 694 kb
#book4 org = 1234 kb  book4 clean = 1210 kb
#book5 org = 1676 kb  book5 clean = 1645 kb
#book6 org = 1103 kb  book6 clean = 1083 kb
#book7 org = 1275 kb  book7 clean = 1251 kb

def cleanPage(name):
    global lineRemoved
    #relative file path => the path from your file to another file
    with open(f"out/{name}","r",encoding="utf-8") as f:
        file = f.readlines()
        
    #print(file)

    reducedFile=[]
    number=""
    for line in file:
        if "Page | " in line:
            for letter in line:
                if letter.isdigit():
                    number+=letter
            line = number
        reducedFile.append(line+" ")
        number=""

    #print(reducedFile)
    
    with open(f"page/{name}","w+",encoding="utf-8") as f:
        for line in reducedFile:
            f.write(line)

for i in range(len(bookList)):
    cleanPage(bookList[i])

#cleanpage = 474 kb
#cleanpage = 531 kb
#cleanpage = 677 kb
#book4 cleanpage = 1208 kb
#book5 cleanpage = 1607 kb
#book6 cleanpage = 1059 kb
#book7 cleanpage = 1228 kb