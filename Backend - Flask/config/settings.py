import os



class Config:
    """Base configuration (default for all environments)"""
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", 'sqlite:///database.db')
    SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key")
    SQLALCHEMY_TRACK_MODIFICATIONS = False