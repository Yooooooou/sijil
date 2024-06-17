from typing import Optional

from pydantic import BaseModel


class SalonSchema(BaseModel):
    name: str
    description: str
    address: str
    phone_number: str
    rating_id: Optional[int] = None
    review_count: Optional[int] = None


class SalonDisplay(BaseModel):
    id: int
    name: str
    rating: Optional[float] = None
