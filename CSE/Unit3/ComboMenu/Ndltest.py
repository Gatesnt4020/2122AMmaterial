testy=[["h","e","l","l","o"],["wo","rl","d"]]
listy=["a","b","c","d"]

#printing a list vertically
for i in range(len(listy)):
    print(listy[i])

print(listy[1])
print(testy[1][0])

#this to find each item in the 2d array
for row in range(len(testy)):
    for col in range(len(testy[row])):
        ptint(testy[row][col])