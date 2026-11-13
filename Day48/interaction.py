from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.common.keys import  Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach",True)


driver = webdriver.Chrome(options=chrome_option)
driver.get("https://en.wikipedia.org/wiki/Main_Page")

article = driver.find_element(By.XPATH,value="/html/body/div[3]/div/div[3]/main/div[3]/div[2]/div[1]/section/div[1]/div/div[3]/ul/li[1]/a/span")
print(article.text)
article_count = driver.find_element(By.CSS_SELECTOR,value="#articlecount a")
print(article_count.text)
# article_count.click()


#search on website
search = driver.find_element(By.NAME,value="search")
search.send_keys("python")
search.send_keys(Keys.ENTER)

#to click on links from anchor tag
# all_portals = driver.find_element(By.LINK_TEXT,value="Content portals")
# all_portals.click()


