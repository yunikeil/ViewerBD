import time

from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, exists, delete, and_

from .. import models, schemas
from app.endpoint.services import get_endpoint


async def create_response(db_session: AsyncSession, *, data_in: schemas.ResponseCreate,) -> models.Response:
    endpoint = await get_endpoint(db_session, id=data_in.endpoint_id)
    
    if not endpoint:
        return None
    
    t = int(time.time())
    api = models.Response(
        **data_in.model_dump(exclude_unset=True),
        created_at = t,
        updated_at = t,
    )
    
    db_session.add(api)
    await db_session.commit()
    await db_session.refresh(api)

    return api


async def get_response(db_session: AsyncSession, *, id: int):
    stmt = select(models.Response).where(models.Response.id == id)
    api: models.Response | None = (await db_session.execute(stmt)).scalar()
    return api


async def update_response(db_session: AsyncSession, *, db_obj: models.Response, obj_in: schemas.ResponseUpdate):
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


async def delete_response(db_session: AsyncSession, *, db_obj: models.Response):
    
    await db_session.delete(db_obj)
    await db_session.commit()

    return db_obj
