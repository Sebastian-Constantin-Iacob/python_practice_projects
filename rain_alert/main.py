import requests

OWM_URL = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "your_open_weather_key_here"  # Your API key
MY_LAT = 50.942062   # Your latitude
MY_LONG = -2.633308  # Your longitude

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
    "hourly": True
}

response = requests.get(url=OWM_URL, params=parameters)
response.raise_for_status()
data = response.json()

print(data["hourly"][0]["weather"][0]["id"])
