import requests

response=requests.get(url="http://api.open-notify.org/iss-now.json")
if response.status_code != 200:
    raise  Exception("Bad response from ISS API")
if response.status_code == 400:
    raise Exception ("That resource does not exist")
elif response.status_code ==401:
    raise Exception("You are not authorized")

# or
response.raise_for_status()
data = response.json()["iss_position"]
print(data)
longitude=response.json()["iss_position"]["longitude"]
latitude=response.json()["iss_position"]["latitude"]
print(longitude)
print(latitude)

