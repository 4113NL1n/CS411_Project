import sqlite3
import os
from dotenv import load_dotenv



DB_PATH = os.getenv("DB_PATH")

def get_db_connection():
    """
    Establish a connection to the SQLite database.

    Returns:
        sqlite3.Connection: A connection object to the SQLite database.

    Raises:
        sqlite3.Error: If there is an issue connecting to the database.
    """
    return sqlite3.connect("DB_PATH")

def initialize_database():
    """
    Initialize the SQLite database by executing the schema creation script.

    Reads the SQL script file specified in `sql/create_user_table.sql` and
    executes its contents to set up the required database tables.

    Raises:
        FileNotFoundError: If the SQL file does not exist.
        sqlite3.Error: If there is an issue executing the SQL script.
    """
    with get_db_connection() as conn:
        with open("sql/create_user_table.sql", "r") as f:
            conn.executescript(f.read())