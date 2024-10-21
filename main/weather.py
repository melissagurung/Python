import requests

def get_weather(city):
    api_key = "957c45aa7618cf31a9c594f01d22dd3a"  # Your [OpenWeatherMap](http://api.openweathermap.org/data/2.5/weather) API key
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    # Construct the full API URL
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    
    # Make the request to the API
    response = requests.get(base_url, params=params)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        weather_description = data['weather'][0]['description']
        return temp, weather_description
    else:
        return None, "Failed to retrieve data. Please check your API key and city name."

# Get weather for Kathmandu
temperature, description = get_weather("Kathmandu")
if temperature is not None:
    print(f"Temperature: {temperature}°C")
    print(f"Weather: {description}")
else:
    print(description)