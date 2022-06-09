from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
import uuid
from __init__ import db
from datetime import datetime

class Register(db.Model, UserMixin):
    id = db.Column(UUID(as_uuid=True), unique=True, primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(50), unique=True, nullable=True)
    password = db.Column(db.Text, unique=False, nullable=True)
    nickname = db.Column(db.String(30), unique=False, nullable=True)
    name = db.Column(db.String(150), unique=False, nullable=True)
    surname = db.Column(db.String(150), unique=False, nullable=True)
    birthday = db.Column(db.Date, unique=False, nullable=True)
    telegram = db.Column(db.String(30), unique=False, nullable=True)
    colour = db.Column(db.String(30), unique=False, nullable=True)
    avatar_name = db.Column(db.String(50), unique=False, nullable=True)
    avatar = db.Column(db.LargeBinary, unique=False, nullable=True)
    gender = db.Column(db.String(10), unique=False, nullable=True)
    my_info = db.Column(db.Text, unique=False, nullable=True)
    created = db.Column(db.Date, default=datetime.now().strftime("%d-%m-%Y"))

# class User(db.Model):
#     id = db.Column(db.Integer, unique=True, primary_key=True)
#     nickname = db.Column(db.String(30), unique=False, nullable=True)
#     name = db.Column(db.String(150), unique=False, nullable=True)
#     surname = db.Column(db.String(150), unique=False, nullable=True)
#     birthday = db.Column(db.Date, unique=False, nullable=True)
#     telegram = db.Column(db.String(30), unique=False, nullable=True)
#     colour = db.Column(db.String(30), unique=False, nullable=True)
#     avatar_name = db.Column(db.String(50), unique=False, nullable=True)
#     avatar = db.Column(db.LargeBinary, unique=False, nullable=True)
#     gender = db.Column(db.String(10), unique=False, nullable=True)
#     my_info = db.Column(db.Text, unique=False, nullable=True)
#     created = db.Column(db.DateTime(timezone=True), server_default=func.now())

class Habit(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(150), unique=False, nullable=True)
    description = db.Column(db.Text, unique=False, nullable=True)
    created = db.Column(db.Date, default=datetime.now().strftime("%d-%m-%Y"))

class Log(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    decription = db.Column(db.String(200), unique=False, nullable=True)
    created = db.Column(db.Date, default=datetime.now().strftime("%d-%m-%Y"))
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey(Register.id), nullable=False)

# class Status(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(10), unique=False, nullable=True)

class Relative(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    child_id = db.Column(UUID(as_uuid=True), db.ForeignKey(Register.id), nullable=False)
    adult_id = db.Column(UUID(as_uuid=True), db.ForeignKey(Register.id), nullable=False)
    created = db.Column(db.Date, default=datetime.now().strftime("%d-%m-%Y"))

class Task(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    wish_period = db.Column(db.Date, unique=False, nullable=True)
    start_period = db.Column(db.Date, unique=False, nullable=True)
    pause_period = db.Column(db.Date, unique=False, nullable=True)
    weekdays = db.Column(db.JSON)
    habit_id = db.Column(db.Integer, db.ForeignKey(Habit.id), nullable=False)
    created = db.Column(db.Date, default=datetime.now().strftime("%d-%m-%Y"))

class Date(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=False, nullable=True)
    habit_id = db.Column(db.Integer, db.ForeignKey(Habit.id), nullable=False)
    created = db.Column(db.Date, default=datetime.now().strftime("%d-%m-%Y"))

