from psycopg2 import connect
from dotenv import load_dotenv
import os

from psycopg2._psycopg import connection

load_dotenv()

def get_connection() -> connection:

   conn: connection = connect(
      host = os.getenv("DB_HOST"),
      port = os.getenv("DB_PORT"),
      dbname = os.getenv("DB_NAME"),
      user = os.getenv("DB_USER"),
      password = os.getenv("DB_PASSWORD"),
   )

   return conn