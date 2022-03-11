with open("temperature_data.csv","r") as f:
    file=f.readlines()
    index=0
    for i in file:
        file[index]=i.rstrip()
        index+=1

anomaly=[]
for row in file:
    row = row.split(",")        #cleaned data
    try:
        anomaly.append(float(row[1]))      #getting the anomaly and adding the anomalies to the list
    except:
        print(row[1])
        pass    #pass is a keyword taht just passes

minValue=min(anomaly)
maxValue=max(anomaly)
aveValue=sum(anomaly)/len(anomaly)

print(f'''
      min anomaly:  {minValue}
      max anomaly:  {maxValue}
      ave anomaly:  {aveValue}
''')