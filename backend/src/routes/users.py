from fastapi import APIRouter, HTTPException, Depends,status 
from database import get_db 
from schema import UserCreate
from sqlalchemy.orm import Session
from models import Users

users_router = APIRouter(prefix="/users") 

@users_router.post("/signup")
def add_user(user: UserCreate, db: Session = Depends(get_db)): 
    existing_user = db.query(Users).filter(Users.email == user.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists."
        )

    new_user = Users(name = user.name, email=user.email)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user