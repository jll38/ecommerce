from fastapi import APIRouter, FastAPI, HTTPException, Query, Path
from fastapi.responses import JSONResponse
from app.schemas.product_schemas import ProductBase
from app.models.sqlalchemy import Product
from app.services.product_service import Product_Service
product_router = APIRouter()

@product_router.get("/products")
def read_products(page: int = 0, limit: int = 0):
    # Convert products_db to a list of Product models
    return Product_Service.get_products(page,limit)

@product_router.get("/products/{product_slug}", response_model=ProductBase)
def read_product(product_slug: str):
    return Product_Service.get_product(product_slug)

@product_router.post("/product/{product_slug}/cart")
def add_product_to_cart(product_slug: str):
    #Implement product/cart logic
    return {"message": "Product added to cart", "product_id": product_id}

@product_router.post("/product/{product_slug}/review")
def post_review_product(product_slug: str):
    #Implement product/review logic
    return {"message": "Review posted", "product_id": product_id}
