import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True

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
    SERVER_NAME = os.getenv("SERVER_NAME")
    SQLALCHEMY_DATABASE_URI = os.getenv("PRODUCTION_DATABASE_URL")

config = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "staging": StagingConfig,
    "production": ProductionConfig
}

