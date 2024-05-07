from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from sqlalchemy.sql import func

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .cart import Cart

from app.db import Base

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    uuid = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    salt = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now())
    verification_token = Column(String, nullable=True)
    email_verified = Column(Boolean, default=False, nullable=False)
    cart = relationship("Cart", back_populates="user", uselist=False, cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="user")
    reviews = relationship('Review', back_populates='author')

    def __repr__(self) -> str:
        """Provides a readable representation of a user object."""
        return f"<User {self.email}>"
