import os
import requests
import csv
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 103
HEIGHT_CM = 172
AGE = 30
NIX_EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
CSV_HEADERS = ["Date", "Time", "Exercise", "Duration", "Calories"]

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
csv_row = []

response = requests.post(url=NIX_EXERCISE_ENDPOINT, json=nix_params, headers=nix_headers)
print(response.text)
data = response.json()

# Get workout details
csv_row.append(str(datetime.today().strftime('%d-%m-%Y')))
csv_row.append(str(datetime.now().strftime("%H:%M:%S")))
csv_row.append(data["exercises"][0]["user_input"])
csv_row.append(data["exercises"][0]["duration_min"])
csv_row.append(data["exercises"][0]["nf_calories"])

if not os.path.exists("workout_log.csv"):
    with open("workout_log.csv", "w", newline="") as outcsv:
        writer = csv.writer(outcsv)
        writer.writerow(CSV_HEADERS)

with open("workout_log.csv", "a") as f:
    writer = csv.writer(f)
    writer.writerow(csv_row)
