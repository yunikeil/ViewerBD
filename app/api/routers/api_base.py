from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from .. import schemas, services


router = APIRouter()


@router.post("/")
async def create(api_data = Depends(schemas.ApiCreate), db_session: AsyncSession = Depends(get_session)) -> schemas.ApiInDB:
    api = await services.create_api(db_session, data_in=api_data)
    return schemas.ApiInDB(**api.to_dict())
    

@router.get("/")
async def get(id: int, db_session: AsyncSession = Depends(get_session)) -> schemas.ApiInDB:
    api = await services.get_api(db_session, id=id)
    
    if not api:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Api not found!"
        )
    
    return schemas.ApiInDB(**api.to_dict())


@router.put("/")
async def update(id: int, api_data = Depends(schemas.ApiCreate), db_session: AsyncSession = Depends(get_session)) -> schemas.ApiInDB:
    api = await services.get_api(db_session, id=id)
    
    if not api:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Api not found!"
        )

    new_api = await services.update_api(db_session, db_obj=api, obj_in=api_data)
    return schemas.ApiInDB(**new_api.to_dict())
    ...


@router.delete("/")
async def delete(id: int, db_session: AsyncSession = Depends(get_session)) -> schemas.ApiInDB:
    api = await services.get_api(db_session, id=id)
    
    if not api:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Api not found!"
        )
    
    deleted_api = await services.delete_api(db_session, db_obj=api)
    return schemas.ApiInDB(**deleted_api.to_dict())


