from fastapi import APIRouter

from .routers import license_base


api_router = APIRouter(
    prefix="/api/license"
)


api_router.include_router(license_base.router, tags=["License"])
