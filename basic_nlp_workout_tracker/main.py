import os
import requests

GENDER = "male"
WEIGHT_KG = 103
HEIGHT_CM = 172
AGE = 30
NIX_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

nix_query = input("Tell me about your exercise: ")
nix_headers = {
    "x-app-id": os.environ["NUTRITIONIX_APP_ID"],
    "x-app-key": os.environ["NUTRITIONIX_API_KEY"]
}
nix_params = {
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
    "query": nix_query
}

response = requests.post(url=NIX_EXERCISE_ENDPOINT, json=nix_params, headers=nix_headers)
print(response.text)

# print(os.environ["NUTRITIONIX_APP_ID"])
# print(os.environ["NUTRITIONIX_API_KEY"])
