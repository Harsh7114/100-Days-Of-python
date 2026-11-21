from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from config import (
    BASE_URL,
    GYM_USERNAME,
    GYM_PASSWORD,
    WAIT_TIMEOUT
)

from automation.browser import create_browser


def login_to_gym(driver):

    wait = WebDriverWait(driver, WAIT_TIMEOUT)

    # Open gym website
    driver.get(BASE_URL)

    print("Gym website opened!")

    # Locate username field
    username_field = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "username")
        )
    )

    username_field.send_keys(GYM_USERNAME)

    print("Username entered!")

    # Locate password field
    password_field = driver.find_element(
        By.ID,
        "password"
    )

    password_field.send_keys(GYM_PASSWORD)

    print("Password entered!")

    # Locate login button
    login_button = driver.find_element(
        By.ID,
        "login-btn"
    )

    login_button.click()

    print("Login button clicked!")

    # Wait for classes page
    wait.until(
        EC.url_contains("/classes")
    )

    # Verify login
    if "/classes" not in driver.current_url:
        raise Exception("Login failed!")

    welcome_message = wait.until(
        EC.visibility_of_element_located(
            (By.ID, "welcome-message")
        )
    )

    print("Login successful!")
    print(welcome_message.text)

    return True

    print("Login successful!")
    print(welcome_message.text)

    return True
if __name__ == "__main__":

    driver = create_browser()

    try:
        login_to_gym(driver)

        input("Press Enter to close browser...")

    finally:
        driver.quit()