from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from CRUD.user_crud import get_all_users, get_user_by_id, create_user, update_user
from dependencies.database.db import get_db
from schema.user_schema import UserCreate, UserUpdate

router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.get('/')
def get(db: Session = Depends(get_db)):
    return get_all_users(db)


@router.get('/{id}')
def get(id: int, db: Session = Depends(get_db)):
    return get_user_by_id(db, id)


@router.post('/')
def create(request: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, request)


@router.patch('/')
def update(id: int, request: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, id, request)
