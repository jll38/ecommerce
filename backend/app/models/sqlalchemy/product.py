from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class ProductModel(Base):
    __tablename__ = 'products'
    product_id = Column("id", String, primary_key=True, index=True)
    product_type = Column("product_type", String, index=True)
    product_name = Column("product_name", String)
    price = Column("product_price", Float, nullable=False)
    description = Column("product_description", Text, nullable=True)
    image_url = Column("image_url", String, nullable=True)

class ProductSizeModel(Base):
    __tablename__ = 'product_sizes'
    size_id = Column("id", Integer, primary_key=True)
    product_id = Column("product_id", String, ForeignKey('products.id'), nullable=False)
    size = Column("size", String)
    stock_quantity = Column("stock_quantity", Integer, nullable=False, default=0)
