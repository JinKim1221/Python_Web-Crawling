from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox() # "./geckodriver.exe"


headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
url = "https://www.naver.com/"

# browser.get(url)
# element = browser.find_element_by_id("query")
# element.click()
# element.send_keys("web crawling")
# element.send_keys(Keys.ENTER)

browser.get("http://daum.net")
elem = browser.find_element_by_name("q")
elem.send_keys("web crawling")
# elem.send_keys(Keys.ENTER)
elem = browser.find_element_by_xpath("/html/body/div[2]/header/div[1]/div/div[1]/form/fieldset/div/div/button[2]")
# print(elem)
elem.click()

browser.quit()
# browser.back()
# browser.forward()
# browser.refresh()
# browser.back()