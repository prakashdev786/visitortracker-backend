import os
from datetime import timedelta

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
     # jwt configuration
    SECRET_KEY =  os.getenv('SECRET_KEY') or 'default-secret-key'
    JWT_SECRET_KEY =  SECRET_KEY
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=1)
    JWT_REFRESH_TOKEN_EXPIRES =  timedelta(days=7)

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SERVER_NAME = os.getenv("SERVER_NAME")
    SQLALCHEMY_DATABASE_URI = os.getenv("DEVELOPMENT_DATABASE_URL")
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'prakash950288@gmail.com'  
    MAIL_PASSWORD = os.getenv('MAILPASS')

class TestingConfig(Config):
    TESTING = True
    SERVER_NAME = os.getenv("SERVER_NAME")
    SQLALCHEMY_DATABASE_URI = os.getenv("TEST_DATABASE_URL")

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SERVER_NAME = os.getenv("SERVER_NAME")
    SQLALCHEMY_DATABASE_URI = os.getenv("STAGING_DATABASE_URL")
    
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.getenv("PRODUCTION_DATABASE_URL")
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=12) 

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig
}

