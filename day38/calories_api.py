import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("API_NINZA")
url = "https://api.api-ninjas.com/v1/caloriesburned"

def get_calories(activity,weight,duration,intensity=None):
    headers = {
        "X-Api-Key": API_KEY
    }

    params = {
        "activity": activity,
        "weight": weight,
        "duration": duration
    }
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()
    if not data:
        return None
    return data
# if response.status_code == requests.codes.ok:
#     data = response.json()
#     print(data)
# else:
# #     print("Error:", response.status_code, response.text)
# data = get_calories(
#     activity="cycling",
#     weight=154,
#     duration=30
# )
#
# print(data)