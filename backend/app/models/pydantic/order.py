from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class OrderItemSchema(BaseModel):
    id: int
    order_id: int
    product_id: int
    quantity: int

    class Config:
        from_attributes = True

class OrderSchema(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    items: List[OrderItemSchema] = []

    class Config:
        from_attributes = True
