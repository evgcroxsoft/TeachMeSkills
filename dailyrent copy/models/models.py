from datetime import datetime
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
from sqlalchemy.orm import relationship
from sqlalchemy_utils import UUIDType
import uuid

from database.database import Base, engine


class DataBase(Base):
    __abstract__ = True
    created_at = Column(Date, default=datetime.date)


class User(DataBase):
    __tablename__ = 'users'

    id = Column(UUIDType(binary=False), primary_key=True, default=uuid.uuid4())
    email = Column(String(100), unique=True, nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(100))
    telephone = Column(String(20))
    hashed_password = Column(String(100), nullable=False)
    renter = Column(Boolean, default=False)
    hoster = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)

    accommodations = relationship('Accommodation', backref='users', cascade='all, delete')
    bookings = relationship('Booking', backref='users')


class Accommodation(DataBase):
    __tablename__ = 'accommodations'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    persons = Column(Integer)
    is_active = Column(Boolean, default=True)
    type = Column(String(100), nullable=False)
    city = Column(String(100), nullable=False)
    country = Column(String(100), nullable=False)
    price = Column(Integer)
    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))
    # price_id = Column(Integer, ForeignKey('prices.id'))

    # users = relationship('User', back_populates='accommodations')


class Booking(DataBase):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    date_start = Column(Date, nullable=False)
    date_end = Column(Date, nullable=False)
    persons = Column(Integer)
    status = Column(String(100))
    price = Column(Integer)
    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))
    accommodation_id = Column(Integer, ForeignKey('accommodations.id'))


class RenterFeedback(DataBase):
    __tablename__ = 'renter_feedbacks'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    description = Column(String(200), nullable=False)
    rating = Column(Integer)
    booking_id = Column(Integer, ForeignKey('accommodations.id'))
    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))


class HosterFeedback(DataBase):
    __tablename__ = 'hoster_feedbacks'

    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    description = Column(String(200), nullable=False)
    rating = Column(Integer)
    booking_id = Column(Integer, ForeignKey('accommodations.id'))
    user_id = Column(UUIDType(binary=False), ForeignKey('users.id'))


# create all tables, this line need to be after models
Base.metadata.create_all(bind=engine)