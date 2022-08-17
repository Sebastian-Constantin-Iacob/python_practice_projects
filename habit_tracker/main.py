import requests
import datetime

USERNAME = "YOUR ID"
TOKEN = "YOUR TOKEN"
GRAPH_NAME = "YOUR GRAPH NAME"
GRAPH_ID = "YOUR GRAPH ID"

currentDate = datetime.date.today().strftime("%Y%m%d")

# Create a user ( It is done with a post API request, see Docs ->  https://docs.pixe.la/entry/post-user )
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# response.raise_for_status()

# Create graph ( It is done with a post API request, see Docs ->  https://docs.pixe.la/entry/post-graph )
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_config = {
    "id": GRAPH_ID,
    "name": GRAPH_NAME,
    "unit": "commit",
    "type": "int",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# response.raise_for_status()
# print(response.text)

# Create pixel ( It is done with a post API request, see Docs ->  https://docs.pixe.la/entry/post-pixel )
upd_graph_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
upd_graph_params = {
    "date": str(currentDate),
    "quantity": '1'
}

# response = requests.post(url=upd_graph_endpoint, json=upd_graph_params, headers=headers)
# print(response.text)

# Update pixel ( It is done with a put API request, see Docs ->  https://docs.pixe.la/entry/put-pixel )
upd_pixel_endpoint = f"{upd_graph_endpoint}/{str(currentDate)}"
upd_pixel_params = {
    "date": str(currentDate),
    "quantity": "5"
}

# response = requests.put(url=upd_pixel_endpoint, json=upd_pixel_params, headers=headers)
# print(response.text)

# Delete pixel ( It is done with a delete API request, see Docs ->  https://docs.pixe.la/entry/delete-pixel )
dlt_pixel_endpoint = upd_pixel_endpoint
response = requests.delete(url=dlt_pixel_endpoint, headers=headers)
response.raise_for_status()
print(response.text)
