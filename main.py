import WeatherAPI

api_key = "TM7MBVREX98R2H5JF9XA2TQW9"  # Coloca aquí tu clave de API
weather_api = WeatherAPI.GetWeather(api_key)

if __name__ == "__main__":
    
    current_uv_index = weather_api.get_current_uv_index()
    print("Current UV Index:", current_uv_index)