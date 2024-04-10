from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class CategoryModel(Base):
    __tablename__ = 'categories'
    
    id = Column("id", Integer, primary_key=True, index=True)
    name = Column("category_name", String, nullable=False)
    description = Column("description", Text, nullable=True)
    
    products = relationship("Product", back_populates="category")