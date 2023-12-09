from enum import Enum

from pydantic import BaseModel


class ParameterLocation(str, Enum):
    cookie = "cookie"
    header = "header"
    payload = "payload"


class ParameterType(str, Enum):
    str = "str"
    int = "int"
    bool = "bool"
    float = "float"


class ParameterCreate(BaseModel):
    endpoind_id: int
    name: str = "Name"
    location: ParameterLocation = ParameterLocation.payload
    type: ParameterType = ParameterType.str
    requred: bool = False
    description: str = "Description"


class ParameterUpdate(ParameterCreate):
    pass


class ParameterInDB(ParameterCreate):
    id: int
    created_at: int
    updated_at: int
