#as -> an alias
import datetime as dt
lm=["January","March","May","July","August","October","December"]
mm= ["November","April","June","September"]
sm=["February "]
year = dt.datetime.now().year
month = dt.datetime.now().month
day = dt.datetime.now().day
'''
year = dt.datetime.now().year
month = dt.datetime.now().month
day = dt.datetime.now().day
#ask the user for what year they were born in
uy = int(input("what year you born in "))
um = int(input("what month were you born in "))
ud = int(input("what day were you born in "))
#print out how long ago that was
'''
#Spencer code
'''
if um > month: 
    ageinMonths = (((year - 1) - uy) * 12  + ud/30 + um)
else: 
    ageinMonths = ((year - uy) * 12  + ud/30 + um)
print(f'You are {round((ageinMonths/12), 1)} years old.')
'''
#Keenan code
'''
year = ""
while not(year.isdigit()):
    year = input("What year where you born in?  ")
month = ""
while not(month.isdigit()):
    month = input("What month where you born in?(January - 1, Febuary - 2, ect.)  ")
day = ""
while not(day.isdigit()):
    day = input("What day where you born on?")
cYear = dt.datetime.now().year
cMonth = dt.datetime.now().month
cDay = dt.datetime.now().day
bDay = False
yearsOld = cYear - int(year)
if not(int(month) <= cMonth and int(day) <= cDay):
    yearsOld-=1
else:
    bDay = True
if bDay:
    if cMonth == int(month):
        daysOld = cDay - int(day)
    else:
        daysOld = cDay
else:
    daysOld = cDay
monthsOld = cMonth - int(month)
if monthsOld < 0:
    monthsOld += 12
print(str(yearsOld)+ " years old, "+str(monthsOld)+" months old, "+str(daysOld)+" days old")
'''
#module.constructor.function()
#print(dt.datetime.now().year)