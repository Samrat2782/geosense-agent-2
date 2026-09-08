import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL


load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")


def get_database_url():
    return URL.create(
        drivername="postgresql+psycopg2",
        username=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=int(DB_PORT),
        database=DB_NAME,
    )


def get_engine():
    return create_engine(get_database_url())


if __name__ == "__main__":
    engine = get_engine()

    try:
        with engine.connect() as connection:
            print("GeoSense PostgreSQL connection: OK")
    except Exception as e:
        print("GeoSense PostgreSQL connection: FAILED")
        print(e)