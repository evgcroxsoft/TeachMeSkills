from flask import Flask, request, flash, redirect, url_for, render_template
import __init__
from __init__ import db, app
from models import Register
from werkzeug.security import generate_password_hash
import re
from send_email import send_email

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        '''https://regex101.com/r/qmTzU0/2/'''
        form_nickname = request.form['nickname']
        form_email = request.form['form_email']
        form_password = request.form['password']
        form_password_2 = request.form['password_2']

        user_check = Register.query.filter_by(email=form_email).first()
        regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 

        if user_check:
            if form_email == user_check.email:
                flash('Such Email already exists', category = 'error')
                return redirect(url_for('register'))
        
        if re.fullmatch(regex_email, form_email) == None:
            flash('Email no match!', category = 'error')
            return redirect(url_for('register'))

        regex_password = r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"


        if form_password != form_password_2:
            flash('Different passwords', category = 'error')
            return redirect(url_for('register'))
        
        if len(form_password) < 8:
            flash('Password less then 8 digits', category = 'error')
            return redirect(url_for('register'))
        
        if re.fullmatch(regex_password, form_password) == None:
            flash('Password no Match!', category = 'error')
            return redirect(url_for('register'))
            
        hashed = generate_password_hash(form_password)

        user = Register(
                        nickname=form_nickname,
                        email=form_email, 
                        password=hashed
                        )

        try:
            db.session.add(user)
            send_email(form_email)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            flash('Some problem with registration, please try again!')
            return render_template('register.html')

    return render_template('register.html')
