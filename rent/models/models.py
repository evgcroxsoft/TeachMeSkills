import datetime
from datetime import datetime, date

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Date
from sqlalchemy.orm import relationship


class ModelBase():
    created_at: Column(Date, default=datetime.date)
    updated_at: Column(Date, default=datetime.date)
    abstract__ = True


class UserBase(ModelBase):
    id = Column(Integer, primary_key=True)
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
    daily_price = Column(Integer)
    is_available = Column(Boolean, default=True)
    landlords_id = Column(Integer, ForeignKey("landlords.id"))


class Cart(ModelBase):
    __tablename__ = "cart"

    appartment_id = Column(Integer, ForeignKey("item.id"))
    tenant_id = Column(Integer, ForeignKey("tenants.id"), unique=True)

class Order (ModelBase):
    __tablename__ = "order"

    landlords_id = Column(Integer, ForeignKey("landlords.id"))
    feedback_id = Column(Integer, ForeignKey("landlords.id"))

class Media(ModelBase):
    __tablename__ = "appartments"

class Feedback(ModelBase):
    __tablename__ = "feedbacks"

    id = Column(Integer, primary_key=True)
    star = Column(Integer)
    comment = Column(Text)



    # items = relationship("Item", back_populates="owner")
