import os,time

while True:
    print(f"1) ipconfig\n2) tracert\n3) ping\n4) nslookup")
    ui = input("Which command would you like to do >> ")
    if ui != "1" and ui != "2" and ui != "3" and ui != "4":
        print('Please input 1-4 please')
        continue
    if ui == "1":
        os.system('cls' if os.name=='nt' else 'clear')
        os.system('ipconfig' if os.name=='nt' else 'clear')
        time.sleep(2)
    elif ui == "2":
        os.system('cls' if os.name=='nt' else 'clear')
        ui = input("Enter the address you would like to trace >> ")
        os.system('tracert '+ui if os.name=='nt' else 'clear')
        time.sleep(2)
    elif ui == "3":
        os.system('cls' if os.name=='nt' else 'clear')
        ui = input("Enter the address you would like ping >> ")
        os.system('ping '+ui if os.name=='nt' else 'clear')
        time.sleep(2)
    else:
        os.system('cls' if os.name=='nt' else 'clear')
        ui = input("Enter the website you would like to look up >> ")
        os.system('nslookup '+ui if os.name=='nt' else 'clear')
        time.sleep(2)