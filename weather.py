import requests
from dotenv import load_dotenv
import os
import json 
api_key = os.getenv('API_KEY')
 
def get_weather(city_name,API_key):
    response = json.loads (requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}").json())
    print(response)
get_weather("nEW yORK", api_key)