def anyBaseToDec(ui,base):
    letters="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(len(letters))
    highExp = len(ui)-1
    decimal=0
    for i in ui:
        numba= letters.index(i)
        decimal+=(numba*base**highExp)
        highExp-=1
    print(decimal)
    
ui = input("number please ")
base = int(input("base please "))
anyBaseToDec(ui,base)