#________________________________________________________SCHEMAS__________________________________________________________________________________
from datetime import date
from pydantic import BaseModel, EmailStr
import uuid

from models.enum import AccommodationCity, AccommodationCountry, AccommodationType, BookingStatus

# ----------------------------------------------------------User----------------------------------------------------------------------------------

class BaseUserScheme(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    phone: str | None = None
    renter: bool = False
    hoster: bool = False
    is_active: bool

    class Config:
        orm_mode = True

class UserCreateScheme(BaseUserScheme):
    hashed_password: str

    class Config:
        orm_mode = True

class UserRetrieveScheme(BaseUserScheme):
    created_at: date
    updated_at: date | None

    class Config:
        orm_mode = True


# ---------------------------------------------------------Accommodation---------------------------------------------------------------------------------

class BaseAccommodationScheme(BaseModel):
    name: str
    persons: int | None = None
    is_active: bool
    created_at: date
    accommodation_type: AccommodationType | None = None
    city: AccommodationCity | None = None
    country: AccommodationCountry | None = None
    price: int | None = None

    class Config:
        orm_mode = True

class AccommodationScheme(BaseAccommodationScheme):
    created_at: date
    updated_at: date | None

    class Config:
        orm_mode = True

# ---------------------------------------------------------Booking---------------------------------------------------------------------------------

class BaseBookingScheme(BaseModel):
    date_start: date 
    date_end: date
    persons: int
    accommodation_id: int

    class Config:
        orm_mode = True


class BookingScheme(BaseBookingScheme):
    created_at: date
    updated_at: date | None
    price: int | None = None

    class Config:
        orm_mode = True


# ---------------------------------------------------------Feedbacks---------------------------------------------------------------------------------

class BaseFeedbackScheme(BaseModel):
    description: str
    rating: int
    booking_id: int

    class Config:
        orm_mode = True


class FeedbackScheme(BaseFeedbackScheme):
    created_at: date
    updated_at: date | None

    class Config:
        orm_mode = True


class RenterFeedbackScheme(BaseFeedbackScheme):
    renter_id: uuid.UUID

    class Config:
        orm_mode = True

class HosterFeedbackScheme(BaseFeedbackScheme):
    hoster_id: uuid.UUID

    class Config:
        orm_mode = True

# ---------------------------------------------------------Token---------------------------------------------------------------------------------


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None
