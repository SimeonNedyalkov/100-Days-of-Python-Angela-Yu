import requests
from datetime import datetime
TOKEN = "simeon123"
USERNAME = "acinarret"
pixela_endpoint = "https://pixe.la/v1/users"
parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
response = requests.post(url=pixela_endpoint, json=parameters)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_parameters = {
    "id": "graph1",
    "name": "Cycling graph",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_response = requests.post(url=graph_endpoint, json=graph_parameters, headers= headers)
today = datetime.now()
pixel_pixela_endpoint = "https://pixe.la/v1/users/acinarret/graphs/graph1"
pixel_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "20"
}
pixel_response = requests.post(url=pixel_pixela_endpoint, json=pixel_parameters,headers=headers)

update_endpoint = f"https://pixe.la/v1/users/acinarret/graphs/graph1/{today.strftime('%Y%m%d')}"
update_parameters = {
    "quantity": "8.3",
}
update_response = requests.put(url=update_endpoint, json=update_parameters,headers=headers)

delete_response = requests.delete(url=update_endpoint, headers=headers)
print(delete_response.text)
