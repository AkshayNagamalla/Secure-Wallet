from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel 
from sqlalchemy.orm import Session
from database import blob_storage, BLOB_BUCKET, get_db
from schema import FileCreate
from models import Items
from utils.supabase_utils import generate_presigned_s3_upload_url

files_router = APIRouter(prefix="/files") 

@files_router.get("/{file_id}")
def get_file(file_id: str, db: Session = Depends(get_db)): 
    pass

@files_router.put("/add")
def add_file(file: FileCreate, db:Session = Depends(get_db)): 
    upload_url = generate_presigned_s3_upload_url(file.name, 3600)

    db_item = Items(    
        owner_id=file.owner_id,
        parent_id=file.parent_id,
        name=file.name,
        type=file.type,
        mime_type=file.mime_type
    )
    db.add(db_item)
    db.commit()
    db.refresh(db_item)

    return {"file_id": db_item.id, "upload_url": upload_url}