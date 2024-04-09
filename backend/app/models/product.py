from sqlalchemy import Column, String, Float, Integer, Text
from app.db import Base

class Product(Base):
    __tablename__ = 'products'

    product_id = Column(String, primary_key=True, index=True)
    product_type = Column(String, index=True)
    product_name = Column(String)
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=True)
    stock_quantity = Column(Integer, nullable=False, default=0)
    image_url = Column(String, nullable=True)
