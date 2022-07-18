from pydantic import BaseModel
from typing import List, Union
import uuid
from datetime import date

class AppartmentBaseSchema(BaseModel):
    city : str
    street : str
    house_number : str
    flat_number : str
    description : Union[str, None] = None
    daily_price : int

class AppartmentCreateSchema(AppartmentBaseSchema):
    id = int
    landlords_id = uuid
    created_at: date

class AppartmentUpdateSchema(AppartmentBaseSchema):
    updated_at: date
    is_active: bool

class AppartmentRetrieveSchema(AppartmentBaseSchema):
    id = int
    landlords_id = uuid
    city : str
    street : str
    house_number : str
    flat_number : str
    description : Union[str, None] = None
    daily_price : int
    created_at: date
    updated_at: date
    is_active: bool

    class Config:
        orm_mode = True