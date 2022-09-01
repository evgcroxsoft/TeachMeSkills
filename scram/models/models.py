from datetime import datetime, date
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Date
from sqlalchemy.orm import relationship
import uuid
from sqlalchemy_utils import UUIDType

from database.database import Base


class ModelBase(Base):
    __abstract__ = True
    created_at = Column(Date, default=datetime.date)
    updated_at = Column(Date, default=datetime.date)


class UserBase(ModelBase):
    __abstract__ = True
    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4())
    first_name = Column(String(50))
    last_name = Column(String(100))
    email = Column(String(100), unique=True, nullable=False)
    telephone = Column(String(20))
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)


class FeedbackBase(ModelBase):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    star = Column(Integer)
    comment = Column(Text)


class Hoster(UserBase):
    __tablename__ = "hosters"


class Renter(UserBase):
    __tablename__ = "renters"


class HosterFeedback(FeedbackBase):
    __tablename__ = "hoster_feedbacks"

class RenterFeedback(FeedbackBase):
    __tablename__ = "renter_feedbacks"


class Price(ModelBase):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    start_date = Column(Date)
    end_date = Column(Date)


class Booking(ModelBase):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(String(50))
    renter_id = Column(UUIDType, ForeignKey("renters.id"))
    hoster_feedback_id = Column(Integer, ForeignKey("hoster_feedbacks.id"))
    renter_feedback_id = Column(Integer, ForeignKey("renter_feedbacks.id"))


class Accomodation(ModelBase):
    __tablename__ = "accomodations"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    city = Column(String(100))
    address = Column(String(50))
    type = Column(String(50))
    # media = Column(?)
    description = Column(Text)
    is_active = Column(Boolean, default=True)
    is_available = Column(Boolean, default=True)
    hoster_id = Column(UUIDType, ForeignKey("hosters.id"))
    price_id = Column(Integer, ForeignKey("prices.id"))
    booking_id = Column(Integer, ForeignKey("bookings.id"))

    # items = relationship("Item", back_populates="owner")
