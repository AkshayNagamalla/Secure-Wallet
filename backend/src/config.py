import os 
from dotenv import load_dotenv

load_dotenv() 

class Settings:
    DB_USER: str = os.getenv("DB_USER")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD")
    DB_HOST: str = os.getenv("DB_HOST")
    DB_PORT: int = os.getenv("DB_PORT")
    DB_NAME: str = os.getenv("DB_NAME") 
    SUPABASE_URL: str = os.getenv("SUPABASE_URL") 
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY") 

    BUCKET_NAME: str = os.getenv("BUCKET_NAME")
    S3_ENDPOINT: str = os.getenv("S3_ENDPOINT")
    S3_REGION: str = os.getenv("S3_REGION")
    S3_ACCESS_KEY_ID: str = os.getenv("S3_ACCESS_KEY_ID")
    S3_SECRET_ACCESS_KEY: str = os.getenv("S3_SECRET_ACCESS_KEY")
    


settings = Settings()