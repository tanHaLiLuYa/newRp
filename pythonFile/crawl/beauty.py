from bs4 import BeautifulSoup
import urllib

html = urllib.request.urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html,features="lxml")

nameList = bsObj.findAll("span", {"class":"green"})
for name in nameList:
    print(name.get_text())