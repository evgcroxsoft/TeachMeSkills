from flask import request, flash, redirect, url_for, render_template
import re
from send_email import send_email
from werkzeug.security import generate_password_hash
from __init__ import db, app
from models import User

@app.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        '''https://regex101.com/r/qmTzU0/2/'''
        nickname = request.form['nickname']
        email = request.form['form_email']
        password = request.form['password']
        password_2 = request.form['password_2']

        user = User.query.filter_by(email=email).first()
        regex_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' 

        if user:
            if email == user.email:
                flash('Such Email already exists', category='error')
                return redirect(url_for('register'))
        
        if re.fullmatch(regex_email, email) == None:
            flash('Email no match!', category='error')
            return redirect(url_for('register'))

        regex_password = r"^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$"


        if password != password_2:
            flash('Passwords do not match', category = 'error')
            return redirect(url_for('register'))
        
        if len(password) < 8:
            flash('Password should have more than 8 characters', category='error')
            return redirect(url_for('register'))
        
        if re.fullmatch(regex_password, password) == None:
            flash('Password no Match!', category='error')
            return redirect(url_for('register'))
            
        hashed = generate_password_hash(password)

        user = User(
                    nickname=nickname,
                    email=email, 
                    password=hashed
                    )

        try:
            db.session.add(user)
            send_email(email)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            flash('Some problem with registration, please try again!')
            return render_template('register.html')

    return render_template('register.html')
