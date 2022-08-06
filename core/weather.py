import datetime as dt 
import requests 
import json

BASE_URL= "http://api.openweathermap.org/geo/1.0/reverse?lat={}&lon={}&limit=5&appid={}"
API_KEY = 'e1251f4b3ec66f597745dea88f953ebd'

def get_city_name(lat:float, lon:float, apikey=API_KEY):
    url = BASE_URL.format(lat, lon, apikey)
    response = requests.get(url).json()
    return response[0]['name']

def kelvin_to_celsius(kelvin):
    celsius = kelvin - 273.15
    farenheit = celsius * (9/5) + 32
    return int(celsius), int(farenheit)

def get_weather_info(lat:float, lon:float, apikey=API_KEY):
    city = get_city_name(lat, lon, apikey)
    url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, apikey)
    response = requests.get(url).json()

    temp_kelvin = int(response['main']['temp'])
    temp_celsius, temp_farenheit  = kelvin_to_celsius(temp_kelvin)
    humidity = response['main']['humidity']
    description = response['weather'][0]['description']
    sunrise_time = dt.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
    sunset_time = dt.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])
    wind_speed = response['wind']['speed']

    print(temp_kelvin, temp_celsius, temp_farenheit)
    print(humidity)
    print(description)
    print(sunrise_time)
    print(sunset_time)
    print(wind_speed)
    

