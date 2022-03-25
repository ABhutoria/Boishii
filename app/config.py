from os import environ, path
from dotenv import load_dotenv

baseDirectory = path.abspath(path.dirname(__file__))
load_dotenv(path.join(baseDirectory, '.env'))

class Config:
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SECRET_KEY = environ.get('SECRET_KEY')

    # Change once ready for production
    DEBUG = True
    TESTING = True

    SQLALCHEMY_DATABASE_URI =  environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    
