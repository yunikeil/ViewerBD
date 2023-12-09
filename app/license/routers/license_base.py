from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from .. import schemas, services


router = APIRouter()


@router.post("/")
async def create(license_data: schemas.LicenseCreate = Depends(schemas.LicenseCreate), db_session: AsyncSession = Depends(get_session)) -> schemas.LicenseInDB:
    old_license = await services.get_license_by_api_id(db_session, api_id=license_data.api_id)
    
    if old_license:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="License already exists!"
        )
    
    license = await services.create_license(db_session, data_in=license_data)
    if not license:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Api not found!"
        )
    return schemas.LicenseInDB(**license.to_dict())
    

@router.get("/")
async def get(id: int, db_session: AsyncSession = Depends(get_session)) -> schemas.LicenseInDB:
    license = await services.get_license(db_session, id=id)
    
    if not license:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="License not found!"
        )
    
    return schemas.LicenseInDB(**license.to_dict())


@router.put("/")
async def update(id: int, contact_data = Depends(schemas.LicenseUpdate), db_session: AsyncSession = Depends(get_session)) -> schemas.LicenseInDB:
    license = await services.get_license(db_session, id=id)
    
    if not license:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="License not found!"
        )

    new_license = await services.update_license(db_session, db_obj=license, obj_in=contact_data)
    return schemas.LicenseInDB(**new_license.to_dict())
    ...


@router.delete("/")
async def delete(id: int, db_session: AsyncSession = Depends(get_session)) -> schemas.LicenseInDB:
    license = await services.get_license(db_session, id=id)
    
    if not license:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="License not found!"
        )
    
    deleted_license = await services.delete_license(db_session, db_obj=license)
    return schemas.LicenseInDB(**deleted_license.to_dict())


