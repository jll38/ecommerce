from fastapi import APIRouter, FastAPI

product_router = APIRouter()

@product_router.get('/product')
def read_products():
    pass

@product_router.get('/product/${product_id}')
def read_product():
    pass

@product_router.post('/product/${product_id}')
def read_product(): 
    pass

