from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base
from .join_tables import product_categories

class Product(Base):
    __tablename__ = 'products'
    
    id = Column(Integer, primary_key=True)
    slug = Column(String)
    product_type = Column(String, index=True)
    product_name = Column(String)
    price = Column(Float, nullable=False)
    blurb = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    image_url = Column(String, nullable=True)

    categories = relationship("Category", secondary=product_categories, back_populates="products")

    def __repr__(self):
        return f"Product(id={self.id}), slug={self.product_type}, product_type={self.product_type}, product_name={self.product_name}, price={self.price}, blur={self.blurb}, description={description}, image_url={image_url})"

class ProductSize(Base):
    __tablename__ = 'product_sizes'
    __table_args__ = {'extend_existing': True}

    size_id = Column("id", Integer, primary_key=True)
    product_id = Column("product_id", Integer, ForeignKey('products.id'), nullable=False)
    size = Column("size", String)
    stock_quantity = Column("stock_quantity", Integer, nullable=False, default=0)

