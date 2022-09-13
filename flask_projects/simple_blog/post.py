import requests


class Post:
    response = requests.get(url="https://api.npoint.io/23cc74e61161d4b00a1b", verify=False)
    response.raise_for_status()
    data = response.json()
