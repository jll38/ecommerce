from fastapi import APIRouter, FastAPI, HTTPException
from fastapi.responses import JSONResponse
from app.models.product import ProductModel as Product

product_router = APIRouter()

#Placeholder for DB
products_db = {
    "1": {"product_id": "1", "product_type": "shirt", "product_name": "Muscle Shirt"}
}

@product_router.get("/product", response_model=list[Product])
def read_products():
    # Convert products_db to a list of Product models
    return [Product(**product) for product_id, product in products_db.items()]

@product_router.get("/product/{product_id}", response_model=Product)
def read_product(product_id: str):
    product = products_db.get(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    links = {
        "self": {
            "href": f"http://localhost:8080/product/{product_id}"
        },
        "add_to_cart": {
            "href": f"http://localhost:8080/cart/add/{product_id}",
            "method": "POST"
        },
        "post_review": {
            "href": f"http://localhost:8080/product/{product_id}/review",
            "method": "POST"
        }
    }
    return {**product, "links": links}

@product_router.post("/product/{product_id}/cart")
def add_product_to_cart(product_id: str):
    #Implement product/cart logic
    return {"message": "Product added to cart", "product_id": product_id}

@product_router.post("/product/{product_id}/review")
def post_review_product(product_id: str):
    #Implement product/review logic
    return {"message": "Review posted", "product_id": product_id}
