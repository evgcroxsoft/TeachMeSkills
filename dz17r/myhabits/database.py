from models import User
from __init__ import DB_path, db
from sqlalchemy_utils import database_exists, create_database, drop_database

class DataBase():
    def getUser(self,user_id):
        '''Get Id from User for authentication'''
        try:
            res = User.query.get(user_id)
            if not res:
                print('User not found')
                return False
        except Exception:
            print ('Troubles to take data from DB')

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

# DataBase.resetdb_command()       
