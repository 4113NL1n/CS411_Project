import requests
from dotenv import load_dotenv
import os
import json 
from dataclasses import dataclass
from PIL import Image,ImageTk
from io import BytesIO
from tkinter import Tk, Label


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
def fetch_weather(city_name,API_key):
    """
    Fetch the current weather for a given city.

    Args:
        city_name (str): The name of the city.
        API_key (str): The OpenWeatherMap API key.

    Returns:
        info: An instance of the `info` dataclass containing weather details.
    """
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units=imperial").json()
    data = info(
        main = response.get("weather")[0].get("main"),
        location = response.get("name"),
        high = response.get("main").get("temp_max"),
        curr = response.get("main").get("temp"),
        low = response.get("main").get("temp")
    )
    return data

def search_weather(city):
    """
    Search and fetch the current weather for a city.

    Args:
        city (str): The name of the city.

    Returns:
        info: An instance of the `info` dataclass containing weather details.
    """
    return fetch_weather(city, api_key)

#second api call for the next 4  days
def get_weather_forecast(city_name, API_key):
    response = requests.get(
        f"https://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}&units=imperial"
    ).json()

    # Check for errors in the API response
    if "list" not in response:
        raise ValueError(f"Invalid response from API: {response}")

    forecast = []
    for i in range(0, 5):
        try:
            forecast.append({
                "main": response["list"][i * 9]["weather"][0]["main"],
                "location": response["city"]["name"],
                "high": response["list"][i * 9]["main"]["temp_max"],
                "curr": response["list"][i * 9]["main"]["temp"],
                "low": response["list"][i * 9]["main"]["temp_min"],
            })
        except (IndexError, KeyError) as e:
            raise ValueError(f"Error processing forecast data: {e}")
    return forecast

def search_forecastt(city):
    """
    Search and fetch the 5-day weather forecast for a city.

    Args:
        city (str): The name of the city.

    Returns:
        list: A list of `info` dataclass instances containing weather forecast details.
    """
    return get_weather_forecast(city,api_key)

# third api call
def get_geoCode(city_name,state_code,country_code,limit,API_key):
    """
    Fetch the latitude and longitude for a specified location.

    Args:
        city_name (str): The name of the city.
        state_code (str): The state code.
        country_code (str): The country code.
        limit (int): Maximum number of results to return.
        API_key (str): The OpenWeatherMap API key.

    Returns:
        tuple: A tuple containing latitude and longitude (lat, lon).
    """
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_key}").json()
    lat = response[0].get("lat")
    lon = response[0].get("lon")
    return lat,lon

#fourth call
def get_air_quality(name,sCode,cCode,API_key):
    """
    Fetch air quality information for a location.

    Args:
        name (str): The city name.
        sCode (str): The state code.
        cCode (str): The country code.
        API_key (str): The OpenWeatherMap API key.

    Returns:
        bool: True if the air quality is good, False otherwise.
    """
    lat, lon = get_geoCode(name,sCode,cCode,5,API_key)
    response = requests.get(f"http://api.openweathermap.org/data/2.5/air_pollution?lat={lat}&lon={lon}&appid={API_key}").json()
    quality = response.get("list")[0].get("components")
    if (quality.get("co") < 12400 and 
        quality.get("o3") < 140 and 
        quality.get("no2") < 150 and 
        quality.get("so2") < 250 and 
        quality.get("pm10") < 100 and 
        quality.get("pm2_5") < 50):
        return True
    else:
        return False    

def search_air_quality(name,sCode,cCode):
    """
    Search and fetch air quality information for a location.

    Args:
        name (str): The city name.
        sCode (str): The state code.
        cCode (str): The country code.

    Returns:
        bool: True if the air quality is good, False otherwise.
    """
    return get_air_quality(name,sCode,cCode,api_key)

def get_alerts(sCode):
    """
    Fetch weather alerts for a specific state.

    Args:
        sCode (str): The state code.

    Returns:
        str: A weather alert description if present, otherwise "No Alerts".
    """
    response = requests.get(f"https://api.weather.gov/alerts/active/?area={sCode}").json()
    if len(response.get("features")) != 0:
        return response.get("features")[0].get("properties").get("description")
    return "No Alerts"    

def search_alert(sCode):
    """
    Search and fetch weather alerts for a specific state.

    Args:
        sCode (str): The state code.

    Returns:
        str: A weather alert description if present, otherwise "No Alerts".
    """
    return get_alerts(sCode)
