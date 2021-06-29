from selenium import webdriver

browser = webdriver.Firefox() # "./geckodriver.exe"


headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
url = "https://www.google.com/?gws_rd=ssl"

browser.get(url)


element = browser.find_element_by_id("L2AGLb")
element.click()
# background_elem = browser.find_element_by_class_name("o3j99 ikrT4e om7nvf")
# background_elem.click()
# login_elem = browser.find_element_by_class_name("gb_3 gb_4 gb_9d gb_3c")
# login_elem.click()
# browser.back()
# browser.forward()
# browser.refresh()
# browser.back()