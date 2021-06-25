import requests
import re
from bs4 import BeautifulSoup

url = "https://www.amazon.co.uk/s?k=laptop&ref=nb_sb_noss_1"
headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}

res = requests.get(url, headers=headers)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

items = soup.find_all("div", attrs= {"class" : re.compile("^s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 AdHolder sg-col sg-col-12-of-16")})
# print(items[0].find("span", attrs={"class" : "a-offscreen"}).get_text())

for item in items : 
    name = item.find("a", attrs={"class" : "a-link-normal a-text-normal"}).get_text()
    price = item.find("span", attrs={"class" : "a-offscreen"}).get_text()
    rate = item.find("span", attrs={"class" : "a-icon-alt"}).get_text()
    rate_cnt = item.find("span", attrs={"class" : "a-size-base"}).get_text()

    print("Product Name : " + name +"\nPrice : "+price+"\nRate :  "+ rate+"\nNumber of reviews : "+ rate_cnt +"\n")