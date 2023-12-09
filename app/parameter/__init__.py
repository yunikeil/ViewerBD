from fastapi import APIRouter

from .routers import parameter_base


api_router = APIRouter(
    prefix="/api/endpoint/parameter"
)


api_router.include_router(parameter_base.router, tags=["Parameter"])
