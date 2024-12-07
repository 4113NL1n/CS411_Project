from utils.sql_utils import execute_script,get_db_connection
def main():
    print("Starting the script...")  # Make sure the function is called
    try:
        execute_script()
        print("Database table created successfully.")
    except Exception as e:
        print(f"Error creating table: {e}")
    insert_data("Allen Lin","rrwerw","fewuefuw")
    sql_query = "SELECT * FROM user;"
    with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(sql_query)
            users = cursor.fetchall()
    for user in users:
            print(user) 
            
def insert_data(username, passw,salt):
    sql_insert_query = """
        INSERT INTO user (username, pass, salt)
        VALUES (?, ?, ?);
        """
    with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute(sql_insert_query, (username, passw, salt))
                conn.commit() 
if __name__ == "__main__":
    main()