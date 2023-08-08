import requests
from config import TRANSLATE_API

ip_url = "https://ip-geolocation-ipwhois-io.p.rapidapi.com/json/"
headers = {
    "X-RapidAPI-Key": TRANSLATE_API,
    "X-RapidAPI-Host": "ip-geolocation-ipwhois-io.p.rapidapi.com"
}

response = requests.get(ip_url, headers=headers)
location_data = response.json()

try:
    city = location_data['city']
except KeyError:
    try:
        city = location_data['region']
    except KeyError:
        city = "Unknown city"

try:
    country = location_data['country']
except KeyError:
    country = "Unknown country"

weather_url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
querystring = {"city": city}

headers = {
    "X-RapidAPI-Key": TRANSLATE_API,
    "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
}

response = requests.get(weather_url, headers=headers, params=querystring)
weather_data = response.json()

try:
    temp_c = weather_data['temp']
except KeyError:
    temp_c = "Unknown temperature"

try:
    weather = weather_data['description']
except KeyError:
    weather = "Unknown weather"

print(f"City: {city}")
print(f"Temperature: {temp_c} C")
print(f"Weather: {weather}")
