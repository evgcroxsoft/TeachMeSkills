from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.dialects.postgresql import UUID
import uuid
from __init__ import db
from datetime import datetime
import datetime

class User(db.Model, UserMixin):
    id = db.Column(UUID(as_uuid=True), unique=True, primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(50), unique=True, nullable=True)
    password = db.Column(db.Text, nullable=True)
    nickname = db.Column(db.String(30), nullable=True)
    name = db.Column(db.String(150), nullable=True)
    surname = db.Column(db.String(150), nullable=True)
    birthday = db.Column(db.Date, nullable=True)
    telegram = db.Column(db.String(30), nullable=True)
    colour = db.Column(db.String(30), nullable=True)
    avatar_name = db.Column(db.String(50), nullable=True)
    avatar = db.Column(db.LargeBinary, nullable=True)
    gender = db.Column(db.String(10), nullable=True)
    info = db.Column(db.Text, nullable=True)
    created = db.Column(db.Date, default=datetime.date.today())

class Habit(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String(150), nullable=True)
    description = db.Column(db.Text, nullable=True)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey(User.id), nullable=False)
    created = db.Column(db.Date, default=datetime.date.today())

# class Log(db.Model):
#     id = db.Column(db.Integer, unique=True, primary_key=True)
#     decription = db.Column(db.String(200), unique=False, nullable=True)
#     created = db.Column(db.Date, default=datetime.now().strftime("%d-%m-%Y"))
#     user_id = db.Column(UUID(as_uuid=True), db.ForeignKey(Register.id), nullable=False)

# class Status(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(10), unique=False, nullable=True)

# class Relative(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     child_id = db.Column(UUID(as_uuid=True), db.ForeignKey(Register.id), nullable=False)
#     adult_id = db.Column(UUID(as_uuid=True), db.ForeignKey(Register.id), nullable=False)
#     created = db.Column(db.Date, default=datetime.now().strftime("%d-%m-%Y"))

class Task(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    wish_period = db.Column(db.Integer, nullable=True)
    start_period = db.Column(db.Date, nullable=True)
    pause_period = db.Column(db.Date, nullable=True)
    weekdays = db.Column(db.PickleType, nullable=True)
    life = db.Column(db.Integer, default=3, nullable=True)
    total_lifes = db.Column(db.Integer, default=3, nullable=True)
    habit_id = db.Column(db.Integer, db.ForeignKey(Habit.id), nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey(User.id), nullable=False)
    created = db.Column(db.Date, default=datetime.date.today())

class Statistic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weekdays = db.Column(db.String(10), nullable=True)
    life = db.Column(db.Integer, default=1, nullable=True)
    status = db.Column(db.String(10), nullable=True)
    task_id = db.Column(db.Integer, db.ForeignKey(Task.id), nullable=False)
    user_id = db.Column(UUID(as_uuid=True), db.ForeignKey(User.id), nullable=False)
    created = db.Column(db.Date, default=datetime.date.today())

