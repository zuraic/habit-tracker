import requests
from datetime import datetime

USERNAME = "red-mile"
TOKEN = "0Y6G0Z1bet57xy"
GRAPH_ID = "mile"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# create your user account
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# create a graph definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "cycle",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# post value to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
# today = datetime(year=2021, month=12, day=23)
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("how many kilometers did you cycle today? ")
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

# update value to the graph
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "34.5"
}

# response = requests.put(url=update_endpoint, headers=headers, json=new_pixel_data)
# print(response.text)

# delete value to the graph

# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
