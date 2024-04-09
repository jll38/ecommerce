from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, DateTime, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()
class ReviewModel(Base):
    __tablename__ = 'reviews'
    
    id = Column("id", Integer, primary_key=True, index=True)
    product_id = Column("product_id", Integer, ForeignKey('products.id'))
    author_id = Column("author_id", Integer, ForeignKey('users.id'))
    content = Column("review_content", Text, nullable=False)
    rating = Column("product_rating", Integer, nullable=False)
    
    product = relationship("Product", back_populates="reviews")
    author = relationship("User", back_populates="reviews")
