import geocoder
import requests
import sys
import json
import datetime

urlBegining="https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
urlFinish="?unitGroup=metric&elements=datetime%2Cuvindex&include=stats%2Cstatsfcst%2Cfcst%2Cremote%2Cobs%2Chours&key=TM7MBVREX98R2H5JF9XA2TQW9&options=nonulls%2Cstnslevel1&contentType=json"
urlFull=""
now = datetime.datetime.now()
actualUVindex=0


def get_lat_lng():
    # Get the IP address of the user
    ip_address = geocoder.ip('me').ip
    # Use geocoder to get the location information
    location = geocoder.ip(ip_address)
    # Extract latitude and longitude
    lat_lng = location.latlng
    return lat_lng

if __name__ == "__main__":
    lat_lng = get_lat_lng()
    print("Latitude:", lat_lng[0])
    print("Longitude:", lat_lng[1])

urlFull=str(urlBegining+str(lat_lng[0])+"%2C"+str(lat_lng[1])+urlFinish)
print(urlFull)
response = requests.request("GET",urlFull)
if response.status_code!=200:
    print('Unexpected Status code: ', response.status_code)
    sys.exit()  

# Parse the results as JSON
jsonData = response.json()
actualUVindex=jsonData["days"][0]["hours"][now.hour]["uvindex"]
print(actualUVindex)