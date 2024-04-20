from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, DateTime, Table, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base
from .cart import Cart

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    salt = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    cart = relationship("Cart", back_populates="user", uselist=False, cascade="all, delete-orphan")

    orders = relationship("Order", back_populates="user")
    reviews = relationship("Review", back_populates="author")
