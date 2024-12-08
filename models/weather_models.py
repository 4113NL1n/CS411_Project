from api.weather_api import search_weather,search_forecastt,search_alert,search_air_quality
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, Response, request
load_dotenv()
app = Flask(__name__)

def __init__(self):
    self.weathers = []

    @app.route('/weather', methods=['GET'])
    def get_weather_fave():
        for i in list:
            self.weathers.append(search_weather(i))
        return jsonify(self.weathers)
    
    @app.route('/weather/<city>', methods=['GET'])
    def get_weather(city):
        data = search_weather(city)
        return jsonify(data)

    @app.route('/weather<city>', methods=['GET'])
    def get_forecast(city):
        data = search_forecastt(city)  
        return jsonify(data)

    @app.route('/weather/<city>/<state_code>/<country_code>', methods=['GET']) 
    def get_air(city,state_code,country_code):
        data = search_air_quality(city,state_code,country_code)  
        return jsonify(data)

    @app.route('/weather/<city>', methods=['GET'])
    def get_alerts(state_code):
        return jsonify(search_alert(state_code))

    @app.route('/weather/<city>', methods=['PUT'])
    def save_favorite(name):
        list.append(name)
    
