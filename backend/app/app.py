from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.product_router import product_router
from app.services.user_service import User_Service

description = """
Ecommerce  API 🔥

You will be able to:
* **Fetch Products from the Database**
* **Add Items to cart** (_not implemented_)
* **Manage Orders** (_not implemented_)


"""
app = FastAPI(title="E-Commerce API", description=description,
              summary="The Backend to my E-Commerce Website",
              contact={
                  "name": "Julian Lechner",
                  "url": "https://jlechner.com",
                  "email": "julian@jlechner.com",
              },)


# User_Service.create_user(
#     {"username": "user", "hashed_password": "password", "is_active": False})

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, adjust in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_router)


@app.get("/")
async def root():
    return {"message": "Hello, world!"}
