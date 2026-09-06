import requests
from datetime import datetime as dt
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
sunrise = data["results"]["sunrise"]
sunset  = data["results"]["sunset"]
print(sunrise,sunset)
time_now = dt.now()
print(time_now)