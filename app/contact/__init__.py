from fastapi import APIRouter

from .routers import contact_base


api_router = APIRouter(
    prefix="/api/contact"
)


api_router.include_router(contact_base.router, tags=["Contact"])
