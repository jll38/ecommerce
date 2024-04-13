from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.models.pydantic.product import ProductSchema as Product
from app.services.product_service import Product_Service

product_router = APIRouter()

#Placeholder for DB
products_db = {
    "1": {
        "product_id": "1",
        "product_type": "shirt",
        "product_name": "Muscle Shirt",
        "price": 29.99,  # Added required price field
        "stock_quantity": 100  # Added required stock_quantity field
    }
}

@product_router.get("/products", response_model=list[Product])
def read_products():
    # Convert products_db to a list of Product models
    return [Product(**product) for product_id, product in products_db.items()]

@product_router.get("/products/{product_id}", response_model=Product)
def read_product(product_id: str):
    return Product_Service.retrieve_product(product_id)

@product_router.post("/product/{product_id}/cart")
def add_product_to_cart(product_id: str):
    #Implement product/cart logic
    return {"message": "Product added to cart", "product_id": product_id}

@product_router.post("/product/{product_id}/review")
def post_review_product(product_id: str):
    #Implement product/review logic
    return {"message": "Review posted", "product_id": product_id}
