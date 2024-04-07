from pydantic import BaseModel, Extra

class Product(BaseModel):
    product_id: str
    product_type: str
    product_name: str
    
    class Config:
        extra = Extra.allow  # This allows the model to include fields that are not explicitly defined
