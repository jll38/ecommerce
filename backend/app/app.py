from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers.product_router import product_router
app = FastAPI()


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