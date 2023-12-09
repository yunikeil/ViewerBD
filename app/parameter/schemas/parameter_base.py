from enum import Enum

from pydantic import BaseModel


class ParameterLocation(str, Enum):
    cookie = "COOCKIE"
    header = "HEADER"
    payload = "PAYLOAD"


class ParameterType(str, Enum):
    str = "STR"
    int = "INT"
    bool = "BOOL"
    float = "FLOAT"


class ParameterCreate(BaseModel):
    endpoint_id: int
    name: str = "Name"
    location: ParameterLocation = ParameterLocation.payload
    type: ParameterType = ParameterType.str
    required: bool = False
    description: str = "Description"


class ParameterUpdate(BaseModel):
    name: str = "Name"
    location: ParameterLocation = ParameterLocation.payload
    type: ParameterType = ParameterType.str
    required: bool = False
    description: str = "Description"


class ParameterInDB(ParameterCreate):
    id: int
    created_at: int
    updated_at: int
