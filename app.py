from utils.sql_utils import execute_script,check_database_connection,check_table_exists
from model.user_model import create_user,log_in,update_pass
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
    

@app.route('/app/<username>/<passw>', methods=['POST'])
def create_acc(username, passw):
    if create_user(username,passw):
        app.logger.info("Account Created")
    else: 
        app.logger.info("Account Username taken")

@app.route('/app/<username>/<passw>', methods=['GET'])
def log_in(username,passw):
    if(log_in(username,passw)):
        app.logger.info("logged in")
    else:
        app.logger.info("Unable to log in, password and username wrong")

@app.route('/app/<username>/<old_passw>/<new_passw>', methods=['PUT'])
def update_pass(username,old_passw,new_passw):
    if(log_in(username,old_passw)):
        app.logger.info("attemping to change password")
        update_pass(username,old_passw,new_passw)
        app.logger.info("Successfully changed password")
    else:
        app.logger.info("Unable to log in, password and username wrong")
        

if __name__ == "__main__":
    execute_script()


    