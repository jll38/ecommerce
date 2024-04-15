# Import all models to ensure they are known to the Base metadata
from .user import UserModel
from .review import ReviewModel
from .product import ProductModel, ProductSizeModel
from .order import OrderModel, OrderItemModel
from .category import CategoryModel

models_arr = [UserModel, ReviewModel, OrderModel, OrderItemModel,
              ProductModel, ProductSizeModel, CategoryModel]
