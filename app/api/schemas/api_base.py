from pydantic import BaseModel


class ApiCreate(BaseModel):
    name: str
    title: str
    version: str
    description: str
    base_url: str


class ApiUpdate(ApiCreate):
    id: int
