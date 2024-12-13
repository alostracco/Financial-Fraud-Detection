import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

def get_db_connection():
    user = os.getenv('DB_USER')
    password = os.getenv('DB_PASSWORD')
    host = os.getenv('DB_HOST')
    port = os.getenv('DB_PORT', '5432')
    dbname = os.getenv('DB_NAME')
    
    return create_engine(f'postgresql://{user}:{password}@{host}:{port}/{dbname}')
