from pydantic import BaseModel 
from models.items_model import ItemType
import uuid

class FileCreate(BaseModel):

    owner_id: uuid.UUID
    parent_id: uuid.UUID | None
    name: str
    type: ItemType
    mime_type: str | None