import pydash
import requests
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def get_timpul(request, city_name):
    return Response(status=status.HTTP_200_OK, data=f'sunny in {city_name}')
