from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship, Mapped
from app.db import Base
from sqlalchemy.dialects.postgresql import UUID
from typing import TYPE_CHECKING
from datetime import datetime
if TYPE_CHECKING:
    from .user import User



class Cart(Base):
    __tablename__ = 'carts'
    id = Column(Integer, primary_key=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.uuid'), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user: Mapped["User"] = relationship("User", back_populates="cart", foreign_keys=[user_id])
    items: Mapped["Cart_Item"] = relationship("Cart_Item", back_populates="cart", cascade="all, delete-orphan")


class Cart_Item(Base):
    __tablename__ = 'cart_items'

    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    cart_id = Column(Integer, ForeignKey('carts.id'), nullable=False)
    product_size_id = Column(Integer, ForeignKey('product_sizes.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Float, nullable=False, default=0.0)

    cart = relationship("Cart", back_populates="items")
    product_size = relationship("ProductSize", back_populates="cart_items")
