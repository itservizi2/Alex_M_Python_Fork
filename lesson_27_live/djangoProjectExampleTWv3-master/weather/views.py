from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(["GET"])
def get_weather(request, city_name):
    # TODO: Add code (that works) that will fidn the weather for the city with the city name
    # If the city is invalid (or no weather can be found) return the appropriate response code and response message
    return Response(status=status.HTTP_200_OK, data=f'Sunny in {city_name}')
