from pydantic import BaseModel, EmailStr


class LicenseCreate(BaseModel):
    api_id: int
    name: str = "Name"
    url: str = "license.domen/mirea"


class LicenseUpdate(BaseModel):
    name: str = "Name"
    url: str = "license.domen/mirea"


class LicenseInDB(LicenseCreate):
    id: int
    created_at: int
    updated_at: int
