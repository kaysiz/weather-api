from rest_framework.response import Response
from rest_framework.views import APIView
import requests


class WeatherView(APIView):
    """Get current weather"""

    def get(self, request, format=None):
        city = request.GET.get("city")
        url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=94a76e95e50491086a277ca150f7a6b4'
        city_weather = requests.get(
            url.format(city)).json()  # request the API data and convert the JSON to Python data types
        if city_weather['cod'] != '404':
            return Response(
                {
                    "min_temp": city_weather['main']['temp_min'], "max_temp": city_weather['main']['temp_max'],
                    "humidity": city_weather['main']['humidity']
                }
            )
        else:
            return Response({
                "message": city_weather['message']
            })
