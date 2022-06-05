from flask import Flask, request, flash, redirect, url_for, render_template
import __init__
from __init__ import db, app
from models import Register
from werkzeug.security import check_password_hash
import re

@app.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        form_email = request.form['form_email']
        form_password = request.form['form_password'] 
        
        check_user = Register.query.filter_by(email=form_email).first()

        if not check_user:
            flash('User not found')
            return render_template('login.html')

        if check_password_hash(check_user.password, form_password):
            return redirect(url_for('home'))
        else: 
            flash('Wrong passport')
            return render_template('login.html')

    return render_template('login.html')