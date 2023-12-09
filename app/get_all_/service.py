from typing import List

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text


from . import schema


async def get_all(db_session: AsyncSession, table_name: schema.TableName) -> List[dict]:  
    result = await db_session.execute(text(f"SELECT * FROM {table_name.value}"))
    
    formatted_rows = [
        dict(zip(result.keys(), row))
        for row in result.fetchall()
    ]
    
    return formatted_rows
