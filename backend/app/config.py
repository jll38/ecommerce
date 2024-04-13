import os
from dotenv import load_dotenv

load_dotenv()

DATABASE = {
    'dialect': 'postgresql',
    'driver': 'psycopg2',
    'username': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'host': os.getenv('POSTGRES_HOST'),
    'port': '5432',  # default port for PostgreSQL
    'database': os.getenv('POSTGRES_DB'),
}
