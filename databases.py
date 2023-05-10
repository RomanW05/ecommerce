# In this section we create the databases necessarly and their schemas to operate the store

from sqlalchemy import create_engine
import psycopg2
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

username = os.getenv('postgres_username')
password = os.getenv('postgres_password')
host = os.getenv('postgres_host')
port = os.getenv('postgres_port')
DATABASE_URI = f'postgresql://{username}:{password}@{host}:{port}/inventory'

