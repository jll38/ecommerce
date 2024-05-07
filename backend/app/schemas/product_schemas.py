from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime
import uuid

class CategoryBase(BaseModel):
    name: str = Field(..., example="Electronics")

class ProductSizeBase(BaseModel):
    size: str = Field(..., example="Medium")
    stock_quantity: int = Field(..., description="The quantity of this size in stock", example=100)

class ProductBase(BaseModel):
    slug: str = Field(..., example="unique-product-slug-1234")
    product_type: str = Field(..., example="Accessory")
    product_name: str = Field(..., example="Stylish Sunglasses")
    price: float = Field(..., gt=0, example=19.99)
    blurb: Optional[str] = Field(None, example="A short description of the product")
    description: Optional[str] = Field(None, example="A detailed description of the product")
    image_url: Optional[str] = Field(None, example="http://example.com/image.png")
    sale_price: Optional[float]  = Field(..., gt=0, example=9.99)

class ProductCreate(ProductBase):
    # Here we do not include relationships, assuming that only base product data is needed for creation
    pass

class ProductUpdate(ProductBase):
    price: Optional[float] = Field(None, gt=0, example=19.99)

    @validator('price')
    def check_price(cls, v):
        if v is not None and v <= 0:
            raise ValueError("Price must be greater than zero.")
        return v

class ProductResponse(ProductBase):
    id: int = Field(..., example=1)
    created_at: datetime = Field(..., example=datetime.now())
    # Relationships
    categories: List[CategoryBase] = []
    sizes: List[ProductSizeBase] = []

class ProductListResponse(BaseModel):
    products: List[ProductResponse]

class CategoryResponse(CategoryBase):
    id: int = Field(..., example=1)

class ProductSizeResponse(ProductSizeBase):
    size_id: int = Field(..., example=1)
