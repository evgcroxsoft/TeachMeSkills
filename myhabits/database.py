from sqlalchemy_utils import create_database, database_exists, drop_database
from __init__ import DB_path, db
from models import User

class Database():
    def resetdb_command():
        '''Destroys and creates the database + tables.'''
        
        if database_exists(DB_path):
            print('Deleting database.')
            drop_database(DB_path)
        
        if not database_exists(DB_path):
            print('Creating database.')
            create_database(DB_path)
        
        db.create_all()
        print('Shiny!')

# Database.resetdb_command()
