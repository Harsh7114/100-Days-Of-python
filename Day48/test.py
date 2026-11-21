from selenium import  webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import Keys
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.saucedemo.com/")

username = driver.find_element(By.ID,value="user-name")
username.send_keys("standard_user")
password = driver.find_element(By.ID,value="password")
password.send_keys("secret_sauce")
login_button = driver.find_element(By.ID,"login-button")
login_button.click()