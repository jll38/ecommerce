from pydantic import BaseModel
from typing import Optional

class ProductSchema(BaseModel):
    product_id: str
    product_type: str
    product_name: str
    price: float
    description: Optional[str] = None
    stock_quantity: int
    image_url: Optional[str] = None

    class Config:
        orm_mode = True