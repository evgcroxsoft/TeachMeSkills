from flask import flash, redirect, render_template, url_for
from app import DB_path, db

class Crud():
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
