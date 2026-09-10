import json
import os
from dotenv import load_dotenv
load_dotenv("../.env")
import requests
from twilio.rest import Client

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
#my_lats = 12.900255
my_lats = 22.119801
#my_long = 77.519087
my_long=84.037399
data = requests.get(url="https://api.openweathermap.org/data/2.5/forecast",
                    params={
                        "lat":my_lats,
                        "lon":my_long,
                        "appid":os.environ["WEATHER_API"],
                        "cnt":4, #upto 12hrs
                    })
# data = requests.get(
#     url="https://api.openweathermap.org/data/2.5/weather",
#     params={
#         "lat": my_lats,
#         "lon": my_long,
#         "appid": api_key,
#         "units": "metric"  # Optional: returns Celsius instead of Kelvin
#     }
# )
data.raise_for_status()

response = data.json()
first_id = response["list"][0]["weather"][0]["id"]
print(first_id)
# with open("data.json", "w") as f:
#     json.dump(response, f, indent=4)
will_rain = False
for hour in response["list"]:
    condition = hour["weather"][0]["id"]
    print(condition)
    if int(condition)<700:
        will_rain=True
if will_rain:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's Going to rain today take Your Umbrella",
        from_="+Your twilo assigned phone no ",
        to="+91 verified no where u want to send sms ",
    )
    print(message.status)