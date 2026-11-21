
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.common.exceptions import (
    TimeoutException,
    ElementClickInterceptedException
)


# 1. Chrome configuration
chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option(
    "detach", True
)

prefs = {
    "profile.default_content_setting_values.geolocation": 1
}

chrome_options.add_experimental_option("prefs", prefs)


# 2. Launch browser
driver = webdriver.Chrome(options=chrome_options)

wait = WebDriverWait(driver, 10)

driver.get("https://www.speedtest.net/")


# 3. Handle Windows promotional popup
try:

    close_button = WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//button[@title="Dismiss"]')
        )
    )

    close_button.click()

    print("Windows popup closed!")

except TimeoutException:

    print("Windows popup not displayed!")


# 4. Handle privacy popup
try:

    privacy_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (By.ID, "onetrust-accept-btn-handler")
        )
    )

    privacy_button.click()

    print("Privacy popup handled!")

except TimeoutException:

    print("Privacy popup not displayed!")

except ElementClickInterceptedException:

    print("Privacy button is blocked by another element!")


# 5. Click Go button
go_button = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH,
         "/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button")
    )
)

go_button.click()

print("Speed test started!")

#handle add
try:
    download_element = WebDriverWait(driver, 120).until(
        EC.visibility_of_element_located(
            (By.XPATH, '/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[1]/div/h3')
                )
    )
    download_speed= download_element.text
    print("Download Speed:", download_speed, "Mbps")

    upload_element = WebDriverWait(driver,120).until(
        EC.visibility_of_element_located(
            (By.XPATH,'/html/body/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[2]/div[1]/div[2]/div/h3')
        )
    )
    upload_speed = upload_element.text
    print("Upload Speed:", upload_speed, "Mbps")

except TimeoutException:
    print("Speed test results did not appear within 120 seconds!")