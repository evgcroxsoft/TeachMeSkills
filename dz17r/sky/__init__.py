# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_bootstrap import Bootstrap
# from sqlalchemy_utils import database_exists, create_database, drop_database


# def get_env_variable(name):
#     '''Give message if some of value couln't downloaded'''
#     try:
#         return os.environ[name]
#     except KeyError:
#         message = f"Expected environment variable {name} not set."
#         raise Exception(message)

# POSTGRES_URL = get_env_variable("POSTGRES_URL")
# POSTGRES_USER = get_env_variable("POSTGRES_USER")
# POSTGRES_PW = get_env_variable("POSTGRES_PW")
# POSTGRES_DB = get_env_variable("POSTGRES_DB")

# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)

# def create_app():
#   app = Flask(__name__)
#   Bootstrap(app)

#   return app

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
# db = SQLAlchemy(app)

# from sky import models, routes

# # @app.cli.command('resetdb')
# # def resetdb_command():
# #     """Destroys and creates the database + tables."""

# #     if database_exists(DB_URL):
# #         print('Deleting database.')
# #         drop_database(DB_URL)
# #     if not database_exists(DB_URL):
# #         print('Creating database.')
# #         create_database(DB_URL)

# #     print('Creating tables.')
# #     db.create_all()
# #     print('Shiny!')


# # resetdb_command()

# if __name__ == "main":
#     app.run(debug=True)