from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from .. import schemas, services


router = APIRouter()


@router.post("/")
async def create(api_data: schemas.EndpointCreate = Depends(schemas.EndpointCreate), db_session: AsyncSession = Depends(get_session)) -> schemas.EndpointInDB:   
    contact = await services.create_endpoint(db_session, data_in=api_data)
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Api not found!"
        )
    return schemas.EndpointInDB(**contact.to_dict())
    

@router.get("/")
async def get(id: int, db_session: AsyncSession = Depends(get_session)) -> schemas.EndpointInDB:
    contact = await services.get_endpoint(db_session, id=id)
    
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found!"
        )
    
    return schemas.EndpointInDB(**contact.to_dict())


@router.put("/")
async def update(id: int, contact_data = Depends(schemas.EndpointUpdate), db_session: AsyncSession = Depends(get_session)) -> schemas.EndpointInDB:
    contact = await services.get_endpoint(db_session, id=id)
    
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found!"
        )

    new_api = await services.update_endpoint(db_session, db_obj=contact, obj_in=contact_data)
    return schemas.EndpointInDB(**new_api.to_dict())
    ...


@router.delete("/")
async def delete(id: int, db_session: AsyncSession = Depends(get_session)) -> schemas.EndpointInDB:
    contact = await services.get_endpoint(db_session, id=id)
    
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found!"
        )
    
    deleted_contact = await services.delete_endpoint(db_session, db_obj=contact)
    return schemas.EndpointInDB(**deleted_contact.to_dict())


