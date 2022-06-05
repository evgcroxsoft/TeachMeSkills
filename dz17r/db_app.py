import os
import datetime
from unittest.mock import DEFAULT
import bcrypt
import psycopg2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy_utils import database_exists, create_database, drop_database
import uuid

def get_env_variable(name):
    '''Give message if some of value couln't downloaded'''
    try:
        return os.environ[name]
    except KeyError:
        message = "Expected environment variable '{}' not set.".format(name)
        raise Exception(message)

# the values of those depend on your setup
POSTGRES_URL = get_env_variable("POSTGRES_URL")
POSTGRES_USER = get_env_variable("POSTGRES_USER")
POSTGRES_PW = get_env_variable("POSTGRES_PW")
POSTGRES_DB = get_env_variable("POSTGRES_DB")

# app = Flask(__name__)
# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
# db = SQLAlchemy(app)

# class Events(db.Model):
#     id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     name = db.Column(db.String(150), unique=False, nullable=True)
#     date = db.Column(db.Date, unique=False, nullable=True)
#     place = db.Column(db.String(200), unique=False, nullable=True)
#     url = db.Column(db.String, unique=False, nullable=True)
#     description = db.Column(db.Text, unique=False, nullable=True)
#     date_added = db.Column(db.DateTime(timezone=True), server_default=func.now())

# class Users(db.Model):
#     id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
#     email = db.Column(db.String(50), unique=True, nullable=True)
#     hash = db.Column(db.Text, unique=False, nullable=True)
#     name = db.Column(db.String(150), unique=False, nullable=True)
#     surname = db.Column(db.String(150), unique=False, nullable=True)
#     birthday = db.Column(db.Date, unique=False, nullable=True)
#     address = db.Column(db.String(200), unique=False, nullable=True)
#     date_added = db.Column(db.DateTime(timezone=True), server_default=func.now())


@app.cli.command('resetdb')
def resetdb_command():
    """Destroys and creates the database + tables."""

    if database_exists(DB_URL):
        print('Deleting database.')
        drop_database(DB_URL)
    if not database_exists(DB_URL):
        print('Creating database.')
        create_database(DB_URL)

    print('Creating tables.')
    db.create_all()
    print('Shiny!')