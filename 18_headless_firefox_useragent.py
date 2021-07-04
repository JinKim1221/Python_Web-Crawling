
from selenium import webdriver
import requests
from bs4 import BeautifulSoup
import time
# headless : web scraping in Server without showing the browser -> faster
options = webdriver.FirefoxOptions()
options.headless = True
options.add_argument("window-size=1920x1080")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0")

browser = webdriver.Firefox(options=options)
browser.maximize_window()

# headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)

detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)

browser.quit()