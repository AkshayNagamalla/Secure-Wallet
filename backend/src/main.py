from fastapi import FastAPI 
from database import engine
from sqlalchemy import text
import os


app = FastAPI() 

@app.get("/") 
def root():
    return {"message" : "Server is working :-)"}

@app.get("/health")
def health_check():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "details": str(e)}
