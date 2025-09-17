import requests
import os
import json

def get_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    #print (url)
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200:

        #print(json.dumps(data, indent=4))


        # Get temperature from the 'main' key, and convert from Kelvin to Celsius
        # The temperature key in OpenWeatherMap is 'temp'
        temperature_kelvin = data['main']['temp']
        temperature_celsius = temperature_kelvin - 273.15
        
        # Get condition from the 'weather' key, which is a list
        # We access the first item [0] and then the 'description'
        condition = data['weather'][0]['description']
        
        # Format the output with the new variables
        return f"Current temperature in {city} is {temperature_celsius:.2f}°C, Condition: {condition}"

    else:
        return "Failed to fetch weather data"

api_key = os.getenv('API_TOKEN')
city = 'Tel Aviv'
print(get_weather(api_key, city))
