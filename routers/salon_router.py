from typing import Annotated, List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from CRUD.salon_crud import create_salon, get_all_salons
from dependencies.database.db import get_db
from schema.salon_schema import SalonSchema, SalonDisplay

router = APIRouter(
    tags=['salons'],
    prefix='/salons'
)


@router.post('/', response_model=SalonSchema)
def create(request: Annotated[SalonSchema, Depends()], db: Session = Depends(get_db)):
    return create_salon(db, request)


@router.get('/', response_model=List[SalonDisplay])
def get(db: Session = Depends(get_db)):
    return get_all_salons(db)
