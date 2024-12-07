from utils.sql_utils import execute_script,get_db_connection
from models.user_models import create_user
from weather import search_weather
import sqlite3
def create_db():
    print("Starting the script...")
    try:
        execute_script()
        print("Database table created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")

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

def get_weather(city):
    data = search_weather(city)
    print(data)
    
if __name__ == "__main__":
    get_weather("Boston")
