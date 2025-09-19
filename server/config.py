"""Flask config."""
from os import environ, path
from pydantic_settings import BaseSettings
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Settings(BaseSettings):  
    SQLALCHEMY_DATABASE_URI: str = environ.get("LOCAL_DB_URI")
settings = Settings()