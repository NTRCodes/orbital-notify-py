from fastapi import APIRouter
from .routes import health

api_router = APIRouter(
    prefix="/api",
    tags=["api"],
    responses={404: {"description": "Not found"}},
)

api_router.include_router(health.router)

@api_router.get("/")
async def root():
    return {"message": "Welcome to the API!"}