from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from .. import schemas, services


router = APIRouter()


@router.post("/")
async def create(api_data: schemas.ParameterCreate = Depends(schemas.ParameterCreate), db_session: AsyncSession = Depends(get_session)) -> schemas.ParameterInDB:       
    contact = await services.create_parameter(db_session, data_in=api_data)
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Endpoint not found!"
        )
    return schemas.ParameterInDB(**contact.to_dict())
    

@router.get("/")
async def get(id: int, db_session: AsyncSession = Depends(get_session)) -> schemas.ParameterInDB:
    contact = await services.get_parameter(db_session, id=id)
    
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parameter not found!"
        )
    
    return schemas.ParameterInDB(**contact.to_dict())


@router.put("/")
async def update(id: int, contact_data = Depends(schemas.ParameterUpdate), db_session: AsyncSession = Depends(get_session)) -> schemas.ParameterInDB:
    contact = await services.get_parameter(db_session, id=id)
    
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parameter not found!"
        )

    new_api = await services.update_parameter(db_session, db_obj=contact, obj_in=contact_data)
    return schemas.ParameterInDB(**new_api.to_dict())
    ...


@router.delete("/")
async def delete(id: int, db_session: AsyncSession = Depends(get_session)) -> schemas.ParameterInDB:
    contact = await services.get_parameter(db_session, id=id)
    
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parameter not found!"
        )
    
    deleted_contact = await services.delete_parameter(db_session, db_obj=contact)
    return schemas.ParameterInDB(**deleted_contact.to_dict())


