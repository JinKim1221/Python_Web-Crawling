# import requests
# from bs4 import BeautifulSoup

# headers = {
#     "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"
#     # "Accept-Language" : "ko-KR, ko"
#     }

# url = "https://play.google.com/store/books/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAE%3D:S:ANO1ljIvTNM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYAQ%3D%3D:S:ANO1ljK-5i4&gl=IE"

# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# books = soup.find_all("div", attrs={"class" : "ImZGtf mpg5gc"})

# for book in books:
#     title = book.find("div", attrs={"class" : "WsMG1c nnK0zc"}).get_text()
#     print(title)

from bs4.element import Script
from selenium import webdriver
browser = webdriver.Firefox()
browser.maximize_window()

url = "https://play.google.com/store/books/collection/cluster?clp=0g4XChUKD3RvcHNlbGxpbmdfcGFpZBAHGAE%3D:S:ANO1ljIvTNM&gsr=ChrSDhcKFQoPdG9wc2VsbGluZ19wYWlkEAcYAQ%3D%3D:S:ANO1ljK-5i4&gl=IE"
browser.get(url)


# scroll down to where the spot(1080) of screen 
# browser.execute_script("window.scrollTo(0, 1080)")

# scroll down to the bottom of browser
browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")