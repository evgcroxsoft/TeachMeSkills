from uuid import UUID
from typing import Union
from pydantic import BaseModel, EmailStr
from datetime import datetime, date


# BaseScheme

class BaseScheme(BaseModel):
    updated_at: date
    created_at: date

class UserCreateScheme(BaseModel):
    hashed_password: str


class UserBaseScheme(BaseScheme):
    first_name: str
    last_name: str
    email: EmailStr
    telephone: str
    is_active: bool


class AccomodationBaseScheme(BaseScheme):
    name: str
    city: str
    address: str
    type: str
    # media = Column(?)
    description: Union[str, None] = None
    is_active: bool
    is_available: bool
    hoster_id: UUID
    price_id: int
    booking_id: int


class BookingBaseScheme(BaseScheme):
    start_date: date
    end_date: date
    status: str
    renter_id: UUID
    hoster_feedback_id: int
    renter_feedback_id: int


class FeedbackBaseScheme(BaseScheme):
    star: int
    comment: str


class PriceBaseScheme(BaseScheme):
    name: str
    start_date: date
    end_date: date


# HosterScheme
class HosterCreate(UserCreateScheme, UserBaseScheme):
    pass


class HosterUpdate(UserBaseScheme):
    pass


class HosterRetrieve(UserBaseScheme):
    id: UUID

    class Config:
        orm_mode = True


# RenterScheme
class RenterCreate(UserCreateScheme, UserBaseScheme):
    pass


class RenterUpdate(UserBaseScheme):
    pass


class RenterRetrieve(UserBaseScheme):
    pass


# AccomodationScheme
class AccomodationCreateScheme(AccomodationBaseScheme):
    id: int


class AccomodationUpdateScheme(AccomodationBaseScheme):
    pass


class AccomodationRetrieveScheme(AccomodationBaseScheme):
    pass


# BookingScheme
class BookingCreateScheme(BookingBaseScheme):
    id: int


class BookingUpdateScheme(BookingBaseScheme):
    pass


class BookingRetrieveScheme(BookingBaseScheme):
    pass


# RenterFeedbackScheme
class RenterFeedbackCreateScheme(FeedbackBaseScheme):
    pass


class RenterFeedbackUpdateScheme(FeedbackBaseScheme):
    updated_at: date


class RenterFeedbackRetrieveScheme(FeedbackBaseScheme):
    pass


# HosterFeedbackScheme
class HosterFeedbackCreateScheme(FeedbackBaseScheme):
    id: int


class HosterFeedbackUpdateScheme(FeedbackBaseScheme):
    pass


class HosterFeedbackRetrieveScheme(FeedbackBaseScheme):
    pass


# PriceScheme
class PriceCreateScheme(PriceBaseScheme):
    id: int


class PricekUpdateScheme(PriceBaseScheme):
    pass


class PriceRetrieveScheme(PriceBaseScheme):
    pass

    class Config:
        orm_mode = True
