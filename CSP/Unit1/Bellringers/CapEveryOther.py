#Ask the user for a word
word = input("enter a word ")
#capitalize every other letter
out=""
for i in range(len(word)):
    if i%2==0:      #even
        out+=word[i].upper()
    else:
        out+=word[i]
#output the word
print(out)