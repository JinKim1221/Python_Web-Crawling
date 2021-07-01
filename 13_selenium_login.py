from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox() # "./geckodriver.exe"

headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
url = "https://www.google.com/"
browser.get(url)

elem = browser.find_element_by_id("L2AGLb")
elem.click()

browser.refresh()


login_elem = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div/div/div/div[2]/a")
login_elem.click()

id_elem = browser.find_element_by_id("identifierId")
id_elem.send_keys("test")

next_elem = browser.find_element_by_xpath("/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span")
next_elem.click()

# pass_elem = browser.find_element_by_id("")

# browser.quit()