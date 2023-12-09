from enum import Enum

from pydantic import BaseModel, field_validator


class Methods(str, Enum):
    get: str = "GET"
    post: str = "POST"
    update: str = "PUT"
    delete: str = "DELETE"


class EndpointCreate(BaseModel):
    api_id: int
    #request_schema_id: int
    path: str = "/"
    method: Methods = Methods.get
    summary: str = "Summary"
    description: str = "Description"


class EndpointUpdate(EndpointCreate):
    pass


class EndpointInDB(EndpointCreate):
    id: int
    created_at: int
    updated_at: int
