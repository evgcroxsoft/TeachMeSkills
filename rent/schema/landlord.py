from pydantic import BaseModel
from typing import List
import uuid
from datetime import date


class LandlordBaseSchema(BaseModel):
    
    email = str
    first_name = str
    last_name = str

class LandlordCreateSchema(LandlordBaseSchema):
    id = uuid
    hashed_password: str
    created_at: date

class LandlordUpdateSchema(LandlordCreateSchema):
    updated_at: date
    is_active: bool

class LandlordRetrieveSchema(LandlordCreateSchema):
    id : uuid
    email = str
    first_name = str
    last_name = str
    created_at: date
    updated_at: date
    is_active: bool
    # appartments: List[Appartment] = []

    class Config:
        orm_mode = True