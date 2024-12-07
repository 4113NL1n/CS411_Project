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
    
def get_weather(city_name,API_key):
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}").json()
    data = info(
        main = response.get("weather")[0].get("main"),
        location = response.get("sys").get("country"),
        high = response.get("main").get("temp_max"),
        curr = response.get("main").get("temp"),
        low = response.get("main").get("temp")
    )
