# ---------------------------------------------------------Base----------------------------------------------------------------------------------
from datetime import date
from pydantic import BaseModel, EmailStr
import uuid


class BaseUserScheme(BaseModel):
    email: EmailStr
    first_name: str
    last_name: str
    telephone: str | None = None
    renter: bool = False
    hoster: bool = False
    is_active: bool
    created_at: date

    class Config:
        orm_mode = True

# ----------------------------------------------------------User----------------------------------------------------------------------------------


class UserInScheme(BaseUserScheme):
    update_at: date | None = None

    class Config:
        orm_mode = True


class UserInDBScheme(BaseUserScheme):
    hashed_password: str

    class Config:
        orm_mode = True

# ---------------------------------------------------------Accommodation---------------------------------------------------------------------------------


class BaseAccommodationScheme(BaseModel):
    name: str
    persons: int
    is_active: bool
    created_at: date
    type: str | None = None
    city: str | None = None
    country: str | None = None
    price: int

    class Config:
        orm_mode = True


class AccommodationScheme(BaseAccommodationScheme):
    update_at: date | None = None

    class Config:
        orm_mode = True

# ---------------------------------------------------------Booking---------------------------------------------------------------------------------


class BaseBookingScheme(BaseModel):
    date_start: date
    date_end: date
    persons: int
    created_at: date
    status: str
    accommodation_id: int

    class Config:
        orm_mode = True


class BookingScheme(BaseBookingScheme):
    update_at: date | None = None
    price: int | None = None

    class Config:
        orm_mode = True


# ---------------------------------------------------------Feedbacks---------------------------------------------------------------------------------

class BaseFeedbackScheme(BaseModel):
    description: str
    rating: int
    booking_id: int
    created_at: date

    class Config:
        orm_mode = True


class FeedbackScheme(BaseFeedbackScheme):
    update_at: date | None = None

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

class CreateFeedbackScheme(HosterFeedbackScheme, RenterFeedbackScheme):
    pass

    class Config:
        orm_mode = True


# ---------------------------------------------------------Token---------------------------------------------------------------------------------


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None

