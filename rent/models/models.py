from abc import ABC

import datetime
from datetime import datetime, date

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Date
from sqlalchemy.orm import relationship

import uuid
from uuid import UUID

from database.base import Base


class ModelBase(ABC):
    created_at: Column(Date, default=datetime.date)
    updated_at: Column(Date, default=datetime.date)


class UserBase(ModelBase):
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)
    email = Column(String, unique=True, nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(100))
    hashed_password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)


class Landlord(UserBase):
    __tablename__ = "landlords"


class Tenant(UserBase):
    __tablename__ = "tenants"


class Appartment(ModelBase):
    __tablename__ = "appartments"

    id = Column(Integer, primary_key=True)
    city = Column(String(100))
    street = Column(String(100))
    house_number = Column(String(5))
    flat_number = Column(String(5))
    description = Column(String)
    daily_price = Column(Integer(10))
    is_available = Column(Boolean, default=True)
    landlords_id = Column(UUID, ForeignKey("landlords.id"))


class Cart(ModelBase):
    __tablename__ = "cart"

    appartment_id = Column(Integer, ForeignKey("item.id"))
    tenant_id = Column(UUID, ForeignKey("tenants.id"), unique=True)

class Order (ModelBase):
    __tablename__ = "order"

    landlords_id = Column(Integer, ForeignKey("landlords.id"))
    feedback_id = Column(Integer, ForeignKey("landlords.id"))

class Media(ModelBase):
    __tablename__ = "appartments"

class Feedback(ModelBase):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True)
    star = Column(Integer(10))
    comment = Column(Text)



    # items = relationship("Item", back_populates="owner")