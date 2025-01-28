import pymysql
import pymysql.cursors
import os
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    try:
        connection = pymysql.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME"),
            port=int(os.getenv("DB_PORT", 3306)),
            cursorclass=pymysql.cursors.DictCursor
        )
        return connection
    except pymysql.MySQLError as err:
        print(f"❌ Error al conectar con la base de datos: {err}")
        return None
