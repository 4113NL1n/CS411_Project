from api.weather_api import search_weather,search_forecastt,search_alert,search_air_quality
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, Response, request
load_dotenv()
app = Flask(__name__)
@app.route('/weather', methods=['GET'])
def get_weather(city):
    data = search_weather(city)
    return data

@app.route('/weather', methods=['GET'])
def get_forecast(city):
    data = search_forecastt(city)  
    return data

@app.route('/weather', methods=['GET'])
def get_air(city,state_code,country_code):
    data = search_air_quality(city,state_code,country_code)  
    return data

@app.route('/weather', methods=['GET'])
def get_alerts(state_code):
    return search_alert(state_code)

@app.route('/weather', methods=['PUT'])
def save_favorite(name):
    list.append(name)
    
@app.route('/weather', methods=['GET'])
def get_weather_fave():
    retList = []
    for i in list:
        retList.append(search_weather(i))
    return retList
