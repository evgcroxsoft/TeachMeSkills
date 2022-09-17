#________________________________________________________MODELS__________________________________________________________________________________

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Enum
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
import uuid

from database.app_db import Base, engine
from models.enum import AccommodationCountry, AccommodationType, BookingStatus, AccommodationCity, AccommodationCountry

# ------------------------------------------------------Abstract---------------------------------------------------------------------------------

class DataBase(Base):
    __abstract__ = True
    created_at = Column(Date)
    updated_at = Column(Date)

# ------------------------------------------------------User---------------------------------------------------------------------------------

class User(DataBase):
    __tablename__ = 'users'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4())
    email = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(100))
    phone = Column(String(20))
    hashed_password = Column(String(100), nullable=False)
    renter = Column(Boolean, default=False)
    hoster = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    accommodations = relationship('Accommodation', backref='users', cascade='all, delete')
    bookings = relationship('Booking', backref='users')

# ------------------------------------------------------Accommodation---------------------------------------------------------------------------------

class Accommodation(DataBase):
    __tablename__ = 'accommodations'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    persons = Column(Integer)
    is_active = Column(Boolean, default=True)
    accommodation_type = Column(Enum(AccommodationType))
    city = Column(Enum(AccommodationCity))
    country = Column(Enum(AccommodationCountry))
    price = Column(Integer)
    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))

# --------------------------------------------------------Booking---------------------------------------------------------------------------------

class Booking(DataBase):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    date_start = Column(Date, nullable=False)
    date_end = Column(Date, nullable=False)
    persons = Column(Integer)
    status = Column(Enum(BookingStatus))
    price = Column(Integer)
    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))
    accommodation_id = Column(Integer, ForeignKey('accommodations.id'))

# --------------------------------------------------------RenterFeedback---------------------------------------------------------------------------------

class RenterFeedback(DataBase):
    __tablename__ = 'renter_feedbacks'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    description = Column(String(200), nullable=False)
    rating = Column(Integer)
    booking_id = Column(Integer, ForeignKey('accommodations.id'))
    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))

# --------------------------------------------------------HosterFeedback---------------------------------------------------------------------------------

class HosterFeedback(DataBase):
    __tablename__ = 'hoster_feedbacks'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    description = Column(String(200), nullable=False)
    rating = Column(Integer)
    booking_id = Column(Integer, ForeignKey('accommodations.id'))
    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))


#Create all tables: this line need to be after models!
Base.metadata.create_all(bind=engine)