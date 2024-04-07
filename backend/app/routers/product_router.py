from fastapi import APIRouter, FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel

product_router = APIRouter()

@product_router.get('/product')
def read_products():
    pass

@product_router.get('/product/${product_id}')
def read_product():
    return [{'product_id': "1"}, {''}]

@product_router.post('/product/${product_id}')
def read_product(): 
    pass

