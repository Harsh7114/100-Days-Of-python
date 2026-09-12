import requests
import datetime as datetime
pixela_endpoint = "https://pixe.la/v1/users"
USERNAME="saturnvenus"
TOKEN = "gfdkjdfgkjfgkjfgfk"
user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
#response=requests.post(url=pixela_endpoint,json=user_params)
#print(response.text)
# get_user = requests.get(url="https://pixe.la/@saturnvenus")
# print(get_user.text)
#create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_params = {
    "id":"graph1",
    "name":"DSA Graph",
    "unit":"hour",
    "type":"int",
    "color":"ajisai"
}
headers = {
    "X-USER-TOKEN":TOKEN
}
#response_graph = requests.post(url=graph_endpoint,json=graph_params,headers=headers)
#print(response_graph.text)
#too see my graph https://pixe.la/v1/users/saturnvenus/graphs/graph1.html


#to update the pixel using post req
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today = datetime.datetime.now().strftime("%Y%m%d")
yesterday = "20260911"
pixel_parameters ={
    "date":yesterday,
    "quantity":"5",
}
# add_pixel = requests.post(url=pixel_endpoint,json=pixel_parameters,headers=headers)
# print(add_pixel.text)

# remove the pixel usig PUT
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{yesterday}"
update_params = {
    "quantity":"12"
}
update_pixel = requests.put(url=update_endpoint,json=update_params,headers=headers)
print(update_pixel.text)