
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# Find all event list items
events = driver.find_elements(
    By.CSS_SELECTOR, ".event-widget li"
)

# Create an empty dictionary
events_dict = {}

# Extract date and name
for index, event in enumerate(events):

    date = event.find_element(By.TAG_NAME, "time")
    name = event.find_element(By.TAG_NAME, "a")

    event_date = date.get_attribute("datetime").split("T")[0]
    event_name = name.text

    # Add nested dictionary
    events_dict[index] = {
        "time": event_date,
        "name": event_name
    }

print(events_dict)
