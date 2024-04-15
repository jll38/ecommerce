from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base

class ProductModel(Base):
    __tablename__ = 'products'
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True)
    slug = Column(String)
    product_type = Column(String, index=True)
    product_name = Column(String)
    price = Column(Float, nullable=False)
    description = Column(Text, nullable=True)
    image_url = Column(String, nullable=True)

    category = relationship("CategoryModel", back_populates="products")
    order_items = relationship("OrderItemModel", back_populates="product")
    reviews = relationship("ReviewModel", back_populates="product")

class ProductSizeModel(Base):
    __tablename__ = 'product_sizes'
    __table_args__ = {'extend_existing': True}

    size_id = Column("id", Integer, primary_key=True)
    product_id = Column("product_id", Integer, ForeignKey('products.id'), nullable=False)
    size = Column("size", String)
    stock_quantity = Column("stock_quantity", Integer, nullable=False, default=0)

