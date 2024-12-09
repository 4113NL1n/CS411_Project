from dataclasses import dataclass
import logging
import os
import sqlite3
import bcrypt
from typing import Any
from utils.sql_utils import get_db_connection, initialize_database


initialize_database()

def check_user(username):
    try:
        sql_query = "SELECT 1 FROM user WHERE username = ? LIMIT 1" 
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql_query, (username,))
            result = cursor.fetchone()
        if result:
            print(f"Username '{username}' already exists in the database.")
            return False 
        else:
            print(f"Username '{username}' does not exist. You can create an account.")
            return True 
    except sqlite3.Error as e:
        print(f"Error checking username: {e}")
        raise e

def hash_password(password):
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password.decode('utf-8')  # Return hash as a string

def check_password(input_password, stored_hash):
    return bcrypt.checkpw(input_password.encode('utf-8'), stored_hash.encode('utf-8'))

def log_in(name, password):
    if not check_user(name):  # Check if user exists
        try:
            sql_query = "SELECT pass FROM user WHERE username = ? LIMIT 1;" 
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql_query, (name,))
                result = cursor.fetchone()
                if result:
                    stored_hash = result[0]  # Fetched hashed password
                    if check_password(password, stored_hash):
                        return True
                    else:
                        print("Invalid password.")
                        return False
                else:
                    print("User not found.")
                    return False
        except sqlite3.Error as e:
            print(f"Error checking username: {e}")
            raise e
    else:
        print("User does not exist.")
        return False
    
def create_user(name,password) -> None:
    hased_Pass = hash_password(password)
    try:
        sql_insert_query = """
        INSERT INTO user (username, pass)
        VALUES (?, ?);
        """
        with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql_insert_query, (name, hased_Pass))
                conn.commit() 
    except sqlite3.IntegrityError as e :
        raise ValueError(f"Username '{name}' is already taken.")
    



def update_pass(name,Old_pass,new_pass):
    if (not check_user(name)):
        try:
            sql_query = "SELECT pass FROM user WHERE username = ? LIMIT 1;" 
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql_query, (name,))
                result = cursor.fetchone()
                salt = result[0]
                if(check_password(Old_pass,salt)):
                    hashed = hash_password(new_pass)
                    update_query = "UPDATE user SET pass = ? WHERE username = ?;"
                    cursor.execute(update_query, (hashed, name))
                    conn.commit()
                    return True
                else:
                    return False
        except sqlite3.Error as e:
            print(f"Error checking username: {e}")
            raise e
    else:   
        return False