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
# item = soup.find("li", attrs={"class" : "first cp"})
# print(item.a.get_text())
# print(item.next_sibling)
# item2 = item.next_sibling
# item3 = item2.next_sibling
# print(item3.a.get_text())
# item2 = item3.previous_sibling
# print(item2.a.get_text())
# print(item.parent)

# item2 = item.find_next_sibling("li")
# print(item2.a.get_text())
# item3 = item2.find_next_sibling("li")
# print(item3.a.get_text())
# item2 = item3.find_previous_sibling("li")
# print(item2.a.get_text())

# print(item.find_next_siblings("li"))

# item = soup.find("strong", text ="Philadelphia Light Soft Cheese Snack ...")
# print(item)
