#print out 0-99
for r in range(10):#        #range() => list
    for c in range(10):
        print(str(r)+str(c),end=" ")
    print()

print()

r=0
while r < 10:
    c=0
    while c < 10:
        print(str(r)+str(c),end=" ")
        c+=1
    r+=1
    print()