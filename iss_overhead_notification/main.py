import requests
from datetime import datetime

# Use the fallowing link to get your coordinates https://www.latlong.net/
MY_LAT = 50.942062
MY_LONG = -2.633308
my_coordinates = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

# GET ISS current position
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

# GET information on time ( night / day ) | FYI - verify=false in the get response should not be used, but the api
# has an expired SSL certificate
response = requests.get(url="https://api.sunrise-sunset.org/json", params=my_coordinates, verify=False)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
current_time = datetime.now().hour

#
