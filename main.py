import requests
from datetime import datetime
from decouple import config
USERNAME = 'hiren'
TOKEN = config('TOKEN')
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService" : "yes",
    "notMinor": "yes",
}


pixela_endpoint = "https://pixe.la/v1/users"

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Programming Practice",
    "unit": "minutes",
    "type": "int",
    "color": "momiji"
}
headers = {
    "X-USER-TOKEN" : TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
#
# graph_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
today = datetime.now()
#
#
# pixel_config = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "40",
# }
#
# response = requests.post(url=graph_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

#update a pixel

update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{today.strftime('%Y%m%d')}"

updated_config = {
    "quantity" : "50",
}

response = requests.put(url=update_endpoint, json=updated_config, headers=headers)
print(response.text)

#delete a pixel

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20211016"

response = requests.delete(url=delete_endpoint, headers=headers)