from fastapi import APIRouter

from .routers import response_base


api_router = APIRouter(
    prefix="/api/endpoint/response"
)


api_router.include_router(response_base.router, tags=["Response"])

