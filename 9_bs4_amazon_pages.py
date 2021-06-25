
import requests
import re
from bs4 import BeautifulSoup

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
for i in range(1, 6):
        
    url = "https://www.amazon.co.uk/s?k=laptop&page={}&qid=1624653497&ref=sr_pg_2".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("div", attrs= {"class" : re.compile("^s-include-content-margin s-border-bottom s-latency-cf-section")})
    # print(items[0].find("span", attrs={"class" : "a-offscreen"}).get_text())

    for item in items : 
        # exclude advertised items
        ad_items = item.find("span", attrs={"class" : "a-color-secondary"})
        # print(ad_items)
        if ad_items : 
            if ad_items.get_text() == "Sponsored":
                print("Exculde advertised items\n")
                continue
        else :
            print(" ")
        
        name = item.find("h2", attrs={"class" : "a-size-mini a-spacing-none a-color-base s-line-clamp-2"}).get_text()
        if "Samsung" in name:
            print("Exclude Samsug products\n")
            continue

        price = item.find("span", attrs={"class" : "a-offscreen"})
        if price:
            price = price.get_text()
        else :
            price = "No price available"
            continue
    
        rate = item.find("span", attrs={"class" : "a-icon-alt"})
        if rate:
            rate = rate.get_text()[0:4]
        else :
            rate = "No review available"
            continue

        rate_cnt = item.find("span", attrs={"class" : "a-size-base"})
        if rate_cnt:
            rate_cnt = rate_cnt.get_text()
        else :
            rate_cnt = "not available"
            continue

        if float(rate) >= 4.5 :
            print("Product Name : " + name +"\nPrice : "+price+"\nRate :  "+ rate+"\nNumber of reviews : "+ rate_cnt +"\n")