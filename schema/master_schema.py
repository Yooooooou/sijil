from pydantic import BaseModel
from typing import Optional


class MasterCreate(BaseModel):
    first_name: str
    last_name: str
    rating_id: Optional[int] = None
    experience: Optional[int] = None
    bio: str
