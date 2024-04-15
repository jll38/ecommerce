from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base
from .join_tables import product_categories

class ProductModel(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    slug = Column(String)
    product_type = Column(String, index=True)
    product_name = Column(String)
    price = Column(Float, nullable=False)
    blurb = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    image_url = Column(String, nullable=True)

    categories = relationship("CategoryModel", secondary=product_categories, back_populates="products")

class ProductSizeModel(Base):
    __tablename__ = 'product_sizes'
    __table_args__ = {'extend_existing': True}

    size_id = Column("id", Integer, primary_key=True)
    product_id = Column("product_id", Integer, ForeignKey('products.id'), nullable=False)
    size = Column("size", String)
    stock_quantity = Column("stock_quantity", Integer, nullable=False, default=0)

