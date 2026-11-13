from selenium import webdriver
from selenium.webdriver.common.by import By
#keep open the website
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach",True)


driver  = webdriver.Chrome(options=chrome_options)
driver.get(url="https://www.amazon.in/Motorola-Edge-Lily-256GB-Storage/dp/B0G75Q7TDP/ref=sr_1_1?sr=8-1")

price = driver.find_element(By.CLASS_NAME,value="a-price-whole")
print("Element:", price)
print("Text:", repr(price.text))
print("HTML:", price.get_attribute("outerHTML"))



# driver.close() # close perticular tab or single website
# driver.quit() # it close all tabs at once
