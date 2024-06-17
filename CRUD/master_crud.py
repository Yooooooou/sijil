from sqlalchemy.orm import Session

from models.appointment_model import DbAppointment
from models.master_model import DbMaster
from schema.master_schema import MasterCreate


def create_master(db: Session, request: MasterCreate):
    master = DbMaster(
        first_name=request.first_name,
        last_name=request.last_name,
        experience=request.experience,
        bio=request.bio
    )
    db.add(master)
    db.commit()
    db.refresh(master)
    return {"message: ": "master was successfully added"}


def get_all_masters(db: Session):
    return db.query(DbMaster).all()


def get_master_by_id(db: Session, id: int):
    return db.query(DbMaster).filter(DbMaster.id == id).first()


def get_master_appointments(db: Session, id: int):
    appointments = db.query(DbAppointment).filter(DbAppointment.master_id == id).all()
    return appointments



