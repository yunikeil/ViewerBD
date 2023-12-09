from pydantic import BaseModel


class SchemaCreate(BaseModel):
    api_id: int
    name: str = "Name"
    description: str = "Description"
    file_path: str = "statik.url/server1/data/file"


class SchemaUpdate(SchemaCreate):
    pass


class SchemaInDB(SchemaCreate):
    id: int