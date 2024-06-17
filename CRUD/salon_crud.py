from sqlalchemy import func
from sqlalchemy.orm import Session
from statistics import mean

from models.review_model import DbReview
from models.salon_model import DbSalon
from schema.salon_schema import SalonSchema


def create_salon(db: Session, request: SalonSchema):
    salon = DbSalon(
        name=request.name,
        description=request.description,
        address=request.address,
        phone_number=request.phone_number,
        rating_id=request.rating_id,
        review_count=0
    )
    db.add(salon)
    db.commit()
    db.refresh(salon)
    return salon


def get_all_salons(db: Session):
    subquery = (
        db.query(
            DbReview.salon_id,
            func.round(func.avg(DbReview.score), 1).label('average_rating')
        )
        .group_by(DbReview.salon_id)
        .subquery()
    )

    salons_with_ratings = (
        db.query(
            DbSalon.id,
            DbSalon.name,
            subquery.c.average_rating
        )
        .outerjoin(subquery, DbSalon.id == subquery.c.salon_id)
        .all()
    )

    result = [
        {
            'id': salon.id,
            'name': salon.name,
            'rating': salon.average_rating if salon.average_rating is not None else None
        }
        for salon in salons_with_ratings
    ]

    return result
