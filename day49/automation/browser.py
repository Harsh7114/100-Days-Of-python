from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from config import PROFILE_DIR


def create_browser():

    PROFILE_DIR.mkdir(parents=True, exist_ok=True)

    options = Options()

    options.add_argument(
        f"--user-data-dir={PROFILE_DIR}"
    )

    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=options)

    return driver