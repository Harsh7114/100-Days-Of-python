import requests
import  json
url = "https://exercise-api.com/v1/exercises"

response  = requests.get(url)
print("Status :",response.status_code)

data = response.json()
with open(file="data.json",mode="w") as f:
    json.dump(data,f,indent=4)