from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud, schemas
from database import get_db

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/", response_model=list[schemas.UserOut])
def read_users(db: Session = Depends(get_db)):
    return crud.get_users(db)

@router.post("/", response_model=schemas.UserOut)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)