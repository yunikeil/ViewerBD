import time

from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, exists, delete, and_

from .. import models, schemas
from app.api.services import get_api


async def create_schema(db_session: AsyncSession, *, data_in: schemas.SchemaCreate) -> models.Schema:
    api = await get_api(db_session, id=data_in.api_id)
    
    if not api:
        return None
        
    t = int(time.time())
    contact = models.Schema(**data_in.model_dump(exclude_unset=True))
    
    db_session.add(contact)
    await db_session.commit()
    await db_session.refresh(contact)

    return contact


async def get_schema(db_session: AsyncSession, *, id: int):
    stmt = select(models.Schema).where(models.Schema.id == id)
    contact: models.Schema | None = (await db_session.execute(stmt)).scalar()
    return contact


async def get_schema_by_api_id(db_session: AsyncSession, *, api_id: int):
    stmt = select(models.Schema).where(models.Schema.api_id == api_id)
    contact: models.Schema | None = (await db_session.execute(stmt)).scalar()
    return contact


async def update_schema(db_session: AsyncSession, *, db_obj: models.Schema, obj_in: schemas.SchemaUpdate):
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


async def delete_schema(db_session: AsyncSession, *, db_obj: models.Schema):
    
    await db_session.delete(db_obj)
    await db_session.commit()

    return db_obj
