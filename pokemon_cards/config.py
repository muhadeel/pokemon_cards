import os

from dotenv import load_dotenv

load_dotenv()


def get_db_connection_string() -> str:
    """
    Returns a MySQL db connection string.

    :return:
    """
    db_name = os.environ.get('DATABASE_NAME')
    db_host = os.environ.get('DATABASE_HOST')
    db_username = os.environ.get('DATABASE_USER')
    db_port = os.environ.get('DATABASE_PORT') or '3306'
    db_password = os.environ.get('DATABASE_PASSWORD')
    db_connection_string: str = f"mysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"
    return db_connection_string


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = get_db_connection_string()
    SQLALCHEMY_TRACK_MODIFICATIONS = False
