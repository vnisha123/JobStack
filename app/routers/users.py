from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import Annotated 
from app import models, schemas, hashing
# from app.database import get_db
from app.database import db_dep
from app.routers.utils import get_current_user

router = APIRouter()


@router.post("/signup", response_model=schemas.UserOut, status_code=status.HTTP_201_CREATED)
def signup(user_in: schemas.UserCreate, db: db_dep):

    if db.query(models.User).filter(models.User.email == user_in.email).first():
        raise HTTPException(status_code=400, detail="Username already registered")

    hashed = hashing.hash_password(user_in.password)
    
    user_data = user_in.model_dump(exclude={"password"}) 
    db_user = models.User(**user_data, hashed_password=hashed)
    
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.get("/me", response_model=schemas.UserOut)
def get_my_profile(current_user: Annotated[models.User, Depends(get_current_user)]):
    return current_user