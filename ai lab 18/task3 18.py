import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise an error for bad HTTP status codes
        weather_data = response.json()

        # Check if API returned a valid response
        if weather_data.get("cod") != 200:
            print(f"❌ Error: {weather_data.get('message', 'Unable to fetch weather data.')}")
            return

        # Extract and display useful information
        city = weather_data["name"]
        country = weather_data["sys"]["country"]
        temp = weather_data["main"]["temp"]
        feels_like = weather_data["main"]["feels_like"]
        humidity = weather_data["main"]["humidity"]
        weather_desc = weather_data["weather"][0]["description"].title()
        wind_speed = weather_data["wind"]["speed"]

        print(f"\n🌤️  Weather in {city}, {country}")
        print("-" * 40)
        print(f"🌡️  Temperature     : {temp}°C (feels like {feels_like}°C)")
        print(f"💧 Humidity        : {humidity}%")
        print(f"🌬️  Wind Speed      : {wind_speed} m/s")
        print(f"☁️  Condition       : {weather_desc}")
        print("-" * 40)

    except requests.exceptions.HTTPError as http_err:
        print(f"⚠️  HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError:
        print("❌ Connection error: Unable to reach the weather service.")
    except requests.exceptions.Timeout:
        print("⏱️  Timeout error: The request took too long to respond.")
    except requests.exceptions.RequestException as e:
        print(f"❗ An unexpected error occurred: {e}")

# Example usage:
# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
get_weather("London", "dcbc2131855f54ce74f1caefa8239f2f")
