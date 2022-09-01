import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from application.db_myhabits.connector import PostgreConnector
from flask_mail import Mail

app = Flask(__name__)

DB_path = PostgreConnector.path_to_PostgreSQL()
app.config['SQLALCHEMY_DATABASE_URI'] = DB_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
app.config['SECRET_KEY'] = os.urandom(20).hex()
app.config['TESTING'] = False
app.config['MAIL_SERVER'] = os.environ['MAIL_SERVER']
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEBUG'] = True
app.config['MAIL_USERNAME'] = os.environ['MAIL_USERNAME']
app.config['MAIL_PASSWORD'] = os.environ['MAIL_PASSWORD']
app.config['MAIL_DEFAULT_SENDER'] = 'myhabits@croxsoft.com'
app.config['MAIL_MAX_EMAILS'] = None 
# app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATACHMENTS'] = False

mail = Mail(app)

db = SQLAlchemy(app)