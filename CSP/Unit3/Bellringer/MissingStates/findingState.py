import pandas as pd
data = pd.read_csv("MOCK_DATA.csv",header=0)

#find the uniques again
company = data.company.unique()

dir={}

for i in company:
    dir[i] = 0

data1=data["company"]
data2=data["cost"]

for i in range(len(data1)):
    dir[data1[i]] = dir[data1[i]] + data2[i]
    
print(dir)

total=0
for i in data2:
    total+=i
    
print(round(total))