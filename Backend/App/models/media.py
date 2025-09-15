from sqlmodel import SQLModel, Field
from typing import Optional

class Media(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    filename: str
    url: str
    user_id: str
