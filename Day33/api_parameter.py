import requests
from datetime import datetime as dt
from zoneinfo import ZoneInfo
my_lats=12.900255
my_long=77.519087
parameters = {
    "lat":my_lats,
    "lng":my_long,
    "formatted":0,
}

response = requests.get("https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
print(data)
sunrise = data["results"]["sunrise"]
sunset  = data["results"]["sunset"]
# Convert API strings into datetime objects
sunrise = dt.fromisoformat(sunrise)
sunset = dt.fromisoformat(sunset)
# Convert UTC → IST
ist = ZoneInfo("Asia/Kolkata")
sunrise_ist = sunrise.astimezone(ist)
sunset_ist = sunset.astimezone(ist)

print("Sunrise:", sunrise_ist)
print("Sunset:", sunset_ist)
time_now = dt.now(ist)
print("Current IST:", time_now)