from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser = webdriver.Firefox() # "./geckodriver.exe"

# Move to naver.com
url = "https://www.naver.com/"
browser.get(url)

# Click login button
elem = browser.find_element_by_class_name("link_login")
elem.click()

# input id, password
login_elem = browser.find_element_by_id("id")
login_elem.send_keys("test")
pass_elem = browser.find_element_by_id("pw")
pass_elem.send_keys("test--!")

# click login button
signin_elem = browser.find_element_by_id("log.login")
signin_elem.click()

time.sleep(4)

# input new id
browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("sdo7329")

# dispslay html info
print(browser.page_source)

# close browser
# browser.close() # close current browser 
browser.quit() # close all browsers