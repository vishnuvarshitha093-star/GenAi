from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.requests import router as request_router

api_router = APIRouter()
api_router.include_router(auth_router)
api_router.include_router(request_router)
