from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, DateTime, Table, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base
from .join_tables import product_categories


class Category(Base):
    __tablename__ = 'categories'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(Text, nullable=True)
    
    products = relationship("Product", secondary=product_categories, back_populates="categories")