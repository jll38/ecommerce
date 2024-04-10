from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: int
    username: str
    email: str
    is_active: Optional[bool] = True

    class Config:
        orm_mode = True
