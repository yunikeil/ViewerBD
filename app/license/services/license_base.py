import time

from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, exists, delete, and_

from .. import models, schemas
from app.api.services import get_api


async def create_license(db_session: AsyncSession, *, data_in: schemas.LicenseCreate) -> models.License:
    api = await get_api(db_session, id=data_in.api_id)
    
    if not api:
        return None
        
    t = int(time.time())
    license = models.License(
        **data_in.model_dump(exclude_unset=True),
        created_at = t,
        updated_at = t,
    )
    
    db_session.add(license)
    await db_session.commit()
    await db_session.refresh(license)

    return license


async def get_license(db_session: AsyncSession, *, id: int):
    stmt = select(models.License).where(models.License.id == id)
    license: models.License | None = (await db_session.execute(stmt)).scalar()
    return license


async def get_license_by_api_id(db_session: AsyncSession, *, api_id: int):
    # Не совсем актуальный запрос, можно просто обратиться api.license
    stmt = select(models.License).where(models.License.api_id == api_id)
    license: models.License | None = (await db_session.execute(stmt)).scalar()
    return license


async def update_license(db_session: AsyncSession, *, db_obj: models.License, obj_in: schemas.LicenseUpdate):
    db_obj.updated_at = int(time.time())
    obj_data = jsonable_encoder(db_obj)
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.model_dump(exclude_unset=True)
    
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])

    db_session.add(db_obj)
    await db_session.commit()

    return db_obj


async def delete_license(db_session: AsyncSession, *, db_obj: models.License):
    
    await db_session.delete(db_obj)
    await db_session.commit()

    return db_obj
