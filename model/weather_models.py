from api.weather_api import search_weather,search_forecastt,search_alert,search_air_quality
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, Response, request
load_dotenv()
app = Flask(__name__)
fave = []

@app.route('/weather/favorite', methods=['GET'])
def get_weather_fave():
    return jsonify(fave)

@app.route('/weather/<city>', methods=['GET'])
def get_weather(city):
    data = search_weather(city)
    return jsonify(data)

@app.route('/weather/forecast/<city>', methods=['GET'])
def get_forecast(city):
    data = search_forecastt(city)  
    return jsonify(data)

@app.route('/weather/air/<city>/<state_code>/<country_code>', methods=['GET']) 
def get_air(city,state_code,country_code):
    data = search_air_quality(city,state_code,country_code)  
    return jsonify(data)

@app.route('/weather/alerts/<state_code>', methods=['GET'])
def get_alerts(state_code):
    return jsonify(search_alert(state_code))

@app.route('/weather/favorite/save/<city>', methods=['PUT'])
def save_favorite(city):
    fave.append(city)


