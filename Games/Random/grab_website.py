''' Doesn't work (maybe)
    import urllib.request

    url = "https://www.architecture.com/FindAnArchitect/FAAPractices.aspx display=50"    

    uf=urllib.request.urlopen(url)
    html = uf.read()
    #print(html)'''
import requests
from bs4 import BeautifulSoup

link = "https://www.architecture.com/FindAnArchitect/FAAPractices.aspx?display=50"

html = requests.get(link).text
print(html)
"""If you do not want to use requests then you can use the following code below 
   with urllib (the snippet above). It should not cause any issue."""
soup = BeautifulSoup(html, "lxml")
res = soup.findAll("article", {"class": "listingItem"})
for r in res:
    print("Company Name: " + r.find('a').text)
    print("Address: " + r.find("div", {'class': 'address'}).text)
    print("Website: " + r.find_all("div", {'class': 'pageMeta-item'})[3].text)
print('hello')
print(res)