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
# third api call
def get_geoCode(city_name,state_code,country_code,limit,API_key):
    response = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&limit={limit}&appid={API_key}").json()
    lat = response[0].get("lat")
    lon = response[0].get("lon")
    return lat,lon

#fourth call
def get_air_quality(name,sCode,cCode,API_key):
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

# def get_weather_map(layer,API_key):
#     z = 1
#     x = 200
#     y = 200
#     response = requests.get(f"https://tile.openweathermap.org/map/{layer}/{z}/{x}/{y}.png?appid={API_key}")
#     print(response.status_code)
#     img = Image.open(BytesIO(response.content))
#     root = Tk()
#     root.title("Image Popup")
#     image_tk = ImageTk.PhotoImage(img)

#     # Create a label widget to display the image
#     label = Label(root, image=image_tk)
#     label.pack()

#     # Start the Tkinter main loop to display the popup
#     root.mainloop()

def get_past_weather(sCode):
    response = requests.get(f"https://api.weather.gov/alerts/active?area={sCode}").json()
    print(response)
def search_weather(city):
    return get_weather(city, api_key)

def search_forecastt(city):
    return get_weather_forecast(city,api_key)

if __name__ == "__main__":
    get_past_weather("NY")