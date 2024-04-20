from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.models.pydantic.product import ProductSchema as Product

cart_router = APIRouter()


@cart_router.get("/cart", response_model=list[Product])
def get_user_cart(user_id):
    pass


@cart_router.post("/cart")
def add_to_user_cart(user_id, product_id, product_size, product_color):
    pass

@cart_router.delete("/cart")
def remove_from_user_cart(user_id, cart_item_id):
    pass

@cart_router.put("/cart")
def modify_cart_item_quantity(user_id, cart_item_id, modifier):
    pass

