import os
import mysql.connector
from dotenv import load_dotenv

J_HOST = "127.0.0.1"
J_PORT = "3306"
J_USER = "root"
J_PASSWORD = ""
J_NAME = "yugiohdb"

def start():
    load_dotenv()
    print(list_table())
    return list_table()

def get_db():
    connection = mysql.connector.connect(
        host=J_HOST,
        port=J_PORT,
        user=J_USER,
        password=J_PASSWORD,
        database=J_NAME
    )
    return connection

def list_table():
    connection = get_db()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM archetype;")
    rows = cursor.fetchall()
    cursor.close()
    connection.close()
    return rows