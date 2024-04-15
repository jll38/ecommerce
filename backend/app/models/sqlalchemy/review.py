from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base

class Review(Base):
    __tablename__ = 'reviews'
    __table_args__ = {'extend_existing': True}
    
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    author_id = Column(Integer, ForeignKey('users.id'))
    content = Column(Text, nullable=False)
    rating = Column(Integer, nullable=False)
    
    product = relationship("Product", back_populates="reviews")
    author = relationship("User", back_populates="reviews")
