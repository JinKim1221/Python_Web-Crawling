import requests
from bs4 import BeautifulSoup 

url="https://www.tesco.ie/groceries/SpecialOffers/default.aspx"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

# Get all the items from Tesco special offers
items = soup.find_all("div", attrs={"class" : "desc"})
# all 'div' elements that have 'desc' class are found 
for item in items : 
    print(item.get_text())