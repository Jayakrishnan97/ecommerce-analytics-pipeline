import psycopg2
from config.config import DB_CONFIG
import logging


def get_db_connection():

    return psycopg2.connect(
        host = DB_CONFIG["host"],
        port = DB_CONFIG["port"],
        dbname = DB_CONFIG["db_name"],
        user = DB_CONFIG["user"],
        password = DB_CONFIG["password"]
    )

file_path = "/home/jay/Python_DSA/python/projects/E_commerce_Analytics_Pipeline/sql/create_table.sql"

with open(file_path, "r") as file:
    schema = file.read()


def create_tables():
    conn = None
    cursor = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        schema_query = schema

        cursor.execute(schema_query)
        conn.commit()

        logging.info("created tables successfully")
    
    except Exception as e:
        if conn:
            conn.rollback()
            logging.error(f"message: {e}", exc_info=True)
            raise
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


create_tables()