import requests
from dotenv import load_dotenv
import os
import json 
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')
@dataclass
class info:
    main : str 
    location : str
    high : float 
    curr : float
    low : float 

# Call api and return weather condition, location, temp, high temp, low temp
# first api call
def get_weather(city_name,API_key):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=imperial").json()
    print(response)
    data = info(
        main = response.get("weather")[0].get("main"),
        location = response.get("name"),
        high = response.get("main").get("temp_max"),
        curr = response.get("main").get("temp"),
        low = response.get("main").get("temp")
    )
    return data
#second api call for the next 4  days
def get_weather_forecast(city_name,API_key):
    forecast = []
    response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}&units=imperial").json()
    for i in range(1,6):
        data = info(
            main = response.get("list")[i*9].get("weather")[0].get("main"),
            location = response.get("city").get("name"),
            high = response.get("list")[i*9].get("main").get("temp_max"),
            curr = response.get("list")[i*9].get("main").get("temp"),
            low = response.get("list")[i*9].get("main").get("temp_min")
            )
        forecast.append(data)
    return forecast

def search_weather(city):
    return get_weather(city, api_key)

if __name__ == "__main__":
    get_weather_forecast("boston",api_key)
