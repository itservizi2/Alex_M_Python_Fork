from myconfigs import TRANSLATE_API
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def get_weather(request, city):
    ip_url = "https://ip-geolocation-ipwhois-io.p.rapidapi.com/json/"
    headers = {
        "X-RapidAPI-Key": TRANSLATE_API,
        "X-RapidAPI-Host": "ip-geolocation-ipwhois-io.p.rapidapi.com"
    }

    response = requests.get(ip_url, headers=headers)
    location_data = response.json()

    city = city

    weather_url = "https://weather-by-api-ninjas.p.rapidapi.com/v1/weather"
    querystring = {"city": city}

    headers = {
        "X-RapidAPI-Key": TRANSLATE_API,
        "X-RapidAPI-Host": "weather-by-api-ninjas.p.rapidapi.com"
    }

    response = requests.get(weather_url, headers=headers, params=querystring)
    weather_data = response.json()

    temp_c = weather_data['temp']
    try:
        weather = weather_data['description']
    except KeyError:
        weather = "Unknown weather"

    response_text = f"In the city {city} are {temp_c} degrees and the weather is {weather}."

    return Response(response_text)
