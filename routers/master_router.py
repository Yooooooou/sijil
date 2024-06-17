from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from CRUD.master_crud import get_master_by_id, get_all_masters, create_master, get_master_appointments
from dependencies.database.db import get_db
from schema.master_schema import MasterCreate

router = APIRouter(
    tags=['masters'],
    prefix='/router'
)


@router.get('/{id}')
def get(id: int, db: Session = Depends(get_db)):
    return get_master_by_id(db, id)


@router.get('/')
def get(db: Session = Depends(get_db)):
    return get_all_masters(db)


@router.post('/')
def post(request: MasterCreate, db: Session = Depends(get_db)):
    return create_master(db, request)


@router.get('/appointments/{master_id}')
def get(master_id: int, db: Session = Depends(get_db)):
    return get_master_appointments(db, master_id)
