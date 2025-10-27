import uuid
import httpx
from fastapi import APIRouter, UploadFile, File, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
from models import Items
from schema import FileCreate
from models.items_model import ItemType 
from routes.files import add_file 
from config import settings

test_router = APIRouter(prefix="/test")


@test_router.post("/upload-file/")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    unique_filename = f"{uuid.uuid4()}_{file.filename}"

    file_create = FileCreate(
        owner_id=uuid.UUID("8a5a13ff-a941-4407-85d4-1ff659745813"),
        parent_id=None,
        name=unique_filename,
        type=ItemType.File, 
        mime_type=file.content_type
    )

    signed_data = add_file(file_create, db)
    upload_url = signed_data["upload_url"]
    file_id = signed_data["file_id"]

    print(file_id)
    print(upload_url)
    # Step 2: Upload the file to Supabase via signed link
    contents = await file.read()
    try:
        async with httpx.AsyncClient() as client:
            upload_resp = await client.put(upload_url, content=contents)
            if upload_resp.status_code not in (200, 201):
                raise HTTPException(status_code=500, detail="File upload failed")
    finally:
        await file.close()

    # Step 3: Update DB record with final public URL
    public_url = f"{settings.SUPABASE_URL}/storage/v1/object/public/{settings.BUCKET_NAME}/{unique_filename}"

    db_item = db.query(Items).filter(Items.id == file_id).first()
    if db_item:
        db_item.uri = public_url
        db.commit()
        db.refresh(db_item)

    return {"message": "File uploaded successfully", "url": public_url, "id": file_id}
