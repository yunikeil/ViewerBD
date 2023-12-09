from pydantic import BaseModel

class ResponseCreate(BaseModel):
    endpoint_id: int
    response_schema_id: int | None = None
    status_code: int = 200
    description: str = "Description"
    

class ResponseUpdate(BaseModel):
    response_schema_id: int | None = None
    status_code: int = 200
    description: str = "Description"


class ResponseInDB(ResponseCreate):
    id: int
    created_at: int
    updated_at: int
