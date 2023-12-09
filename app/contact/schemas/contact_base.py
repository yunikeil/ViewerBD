from pydantic import BaseModel, EmailStr


class ContactCreate(BaseModel):
    api_id: int
    name: str = "Name"
    email: str = "email@email.email"
    url: str = "t.me/yunikeil"


class ContactUpdate(BaseModel):
    name: str = "Name"
    email: str = "email@email.email"
    url: str = "t.me/yunikeil"


class ContactInDB(ContactCreate):
    id: int
    created_at: int
    updated_at: int
