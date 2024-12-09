from utils.sql_utils import execute_script, check_database_connection, check_table_exists
from model.user_model import create_user, log_in, update_pass
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, request, Response
import logging

load_dotenv()
app = Flask(__name__)

# Setting up logging
logging.basicConfig(level=logging.INFO)

@app.route('/health', methods=['GET'])
def healthcheck() -> Response:
    app.logger.info('Health check')
    return make_response(jsonify({'status': 'healthy'}), 200)

@app.route('/db-check', methods=['GET'])
def db_check() -> Response:
    try:
        execute_script()
        app.logger.info("Checking database connection...")
        check_database_connection()
        app.logger.info("Database connection is OK.")
        app.logger.info("Checking if meals table exists...")
        check_table_exists("meals")
        app.logger.info("Meals table exists.")
        return make_response(jsonify({'database_status': 'healthy'}), 200)
    except Exception as e:
        app.logger.error(f"Error: {str(e)}")
        return make_response(jsonify({'error': str(e)}), 404)

@app.route('/app/create', methods=['POST'])
def create_acc():
    data = request.get_json()
    username = data.get('username')
    passw = data.get('password')
    if create_user(username, passw):
        app.logger.info("Account Created")
        return jsonify({"message": "Account created"}), 201
    else: 
        app.logger.warning("Username already taken")
        return jsonify({"message": "Account username taken"}), 400

@app.route('/app/login', methods=['POST'])
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

@app.route('/app/password', methods=['PUT'])
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

if __name__ == "__main__":
    execute_script()  # Execute the database setup script
    app.run(debug=True)