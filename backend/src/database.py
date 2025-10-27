from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from config import settings
from sqlalchemy.orm import sessionmaker
from supabase import create_client

def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close() 
        
DATABASE_URL = (
    f"postgresql+psycopg2://{settings.DB_USER}:{settings.DB_PASSWORD}@{settings.DB_HOST}:{settings.DB_PORT}/{settings.DB_NAME}?sslmode=require"
)

class Base(DeclarativeBase):
    pass

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine) 

blob_storage = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
BLOB_BUCKET = settings.BUCKET_NAME