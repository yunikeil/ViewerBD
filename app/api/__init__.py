from fastapi import APIRouter

from .routers import api_base


api_router = APIRouter(
    prefix="/api"
)


api_router.include_router(api_base.router, tags=["Api"])
