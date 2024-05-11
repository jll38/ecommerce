from pydantic import BaseModel, Field
from typing import List

class CartItemBase(BaseModel):
    product_id: int = Field(..., description="The ID of the product", example=2)
    product_size: str = Field(..., description="The size of the product", example="Large")
    quantity: int = Field(default=1, gt=0, description="The quantity of the product", example=1)
    price: float = Field(default=0.0, gt=0, description="Price of the item at the time of addition to the cart", example=19.99)

class CartBase(BaseModel):
    id: int = Field(..., description="The ID of the cart", example=1)
    user_id: str = Field(..., description="The UUID of the user associated with this cart", example="123e4567-e89b-12d3-a456-426614174000")
    items: List[CartItemBase] = Field(default_factory=list, description="List of items in the cart")
