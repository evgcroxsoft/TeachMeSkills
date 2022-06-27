import os
from flask import Flask
from connector import PostgreConnector
from flask_sqlalchemy import SQLAlchemy


# def create_app():
app = Flask(__name__)
DB_path = PostgreConnector.path_to_PostgreSQL()
app.config['SQLALCHEMY_DATABASE_URI'] = DB_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
app.config['SECRET_KEY'] = os.urandom(20).hex()
db = SQLAlchemy(app)
