# flake8: noqa
# Use https://hackersandslackers.com/configure-flask-applications/

from dotenv import load_dotenv
import os

load_dotenv()

# TODO: Look into how to set up flask env
class Config:
    pass
    # General Config

    # SECRET_KEY = os.getenv('SECRET_KEY')
    # SESSION_COOKIE_NAME = os.getenv('SESSION_COOKIE_NAME')

    # # Database
    # SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    # SQLALCHEMY_USERNAME = os.getenv('SQLALCHEMY_USERNAME')
    # SQLALCHEMY_PASSWORD = os.getenv('SQLALCHEMY_PASSWORD')
    # SQLALCHEMY_DATABASE_NAME = os.getenv('SQLALCHEMY_DATABASE_NAME')
    # SQLALCHEMY_TABLE = os.getenv('SQLALCHEMY_TABLE')
    # SQLALCHEMY_DB_SCHEMA = os.getenv('SQLALCHEMY_DB_SCHEMA')
    # SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS')


class ProdConfig(Config):
    DEBUG = False
    FLASK_ENV = 'production'

    # AWS
    # AWS_SECRET_KEY = os.getenv('AWS_SECRET_KEY')
    # AWS_KEY_ID = os.getenv('AWS_KEY_ID')

    # # My API
    # API_ENDPOINT = os.getenv('API_ENDPOINT')
    # API_ACCESS_TOKEN = os.getenv('API_ACCESS_TOKEN')
    # API_CLIENT_ID = os.getenv('API_CLIENT_ID')


class DevConfig(Config):
    DEBUG = True
    FLASK_ENV = 'development'
