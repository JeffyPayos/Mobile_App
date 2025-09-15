from pydantic import BaseModel
from typing import Optional

class MediaBase(BaseModel):
    filename: str
    url: str
    user_id: str

class MediaCreate(BaseModel):
    filename: str
    user_id: str

class MediaResponse(MediaBase):
    id: Optional[int]

    class Config:
        from_attributes = True
