import os
from flask import Flask
# from flask_login import LoginManager
from connector import Connector
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
DB_path = Connector.path_to_PostgreSQL()
app.config['SQLALCHEMY_DATABASE_URI'] = DB_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
app.config['SECRET_KEY'] = os.urandom(20).hex()
db = SQLAlchemy(app)
# login_manager = LoginManager(app)