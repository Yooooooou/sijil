from sqlalchemy.orm import Session

from models.review_model import DbReview


def calculate_salon_rating(salon_id: int, db: Session):
    reviews = db.query(DbReview).filter(DbReview.salon_id == salon_id).all()
    if not reviews:
        return None
    total_rating = sum(review.score for review in reviews)
    return total_rating / len(reviews)


def calculate_master_rating(master_id: int, db: Session):
    reviews = db.query(DbReview).filter(DbReview.master_id == master_id).all()
    if not reviews:
        return None
    total_rating = sum(review.score for review in reviews)
    return total_rating / len(reviews)
