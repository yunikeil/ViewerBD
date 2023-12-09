from pydantic import BaseModel


class ApiCreate(BaseModel):
    title: str = "Title"
    version: str = "0.0.1"
    description: str = "Description"
    base_url: str = "/"


class ApiUpdate(ApiCreate):
    pass


class ApiInDB(ApiCreate):
    id: int
    created_at: int
    updated_at: int
