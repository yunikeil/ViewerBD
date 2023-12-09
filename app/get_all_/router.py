from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import get_session
from . import schema, service


router = APIRouter(tags=["Root"])

@router.get("/")
async def get_all(table_name: schema.TableName, db_session: AsyncSession = Depends(get_session)):
    rows = await service.get_all(db_session, table_name=table_name)
    
    if not rows:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Rows not found!"
        )
    
    return rows
