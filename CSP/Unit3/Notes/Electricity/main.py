import pandas as pd
import matplotlib.pyplot as plt

#read your csv
data = pd.read_csv("elec_access_data.csv",header=0)

#which countries we want to look at
ourCountries=["Japan","South Korea","Thailand","Singapore","Hong Kong"]

#find the unique countries how many
countries = data.Entity.unique()

#graph the out countries
#go find each of our countries in the unique countries
for c in countries:
    if c in ourCountries:
        #grab the data of that paticular country
        #x axis data
        years = data[data["Entity"]==c]['Year']
        #if the entity column is equal our country, make a dataframe of the years
        #y axis data
        elecAccess = data[data["Entity"]==c]['Access']
        #if the entity column is equal our country, make a dataframe of the access
        
        #since we are putting multiple countries in one graphs
        #graph 
        plt.plot(years,elecAccess,label=c)

plt.ylabel("% of Country Population")
plt.xlabel("Years")
plt.title("% of Population with Electricity Access")
plt.legend()
plt.show()

#plot out graph
