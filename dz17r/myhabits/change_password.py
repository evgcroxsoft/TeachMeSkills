from flask import Flask, request, flash, redirect, url_for, render_template
import __init__
from __init__ import db, app
from models import Register
from werkzeug.security import generate_password_hash
import re
from send_email import send_email
from session_check import session_check

@app.route('/change_password/<uuid:id>', methods=('GET', 'POST'))
def change_password(id):
    user_check = Register.query.get(id)
    if id == user_check.id:
        limit_link = int(session_check())
        if limit_link < 3:
            if request.method == 'POST':
                form_password = request.form['form-password']
                form_password_2 = request.form['form-password_2']
                print('Hello World')
                regex_password = r'^.*(?=.{8,})(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[@#$%^&+=]).*$'

                if form_password != form_password_2:
                    flash('Different passwords', category = 'error')
                    return redirect(url_for('change_password', id=user_check.id))
                
                if len(form_password) < 8:
                    flash('Password less then 8 digits', category = 'error')
                    return redirect(url_for('change_password', id=user_check.id))
                
                if re.findall(regex_password, form_password) == None:
                    flash('Password no Match!', category = 'error')
                    return redirect(url_for('change_password', id=user_check.id))
                    
                hashed = generate_password_hash(form_password)

                new_password = hashed
                user_check.password = new_password
                try:
                    db.session.commit()
                    send_email(user_check.email)
                    return redirect(url_for('login'))
                except:
                    flash('Some problem with registration, please try again!')
                    return render_template('change_password.html')
        else:
            flash(f'You have already used this link, please try login in or push Forget password again!')
            return redirect(url_for('login'))
    return render_template('change_password.html', id=user_check.id)
