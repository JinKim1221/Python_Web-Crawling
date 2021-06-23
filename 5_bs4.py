import requests
from bs4 import BeautifulSoup 

url="https://www.tesco.ie/groceries/SpecialOffers/default.aspx"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a) # first 'a' element in soup object
# print(soup.a.attrs) # attributes of 'a' element
# print(soup.a["href"]) # the attribute of value of 'a' element

# print(soup.find("div", attrs={"id" : "primaryNav"})) # find id="primaryNav" in 'div' element
item = soup.find("div", attrs={"class" : "desc"})
print(item.a.span)
