import time

from fastapi.encoders import jsonable_encoder
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, exists, delete, and_

from .. import models, schemas


async def create_api(
    db_session: AsyncSession,
    *,
    data_in: schemas.ApiCreate,
) -> models.Api:
    t = int(time.time())
    api = models.Api(
        **data_in.model_dump(exclude_unset=True),
        created_at=t,
        updated_at=t,
    )

    db_session.add(api)
    await db_session.commit()
    await db_session.refresh(api)

    return api


async def get_api(db_session: AsyncSession, *, id: int):
    stmt = select(models.Api).where(models.Api.id == id)
    api: models.Api | None = (await db_session.execute(stmt)).scalar()
    return api


async def update_api(
    db_session: AsyncSession, *, db_obj: models.Api, obj_in: schemas.ApiUpdate
):
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


async def delete_api(db_session: AsyncSession, *, db_obj: models.Api):

    await db_session.delete(db_obj)
    await db_session.commit()

    return db_obj
