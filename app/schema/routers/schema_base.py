from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from .. import schemas, services


router = APIRouter()


@router.post("/")
async def create(api_data: schemas.SchemaCreate = Depends(schemas.SchemaCreate), db_session: AsyncSession = Depends(get_session)) -> schemas.SchemaInDB:   
    contact = await services.create_schema(db_session, data_in=api_data)
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Api not found!"
        )
    return schemas.SchemaInDB(**contact.to_dict())
    

@router.get("/")
async def get(id: int, db_session: AsyncSession = Depends(get_session)) -> schemas.SchemaInDB:
    contact = await services.get_schema(db_session, id=id)
    
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Schema not found!"
        )
    
    return schemas.SchemaInDB(**contact.to_dict())


@router.put("/")
async def update(id: int, contact_data = Depends(schemas.SchemaUpdate), db_session: AsyncSession = Depends(get_session)) -> schemas.SchemaInDB:
    contact = await services.get_schema(db_session, id=id)
    
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Schema not found!"
        )

    new_api = await services.update_schema(db_session, db_obj=contact, obj_in=contact_data)
    return schemas.SchemaInDB(**new_api.to_dict())
    ...


@router.delete("/")
async def delete(id: int, db_session: AsyncSession = Depends(get_session)) -> schemas.SchemaInDB:
    contact = await services.get_schema(db_session, id=id)
    
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Schema not found!"
        )
    
    deleted_contact = await services.delete_schema(db_session, db_obj=contact)
    return schemas.SchemaInDB(**deleted_contact.to_dict())


