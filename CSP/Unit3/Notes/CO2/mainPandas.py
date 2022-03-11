import matplotlib.pyplot as plt
import pandas

#read in the csv
FILENAME="temperature_data.csv"
tempData = pandas.read_csv(FILENAME,header=0)
#header=0 sets the first row as the "headers"

'''#min
print(tempData["Anomaly"].min())
#max
print(tempData["Anomaly"].max())
#average
print(tempData["Anomaly"].mean())
#sum
print(tempData["Anomaly"].sum())
#number of items
print(tempData["Anomaly"].count())'''

#plot a line graph
plt.plot(tempData["Year"],tempData["Anomaly"])
plt.ylabel("Temp Anomalies in C")
plt.xlabel("Years")
plt.title("Change in Temperatures")
plt.show()

#plot a bar graph
plt.bar(tempData["Year"],tempData["Anomaly"],align="center",color="green")
plt.ylabel("Temp Anomalies in C")
plt.xlabel("Years")
plt.title("Change in temperature")
plt.show()

anomaly=0
year=0

#what year did the min and max anomalies occur
print(tempData["Year"].loc[tempData["Anomaly"]==tempData["Anomaly"].min()])
print(tempData["Year"].loc[tempData["Anomaly"]==tempData["Anomaly"].max()])

