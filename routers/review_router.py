from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from CRUD.review_crud import create_review, get_all_salon_reviews, delete_review, get_all_user_reviews
from dependencies.database.db import get_db
from schema.review_schema import ReviewSchema

router = APIRouter(
    tags=['reviews', 'salons'],
    prefix='/reviews'
)


@router.post('/')
def create(request: ReviewSchema, db: Session = Depends(get_db)):
    return create_review(db, request)


@router.get('/salons/{salon_id}')
def get_reviews_by_salon_id(id: int, db: Session = Depends(get_db)):
    return get_all_salon_reviews(db, id)


@router.get("/users/{user_id}")
def get_reviews_by_user_id(id: int, db: Session = Depends(get_db)):
    return get_all_user_reviews(db, id)


@router.delete('/{review_id}')
def delete(review_id: int, db: Session = Depends(get_db)):
    return delete_review(db, review_id)
