import requests
import json
import os
from datetime import datetime

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city_name,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raise error for bad HTTP codes
        weather_data = response.json()

        # Check if API returned a valid response
        if weather_data.get("cod") != 200:
            error_output = {
                "error": weather_data.get("message", "Unable to fetch weather data."),
                "city": city_name,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            print(json.dumps(error_output, indent=4))
            output_text = json.dumps(error_output, indent=4)
        else:
            # Add timestamp for record keeping
            weather_data["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(json.dumps(weather_data, indent=4))
            output_text = json.dumps(weather_data, indent=4)

        # Save (append) to a text file
        file_path = os.path.join(os.getcwd(), "weather_log.txt")
        with open(file_path, "a", encoding="utf-8") as file:
            file.write(output_text + "\n\n")

    except requests.exceptions.HTTPError as http_err:
        error_output = {
            "error": "HTTP error occurred",
            "details": str(http_err),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(json.dumps(error_output, indent=4))
        with open("weather_log.txt", "a", encoding="utf-8") as file:
            file.write(json.dumps(error_output, indent=4) + "\n\n")

    except requests.exceptions.ConnectionError:
        error_output = {
            "error": "Connection error occurred",
            "details": "Unable to connect to the weather service",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(json.dumps(error_output, indent=4))
        with open("weather_log.txt", "a", encoding="utf-8") as file:
            file.write(json.dumps(error_output, indent=4) + "\n\n")

    except requests.exceptions.Timeout:
        error_output = {
            "error": "Request timed out",
            "details": "The weather API did not respond in time",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(json.dumps(error_output, indent=4))
        with open("weather_log.txt", "a", encoding="utf-8") as file:
            file.write(json.dumps(error_output, indent=4) + "\n\n")

    except requests.exceptions.RequestException as e:
        error_output = {
            "error": "An unexpected error occurred",
            "details": str(e),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        print(json.dumps(error_output, indent=4))
        with open("weather_log.txt", "a", encoding="utf-8") as file:
            file.write(json.dumps(error_output, indent=4) + "\n\n")

# Example usage:
# Replace 'YOUR_API_KEY' with your actual OpenWeatherMap API key
get_weather("america", "dcbc2131855f54ce74f1caefa8239f2f")
