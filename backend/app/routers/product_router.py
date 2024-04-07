from fastapi import APIRouter, FastAPI

product_router = APIRouter()

@product_router.get('/products')
def read_products():
    return [{"name": "test"}]