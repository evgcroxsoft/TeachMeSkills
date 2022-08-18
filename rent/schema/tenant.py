from pydantic import BaseModel
from typing import List
import uuid
from datetime import date


class TenantBaseSchema(BaseModel):
    
    email : str
    first_name : str
    last_name : str

class TenantCreateSchema(TenantBaseSchema):
    id : int
    hashed_password : str
    created_at : date

class TenantUpdateSchema(TenantCreateSchema):
    updated_at : date
    is_active : bool

class TenantRetrieveSchema(TenantCreateSchema):
    id : int
    email : str
    first_name : str
    last_name : str
    created_at : date
    updated_at : date
    is_active : bool
    # appartments: List[Appartment] = []

    class Config :
        orm_mode = True