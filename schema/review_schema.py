from pydantic import BaseModel


class ReviewSchema(BaseModel):
    user_id: int
    salon_id: int
    score: int
    comment: str = None
    master_id: int
