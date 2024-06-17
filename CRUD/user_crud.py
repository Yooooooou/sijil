from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from models.user_model import DbUser
from schema.user_schema import UserCreate, UserUpdate


def create_user(db: Session, request: UserCreate):
    new_user = DbUser(
        first_name=request.first_name,
        last_name=request.last_name,
        phone_number=request.phone_number,
        email=request.email
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    return db.query(DbUser).all()


def get_user_by_id(db: Session, id: int):
    return db.query(DbUser).filter(DbUser.id == id).first()


def update_user(db: Session, id: int, request: UserUpdate):
    user = db.query(DbUser).filter(DbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"user with id {id} not found")

    update_data = request.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(user, key, value)
    db.commit()
    db.refresh(user)
    return {"message: ": "user was successfully updated"}
