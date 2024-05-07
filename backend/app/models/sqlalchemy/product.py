from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base
from .join_tables import product_categories
from .review import *

class Product(Base):
    __tablename__ = 'products'

    id = Column(Integer, primary_key=True)
    slug = Column(String)
    product_type = Column(String, index=True)
    product_name = Column(String)
    price = Column(Float, nullable=False)
    sale_price = Column(Float, nullable=True)
    blurb = Column(Text, nullable=True)
    description = Column(Text, nullable=True)
    image_url = Column(String, nullable=True)

    reviews = relationship("Review", back_populates="product")
    categories = relationship("Category", secondary=product_categories, back_populates="products")
    sizes = relationship("ProductSize", back_populates="product")


class ProductSize(Base):
    __tablename__ = 'product_sizes'
    __table_args__ = {'extend_existing': True}

    size_id = Column("id", Integer, primary_key=True)
    product_id = Column("product_id", Integer, ForeignKey('products.id'), nullable=False)
    size = Column("size", String)
    stock_quantity = Column("stock_quantity", Integer, nullable=False, default=0)

    product = relationship("Product", back_populates="sizes")
    cart_items = relationship("Cart_Item", back_populates="product_size")
