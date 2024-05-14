import geocoder
import requests
import sys
import datetime

class GetWeather:
    def __init__(self, api_key):
        self.api_key = api_key
        self.url_beginning = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
        self.url_finish = "?unitGroup=metric&elements=datetime%2Cuvindex&include=stats%2Cstatsfcst%2Cfcst%2Cremote%2Cobs%2Chours&options=nonulls%2Cstnslevel1&contentType=json"

    def get_lat_lng(self):
        ip_address = geocoder.ip('me').ip
        location = geocoder.ip(ip_address)
        lat_lng = location.latlng
        return lat_lng

    def get_weather_data(self, lat, lng):
        url_full = f"{self.url_beginning}{lat}%2C{lng}{self.url_finish}&key={self.api_key}"
        response = requests.get(url_full)
        if response.status_code != 200:
            print('Unexpected Status code: ', response.status_code)
            sys.exit()
        return response.json()

    def get_current_uv_index(self):
        lat, lng = self.get_lat_lng()
        weather_data = self.get_weather_data(lat, lng)
        now = datetime.datetime.now()
        actual_uv_index = weather_data["days"][0]["hours"][now.hour]["uvindex"]
        data=datos = {
            "Time":now.strftime("%Y-%m-%d %H:%M:%S"),
            "Location": {"lat":lat,"lng":lng},
            "UVIndex":actual_uv_index
        }
        return datos

