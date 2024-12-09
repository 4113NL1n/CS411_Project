from api.weather_api import search_weather,search_forecastt,search_alert,search_air_quality
from model.user_model import create_user, log_in, update_pass
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, request, Response
import logging


load_dotenv()
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "weather app"

@app.route('/healt', methods=['GET'])
def healthcheck() -> Response:
    app.logger.info('Health check')
    return make_response(jsonify({'status': 'healthy'}), 200)

@app.route('/create', methods=['POST'])
def create_acc():
    data = request.json
    app.logger.info(f"Received data: {data}")  # Add this log to verify it’s being triggered
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        app.logger.warning("Username or password missing")  # Log a warning if one is missing
        return jsonify({"error": "Username and password are required."}), 400
    try:
        create_user(username, password)
        app.logger.info("Account created successfully.")  # Add this log
        return jsonify({"message": "Account created successfully."}), 201
    except ValueError as e:
        app.logger.error(f"Error: {str(e)}")  # Log error if there is a ValueError
        return jsonify({"error": str(e)}), 400
    
@app.route('/login', methods=['GET'])
def log_in_route():
    data = request.get_json()
    username = data.get('username')
    passw = data.get('password')
    if log_in(username, passw):
        app.logger.info("Logged in successfully")
        return jsonify({"message": "Logged in"}), 200
    else:
        app.logger.warning("Unable to log in, invalid credentials")
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/password', methods=['PUT'])
def update_pass_route():
    data = request.get_json()
    username = data.get('username')
    old_passw = data.get('old_password')
    new_passw = data.get('new_password')
    if log_in(username, old_passw):
        update_pass(username, old_passw, new_passw)
        app.logger.info("Password updated successfully")
        return jsonify({"message": "Password updated successfully"}), 200
    else:
        app.logger.warning("Unable to log in, invalid credentials")
        return jsonify({"message": "Invalid credentials"}), 401
fave = {}

@app.route('/weather/favorite', methods=['GET'])
def get_weather_fave() -> Response:
    return jsonify(fave)

@app.route("/weather/<city>", methods=['GET'])
def get_weather_route(city) -> Response:
    try:
        data = search_weather(city)
        if data:
            print(f"Weather data for {city}: {data}")
            return make_response(jsonify(data), 200)
        else:
            return jsonify({"error": "No data found"}), 404
    except Exception as e:
        app.logger.error(f"Error fetching weather: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route('/weather/forecast/<city>', methods=['GET'])
def get_forecast(city) -> Response:
    data = search_forecastt(city)  
    return jsonify(data)

@app.route('/weather/air/<city>/<state_code>/<country_code>', methods=['GET']) 
def get_air(city,state_code,country_code) -> Response:
    data = search_air_quality(city,state_code,country_code)  
    return jsonify(data)

@app.route('/weather/alerts/<state_code>', methods=['GET'])
def get_alerts(state_code) -> Response:
    return jsonify(search_alert(state_code))

@app.route('/weather/favorite/save/<city>', methods=['PUT'])
def save_favorite(city) -> Response:
    fave.append(city)

# @app.route('/health', methods=['GET'])
# def test() -> Response: 
#     return jsonify({"message": "Hello, world!"}), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
