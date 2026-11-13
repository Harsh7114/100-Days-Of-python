from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(url="https://orteil.dashnet.org/experiments/cookie/")

cookie_button = driver.find_element(By.ID,value="cookie")
money = driver.find_element(By.ID,value="money")
itemlist = driver.find_elements(By.CSS_SELECTOR,value="#store div")
# fetch the id of all the store elements in list
item_ids = [item.get_attribute("id") for item in itemlist]
print(item_ids)

# while True:
#     cookie_button.click()


