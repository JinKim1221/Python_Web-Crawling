from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Firefox( ) # "./geckodriver.exe"
browser.maximize_window()

# Move to skyscanne.ie

url = "https://flight.naver.com/flights"
browser.get(url)

action = ActionChains(browser)
# click depart date
browser.find_element_by_link_text("가는날 선택").click()

# select 20th this month to 21th of next month
browser.find_elements_by_link_text("20")[0].click()
browser.find_elements_by_link_text("21")[1].click()

browser.find_element_by_link_text("도착").click()
input = browser.find_element_by_xpath("/html/body/div/div/div[2]/div[1]/fieldset/div[1]/div/div[2]/div[1]/input")
input.send_keys("Dublin")

# depart = browser.find_elements_by_tag_name("ng-bind-html")
# print(depart)
# action.move_to_element(depart).perform()
