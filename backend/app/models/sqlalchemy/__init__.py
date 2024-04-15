# Import all models to ensure they are known to the Base metadata
from .user import User
from .review import Review
from .product import Product, ProductSize
from .order import Order, OrderItem
from .category import Category

models_arr = [User, Review, Order, OrderItem,
              Product, ProductSize, Category]
