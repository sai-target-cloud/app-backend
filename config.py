import os

class Config:
    """Base configuration"""
    SECRET_KEY = os.getenv("SECRET_KEY", "mysecret")
    DB_PATH = os.getenv("DB_PATH", "app.db")
    DEBUG = False

class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False
    SECRET_KEY = os.getenv("SECRET_KEY")  # must be set in prod
