from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from config import settings

DATABASE_URL = (
    f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}?sslmode=require"
)

Base = declarative_base()
engine = create_engine(DATABASE_URL, pool_pre_ping=True)
