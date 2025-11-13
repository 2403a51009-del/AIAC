import requests
import json

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }
    
    response = requests.get(base_url, params=params)
    weather_data = response.json()
    
    # Display JSON output
    print(json.dumps(weather_data, indent=4))

# Example usage:
# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
get_weather("London", "dcbc2131855f54ce74f1caefa8239f2f")


