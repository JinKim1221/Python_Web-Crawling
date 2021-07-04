
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
# headless : web scraping in Server without showing the browser -> faster
options = webdriver.FirefoxOptions()
options.headless = True
options.add_argument("window-size=1920x1080")

browser = webdriver.Firefox(options=options)
browser.maximize_window()

url = "https://play.google.com/store/books/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAE%3D:S:ANO1ljIvTNM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYAQ%3D%3D:S:ANO1ljK-5i4&gl=IE"
browser.get(url)


interval = 2 # scroll down every two seconds

# save the current height of document
prev_height = browser.execute_script("return document.body.scrollHeight")

while True:
    # scroll down to the bottom of browser
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    
    # wait for the page to load
    time.sleep(interval)
    current_height = browser.execute_script("return document.body.scrollHeight")
    if current_height == prev_height :
        break

    prev_height = current_height

time.sleep(interval)

soup = BeautifulSoup(browser.page_source, "lxml")

books = soup.find_all("div", attrs={"class" : "RZEgze"})
books_onSale = soup.find_all("span", attrs={"class" : "SUZt4c djCuy"})
    
# print(len(books))
for book in books:
    origin_price = book.find("span", attrs={"class" : "SUZt4c djCuy"})

    if origin_price:   
        origin_price = origin_price.get_text()
        title = book.find("div", attrs={"class" : "WsMG1c nnK0zc"}).get_text()    
        sale_price = book.find("span", attrs={"class" : "VfPpfd ZdBevf i5DZme"}).get_text()
        link = book.find("a", attrs={"class" : "JC71ub"})["href"]
        print("book title  : ", title)
        print(f"price  : {origin_price} -> {sale_price}" )
        print("link  : https://play.google.com" +link)
    else:
        continue

browser.get_screenshot_as_file("google_books.png")

browser.quit()