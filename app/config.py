import os
from dotenv import load_dotenv

load_dotenv()  # load environment variables from .env if it exists.


class Config(object):
    """Base Config Object"""
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    UPLOAD_FOLDER = os.environ.get('UPLOAD_FOLDER')
    SECRET_KEY = os.getenv('SECRET_KEY')
