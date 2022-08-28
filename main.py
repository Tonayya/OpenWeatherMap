import datetime as dt
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()   #Please enter your API key in the text file
LATITUDE = ""    #Please add the latitude number within the double quotes
LONGITUDE = ""      #Please add the longitude number within the double quotes


def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius


url = BASE_URL + "lat=" + LATITUDE + "&lon=" + LONGITUDE + "&appid=" + API_KEY

response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celsius = kelvin_to_celsius(temp_kelvin)
temp_min_kelvin = response['main']['temp_min']
temp_min_celsius = kelvin_to_celsius(temp_min_kelvin)
temp_max_kelvin = response['main']['temp_max']
temp_max_celsius = kelvin_to_celsius(temp_max_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])  #added timezone to get the local time
sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temperature at co-ordinates {LATITUDE}°,{LONGITUDE}°: {temp_celsius:.2f}°C")
print(f"Minimum temperature: {temp_min_celsius}°C")
print(f"Maximum temperature: {temp_max_celsius}°C")
print(f"Wind speed: {wind_speed}")
print(f"Humidity level: {humidity}")
print(f"Description: {description}")
print(f"Sunrise time: {sunrise_time}")
print(f"Sunset time: {sunset_time}")
