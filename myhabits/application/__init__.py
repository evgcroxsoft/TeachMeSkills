import os
from flask import Flask
from flask_crontab import Crontab
from flask_sqlalchemy import SQLAlchemy
from celery import Celery
from application.db_myhabits.connector import PostgreConnector
# from application.services.flask_celery import make_celery
from datetime import timedelta

app = Flask(__name__)
DB_path = PostgreConnector.path_to_PostgreSQL()
app.config['SQLALCHEMY_DATABASE_URI'] = DB_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
app.config['SECRET_KEY'] = os.urandom(20).hex()
db = SQLAlchemy(app)

crontab = Crontab(app)
celery = Celery('task_celery', broker='redis://localhost:6379/0', backend= 'redis://localhost:6379/0')
celery.config_from_object('celeryconfig')