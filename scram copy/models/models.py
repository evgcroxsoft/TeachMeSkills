import datetime
from datetime import datetime, date

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Date
from sqlalchemy.orm import relationship

from database.database import Base

# class Host(Base):
#     __tablename__ = "hosts"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)


class ModelBase():
    created_at: Column(Date, default=datetime.date)
    updated_at: Column(Date, default=datetime.date)
    __abstract__ = True


class UserBase(ModelBase):
    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(100))
    email = Column(String(100), unique=True)
    telephone = Column(String(20))
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)
    

class ReviewBase(ModelBase):
    id = Column(Integer, primary_key=True)
    star = Column(Integer)
    comment = Column(Text)


class Hoster(UserBase):
    __tablename__ = "hosters"


class Renter(UserBase):
    __tablename__ = "renters"


class HosterReview(ReviewBase):
    __tablename__ = "hoster_reviews"


class RenterReview(ReviewBase):
    __tablename__ = "hoster_reviews"


class Accomodation(ModelBase):
    __tablename__ = "accomodations"

    id = Column(Integer, primary_key=True)
    name = Column(String(20))
    city = Column(String(100))
    address = Column(String(50))
    type = Column(String(50))
    # media = Column(?)
    description = Column(Text) # TODO
    is_active = Column(Boolean, default=True)
    is_available = Column(Boolean, default=True)
    price_id = Column(Integer, ForeignKey("Price.id"))
    hoster_id = Column(Integer, ForeignKey("Hoster.id"))
    booking_id = Column(Integer, ForeignKey("Booking.id"))


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
    renter_id = Column(Integer, ForeignKey("Renter.id"))
    hoster_review_id = Column(Integer, ForeignKey("HosterReview.id"))
    renter_review_id = Column(Integer, ForeignKey("RenterReview.id"))



    # items = relationship("Item", back_populates="owner")
