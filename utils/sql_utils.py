from contextlib import contextmanager
import os
import sqlite3

DB_PATH = os.getenv("DB_PATH", "sql/user.db")

SQL_CREATE_TABLE_PATH = os.getenv("SQL_CREATE_TABLE_PATH", "sql/create_user_table.sql")


def execute_script():
    if not os.path.exists(SQL_CREATE_TABLE_PATH):
        raise FileNotFoundError(f"SQL script not found: {SQL_CREATE_TABLE_PATH}")
    try:
        with open(SQL_CREATE_TABLE_PATH, "r") as script_file:
            sql_script = script_file.read()
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.executescript(sql_script)
            conn.commit()
    except sqlite3.Error as e:
        raise e

@contextmanager
def get_db_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH)
        yield conn
    except sqlite3.Error as e:
        raise e
    finally:
        if conn:
            conn.close()