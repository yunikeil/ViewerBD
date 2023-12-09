from fastapi import APIRouter

from .routers import schema_base


api_router = APIRouter(
    prefix="/api/schema"
)


api_router.include_router(schema_base.router, tags=["Schema"])
