import os
from flask import Flask
from connector import Connector
from flask_sqlalchemy import SQLAlchemy


# def create_app():
app = Flask(__name__)
DB_path = Connector.path_to_PostgreSQL()
app.config['SQLALCHEMY_DATABASE_URI'] = DB_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
app.config['SECRET_KEY'] = os.urandom(20).hex()
db = SQLAlchemy(app)
    # db.init_app(app)

    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint)

    #     # blueprint for auth routes in our app
    # from .auth import auth as auth_blueprint
    # app.register_blueprint(auth_blueprint)

    # # blueprint for non-auth parts of app
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)

    # return app
