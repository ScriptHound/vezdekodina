import os

from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from dotenv import load_dotenv
load_dotenv('.env')

USERNAME = os.getenv('POSTGRESQL_USER')
PASSWORD = os.getenv('POSTGRESQL_PASSWORD')
HOST = os.getenv('POSTGRESQL_HOST')
PORT = os.getenv('POSTGRESQL_PORT')
DATABASE = os.getenv('POSTGRESQL_DATABASE')

engine = create_async_engine(
    f"postgresql+asyncpg://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}",
    echo=True)
sync_engine = create_engine(
    f"postgresql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}")
