import os
import time
import psycopg2
from psycopg2 import OperationalError

DB_HOST = os.getenv('DATABASE_HOST', 'db')
DB_NAME = os.getenv('DATABASE_NAME')
DB_USER = os.getenv('DATABASE_USER')
DB_PASS = os.getenv('DATABASE_PASSWORD')
DB_PORT = os.getenv('DATABASE_PORT', 5432)
TIMEOUT = 30  # Максимальное время ожидания (в секундах)

def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASS,
                host=DB_HOST,
                port=DB_PORT
            )
            conn.close()
            print("Database is ready!")
            break
        except OperationalError:
            print("Database unavailable, waiting 1 second...")
            time.sleep(1)

if __name__ == "__main__":
    wait_for_db()
