from sqlalchemy_utils import create_database, database_exists, drop_database
from app import DB_path, db, app
from flask import flash, redirect, render_template, url_for


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
    
    def add_in_db(value, url_success, url_except):
        try:
            db.session.add(value)
            db.session.commit()
            return redirect(url_for(url_success))
        except:
            db.session.rollback()
            flash('Some problem with adding, please try again!')
            return redirect(url_for(url_except))
    
    def update_in_db(url_success, url_except):
        try:
            db.session.commit()
            return redirect(url_for(url_success))
        except:
            db.session.rollback()
            flash('Some problem with saving, try again!')
            return redirect(url_for(url_except))
        
    def delete_in_db(value, url_success, url_except):
        try:
            db.session.delete(value)
            db.session.commit()
            print(url_for(url_success))
            return redirect(url_for(url_success))
        except:
            db.session.rollback()
            flash('Some problem with deleting, please try again!')
            return render_template(url_except)

# Database.createdb_command()
Database.resetdb_command()
