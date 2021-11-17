print("How much change? (enter stop to quit)")
UI = input(">>> ")
while UI != "stop":
    UI = float(UI)
    UI = UI * 100
    quarter = 0
    dime = 0
    nickle = 0
    dime = 0
    penny = 0
    while UI - 25 >= 0:
        UI-= 25
        quarter+=1
    while UI - 10 >= 0:
        UI-= 10
        dime+=1
    while UI - 5 >= 0:
        UI-= 5
        nickle+=1
    while UI - 1 >= 0:
        UI-= 1
        penny+=1
    print(f"""
Quarters: {quarter}
Dimes: {dime}
Nickles: {nickle}
Penny: {penny}
          """)
    UI = input(">>> ")
print("Goodbye.")