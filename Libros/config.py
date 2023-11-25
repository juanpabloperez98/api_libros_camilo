# config.py
from dotenv import load_dotenv
import os

load_dotenv()

# config.py
class Config:
    SECRET_KEY = '[Gv6I24i<FjR'
    DB_PASSWORD = os.environ.get('DB_PASSWORD')
    SQLALCHEMY_DATABASE_URI = f'postgresql://postgres:{DB_PASSWORD}@localhost/libros'
    SQLALCHEMY_TRACK_MODIFICATIONS = False