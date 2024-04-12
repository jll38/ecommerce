from pydantic import BaseModel
from fastapi import APIRouter, FastAPI, HTTPException

# Placeholder for DB
products_db = {
    "1": {
        "product_id": "1",
        "product_type": "shirt",
        "product_name": "Muscle Shirt",
        "price": 29.99,  # Added required price field
        "stock_quantity": 100  # Added required stock_quantity field
    }
}


class Product_Service(BaseModel):

    @staticmethod
    def retrieve_product(product_id):
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
        return {**product, "_links": links}
