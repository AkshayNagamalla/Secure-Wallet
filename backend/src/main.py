from fastapi import FastAPI, Depends
from database import engine
from sqlalchemy import text
from database import engine, Base,SessionLocal, get_db 
from models import Users, Items
from sqlalchemy.orm import Session

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal() 
    try:
        yield db
    finally:
        db.close() 

app = FastAPI() 

@app.get("/") 
def root():
    return {"message" : "Server is working :-)"}

@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    try:
        db.execute(text("SELECT 1"))
        return {"status": "ok", "database": "connected"}
    except Exception as e:
        return {"status": "error", "details": str(e)} 
    
@app.get("/tables")
def get_tables(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT table_name FROM information_schema.tables WHERE table_schema='public' "))
        tables = [row[0] for row in result.fetchall()]
        return {"tables" : tables} 
    except Exception as e:
        return {"status": "error", "details": str(e)} 