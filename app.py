from utils.sql_utils import execute_script,get_db_connection,check_database_connection,check_table_exists
from models.user_models import create_user
from api.weather_api import search_weather,search_forecastt,search_alert,search_air_quality
import sqlite3
from dotenv import load_dotenv
from flask import Flask, jsonify, make_response, Response, request
from dataclasses import dataclass
load_dotenv()

app = Flask(__name__)

list = []

@app.route('/api/health', methods=['GET'])
def healthcheck() -> Response:
    """
    Health check route to verify the service is running.

    Returns:
        JSON response indicating the health status of the service.
    """
    app.logger.info('Health check')
    return make_response(jsonify({'status': 'healthy'}), 200)

@app.route('/api/db-check', methods=['GET'])
def db_check() -> Response:
    try:
        execute_script()
        app.logger.info("Checking database connection...")
        check_database_connection()
        app.logger.info("Database connection is OK.")
        app.logger.info("Checking if meals table exists...")
        check_table_exists("meals")
        app.logger.info("meals table exists.")
        return make_response(jsonify({'database_status': 'healthy'}), 200)
    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 404)

def get_user():
    try:
        sql_query = "SELECT * FROM user;"
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql_query)
            users = cursor.fetchall()
        for user in users:
            print(user) 
    except Exception as e:
        raise e

def create_acc(username, passw):
    if create_user(username,passw):
        print("Account success")
    else: 
        print("Account username taken")
