# -*- coding: utf-8 -*-
from os import remove, replace
import requests
from bs4 import BeautifulSoup 
url = "https://www.tesco.ie/groceries/product/browse/default.aspx?N=4294470623&Ne=4294954028"

res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


# chickens = soup.find_all("h3", {"class" : "inBasketInfoContainer"})
# title = chickens[0].a.get_text()
# link = chickens[0].a["href"]
# print(title)
# print("https://www.tesco.ie/" + link)

# Title and Link of each item
# for chicken in chickens : 
#     title = chicken.a.get_text()
#     link = "https://www.tesco.ie/" + chicken.a["href"]
#     print(title, " ", link)

# Price of each item
total_price = 0
chickens = soup.find_all("span", {"class" : "linePrice"})
for chicken in chickens:
    price = chicken.get_text()
    print(price)
    # total_price += float(price)
# print("total price : ", total_price)
# print("average price : ", total_price/ len(chickens))

