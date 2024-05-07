from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship, Mapped
from datetime import datetime
from app.db import Base
from sqlalchemy.dialects.postgresql import UUID
from typing import TYPE_CHECKING
from datetime import datetime
if TYPE_CHECKING:
    from .user import User

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column("id", Integer, primary_key=True, index=True)
    user_id = Column(UUID(as_uuid=True), ForeignKey('users.uuid'), nullable=False)
    created_at = Column("created_at", DateTime, default=datetime.utcnow)
    
    user: Mapped["User"] = relationship("User", back_populates="orders", foreign_keys=[user_id])
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = 'order_items'
    
    id = Column("id", Integer, primary_key=True, index=True)
    order_id = Column("order_id", Integer, ForeignKey('orders.id'))
    product_id = Column("product_id", Integer, ForeignKey('products.id'))
    quantity = Column("quantity", Integer, nullable=False)
    
    order = relationship("Order", back_populates="items")
    product = relationship("Product")
