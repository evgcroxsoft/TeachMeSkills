from sqlalchemy_utils import create_database, database_exists, drop_database
from app import DB_path, db

class Database():
    def createdb_command():
        '''Check and creates the database + tables.'''
        if not database_exists(DB_path):
            print('Creating database.')
            create_database(DB_path)
        db.create_all()

    def resetdb_command():
        '''Destroys and creates the database + tables.'''
        if database_exists(DB_path):
            print('Deleting database.')
            drop_database(DB_path)
        Database.createdb_command()
        print('Shiny!')
    
    def commit_db():
        db.session.commit()
        
Database.createdb_command()
# Database.resetdb_command()
