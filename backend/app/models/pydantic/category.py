from pydantic import BaseModel
from typing import Optional, List
class CategorySchema(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    products: List[ProductSchema] = []

    class Config:
        from_attributes = True