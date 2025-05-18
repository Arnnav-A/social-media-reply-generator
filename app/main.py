from fastapi import FastAPI
from app.api.v1 import endpoints

app = FastAPI(
    title="Human-like Social Media Reply Generator",
    version="1.0.0"
)

app.include_router(endpoints.router)
