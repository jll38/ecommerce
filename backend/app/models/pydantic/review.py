from pydantic import BaseModel
from typing import Optional

class ReviewSchema(BaseModel):
    id: int
    product_id: int
    author_id: int
    content: str
    rating: int

    class Config:
        from_attributes = True
