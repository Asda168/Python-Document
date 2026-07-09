import bcrypt
from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
import models, schemas
from helpers import fail, success


def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode("utf-8"), hashed_password.encode("utf-8"))


def get_users(db: Session):
    users = db.query(models.User).all()
    users_out = [
        schemas.UserOut.model_validate(u).model_dump(mode="json")
        for u in users
    ]
    return success(users_out)


def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = hash_password(user.password)
    db_user = models.User(
        name=user.name,
        email=user.email,
        password=hashed_password,
    )
    db.add(db_user)
    try:
        db.commit()
    except IntegrityError as e:
        db.rollback()
        return fail()
    db.refresh(db_user)
    user_out = schemas.UserOut.model_validate(db_user).model_dump(mode="json")
    return success(user_out)