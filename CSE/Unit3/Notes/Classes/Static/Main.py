#from file import class
from UnitConverter import UnitConverter

#build a program that allows the user to conver calues until they say stop

userInterface = f'''
convert f to c = 1
convert f to k = 2
convert c to f = 3
convert c to k = 4
convert k to c = 5
convert k to f = 6
'''
#should probably add a while statement so user has to enter num for the conversion 
print(userInterface)
ui = input("What would you like to convert? ")
while(ui!="q"):
    if ui == "1":
        print(UnitConverter.fahrenheitToCelsius(int(input("Fah: "))))
    elif ui =="2":
        print(UnitConverter.fahrenheitToKelvin(int(input("Fah: "))))
    elif ui =="3":
        print(UnitConverter.celsiusToFahrenheit(int(input("Cel: "))))
    elif ui =="4":
        print(UnitConverter.celsiusToKelcin(int(input("Cel: "))))
    elif ui=="5":
        print(UnitConverter.kelvinToCelsius(int(input("K: "))))
    elif ui =="6":
        print(UnitConverter.kelvinToFahrenheit(int(input("K: "))))
    ui=input(userInterface)
