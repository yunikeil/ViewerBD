from fastapi import APIRouter

from .routers import endpoint_base


api_router = APIRouter(
    prefix="/api/endpoint"
)


api_router.include_router(endpoint_base.router, tags=["Endpoint"])
