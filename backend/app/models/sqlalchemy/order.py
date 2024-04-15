from sqlalchemy import Column, String, Float, Integer, Text, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db import Base

class Order(Base):
    __tablename__ = 'orders'
    
    id = Column("id", Integer, primary_key=True, index=True)
    user_id = Column("user_id", Integer, ForeignKey('users.id'))
    created_at = Column("created_at", DateTime, default=datetime.utcnow)
    
    user = relationship("User", back_populates="orders")
    items = relationship("OrderItem", back_populates="order")

class OrderItem(Base):
    __tablename__ = 'order_items'
    
    id = Column("id", Integer, primary_key=True, index=True)
    order_id = Column("order_id", Integer, ForeignKey('orders.id'))
    product_id = Column("product_id", Integer, ForeignKey('products.id'))
    quantity = Column("quantity", Integer, nullable=False)
    
    order = relationship("Order", back_populates="items")
    product = relationship("Product")
