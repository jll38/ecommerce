from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, DateTime, Table, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class UserModel(Base):
    __tablename__ = 'users'
    
    id = Column("id", Integer, primary_key=True, index=True)
    username = Column("username", String, unique=True, index=True, nullable=False)
    email = Column("email", String, unique=True, index=True, nullable=False)
    hashed_password = Column("hashed_password", String, nullable=False)
    is_active = Column("is_active", Boolean, default=True)

    orders = relationship("Order", back_populates="user")
    reviews = relationship("Review", back_populates="author")