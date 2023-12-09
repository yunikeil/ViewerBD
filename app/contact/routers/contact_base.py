from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from .. import schemas, services


router = APIRouter()


@router.post("/")
async def create(api_data: schemas.ContactCreate = Depends(schemas.ContactCreate), db_session: AsyncSession = Depends(get_session)) -> schemas.ContactInDB:
    old_contact = await services.get_contact_by_api_id(db_session, api_id=api_data.api_id)
    
    if old_contact:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Contact already exists!"
        )
    
    contact = await services.create_contact(db_session, data_in=api_data)
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Api not found!"
        )
    return schemas.ContactInDB(**contact.to_dict())
    

@router.get("/")
async def get(id: int, db_session: AsyncSession = Depends(get_session)) -> schemas.ContactInDB:
    contact = await services.get_contact(db_session, id=id)
    
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found!"
        )
    
    return schemas.ContactInDB(**contact.to_dict())


@router.put("/")
async def update(id: int, contact_data = Depends(schemas.ContactUpdate), db_session: AsyncSession = Depends(get_session)) -> schemas.ContactInDB:
    contact = await services.get_contact(db_session, id=id)
    
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found!"
        )

    new_api = await services.update_contact(db_session, db_obj=contact, obj_in=contact_data)
    return schemas.ContactInDB(**new_api.to_dict())
    ...


@router.delete("/")
async def delete(id: int, db_session: AsyncSession = Depends(get_session)) -> schemas.ContactInDB:
    contact = await services.get_contact(db_session, id=id)
    
    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found!"
        )
    
    deleted_contact = await services.delete_contact(db_session, db_obj=contact)
    return schemas.ContactInDB(**deleted_contact.to_dict())


