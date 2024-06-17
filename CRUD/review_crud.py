from fastapi import HTTPException
from sqlalchemy.orm import Session
from starlette import status

from models.review_model import DbReview
from schema.review_schema import ReviewSchema
from CRUD.rating_crud import calculate_salon_rating, calculate_master_rating
from models.salon_model import DbSalon
from models.master_model import DbMaster


def create_review(db: Session, request: ReviewSchema):
    new_review = DbReview(
        user_id=request.user_id,
        salon_id=request.salon_id,
        score=request.score,
        comment=request.comment
    )
    db.add(new_review)
    db.commit()
    db.refresh(new_review)
    salon = db.query(DbSalon).filter(DbSalon.id == request.salon_id).first()
    if not salon:
        raise HTTPException(status_code=404, detail="Salon not found")
    salon.rating = calculate_salon_rating(salon.id, db)
    salon.review_count += 1
    master = db.query(DbMaster).filter(DbMaster.id == request.master_id).first()
    if not master:
        raise HTTPException(status_code=404, detail="Master not found")
    master.rating = calculate_master_rating(master.id, db)

    return {"message: ": "your review successfully saved"}


def get_all_salon_reviews(db: Session, salon_id: int):
    reviews = db.query(DbReview).filter(DbReview.salon_id == salon_id).all()
    detailed_reviews = []
    for review in reviews:
        detailed_review = {
            "id": review.id,
            "score": review.score,
            "comment": review.comment,
            "user_id": review.user_id,
            "user_name": f"{review.user.first_name} {review.user.last_name}",
            "salon_id": review.salon_id,
            "salon_name": review.salon.name
        }
        detailed_reviews.append(detailed_review)
    return detailed_reviews


def get_all_user_reviews(db: Session, user_id: int):
    reviews = db.query(DbReview).filter(DbReview.user_id == user_id).all()
    detailed_reviews = []
    for review in reviews:
        detailed_review = {
            "id": review.id,
            "score": review.score,
            "comment": review.comment,
            "user_id": review.user_id,
            "user_name": f"{review.user.first_name} {review.user.last_name}",
            "salon_id": review.salon_id,
            "salon_name": review.salon.name
        }
        detailed_reviews.append(detailed_review)
    return detailed_reviews


def delete_review(db: Session, review_id: int):
    review = db.query(DbReview).filter(DbReview.id == review_id).first()
    if not review:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Review with id {review_id} not found")
    db.delete(review)
    db.commit()
    return {"message: ": "review was successfully deleted"}
