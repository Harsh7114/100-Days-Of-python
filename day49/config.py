import os
from pathlib import Path
from  dotenv import load_dotenv

BASE_DIR =  Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

BASE_URL = os.getenv(
    "BASE_URL",
    "http://127.0.0.1:5000"
)

GYM_USERNAME = os.getenv("GYM_USERNAME")
GYM_PASSWORD = os.getenv("GYM_PASSWORD")

SECRET_KEY = os.getenv("SECRET_KEY")

PROFILE_DIR = BASE_DIR / "profiles" / "chrome_profile"

# Screenshot directory
SCREENSHOT_DIR = BASE_DIR / "screenshots"

SCREENSHOT_DIR.mkdir(exist_ok=True)

# Timeout configuration
WAIT_TIMEOUT = 10