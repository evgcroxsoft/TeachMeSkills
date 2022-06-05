from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from bd_setup import Connect_to_Postgres
from sqlalchemy_utils import database_exists, create_database, drop_database


app = Flask(__name__)
DB_URL = Connect_to_Postgres.path_to_PostgreSQL()
print(DB_URL)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # silence the deprecation warning
db = SQLAlchemy(app)


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

resetdb_command()